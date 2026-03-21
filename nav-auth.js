document.addEventListener('DOMContentLoaded', () => {
  // Select the auth area in desktop navbar and mobile menu
  const desktopAuthArea = document.getElementById('navAuthArea');
  const mobileAuthArea = document.getElementById('mobileAuthArea');
  
  const authData = localStorage.getItem('nn_auth');
  const avatarData = localStorage.getItem('nn_avatar');
  
  // Create Desktop Auth Element
  if (desktopAuthArea) {
    if (authData) {
      const auth = JSON.parse(authData);
      const initials = auth.user.split(' ').map(n=>n[0]).join('').substring(0,2).toUpperCase();
      
      let avatarHtml = `<div class="nav-avatar" id="globalNavAvatar" style="width:36px;height:36px;background:var(--clr-surface2);border-radius:50%;display:flex;align-items:center;justify-content:center;font-family:var(--ff-display);font-weight:700;color:var(--clr-amber);font-size:.9rem">${initials}</div>`;
      
      if(avatarData) {
        avatarHtml = `<div class="nav-avatar" id="globalNavAvatar" style="width:36px;height:36px;border-radius:50%;overflow:hidden"><img src="${avatarData}" style="width:100%;height:100%;object-fit:cover"></div>`;
      }

      desktopAuthArea.innerHTML = `
        <div class="user-menu" id="globalUserMenuBtn" style="position:relative;cursor:pointer;display:flex;align-items:center;gap:12px;padding:4px;border-radius:50px;background:rgba(255,255,255,0.05);border:1px solid var(--clr-border);transition:var(--transition)">
          ${avatarHtml}
          <span class="nav-username" style="font-size:.9rem;font-weight:500;color:var(--clr-white);max-width:100px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap">${auth.user}</span>
          <svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor" stroke="none" style="margin-right:8px;color:var(--clr-gray);transition:transform .3s ease"><path d="M7 10l5 5 5-5z"/></svg>
          
          <div class="user-dropdown" id="globalUserDropdown" style="position:absolute;top:calc(100% + 12px);right:0;width:220px;background:var(--clr-surface);border:1px solid var(--clr-border);border-radius:12px;padding:8px;box-shadow:0 12px 40px rgba(0,0,0,0.5);opacity:0;visibility:hidden;transform:translateY(10px);transition:all .3s cubic-bezier(0.4, 0, 0.2, 1);z-index:100">
            <a href="dashboard.html" style="display:flex;align-items:center;gap:12px;padding:10px 16px;color:var(--clr-gray);text-decoration:none;font-size:.9rem;border-radius:8px;transition:var(--transition)">
              <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path></svg> Dashboard
            </a>
            <a href="dashboard.html?tab=settings" style="display:flex;align-items:center;gap:12px;padding:10px 16px;color:var(--clr-gray);text-decoration:none;font-size:.9rem;border-radius:8px;transition:var(--transition)">
               <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="3"></circle><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"></path></svg> Settings
            </a>
            <div style="height:1px;background:var(--clr-border);margin:8px 0"></div>
            <a href="#" id="globalLogoutBtn" style="display:flex;align-items:center;gap:12px;padding:10px 16px;color:var(--clr-coral);text-decoration:none;font-size:.9rem;border-radius:8px;transition:var(--transition)">
              <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"></path><polyline points="16 17 21 12 16 7"></polyline><line x1="21" y1="12" x2="9" y2="12"></line></svg> Logout
            </a>
          </div>
        </div>
      `;
      
      const menuBtn = document.getElementById('globalUserMenuBtn');
      const dropdown = document.getElementById('globalUserDropdown');
      const logoutBtn = document.getElementById('globalLogoutBtn');
      
      // Hover styles for dropdown links dynamically added since it's injected
      dropdown.querySelectorAll('a').forEach(link => {
        link.addEventListener('mouseover', () => {
          if(link.id === 'globalLogoutBtn') link.style.background = 'rgba(255,107,107,0.1)';
          else { link.style.background = 'var(--clr-surface2)'; link.style.color = 'var(--clr-white)'; }
        });
        link.addEventListener('mouseout', () => {
          link.style.background = 'transparent';
          if(link.id !== 'globalLogoutBtn') link.style.color = 'var(--clr-gray)';
        });
      });

      menuBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        const isOpen = dropdown.style.visibility === 'visible';
        dropdown.style.opacity = isOpen ? '0' : '1';
        dropdown.style.visibility = isOpen ? 'hidden' : 'visible';
        dropdown.style.transform = isOpen ? 'translateY(10px)' : 'translateY(0)';
      });
      
      window.addEventListener('click', () => {
        dropdown.style.opacity = '0';
        dropdown.style.visibility = 'hidden';
        dropdown.style.transform = 'translateY(10px)';
      });
      
      logoutBtn.addEventListener('click', (e) => {
        e.preventDefault();
        localStorage.removeItem('nn_auth');
        localStorage.removeItem('nn_avatar');
        window.location.href = 'auth.html';
      });

    } else {
      // Not logged in -> Show Login CTA
      desktopAuthArea.innerHTML = `<a href="auth.html" class="btn-amber" style="background:var(--clr-amber);color:#0d0d0d;font-weight:600;padding:8px 24px;border-radius:8px;text-decoration:none;display:inline-block;transition:var(--transition);font-size:.95rem">Login / Sign Up</a>`;
    }
  }

  // Handle Mobile Menu Auth Area
  if (mobileAuthArea) {
    if (authData) {
      mobileAuthArea.innerHTML = `
        <li style="border-top:1px solid var(--clr-border);padding-top:16px;margin-top:16px">
          <a href="#" id="mobileLogoutBtn" style="color:var(--clr-coral);text-decoration:none;font-size:1.1rem;font-weight:500">Logout</a>
        </li>
      `;
      document.getElementById('mobileLogoutBtn').addEventListener('click', (e) => {
        e.preventDefault();
        localStorage.removeItem('nn_auth');
        localStorage.removeItem('nn_avatar');
        window.location.href = 'auth.html';
      });
    } else {
      mobileAuthArea.innerHTML = `
        <li style="border-top:1px solid var(--clr-border);padding-top:16px;margin-top:16px">
          <a href="auth.html" style="color:var(--clr-amber);text-decoration:none;font-size:1.1rem;font-weight:500">Login / Sign Up</a>
        </li>
      `;
    }
  }
});
