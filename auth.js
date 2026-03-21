window.NoteNestAuth = {
  _getUsers() {
    return JSON.parse(localStorage.getItem('nn_users')) || []
  },
  
  _saveUsers(users) {
    localStorage.setItem('nn_users', JSON.stringify(users))
  },
  
  isLoggedIn() {
    return !!localStorage.getItem('nn_current_user')
  },
  
  getUser() {
    const id = localStorage.getItem('nn_current_user')
    if (!id) return null
    return this._getUsers().find(u => u.id === id) || null
  },
  
  updateUser(fields) {
    const id = localStorage.getItem('nn_current_user')
    if (!id) return
    const users = this._getUsers()
    const idx = users.findIndex(u => u.id === id)
    if (idx > -1) {
      users[idx] = { ...users[idx], ...fields }
      this._saveUsers(users)
    }
  },
  
  login(email, password) {
    const users = this._getUsers()
    const user = users.find(u => 
      u.email.toLowerCase() === email.toLowerCase().trim() && 
      u.password === password
    )
    if (user) {
      localStorage.setItem('nn_current_user', user.id)
      return { success: true, user }
    }
    return { success: false, error: 'Invalid email or password' }
  },
  
  signup(name, email, password, university='', course='') {
    if (!name.trim()) return { success:false, error:'Name is required' }
    if (!email.trim()) return { success:false, error:'Email is required' }
    if (!/\\S+@\\S+\\.\\S+/.test(email)) 
      return { success:false, error:'Invalid email format' }
    if (password.length < 6) 
      return { success:false, error:'Password must be at least 6 characters' }
    
    const users = this._getUsers()
    if (users.find(u => u.email.toLowerCase() === email.toLowerCase().trim())) 
      return { success:false, error:'Email already registered' }
    
    const newUser = {
      id: 'user_' + Date.now(),
      name: name.trim(),
      email: email.toLowerCase().trim(),
      password,
      university,
      course,
      bio: '',
      avatar: null,
      joinedDate: new Date().toISOString().split('T')[0],
      uploads: [],
      bookmarks: [],
      downloadHistory: [],
      notifications: [
        { id:'n_'+Date.now(), text:'Welcome to NoteNest! Start sharing.', 
          read:false, date:new Date().toISOString().split('T')[0] }
      ]
    }
    users.push(newUser)
    this._saveUsers(users)
    localStorage.setItem('nn_current_user', newUser.id)
    return { success:true, user:newUser }
  },
  
  logout() {
    localStorage.removeItem('nn_current_user')
    window.location.href = 'index.html'
  },
  
  requireAuth(redirectBack=true) {
    if (!this.isLoggedIn()) {
      if (redirectBack) {
        localStorage.setItem('nn_redirect', window.location.href)
      }
      window.location.href = 'auth.html'
      return false
    }
    return true
  },
  
  getRedirectUrl() {
    const url = localStorage.getItem('nn_redirect')
    localStorage.removeItem('nn_redirect')
    return url
  }
}

// Seed users on load
;(function seedUsers() {
  if (!localStorage.getItem('nn_users')) {
    const initialUsers = [
      { id:"demo_user", name:"Demo User", email:"demo@notenest.com", 
        password:"demo123", university:"JNTUK", course:"B.Tech CSE",
        bio:"", avatar:null, joinedDate:"2024-01-01",
        uploads:["mat_001","mat_002"], bookmarks:["mat_003"],
        downloadHistory:[], notifications:[
          {id:"n1", text:"Welcome to NoteNest!", read:false, date:"2024-01-01"},
          {id:"n2", text:"Your upload got 10 downloads!", read:false, date:"2024-11-20"}
        ]
      },
      { id:"test_user", name:"Test Student", email:"student@test.com",
        password:"test123", university:"JNTUA", course:"B.Sc Physics",
        bio:"", avatar:null, joinedDate:"2024-02-01",
        uploads:[], bookmarks:[], downloadHistory:[], notifications:[]
      }
    ]
    localStorage.setItem('nn_users', JSON.stringify(initialUsers))
  }
})()
