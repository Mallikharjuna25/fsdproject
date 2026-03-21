// ── STATE ──
let pdfScale = 1;
let pdfPage = 1;
const totalPages = 2; // Mock total for preview
let userRating = 0;
let isFollowing = false;
let currentMaterial = null;

// ── INIT ──
document.addEventListener('DOMContentLoaded', () => {
  initScrollBehavior();
  loadMaterial();
});

// ── DATA LOADING ──
function loadMaterial() {
  const params = new URLSearchParams(window.location.search);
  let id = params.get('id');
  if (id && !isNaN(parseInt(id))) id = parseInt(id);
  else if (!id) id = 1;

  if (window.NoteNestData) {
    currentMaterial = window.NoteNestData.getById(id);
    if (!currentMaterial) {
      // Fallback to first material if id not found
      const all = window.NoteNestData.getAll();
      if (all.length > 0) currentMaterial = all[0];
    }
  }

  if (!currentMaterial) {
    if (window.NoteNestToast) window.NoteNestToast.show('Material not found', 'error');
    setTimeout(() => window.location.href = 'browse.html', 1500);
    return;
  }

  renderMaterialDetails();
  renderPdfPage();
  checkBookmarkState();
  renderRelatedMaterials();
}

// ── DOM POPULATION ──
function renderMaterialDetails() {
  const m = currentMaterial;
  
  // Title & Document Title
  document.title = `${m.title} — NoteNest`;
  const breadcrumbs = document.querySelectorAll('.breadcrumb a');
  if(breadcrumbs.length >= 3) {
    breadcrumbs[2].textContent = m.subject;
    breadcrumbs[2].href = `browse.html?search=${encodeURIComponent(m.subject)}`;
  }
  document.querySelector('.breadcrumb .current').textContent = m.title;
  document.querySelector('.mat-title').textContent = m.title;
  
  // Badges & Pills
  document.querySelector('.type-badge').textContent = `📝 ${m.type}`;
  const pills = document.querySelectorAll('.meta-pill');
  if(pills.length >= 3) {
    pills[0].textContent = m.subject;
    pills[1].textContent = m.semester || m.year || '';
    pills[2].textContent = m.exam || '';
  }
  
  // Stats
  const statItems = document.querySelectorAll('.stat-item span');
  if(statItems.length >= 3) {
    statItems[0].textContent = (m.downloads * 1.5).toFixed(0); // Mock views
    statItems[1].textContent = m.downloads;
    statItems[2].textContent = m.rating;
  }
  
  // Uploader
  const uploaderName = m.uploader || 'Anonymous';
  const initials = uploaderName.split(' ').map(p=>p[0]).join('').substring(0,2).toUpperCase();
  document.querySelector('.uploader-row .avatar').textContent = initials;
  document.querySelector('.uploader-name').textContent = uploaderName;
  document.querySelector('.upload-date').textContent = `Uploaded on ${new Date(m.date).toLocaleDateString('en-IN', {day:'numeric',month:'short',year:'numeric'})}`;
  
  // Description
  document.querySelector('#descText').innerHTML = `<p>${m.desc || 'No description provided.'}</p>`;
  
  // PDF Preview Title
  const previewTitle = document.querySelector('.preview-title');
  if(previewTitle) {
    previewTitle.innerHTML = `📄 Document Preview <span>(${Math.floor(Math.random()*50)+5} pages)</span>`;
  }
  
  // Download Card
  document.querySelector('.dl-filename').textContent = `${m.title.replace(/[^a-zA-Z0-9]/g, '_').substring(0,30)}.${m.format.toLowerCase()}`;
  document.querySelector('.dl-filesize').textContent = `Size: ${(Math.random()*15+2).toFixed(1)} MB • Format: ${m.format}`;
  
  // Info Card
  const infoVals = document.querySelectorAll('.info-val');
  if(infoVals.length >= 7) {
    infoVals[0].textContent = m.format;
    infoVals[1].textContent = Math.floor(Math.random()*50 + 5) + ' pages';
    infoVals[2].textContent = m.subject;
    infoVals[3].textContent = m.type;
    infoVals[4].textContent = 'NoteNest University';
    infoVals[5].textContent = 'English';
    infoVals[6].textContent = new Date(m.date).toLocaleDateString('en-IN', {day:'numeric',month:'short',year:'numeric'});
  }
  
  // Tags
  const tagContainer = document.querySelector('.tag-pills');
  tagContainer.innerHTML = '';
  [m.subject, m.type, m.year, m.semester, m.exam].filter(Boolean).forEach(t => {
    const a = document.createElement('a');
    a.className = 'tag-pill';
    a.href = `browse.html?search=${encodeURIComponent(t)}`;
    a.textContent = '#' + t.toLowerCase().replace(/[^a-z0-9]/g, '');
    tagContainer.appendChild(a);
  });
}

