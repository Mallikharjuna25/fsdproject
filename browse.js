// ── DATA WILL COME FROM NOTENESTDATA ──
const ICONS = {
  Chemistry: '🧪', Mathematics: '📐', Physics: '🔭', 'Computer Science': '💻',
  Biology: '🧬', Law: '⚖️', Economics: '📊', 'Civil Engg': '🏗️', Electronics: '📡'
};
const BADGE_CLR = { PDF: 'pdf', DOC: 'doc', PPT: 'ppt', Image: 'img' };

// ── FILTER GROUPS DEF ──
const FILTER_GROUPS = [
  { id: 'type', label: 'Material Type', options: ['Notes', 'Model Papers', 'Question Papers', 'Assignments', 'Lab Reports', 'Textbooks'] },
  { id: 'subject', label: 'Subject', searchable: true, options: ['Mathematics', 'Physics', 'Chemistry', 'Computer Science', 'Biology', 'Law', 'Economics', 'Civil Engg', 'Electronics'] },
  { id: 'year', label: 'Year / Semester', options: ['1st Year', '2nd Year', '3rd Year', '4th Year', 'Sem 1', 'Sem 2', 'Sem 3', 'Sem 4', 'Sem 5', 'Sem 6', 'Sem 7', 'Sem 8'] },
  { id: 'exam', label: 'Exam Type', options: ['Mid-1', 'Mid-2', 'Semester End', 'GATE', 'UPSC', 'JEE'] },
  { id: 'format', label: 'File Format', options: ['PDF', 'DOC', 'PPT', 'Image'] },
  { id: 'rating', label: 'Rating', options: ['4★ & above', '3★ & above'] },
  { id: 'date', label: 'Upload Date', options: ['This Week', 'This Month'] }
];

// ── STATE ──
let state = { search: '', filters: {}, sort: 'downloads', view: 'grid', page: 1, perPage: 12, popTag: '' };

// ── HELPER FUNCTIONS ──
function stars(n) { return '★'.repeat(n) + '☆'.repeat(5 - n); }
function fmt(n) { return n >= 1000 ? (n / 1000).toFixed(1) + 'k' : n; }
function fmtDate(s) { return new Date(s).toLocaleDateString('en-IN', { day: 'numeric', month: 'short', year: 'numeric' }); }
function initials(n) { return n.split(' ').map(p => p[0]).join('').slice(0, 2).toUpperCase(); }

// ── BUILD SIDEBAR ──
function buildFilterHTML(suffix) {
  return FILTER_GROUPS.map(g => {
    const searchHtml = g.searchable ? `<input type="text" class="subject-search" placeholder="Search subjects..." oninput="filterSubjectList(this, 'fg-${g.id}-${suffix}')">` : '';
    const optionsHtml = g.options.map(o => `
      <label class="filter-check">
        <input type="checkbox" data-group="${g.id}" data-val="${o}" onchange="onFilterChange()"> ${o}
      </label>
    `).join('');
    return `
      <div class="filter-group" id="fg-${g.id}-${suffix}">
        <div class="filter-group-header" onclick="toggleFilterGroup(this)">
          <span>${g.label}</span>
          <span class="fg-arrow">▾</span>
        </div>
        <div class="filter-group-body">
          ${searchHtml}
          ${optionsHtml}
        </div>
      </div>
    `;
  }).join('');
}

function toggleFilterGroup(el) { el.parentElement.classList.toggle('open'); }

function filterSubjectList(inp, gid) {
  const q = inp.value.toLowerCase();
  const checks = document.querySelectorAll(`#${gid} .filter-check`);
  checks.forEach(lbl => {
    lbl.style.display = lbl.textContent.toLowerCase().includes(q) ? '' : 'none';
  });
}

