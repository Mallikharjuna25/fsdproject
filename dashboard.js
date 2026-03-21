// ── DOM ELEMENTS ──
const sbAvatarText = document.getElementById('sbAvatarText');
const sbAvatarImg = document.getElementById('sbAvatarImg');
const sbName = document.getElementById('sbName');
const sbEmail = document.getElementById('sbEmail');
const welcomeMsg = document.getElementById('welcomeMsg');
const notifBadge = document.getElementById('notifBadge');
const deleteModal = document.getElementById('deleteModal');
let deleteTargetId = null;

let mockNotifs = [
  { id: 'n1', title: 'Welcome to NoteNest', desc: 'Complete your profile to get the most out of NoteNest.', time: 'Just now', read: false }
];

// ── INIT ──
document.addEventListener('DOMContentLoaded', () => {
  if (window.NoteNestAuth && !window.NoteNestAuth.requireAuth()) return;
  initAuth();
  handleUrlTab();
  renderDashboard();
  renderUploads('all');
  renderBookmarks();
  renderDownloads();
  renderNotifs();
  renderChart();
});

// ── AUTH STATE ──
function initAuth() {
  const user = window.NoteNestAuth.getUser() || { name: 'Student', email: 'student@university.edu' };
  sbName.textContent = user.name;
  sbEmail.textContent = user.email;
  welcomeMsg.textContent = `Good morning, ${user.name.split(' ')[0]}! 🎓`;
  
  // Set initials
  const initials = user.name.split(' ').map(n => n[0]).join('').substring(0, 2).toUpperCase();
  sbAvatarText.textContent = initials;
  
  // Settings Form Pre-fill
  document.getElementById('setFullName').value = user.name;
  
  // Check Avatar
  if(user.avatar) {
    applyAvatar(user.avatar);
  }
}


// ── TAB SWITCHING ──
function switchTab(tabId) {
  // Update sidebar links
  document.querySelectorAll('.sb-link').forEach(link => {
    link.classList.toggle('active', link.dataset.tab === tabId);
  });
  
  // Update content panes
  document.querySelectorAll('.tab-pane').forEach(pane => {
    pane.classList.remove('active');
  });
  document.getElementById(`tab-${tabId}`).classList.add('active');
  
  // Scroll to top
  window.scrollTo(0,0);
  
  // Optional URL update (without reload)
  history.replaceState(null, '', `?tab=${tabId}`);
  
  // Close mobile menus if open
  userMenuBtn.classList.remove('active');
}

function handleUrlTab() {
  const urlParams = new URLSearchParams(window.location.search);
  const tab = urlParams.get('tab');
  if(tab && document.getElementById(`tab-${tab}`)) {
    switchTab(tab);
  }
}

// ── RENDER DASHBOARD ──
function renderDashboard() {
  if(!window.NoteNestAuth || !window.NoteNestData) return;
  const user = window.NoteNestAuth.getUser();
  if(!user) return;
  
  const uploads = user.uploads || [];
  const downloads = user.downloadHistory || [];
  const bookmarks = user.bookmarks || [];
  
  // Update stats
  document.querySelector('.s-card.amber .sc-value').textContent = uploads.length;
  document.querySelectorAll('.s-card')[1].querySelector('.sc-value').textContent = downloads.length;
  document.querySelectorAll('.s-card')[2].querySelector('.sc-value').textContent = bookmarks.length;
  
  const list = document.getElementById('recentActivityList');
  list.innerHTML = '';
  const items = [];
  if(uploads.length) items.push({ icon: '↑', title: 'Uploaded material', meta: 'Recently' });
  if(downloads.length) items.push({ icon: '↓', title: `Downloaded ${downloads[downloads.length-1].title}`, meta: 'Recently' });
  if(bookmarks.length > 0) items.push({ icon: '★', title: 'Saved material', meta: 'Recently' });
  
  if(items.length === 0) {
    list.innerHTML = '<p style="color:var(--clr-gray);padding:10px 0;font-size:0.9rem">No recent activity.</p>';
    return;
  }
  
  items.forEach(item => {
    list.innerHTML += `
      <div class="mini-item" style="pointer-events:none">
        <div class="mi-icon">${item.icon}</div>
        <div class="mi-info">
          <div class="mi-title">${item.title}</div>
          <div class="mi-meta">${item.meta}</div>
        </div>
      </div>
    `;
  });
}

function renderChart() {
  const chartBox = document.getElementById('activityChart');
  const months = ['Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov'];
  const data = [20, 40, 15, 60, 45, 85]; // percentages showing activity volume
  
  let html = '';
  data.forEach((val, i) => {
    const isUp = i > 0 && val > data[i-1];
    html += `
      <div class="chart-bar-group">
        <div class="c-bar ${isUp ? 'up' : 'dn'}" style="height:${val}%" title="${val} interactions in ${months[i]}"></div>
        <div class="c-label">${months[i]}</div>
      </div>
    `;
  });
  chartBox.innerHTML = html;
}