function renderRelatedMaterials() {
  if (!window.NoteNestData) return;
  const related = window.NoteNestData.getRelated(currentMaterial.id, 4);
  const container = document.querySelector('.related-list');
  container.innerHTML = '';
  
  related.forEach(r => {
    const a = document.createElement('a');
    a.href = `material.html?id=${r.id}`;
    a.className = 'rel-card';
    a.innerHTML = `
      <div>
        <span class="rel-type">${r.type}</span>
        <div class="rel-title">${r.title}</div>
      </div>
      <div class="rel-meta">
        <span>👁 ${(r.downloads * 1.5).toFixed(0)}</span>
        <span>⬇ ${r.downloads}</span>
        <span>★ ${r.rating}</span>
      </div>
    `;
    container.appendChild(a);
  });
}

// ── SCROLL & NAV ──
function initScrollBehavior() {
  const nav = document.getElementById('navbar');
  const backTop = document.getElementById('backTop');
  
  window.addEventListener('scroll', () => {
    if(nav) nav.classList.toggle('scrolled', window.scrollY > 50);
    if(backTop) backTop.classList.toggle('show', window.scrollY > 400);
  }, { passive: true });
}

// ── PDF PREVIEW MOCK ──
function changePage(delta) {
  const newPage = pdfPage + delta;
  if (newPage < 1 || newPage > totalPages) return;
  pdfPage = newPage;
  
  document.getElementById('currentPage').textContent = pdfPage;
  document.getElementById('prevPageBtn').disabled = pdfPage === 1;
  document.getElementById('nextPageBtn').disabled = pdfPage === totalPages;
  
  renderPdfPage();
}

function zoomPreview(delta) {
  pdfScale = Math.max(0.5, Math.min(2, pdfScale + delta));
  const wrapper = document.getElementById('pdfPageWrapper');
  wrapper.style.transform = `scale(${pdfScale})`;
}

function renderPdfPage() {
  const wrapper = document.getElementById('pdfPageWrapper');
  
  let content = '';
  if (pdfPage === 1) {
    content = `
      <div class="pdf-skeleton">
        <div class="sk-title" style="margin-bottom:20px;height:28px;width:70%;background:#1a6b4a;opacity:0.2"></div>
        <div class="sk-line"></div>
        <div class="sk-line"></div>
        <div class="sk-line short"></div>
        <div class="sk-box"></div>
        <div class="sk-line"></div>
        <div class="sk-line"></div>
        <div class="sk-line half"></div>
      </div>
    `;
  } else {
    content = `
      <div class="pdf-skeleton">
        <div class="sk-line"></div>
        <div class="sk-line"></div>
        <div class="sk-line"></div>
        <div class="sk-line short" style="margin-bottom:30px"></div>
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-bottom:20px">
          <div class="sk-box" style="margin:0;height:120px"></div>
          <div class="sk-box" style="margin:0;height:120px"></div>
        </div>
        <div class="sk-line"></div>
        <div class="sk-line half"></div>
      </div>
    `;
  }
  
  wrapper.innerHTML = content + '<div class="watermark">NOTENEST</div>';
  wrapper.style.opacity = '0.5';
  setTimeout(() => wrapper.style.opacity = '1', 150);
}