// ── RENDERING ──
function renderCard(m) {
  const user = window.NoteNestAuth ? window.NoteNestAuth.getUser() : null;
  const isBookmarked = user && user.bookmarks && user.bookmarks.includes(m.id);
  const icon = ICONS[m.subject] || '📄';
  const badge = BADGE_CLR[m.format] || 'pdf';
  const isListView = state.view === 'list';

  // Card element
  const card = document.createElement('article');
  card.className = 'mat-card card-anim';
  
  // Thumb
  const thumb = document.createElement('div');
  thumb.className = 'mat-thumb';
  thumb.innerHTML = `<span class="mat-thumb-icon">${icon}</span><span class="mat-badge ${badge}">${m.format}</span>`;
  
  // Body
  const body = document.createElement('div');
  body.className = 'mat-card-body';
  
  const title = document.createElement('a');
  title.href = `material.html?id=${m.id}`;
  title.className = 'mat-title';
  title.textContent = m.title;
  title.style.textDecoration = 'none';
  title.style.color = 'inherit';
  
  const tags = document.createElement('div');
  tags.className = 'mat-tags';
  [m.subject, m.semester, m.year].forEach(t => {
    if(!t) return;
    const tag = document.createElement('span');
    tag.className = 'mat-tag';
    tag.textContent = t;
    tags.appendChild(tag);
  });
  
  body.appendChild(title);
  body.appendChild(tags);
  
  if (isListView) {
    const desc = document.createElement('div');
    desc.className = 'mat-desc';
    desc.textContent = m.desc || '';
    body.appendChild(desc);
  }
  
  const uploader = document.createElement('div');
  uploader.className = 'mat-uploader';
  uploader.innerHTML = `<div class="mat-avatar">${initials(m.uploader || 'A')}</div> ${m.uploader || 'Anonymous'} • ${fmtDate(m.date)}`;
  
  const ratingRow = document.createElement('div');
  ratingRow.className = 'mat-rating-row';
  ratingRow.innerHTML = `
    <span class="mat-stars">${stars(m.rating || 5)}</span>
    <span class="mat-dl-count">
      <svg viewBox="0 0 24 24"><path d="M21 15v4a2 2 0 01-2 2H5a2 2 0 01-2-2v-4M7 10l5 5 5-5M12 15V3"/></svg>
      ${fmt(m.downloads || 0)}
    </span>
  `;
  
  const actions = document.createElement('div');
  actions.className = 'mat-actions';
  
  const dlBtn = document.createElement('button');
  dlBtn.className = 'mat-download-btn';
  dlBtn.innerHTML = `<svg viewBox="0 0 24 24" style="width:13px;height:13px;stroke:currentColor;fill:none;stroke-width:2.5;stroke-linecap:round;stroke-linejoin:round"><path d="M21 15v4a2 2 0 01-2 2H5a2 2 0 01-2-2v-4M7 10l5 5 5-5M12 15V3"/></svg> Download`;
  dlBtn.onclick = (e) => {
    e.preventDefault();
    e.stopPropagation();
    if(window.NoteNestData) {
      window.NoteNestData.incrementDownloads(m.id);
      if(window.NoteNestAuth && window.NoteNestAuth.isLoggedIn()){
        window.NoteNestData.saveDownload(m.id);
      }
    }
    if(window.NoteNestToast) window.NoteNestToast.show('Download started for ' + m.title, 'success');
    renderAll();
  };
  
  const bkBtn = document.createElement('button');
  bkBtn.className = 'mat-bookmark-btn' + (isBookmarked ? ' saved' : '');
  bkBtn.innerHTML = `<svg viewBox="0 0 24 24"><path d="M19 21l-7-5-7 5V5a2 2 0 012-2h10a2 2 0 012 2z"/></svg>`;
  bkBtn.onclick = (e) => {
    e.preventDefault();
    e.stopPropagation();
    if (window.NoteNestAuth && !window.NoteNestAuth.isLoggedIn()) {
      if(window.NoteNestToast) window.NoteNestToast.show('Please log in to save bookmarks.', 'error');
      setTimeout(() => window.location.href = 'auth.html', 1500);
      return;
    }
    if(window.NoteNestData) {
      window.NoteNestData.saveBookmark(m.id);
      const isNowSaved = !isBookmarked;
      if(window.NoteNestToast) window.NoteNestToast.show(isNowSaved ? 'Saved to Bookmarks' : 'Removed from Bookmarks', 'success');
      renderAll();
    }
  };
  
  actions.appendChild(dlBtn);
  actions.appendChild(bkBtn);
  
  body.appendChild(uploader);
  body.appendChild(ratingRow);
  body.appendChild(actions);
  
  card.appendChild(thumb);
  card.appendChild(body);
  
  return card;
}

