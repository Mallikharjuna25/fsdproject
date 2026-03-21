window.NoteNestData = {
  getAll() {
    return JSON.parse(localStorage.getItem('nn_materials')) || []
  },
  
  getById(id) {
    return this.getAll().find(m => m.id === id) || null
  },
  
  search(query) {
    if (!query) return this.getAll()
    query = query.toLowerCase()
    return this.getAll().filter(m =>
      m.title.toLowerCase().includes(query) ||
      m.subject.toLowerCase().includes(query) ||
      m.description.toLowerCase().includes(query) ||
      m.tags.some(t => t.toLowerCase().includes(query))
    )
  },
  
  filter(opts) {
    let results = this.getAll()
    if (opts.type) results = results.filter(m => m.type === opts.type)
    if (opts.subject) results = results.filter(m => m.subject === opts.subject)
    if (opts.semester) results = results.filter(m => m.semester === opts.semester)
    if (opts.year) results = results.filter(m => m.year === opts.year)
    if (opts.examType) results = results.filter(m => m.examType === opts.examType)
    if (opts.format) results = results.filter(m => m.fileFormat === opts.format)
    if (opts.minRating) results = results.filter(m => m.rating >= opts.minRating)
    if (opts.tag) results = results.filter(m => m.tags.includes(opts.tag))
    if (opts.department) results = results.filter(m => m.department === opts.department)
    return results
  },
  
  sort(arr, by) {
    const copy = [...arr]
    if (by === 'downloads') return copy.sort((a,b) => b.downloads - a.downloads)
    if (by === 'rating') return copy.sort((a,b) => b.rating - a.rating)
    if (by === 'newest') return copy.sort((a,b) => new Date(b.uploadDate) - new Date(a.uploadDate))
    return copy
  },
  
  getRelated(id, limit=4) {
    const mat = this.getById(id)
    if (!mat) return []
    return this.getAll()
      .filter(m => m.id !== id && m.subject === mat.subject)
      .slice(0, limit)
  },
  
  getAllTags() {
    const counts = {}
    this.getAll().forEach(m => 
      m.tags.forEach(t => counts[t] = (counts[t]||0) + 1))
    return Object.entries(counts)
      .sort((a,b) => b[1]-a[1])
      .map(([tag, count]) => ({ tag, count }))
  },
  
  getStats() {
    const mats = this.getAll()
    return {
      totalMaterials: mats.length,
      totalDownloads: mats.reduce((s,m) => s + m.downloads, 0),
      totalSubjects: [...new Set(mats.map(m => m.subject))].length,
      totalUsers: (JSON.parse(localStorage.getItem('nn_users'))||[]).length
    }
  },

  saveUpload(material) {
    const mats = this.getAll()
    mats.unshift(material)
    localStorage.setItem('nn_materials', JSON.stringify(mats))
    if(window.NoteNestAuth) {
      const user = window.NoteNestAuth.getUser()
      if (user) {
        user.uploads = user.uploads || []
        user.uploads.push(material.id)
        window.NoteNestAuth.updateUser({ uploads: user.uploads })
      }
    }
  },
  
  saveBookmark(userId, materialId) {
    if(!window.NoteNestAuth) return false
    const user = window.NoteNestAuth.getUser()
    if (!user) return false
    user.bookmarks = user.bookmarks || []
    const idx = user.bookmarks.indexOf(materialId)
    if (idx > -1) {
      user.bookmarks.splice(idx, 1) // remove
    } else {
      user.bookmarks.push(materialId) // add
    }
    window.NoteNestAuth.updateUser({ bookmarks: user.bookmarks })
    return idx === -1 // true = now bookmarked
  },
  
  isBookmarked(materialId) {
    if(!window.NoteNestAuth) return false
    const user = window.NoteNestAuth.getUser()
    if (!user) return false
    return (user.bookmarks || []).includes(materialId)
  },
  
  saveDownload(materialId) {
    if(!window.NoteNestAuth) return
    const user = window.NoteNestAuth.getUser()
    if (!user) return
    user.downloadHistory = user.downloadHistory || []
    const mat = this.getById(materialId)
    user.downloadHistory.unshift({
      id: materialId,
      title: mat ? mat.title : 'Unknown',
      date: new Date().toISOString().split('T')[0],
      format: mat ? mat.fileFormat : 'PDF'
    })
    if (user.downloadHistory.length > 50) 
      user.downloadHistory = user.downloadHistory.slice(0,50)
    window.NoteNestAuth.updateUser({ downloadHistory: user.downloadHistory })
  },
  
  incrementDownloads(id) {
    const mats = this.getAll()
    const mat = mats.find(m => m.id === id)
    if (mat) {
      mat.downloads++
      localStorage.setItem('nn_materials', JSON.stringify(mats))
    }
  },
  
  incrementViews(id) {
    const mats = this.getAll()
    const mat = mats.find(m => m.id === id)
    if (mat) {
      mat.views++
      localStorage.setItem('nn_materials', JSON.stringify(mats))
    }
  },
  
  addComment(materialId, comment) {
    const mats = this.getAll()
    const mat = mats.find(m => m.id === materialId)
    if (mat) {
      mat.comments = mat.comments || []
      mat.comments.unshift({
        id: 'c_' + Date.now(),
        userId: comment.userId,
        userName: comment.userName,
        rating: comment.rating || 0,
        text: comment.text,
        date: new Date().toISOString().split('T')[0],
        likes: 0,
        likedBy: []
      })
      localStorage.setItem('nn_materials', JSON.stringify(mats))
    }
  },
  
  addRating(materialId, newRating) {
    const mats = this.getAll()
    const mat = mats.find(m => m.id === materialId)
    if (mat) {
      const total = mat.rating * mat.ratingCount + newRating
      mat.ratingCount++
      mat.rating = Math.round((total / mat.ratingCount) * 10) / 10
      localStorage.setItem('nn_materials', JSON.stringify(mats))
    }
  },
  
  likeComment(materialId, commentId) {
    if(!window.NoteNestAuth) return
    const user = window.NoteNestAuth.getUser()
    if (!user) return
    const mats = this.getAll()
    const mat = mats.find(m => m.id === materialId)
    if (!mat) return
    const comment = mat.comments.find(c => c.id === commentId)
    if (!comment) return
    comment.likedBy = comment.likedBy || []
    if (comment.likedBy.includes(user.id)) return
    comment.likedBy.push(user.id)
    comment.likes++
    localStorage.setItem('nn_materials', JSON.stringify(mats))
  },
  
  updateMaterial(id, fields) {
    const mats = this.getAll()
    const idx = mats.findIndex(m => m.id === id)
    if (idx > -1) {
      mats[idx] = { ...mats[idx], ...fields }
      localStorage.setItem('nn_materials', JSON.stringify(mats))
    }
  },
  
  deleteMaterial(id) {
    const mats = this.getAll().filter(m => m.id !== id)
    localStorage.setItem('nn_materials', JSON.stringify(mats))
  }
}