// ── DESCRIPTION TOGGLE ──
window.toggleDesc = function() {
  const text = document.getElementById('descText');
  const btn = document.getElementById('showMoreBtn');
  const isExpanded = text.classList.contains('expanded');
  
  if (isExpanded) {
    text.classList.remove('expanded');
    btn.innerHTML = 'Show More ↓';
  } else {
    text.classList.add('expanded');
    btn.innerHTML = 'Show Less ↑';
  }
};

// ── FOLLOW UPLOADER ──
window.toggleFollow = function(btn) {
  isFollowing = !isFollowing;
  if (isFollowing) {
    btn.textContent = 'Following';
    btn.style.background = 'var(--clr-green)';
    btn.style.color = 'white';
    btn.style.borderColor = 'var(--clr-green)';
  } else {
    btn.textContent = 'Follow';
    btn.style.background = 'transparent';
    btn.style.color = 'var(--clr-white)';
    btn.style.borderColor = 'var(--clr-border)';
  }
};

// ── DOWNLOAD SIMULATION ──
window.startDownload = function() {
  const btn = document.getElementById('dlBtn');
  const originalText = btn.innerHTML;
  
  btn.style.pointerEvents = 'none';
  btn.innerHTML = '<span class="loader-ring" style="width:20px;height:20px;border-width:2px;display:inline-block"></span> Preparing...';
  
  setTimeout(() => {
    btn.innerHTML = 'Downloading...';
    
    setTimeout(() => {
      btn.innerHTML = '✓ Download Complete';
      btn.style.background = 'var(--clr-green)';
      btn.style.color = 'white';
      
      if (window.NoteNestData && currentMaterial) {
        window.NoteNestData.incrementDownloads(currentMaterial.id);
        if (window.NoteNestAuth && window.NoteNestAuth.isLoggedIn()) {
          window.NoteNestData.saveDownload(currentMaterial.id);
        }
      }
      
      if(window.NoteNestToast) window.NoteNestToast.show('Download completed successfully!', 'success');
      
      // Update stats row
      const statItems = document.querySelectorAll('.stat-item span');
      if (statItems.length >= 3 && currentMaterial) {
        statItems[1].textContent = currentMaterial.downloads + 1;
      }
      
      setTimeout(() => {
        btn.innerHTML = originalText;
        btn.style.background = '';
        btn.style.color = '';
        btn.style.pointerEvents = 'auto';
      }, 3000);
    }, 1500);
  }, 1000);
};

// ── BOOKMARK FEATURE ──
function checkBookmarkState() {
  if (!window.NoteNestAuth || !currentMaterial) return;
  const user = window.NoteNestAuth.getUser();
  const isBookmarked = user && user.bookmarks && user.bookmarks.includes(currentMaterial.id);
  
  const btn = document.getElementById('bookmarkBtn');
  if (isBookmarked) {
    btn.classList.add('active');
    btn.innerHTML = '<svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"></path></svg> Saved';
  }
}

window.toggleBookmark = function() {
  if (window.NoteNestAuth && !window.NoteNestAuth.isLoggedIn()) {
    if(window.NoteNestToast) window.NoteNestToast.show('Please log in to save bookmarks.', 'error');
    setTimeout(() => window.location.href = 'auth.html', 1500);
    return;
  }
  
  if (!currentMaterial || !window.NoteNestData) return;
  
  const user = window.NoteNestAuth.getUser();
  const wasBookmarked = user.bookmarks.includes(currentMaterial.id);
  const btn = document.getElementById('bookmarkBtn');
  
  window.NoteNestData.saveBookmark(currentMaterial.id);
  
  if (wasBookmarked) {
    btn.classList.remove('active');
    btn.innerHTML = '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"></path></svg> Save for later';
    if(window.NoteNestToast) window.NoteNestToast.show('Removed from saved materials', 'success');
  } else {
    btn.classList.add('active');
    btn.innerHTML = '<svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"></path></svg> Saved';
    if(window.NoteNestToast) window.NoteNestToast.show('Saved successfully!', 'success');
  }
};