function filterMaterials() {
  if (!window.NoteNestData) return [];
  let items = window.NoteNestData.getAll();
  
  // Apply Search
  if (state.search) {
    items = window.NoteNestData.search(state.search, items);
  }
  
  // Apply specific popular tag (fast filter)
  if (state.popTag) {
    items = items.filter(m => m.subject === state.popTag || m.exam === state.popTag);
  }
  
  // Apply checkbox filters
  if (Object.keys(state.filters).length > 0) {
    items = window.NoteNestData.filter(state.filters, items);
  }
  
  // Sort
  items = window.NoteNestData.sort(items, state.sort);
  
  return items;
}

function renderAll() {
  const items = filterMaterials();
  const perPage = state.perPage;
  const pages = Math.ceil(items.length / perPage) || 1;
  if (state.page > pages) state.page = 1;
  const startIdx = (state.page - 1) * perPage;
  const pageItems = items.slice(startIdx, startIdx + perPage);

  document.getElementById('resultCount').textContent = items.length;
  
  const grid = document.getElementById('resultsGrid');
  grid.innerHTML = '';
  
  const empty = document.getElementById('emptyState');
  const pagination = document.getElementById('pagination');
  
  if (items.length === 0) {
    empty.style.display = 'block';
    pagination.style.display = 'none';
  } else {
    empty.style.display = 'none';
    pagination.style.display = 'flex';
    pageItems.forEach((m, idx) => {
      const card = renderCard(m);
      card.style.animationDelay = (idx * 0.05) + 's';
      grid.appendChild(card);
    });
  }
  
  renderPagination(items.length);
  renderChips();
}

function renderPagination(total) {
  const maxPages = Math.ceil(total / state.perPage) || 1;
  const btns = document.getElementById('pageBtns');
  btns.innerHTML = '';
  
  const mkBtn = (label, p, isActive) => {
    const b = document.createElement('button');
    b.className = 'page-btn' + (isActive ? ' active' : '');
    b.innerHTML = label;
    b.disabled = p < 1 || p > maxPages;
    b.onclick = () => { state.page = p; renderAll(); window.scrollTo({top: 400, behavior: 'smooth'}); };
    return b;
  };
  
  btns.appendChild(mkBtn('←', state.page - 1));
  for (let i = 1; i <= maxPages; i++) {
    if (i === 1 || i === maxPages || (i >= state.page - 1 && i <= state.page + 1)) {
      btns.appendChild(mkBtn(i, i, i === state.page));
    } else if (i === state.page - 2 || i === state.page + 2) {
      const dot = document.createElement('span'); dot.textContent = '...'; btns.appendChild(dot);
    }
  }
  btns.appendChild(mkBtn('→', state.page + 1));
}

function renderChips() {
  const container = document.getElementById('activeChips');
  container.innerHTML = '';
  let count = 0;
  
  Object.keys(state.filters).forEach(g => {
    state.filters[g].forEach(v => {
      count++;
      const chip = document.createElement('div');
      chip.className = 'chip';
      chip.innerHTML = `${v} <button onclick="removeFilter('${g}','${v}')">✕</button>`;
      container.appendChild(chip);
    });
  });
  
  if (state.popTag) {
    count++;
    const chip = document.createElement('div');
    chip.className = 'chip';
    chip.innerHTML = `#${state.popTag} <button onclick="removePopTag()">✕</button>`;
    container.appendChild(chip);
  }
  
  const fCount = document.getElementById('filterCount');
  if (fCount) {
    fCount.textContent = count;
    fCount.style.display = count > 0 ? 'inline-block' : 'none';
  }
}

function removeFilter(g, v) {
  const cb = document.querySelector(`input[data-group="${g}"][data-val="${v}"]`);
  if (cb) cb.checked = false;
  onFilterChange();
}
function removePopTag() {
  state.popTag = '';
  document.querySelectorAll('.pop-tag').forEach(b => b.classList.remove('active'));
  renderAll();
}

function onFilterChange() {
  const filters = {};
  document.querySelectorAll('input[type="checkbox"]:checked').forEach(cb => {
    const g = cb.dataset.group;
    if (!filters[g]) filters[g] = [];
    filters[g].push(cb.dataset.val);
  });
  state.filters = filters;
  state.page = 1;
  renderAll();
}