// Seed on load
;(function seedData() {
  if (!localStorage.getItem('nn_materials')) {
    const initData = [
      { id: "mat_001", title: "Engineering Mathematics Unit 1", description: "Comprehensive notes covering matrices, eigenvalues, and eigenvectors.", type: "Notes", subject: "Mathematics", department: "Engineering", course: "B.Tech", semester: "Sem 1", year: "1st Year", examType: "Semester End", university: "JNTUK", tags: ["maths", "engineering", "matrices"], fileFormat: "PDF", fileSize: "4.2 MB", pages: 48, uploadedBy: "Ravi Kumar", uploaderId: "demo_user", uploadDate: "2024-11-20", downloads: 892, views: 1240, rating: 4.7, ratingCount: 128, comments: [{ id: "c1", userId: "u2", userName: "Priya S", rating: 5, text: "Very helpful notes!", date: "2024-11-22", likes: 12, likedBy: [] }] },
      { id: "mat_002", title: "Physics Quantum Mechanics", description: "Summary of Schrödinger equations.", type: "Notes", subject: "Physics", department: "Science", course: "B.Sc", semester: "Sem 2", year: "1st Year", examType: "Mid Term", university: "AU", tags: ["physics", "quantum"], fileFormat: "PDF", fileSize: "2.1 MB", pages: 20, uploadedBy: "Ravi Kumar", uploaderId: "demo_user", uploadDate: "2024-11-25", downloads: 412, views: 600, rating: 4.5, ratingCount: 65, comments: [] },
      { id: "mat_003", title: "Organic Chemistry Reactions", description: "SN1, SN2 mechanisms.", type: "Notes", subject: "Chemistry", department: "Science", course: "B.Sc", semester: "Sem 3", year: "2nd Year", examType: "Semester End", university: "OU", tags: ["chemistry", "organic"], fileFormat: "PDF", fileSize: "3.5 MB", pages: 30, uploadedBy: "Demo User", uploaderId: "demo_user", uploadDate: "2024-12-01", downloads: 120, views: 250, rating: 4.8, ratingCount: 40, comments: [] },
      { id: "mat_004", title: "Data Structures Trees", description: "Binary trees, AVL, BST.", type: "Notes", subject: "Data Structures", department: "Computer Science", course: "B.Tech", semester: "Sem 3", year: "2nd Year", examType: "Semester End", university: "JNTUK", tags: ["cs", "ds", "trees"], fileFormat: "PDF", fileSize: "5.1 MB", pages: 60, uploadedBy: "Alice", uploaderId: "u_alice", uploadDate: "2024-12-05", downloads: 1540, views: 2100, rating: 4.9, ratingCount: 300, comments: [] },
      { id: "mat_005", title: "Algorithms Graphs", description: "Dijkstra, BFS, DFS.", type: "Notes", subject: "Algorithms", department: "Computer Science", course: "B.Tech", semester: "Sem 4", year: "2nd Year", examType: "Semester End", university: "JNTUK", tags: ["cs", "algo", "graphs"], fileFormat: "PDF", fileSize: "4.8 MB", pages: 55, uploadedBy: "Bob", uploaderId: "u_bob", uploadDate: "2024-12-10", downloads: 1100, views: 1800, rating: 4.6, ratingCount: 210, comments: [] },
      { id: "mat_006", title: "Digital Electronics Logic Gates", description: "Boolean algebra, K-maps.", type: "Notes", subject: "Digital Electronics", department: "ECE", course: "B.Tech", semester: "Sem 2", year: "1st Year", examType: "Semester End", university: "JNTUA", tags: ["ece", "digital", "logic"], fileFormat: "PDF", fileSize: "6.2 MB", pages: 70, uploadedBy: "Charlie", uploaderId: "u_charlie", uploadDate: "2024-12-15", downloads: 800, views: 1200, rating: 4.4, ratingCount: 150, comments: [] },
      { id: "mat_007", title: "Civil Eng Fluid Mechanics", description: "Bernoulli's principle.", type: "Notes", subject: "Civil Engineering", department: "Civil", course: "B.Tech", semester: "Sem 4", year: "2nd Year", examType: "Semester End", university: "JNTUH", tags: ["civil", "fluids"], fileFormat: "PDF", fileSize: "7.1 MB", pages: 80, uploadedBy: "Dave", uploaderId: "u_dave", uploadDate: "2024-12-20", downloads: 600, views: 900, rating: 4.3, ratingCount: 90, comments: [] },
      { id: "mat_008", title: "Mechanical Eng Thermodynamics", description: "Laws of thermodynamics.", type: "Notes", subject: "Mechanical Engineering", department: "Mechanical", course: "B.Tech", semester: "Sem 3", year: "2nd Year", examType: "Semester End", university: "AU", tags: ["mech", "thermo"], fileFormat: "PDF", fileSize: "8.5 MB", pages: 95, uploadedBy: "Eve", uploaderId: "u_eve", uploadDate: "2025-01-05", downloads: 750, views: 1100, rating: 4.7, ratingCount: 160, comments: [] },
      { id: "mat_009", title: "English Communication Skills", description: "Grammar and vocabulary.", type: "Notes", subject: "English", department: "Humanities", course: "B.Tech", semester: "Sem 1", year: "1st Year", examType: "Semester End", university: "OU", tags: ["english", "comm"], fileFormat: "PDF", fileSize: "1.2 MB", pages: 15, uploadedBy: "Frank", uploaderId: "u_frank", uploadDate: "2025-01-10", downloads: 200, views: 400, rating: 4.1, ratingCount: 30, comments: [] },
      { id: "mat_010", title: "Environmental Science Ecology", description: "Ecosystems and biodiversity.", type: "Notes", subject: "Environmental Science", department: "Science", course: "B.Sc", semester: "Sem 1", year: "1st Year", examType: "Semester End", university: "JNTUK", tags: ["evs", "ecology"], fileFormat: "PDF", fileSize: "3.2 MB", pages: 35, uploadedBy: "Grace", uploaderId: "u_grace", uploadDate: "2025-01-15", downloads: 350, views: 600, rating: 4.2, ratingCount: 50, comments: [] },
      { id: "mat_011", title: "Economics Micro", description: "Supply and demand.", type: "Notes", subject: "Economics", department: "Arts", course: "B.A", semester: "Sem 2", year: "1st Year", examType: "Semester End", university: "DU", tags: ["arts", "eco", "micro"], fileFormat: "PDF", fileSize: "2.8 MB", pages: 25, uploadedBy: "Heidi", uploaderId: "u_heidi", uploadDate: "2025-01-20", downloads: 400, views: 700, rating: 4.5, ratingCount: 80, comments: [] },
      { id: "mat_012", title: "Economics Macro", description: "GDP and inflation.", type: "Notes", subject: "Economics", department: "Arts", course: "B.A", semester: "Sem 3", year: "2nd Year", examType: "Semester End", university: "DU", tags: ["arts", "eco", "macro"], fileFormat: "PDF", fileSize: "3.1 MB", pages: 28, uploadedBy: "Ivan", uploaderId: "u_ivan", uploadDate: "2025-01-25", downloads: 450, views: 800, rating: 4.6, ratingCount: 90, comments: [] },
      { id: "mat_013", title: "Mathematics Model Paper 1", description: "Practice paper.", type: "Model Paper", subject: "Mathematics", department: "Engineering", course: "B.Tech", semester: "Sem 1", year: "1st Year", examType: "Semester End", university: "JNTUK", tags: ["maths", "model"], fileFormat: "PDF", fileSize: "0.5 MB", pages: 5, uploadedBy: "Judy", uploaderId: "u_judy", uploadDate: "2025-02-01", downloads: 1200, views: 2000, rating: 4.8, ratingCount: 250, comments: [] },
      { id: "mat_014", title: "Physics Question Paper 2023", description: "Previous year question paper.", type: "Question Paper", subject: "Physics", department: "Science", course: "B.Sc", semester: "Sem 2", year: "1st Year", examType: "Semester End", university: "AU", tags: ["physics", "pyq"], fileFormat: "PDF", fileSize: "0.8 MB", pages: 3, uploadedBy: "Kevin", uploaderId: "u_kevin", uploadDate: "2025-02-05", downloads: 1800, views: 2500, rating: 4.9, ratingCount: 400, comments: [] },
      { id: "mat_015", title: "Chemistry Lab Manual", description: "Titration experiments.", type: "Lab Report", subject: "Chemistry", department: "Science", course: "B.Sc", semester: "Sem 3", year: "2nd Year", examType: "Practical", university: "OU", tags: ["chemistry", "lab"], fileFormat: "PDF", fileSize: "4.5 MB", pages: 40, uploadedBy: "Leo", uploaderId: "u_leo", uploadDate: "2025-02-10", downloads: 500, views: 800, rating: 4.4, ratingCount: 110, comments: [] },
      { id: "mat_016", title: "Data Structures Assignment 1", description: "Linked lists code.", type: "Assignment", subject: "Data Structures", department: "Computer Science", course: "B.Tech", semester: "Sem 3", year: "2nd Year", examType: "Internal", university: "JNTUK", tags: ["cs", "ds", "assignment"], fileFormat: "ZIP", fileSize: "0.2 MB", pages: 1, uploadedBy: "Mia", uploaderId: "u_mia", uploadDate: "2025-02-15", downloads: 300, views: 500, rating: 4.0, ratingCount: 40, comments: [] },
      { id: "mat_017", title: "Algorithms CLRS Solution", description: "Chapter 1-5 solutions.", type: "Textbook", subject: "Algorithms", department: "Computer Science", course: "B.Tech", semester: "Sem 4", year: "2nd Year", examType: "Reference", university: "Global", tags: ["cs", "algo", "clrs"], fileFormat: "PDF", fileSize: "12.5 MB", pages: 200, uploadedBy: "Nick", uploaderId: "u_nick", uploadDate: "2025-02-20", downloads: 5000, views: 8000, rating: 5.0, ratingCount: 1200, comments: [] },
      { id: "mat_018", title: "Digital Electronics Simulation", description: "Proteus files.", type: "Lab Report", subject: "Digital Electronics", department: "ECE", course: "B.Tech", semester: "Sem 2", year: "1st Year", examType: "Practical", university: "JNTUA", tags: ["ece", "digital", "proteus"], fileFormat: "ZIP", fileSize: "1.5 MB", pages: 1, uploadedBy: "Olivia", uploaderId: "u_olivia", uploadDate: "2025-02-25", downloads: 400, views: 700, rating: 4.3, ratingCount: 75, comments: [] },
      { id: "mat_019", title: "Civil Eng AutoCad Designs", description: "Floor plans.", type: "Assignment", subject: "Civil Engineering", department: "Civil", course: "B.Tech", semester: "Sem 4", year: "2nd Year", examType: "Internal", university: "JNTUH", tags: ["civil", "autocad"], fileFormat: "ZIP", fileSize: "5.5 MB", pages: 1, uploadedBy: "Paul", uploaderId: "u_paul", uploadDate: "2025-03-01", downloads: 250, views: 400, rating: 4.2, ratingCount: 45, comments: [] },
      { id: "mat_020", title: "Mechanical Eng Workshop Ref", description: "Lathe machine operations.", type: "Textbook", subject: "Mechanical Engineering", department: "Mechanical", course: "B.Tech", semester: "Sem 3", year: "2nd Year", examType: "Reference", university: "AU", tags: ["mech", "workshop"], fileFormat: "PDF", fileSize: "9.2 MB", pages: 120, uploadedBy: "Quinn", uploaderId: "u_quinn", uploadDate: "2025-03-05", downloads: 600, views: 1000, rating: 4.6, ratingCount: 130, comments: [] },
      { id: "mat_021", title: "English Essay Topics", description: "List of 100 topics.", type: "Assignment", subject: "English", department: "Humanities", course: "B.Tech", semester: "Sem 1", year: "1st Year", examType: "Internal", university: "OU", tags: ["english", "essay"], fileFormat: "DOCX", fileSize: "0.1 MB", pages: 5, uploadedBy: "Rachel", uploaderId: "u_rachel", uploadDate: "2025-03-10", downloads: 150, views: 300, rating: 3.9, ratingCount: 20, comments: [] },
      { id: "mat_022", title: "Environmental Science Project", description: "Pollution study.", type: "Lab Report", subject: "Environmental Science", department: "Science", course: "B.Sc", semester: "Sem 1", year: "1st Year", examType: "Practical", university: "JNTUK", tags: ["evs", "project"], fileFormat: "PDF", fileSize: "2.5 MB", pages: 20, uploadedBy: "Sam", uploaderId: "u_sam", uploadDate: "2025-03-12", downloads: 200, views: 350, rating: 4.1, ratingCount: 35, comments: [] },
      { id: "mat_023", title: "Economics Micro Quiz", description: "MCQs.", type: "Model Paper", subject: "Economics", department: "Arts", course: "B.A", semester: "Sem 2", year: "1st Year", examType: "Quiz", university: "DU", tags: ["arts", "eco", "quiz"], fileFormat: "PDF", fileSize: "0.3 MB", pages: 4, uploadedBy: "Tom", uploaderId: "u_tom", uploadDate: "2025-03-15", downloads: 350, views: 500, rating: 4.4, ratingCount: 60, comments: [] },
      { id: "mat_024", title: "Economics Macro Paper 2022", description: "Past paper.", type: "Question Paper", subject: "Economics", department: "Arts", course: "B.A", semester: "Sem 3", year: "2nd Year", examType: "Semester End", university: "DU", tags: ["arts", "eco", "pyq"], fileFormat: "PDF", fileSize: "0.6 MB", pages: 3, uploadedBy: "Ursula", uploaderId: "u_ursula", uploadDate: "2025-03-18", downloads: 900, views: 1300, rating: 4.8, ratingCount: 190, comments: [] }
    ]
    localStorage.setItem('nn_materials', JSON.stringify(initData))
  }
})()