// ── STAR RATING ──
window.hoverRating = function(val) {
  const stars = document.getElementById('ratingInput').children;
  for (let i = 0; i < 5; i++) {
    stars[i].classList.toggle('hover', i < val);
  }
};

window.resetRating = function() {
  const stars = document.getElementById('ratingInput').children;
  for (let i = 0; i < 5; i++) {
    stars[i].classList.remove('hover');
    stars[i].classList.toggle('active', i < userRating);
  }
};

window.setRating = function(val) {
  userRating = val;
  window.resetRating();
};

// ── SUBMIT COMMENT ──
window.submitComment = function() {
  const text = document.getElementById('commentText').value.trim();
  
  if (!text) {
    if(window.NoteNestToast) window.NoteNestToast.show('Please type a comment first', 'warning');
    return;
  }
  if (userRating === 0) {
    if(window.NoteNestToast) window.NoteNestToast.show('Please select a star rating', 'warning');
    return;
  }

  const list = document.getElementById('commentList');
  const d = new Date();
  const dateStr = 'Just now';
  
  const starsHtml = '★★★★★'.substring(0, userRating) + '☆☆☆☆☆'.substring(0, 5 - userRating);
  const user = window.NoteNestAuth && window.NoteNestAuth.isLoggedIn() ? window.NoteNestAuth.getUser().name : 'You';
  const initials = user.split(' ').map(p=>p[0]).join('').substring(0,2).toUpperCase();
  
  const commentHtml = `
    <div class="comment-item" style="animation:fadeUp 0.5s ease both">
      <div class="avatar" style="background:linear-gradient(135deg,var(--clr-amber),var(--clr-amber-dark));color:#0d0d0d">${initials}</div>
      <div class="comment-body">
        <div class="comment-meta">
          <span class="comment-author">${user}</span>
          <span class="comment-stars">${starsHtml}</span>
          <span class="comment-date">${dateStr}</span>
        </div>
        <p class="comment-text">${text.replace(/</g, "&lt;").replace(/>/g, "&gt;")}</p>
        <div class="comment-actions">
          <button class="like-btn" onclick="toggleLike(this)"><svg viewBox="0 0 24 24"><path d="M14 9V5a3 3 0 00-3-3l-4 9v11h11.28a2 2 0 002-1.7l1.38-9a2 2 0 00-2-2.3zM7 22H4a2 2 0 01-2-2v-7a2 2 0 012-2h3"/></svg> <span class="like-count">0</span></button>
          <button class="like-btn" title="Edit">Edit</button>
        </div>
      </div>
    </div>
  `;
  
  list.insertAdjacentHTML('afterbegin', commentHtml);
  
  // Real logic would be something like NoteNestData.addComment(currentMaterial.id, commentObj)
  
  document.getElementById('commentText').value = '';
  userRating = 0;
  window.resetRating();
  
  if(window.NoteNestToast) window.NoteNestToast.show('Review posted successfully!', 'success');
};

// ── COMMENT LIKES ──
window.toggleLike = function(btn) {
  const isLiked = btn.classList.contains('liked');
  const countSpan = btn.querySelector('.like-count');
  let count = parseInt(countSpan.textContent) || 0;
  
  if (isLiked) {
    btn.classList.remove('liked');
    count--;
  } else {
    btn.classList.add('liked');
    count++;
  }
  
  countSpan.textContent = count;
};

// ── COPY LINK ──
window.copyLink = function() {
  navigator.clipboard.writeText(window.location.href).then(() => {
    if(window.NoteNestToast) window.NoteNestToast.show('Link copied to clipboard!', 'success');
  }).catch(() => {
    if(window.NoteNestToast) window.NoteNestToast.show('Failed to copy link', 'error');
  });
};