// ── RENDER UPLOADS ──
function renderUploads(filterStatusObj) {
  const grid = document.getElementById('uploadsGrid');
  grid.innerHTML = '';
  
  if(!window.NoteNestAuth || !window.NoteNestData) return;
  const user = window.NoteNestAuth.getUser();
  if(!user) return;
  
  const uploads = (user.uploads || []).map(id => window.NoteNestData.getById(id)).filter(Boolean);
  
  uploads.forEach(u => {
    grid.innerHTML += `
      <div class="mat-card" id="card-${u.id}">
        <span class="mc-status pub">Published</span>
        <div class="mc-type">📄 ${u.type}</div>
        <h3 class="mc-title">${u.title}</h3>
        <div class="mc-stats">
          <span><svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path><circle cx="12" cy="12" r="3"></circle></svg> ${u.views || 0}</span>
          <span><svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg> ${u.downloads || 0}</span>
        </div>
        <div class="mc-actions">
          <button class="btn-outline" style="flex:1" onclick="window.location.href='material.html?id=${u.id}'">View</button>
          <button class="btn-danger" aria-label="Delete" onclick="openDeleteModal('${u.id}')">
            <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2"><polyline points="3 6 5 6 21 6"></polyline><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path></svg>
          </button>
        </div>
      </div>
    `;
  });
  
  if(grid.innerHTML === '') {
    grid.innerHTML = `<p style="color:var(--clr-gray);grid-column:1/-1;text-align:center;padding:40px">No uploads found.</p>`;
  }
}

function filterUploads(q) {
  // basic filtering mock
  console.log('Searching for:', q);
}

function filterStatus(val) {
  renderUploads(val);
}

// ── DELETE UPLOAD ──
function openDeleteModal(id) {
  deleteTargetId = id;
  deleteModal.classList.add('show');
}
function closeDeleteModal() {
  deleteModal.classList.remove('show');
  deleteTargetId = null;
}
document.getElementById('confirmDelBtn').addEventListener('click', () => {
  if(!deleteTargetId) return;
  const card = document.getElementById(`card-${deleteTargetId}`);
  if(card) {
    card.style.opacity = '0';
    card.style.transform = 'scale(0.9)';
    
    // Actually delete from user's array
    if(window.NoteNestAuth) {
      const user = window.NoteNestAuth.getUser();
      if(user && user.uploads) {
        window.NoteNestAuth.updateUser({ uploads: user.uploads.filter(id => id !== deleteTargetId) });
      }
    }
    
    setTimeout(() => {
      card.remove();
      renderDashboard();
      showToast('Material deleted successfully');
    }, 300);
  }
  closeDeleteModal();
});

// ── RENDER BOOKMARKS ──
function renderBookmarks() {
  const grid = document.getElementById('bookmarksGrid');
  grid.innerHTML = '';
  
  if(!window.NoteNestAuth || !window.NoteNestData) return;
  const user = window.NoteNestAuth.getUser();
  if(!user) return;
  
  const bookmarks = (user.bookmarks || []).map(id => window.NoteNestData.getById(id)).filter(Boolean);
  
  bookmarks.forEach(b => {
    grid.innerHTML += `
      <div class="mat-card" id="bm-${b.id}">
        <div class="mc-type" style="cursor:pointer" onclick="window.location.href='material.html?id=${b.id}'">☆ ${b.type}</div>
        <h3 class="mc-title" style="cursor:pointer" onclick="window.location.href='material.html?id=${b.id}'">${b.title}</h3>
        <p style="font-size:.85rem;color:var(--clr-gray);margin-bottom:16px">By ${b.uploadedBy}</p>
        <div class="mc-actions" style="justify-content:space-between;align-items:center">
          <span style="font-size:.75rem;color:var(--clr-gray2)">${b.fileFormat || 'PDF'}</span>
          <button class="btn-danger" style="border:none;padding:6px;background:var(--clr-surface2)" onclick="removeBm('${b.id}')">Remove</button>
        </div>
      </div>
    `;
  });
  if(grid.innerHTML === '') {
    grid.innerHTML = `<p style="color:var(--clr-gray);grid-column:1/-1;text-align:center;padding:40px">No saved materials.</p>`;
  }
}

function removeBm(id) {
  if(window.NoteNestData) {
    const user = window.NoteNestAuth.getUser();
    window.NoteNestData.saveBookmark(user.id, id);
    renderBookmarks();
    renderDashboard();
    showToast('Removed from bookmarks');
  }
}