function clearAllFilters() {
  document.querySelectorAll('input[type="checkbox"]').forEach(cb => cb.checked = false);
  state.filters = {};
  state.search = '';
  state.popTag = '';
  state.page = 1;
  document.getElementById('searchInput').value = '';
  document.querySelectorAll('.pop-tag').forEach(b => b.classList.remove('active'));
  renderAll();
}

// ── EVENTS ──
document.addEventListener('DOMContentLoaded', () => {
  // Build sidebars
  document.getElementById('filtersDesktop').innerHTML = buildFilterHTML('d');
  document.getElementById('sidebarInner').innerHTML = `
    <div class="sidebar-header"><h3>Filters</h3><button class="clear-all-btn" onclick="clearAllFilters()">Clear All</button></div>
    ${buildFilterHTML('m')}
    <div class="filter-actions"><button class="apply-btn" onclick="closeDrawer()">Apply</button></div>
  `;
  
  // Open first 2 groups
  document.querySelectorAll('.filter-group').forEach((fg, i) => { if (i < 2) fg.classList.add('open'); });
  
  // Hero animations
  setTimeout(() => {
    document.querySelectorAll('.page-hero .fade-in').forEach((el, i) => {
      setTimeout(() => el.classList.add('visible'), i * 150);
    });
  }, 100);
  
  // Search
  document.getElementById('searchInput').oninput = (e) => { state.search = e.target.value; state.page = 1; renderAll(); };
  document.getElementById('searchBtn').onclick = () => renderAll();
  
  // Tags
  document.querySelectorAll('.pop-tag').forEach(btn => {
    btn.onclick = () => {
      const tag = btn.dataset.tag;
      if (state.popTag === tag) { state.popTag = ''; btn.classList.remove('active'); }
      else { state.popTag = tag; document.querySelectorAll('.pop-tag').forEach(b => b.classList.remove('active')); btn.classList.add('active'); }
      state.page = 1; renderAll();
    };
  });
  
  // Controls
  document.getElementById('sortSelect').onchange = (e) => { state.sort = e.target.value; renderAll(); };
  document.getElementById('perPageSelect').onchange = (e) => { state.perPage = parseInt(e.target.value); state.page = 1; renderAll(); };
  
  // View Toggle
  document.getElementById('gridViewBtn').onclick = () => { state.view = 'grid'; document.getElementById('resultsGrid').classList.remove('list-view'); renderAll(); };
  document.getElementById('listViewBtn').onclick = () => { state.view = 'list'; document.getElementById('resultsGrid').classList.add('list-view'); renderAll(); };
  
  // Mobile Drawer
  const btn = document.getElementById('mobileFilterBtn');
  const drawer = document.getElementById('sidebarDrawer');
  const overlay = document.getElementById('filterOverlay');
  if(btn) btn.onclick = () => { drawer.classList.add('open'); overlay.classList.add('open'); };
  if(overlay) overlay.onclick = closeDrawer;
  if(document.getElementById('drawerClose')) document.getElementById('drawerClose').onclick = closeDrawer;
  
  function closeDrawer() {
    drawer.classList.remove('open');
    overlay.classList.remove('open');
  }

  // Initial render
  renderAll();
});

// Global exposure for debugging
window.renderAll = renderAll;
window.state = state;
window.clearAllFilters = clearAllFilters;
window.onFilterChange = onFilterChange;
window.removeFilter = removeFilter;
window.removePopTag = removePopTag;
window.toggleFilterGroup = toggleFilterGroup;
window.filterSubjectList = filterSubjectList;
window.closeDrawer = () => {
  document.getElementById('sidebarDrawer').classList.remove('open');
  document.getElementById('filterOverlay').classList.remove('open');
};

// Scroll listener
const nav = document.getElementById('navbar');
const btop = document.getElementById('backTop');
window.onscroll = () => {
  if (window.scrollY > 50) nav.classList.add('scrolled'); else nav.classList.remove('scrolled');
  if (window.scrollY > 400) btop.classList.add('show'); else btop.classList.remove('show');
};

// Hamburger
const ham = document.getElementById('hamburger');
const mobileMenu = document.getElementById('mobileMenu');
if(ham) ham.onclick = () => { ham.classList.toggle('open'); mobileMenu.classList.toggle('open'); };
