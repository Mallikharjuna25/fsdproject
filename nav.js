document.addEventListener('DOMContentLoaded', () => {
  const page = window.location.pathname.split('/').pop() || 'index.html'
  const isLoggedIn = window.NoteNestAuth && window.NoteNestAuth.isLoggedIn()
  const user = isLoggedIn ? window.NoteNestAuth.getUser() : null
  const initials = user ? user.name.split(' ').map(n=>n[0]).join('').substring(0,2).toUpperCase() : ''
  const avatarHtml = (user && user.avatar) 
    ? `<img src="${user.avatar}" style="width:100%;height:100%;border-radius:50%;object-fit:cover">`
    : `${initials}`

  const navHtml = `
  <nav class="navbar" id="navbar">
    <div class="container nav-inner">
      <a href="index.html" class="nav-logo">
        <svg viewBox="0 0 24 24" width="24" height="24" fill="var(--green)"><path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8zM14 2v6h6M16 13H8M16 17H8M10 9H8"/></svg>
        NoteNest
      </a>
      <ul class="nav-links" id="nav-links">
        <li><a href="index.html" class="${page==='index.html'||page===''?'active':''}">Home</a></li>
        <li><a href="browse.html" class="${page==='browse.html'?'active':''}">Browse</a></li>
        <li><a href="categories.html" class="${page==='categories.html'?'active':''}">Categories</a></li>
        <li><a href="upload.html" class="${page==='upload.html'?'active':''}">Upload</a></li>
        ${isLoggedIn ? `<li><a href="dashboard.html" class="${page==='dashboard.html'?'active':''}">Dashboard</a></li>` : ''}
      </ul>
      <div class="nav-actions">
        ${!isLoggedIn ? `
          <a href="auth.html" class="nav-cta">Login / Sign Up</a>
        ` : `
          <div class="user-menu" id="userMenu">
            <div class="avatar" id="userAvatar" style="background:${user.avatar?'transparent':'var(--green)'}">${avatarHtml}</div>
            <div class="dropdown" id="userDropdown" style="display:none">
              <p class="dropdown-name">${user.name}</p>
              <a href="dashboard.html">Dashboard</a>
              <a href="dashboard.html#uploads">My Uploads</a>
              <a href="dashboard.html#bookmarks">Bookmarks</a>
              <a href="#" id="logoutBtn" style="color:var(--red)">Logout</a>
            </div>
          </div>
        `}
      </div>
      <button class="hamburger" id="hamburger">☰</button>
    </div>
  </nav>
  `

  const styleEl = document.createElement('style')
  styleEl.textContent = `
    .user-menu { position:relative; cursor:pointer; }
    .dropdown { 
      position:absolute; top:calc(100% + 10px); right:0;
      background:#1c1c1c; border:1px solid #2a2a2a;
      border-radius:10px; padding:8px; min-width:180px;
      z-index:1001; box-shadow: 0 4px 20px rgba(0,0,0,0.5);
    }
    .dropdown a { 
      display:block; padding:10px 14px; color:#fff; 
      text-decoration:none; border-radius:6px; transition: 0.2s ease;
    }
    .dropdown a:hover { background:#2a2a2a; }
    .dropdown-name {
      padding:10px 14px; color:#888; font-size:13px;
      border-bottom:1px solid #2a2a2a; margin-bottom:4px; font-family:'DM Sans', sans-serif; margin-top:0;
    }
  `
  document.head.appendChild(styleEl)

  document.getElementById('navbar-root').innerHTML = navHtml

  // Events
  const ham = document.getElementById('hamburger')
  const links = document.getElementById('nav-links')
  if (ham && links) {
    ham.addEventListener('click', () => {
      links.classList.toggle('open')
    })
  }

  const uMenu = document.getElementById('userMenu')
  const dropdown = document.getElementById('userDropdown')
  if (uMenu && dropdown) {
    uMenu.addEventListener('click', (e) => {
      e.stopPropagation()
      dropdown.style.display = dropdown.style.display === 'none' ? 'block' : 'none'
    })
    document.addEventListener('click', (e) => {
      if (!uMenu.contains(e.target)) {
        dropdown.style.display = 'none'
      }
    })
  }

  const logoutBtn = document.getElementById('logoutBtn')
  if (logoutBtn) {
    logoutBtn.addEventListener('click', (e) => {
      e.preventDefault()
      if (window.NoteNestAuth) window.NoteNestAuth.logout()
    })
  }
  
  // Scrolled navbar
  const navbar = document.getElementById('navbar')
  window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
      navbar.style.background = 'rgba(13,13,13,0.95)'
      navbar.style.boxShadow = '0 4px 20px rgba(0,0,0,0.5)'
    } else {
      navbar.style.background = 'rgba(13,13,13,0.8)'
      navbar.style.boxShadow = 'none'
    }
  }, { passive: true })
})