// ── RENDER DOWNLOADS ──
function renderDownloads() {
  const list = document.getElementById('downloadsList');
  list.innerHTML = '';
  
  if(!window.NoteNestAuth) return;
  const user = window.NoteNestAuth.getUser();
  if(!user) return;
  
  const downloads = user.downloadHistory || [];
  
  // Render in reverse to show newest first
  [...downloads].reverse().forEach(d => {
    list.innerHTML += `
      <div class="list-row">
        <div class="lr-icon dl"><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg></div>
        <div class="lr-content">
          <h4 class="lr-title">${d.title}</h4>
          <p class="lr-desc">${d.format || 'PDF'}</p>
        </div>
        <div class="lr-meta">${d.date}</div>
        <button class="btn-outline" onclick="window.location.href='material.html?id=${d.id}'">View</button>
      </div>
    `;
  });
  
  if(list.innerHTML === '') {
    list.innerHTML = '<p style="color:var(--clr-gray);text-align:center;padding:20px">No download history.</p>';
  }
}
function clearDownloads() {
  if(!window.NoteNestAuth) return;
  window.NoteNestAuth.updateUser({ downloadHistory: [] });
  renderDownloads();
  renderDashboard();
  showToast('Download history cleared');
}

// ── RENDER NOTIFICATIONS ──
function renderNotifs() {
  const list = document.getElementById('notificationsList');
  list.innerHTML = '';
  let unreadCount = 0;
  
  mockNotifs.forEach(n => {
    if(!n.read) unreadCount++;
    list.innerHTML += `
      <div class="list-row ${!n.read ? 'unread' : ''}" id="notif-${n.id}">
        <div class="lr-icon noti"><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"></path></svg></div>
        <div class="lr-content">
          <h4 class="lr-title">${n.title}</h4>
          <p class="lr-desc">${n.desc}</p>
        </div>
        <div class="lr-meta">${n.time}</div>
      </div>
    `;
  });
  
  updateBadge(unreadCount);
}

function markAllRead() {
  document.querySelectorAll('.list-row.unread').forEach(row => row.classList.remove('unread'));
  mockNotifs.forEach(n => n.read = true);
  updateBadge(0);
  showToast('All notifications marked as read', 'success');
}

function updateBadge(c) {
  if(c > 0) {
    notifBadge.textContent = c;
    notifBadge.classList.remove('hidden');
  } else {
    notifBadge.classList.add('hidden');
  }
}

// ── SETTINGS & AVATAR ──
function saveProfileSettings(e) {
  e.preventDefault();
  const newName = document.getElementById('setFullName').value;
  if(newName) {
    sbName.textContent = newName;
    
    if(window.NoteNestAuth) {
      window.NoteNestAuth.updateUser({ name: newName });
      
      const initials = newName.split(' ').map(n=>n[0]).join('').substring(0,2).toUpperCase();
      const user = window.NoteNestAuth.getUser();
      if(!user.avatar) {
        sbAvatarText.textContent = initials;
      }
      
      // Force nav.js to re-render avatar
      document.getElementById('navbar-root').innerHTML = ''; // reset so nav.js picks it up if possible
      if (typeof renderNavbar === 'function') renderNavbar();
      else window.location.reload();
    }
  }
  showToast('Profile updated successfully!', 'success');
}

function previewAvatar(e) {
  const file = e.target.files[0];
  if(file) {
    const reader = new FileReader();
    reader.onload = function(event) {
      const dataUrl = event.target.result;
      applyAvatar(dataUrl);
      if(window.NoteNestAuth) {
        window.NoteNestAuth.updateUser({ avatar: dataUrl });
        if (typeof renderNavbar === 'function') renderNavbar();
      }
      showToast('Avatar updated successfully!', 'success');
    };
    reader.readAsDataURL(file);
  }
}

function applyAvatar(dataUrl) {
  const setImg = document.getElementById('avatarPreviewImg');
  const setPrev = document.getElementById('avatarPreviewLabel');
  
  // Settings Preview
  setImg.src = dataUrl;
  setImg.style.display = 'block';
  setPrev.classList.add('has-img');
  
  // Sidebar replace
  sbAvatarImg.src = dataUrl;
  sbAvatarImg.style.display = 'block';
  sbAvatarText.style.display = 'none';
}

// ── UTIL ──
function showToast(msg, type = 'success') {
  const existing = document.getElementById('nn-toast');
  if (existing) existing.remove();
  
  const toast = document.createElement('div');
  toast.id = 'nn-toast';
  
  const icon = type === 'success' ? '✓ ' : 'ℹ ';
  toast.innerHTML = icon + msg;
  
  document.body.appendChild(toast);
  
  requestAnimationFrame(() => { 
    toast.style.opacity = '1'; 
    toast.style.transform = 'translateX(-50%) translateY(0)'; 
  });
  
  setTimeout(() => { 
    toast.style.opacity = '0'; 
    setTimeout(() => toast.remove(), 300); 
  }, 3000);
}

function confirmDeleteAccount() {
  if(confirm("Are you sure you want to delete your account? This action cannot be undone.")) {
    if(window.NoteNestAuth) {
      window.NoteNestAuth.logout();
    }
  }
}
