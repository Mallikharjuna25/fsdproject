// ── SUBJECTS ──
const SUBJECTS = [
  'Mathematics','Physics','Chemistry','Computer Science','Biology','Electronics',
  'Civil Engg','Mechanical Engg','Electrical Engg','Data Science','Artificial Intelligence',
  'Economics','Law','History','Geography','Political Science','Sociology','Psychology',
  'English Literature','Philosophy','Commerce','Accountancy','Finance','Marketing',
  'Pharmacy','Nursing','Architecture','Environmental Science','Biotechnology','Agriculture'
];

// ── TAG SUGGESTIONS ──
const TAG_SUGGESTIONS = [
  'GATE','UPSC','JEE','NEET','JNTUA','VTU','Anna University',
  'notes','solved','previous year','cheat sheet','formula',
  'Sem 1','Sem 2','Sem 3','Sem 4','Sem 5','Sem 6',
  '2024','2025','exam prep','quick revision','important questions'
];

// ── STATE ──
let uploadedFiles = [];
let tags = [];
let selectedSubject = '';

// ── INIT ──
document.addEventListener('DOMContentLoaded', () => {
  if (window.NoteNestAuth) {
    if (!window.NoteNestAuth.requireAuth()) return; // Redirects to login
    const user = window.NoteNestAuth.getUser();
    if (user) {
      const nm = document.getElementById('uploaderName');
      const em = document.getElementById('uploaderEmail');
      if (nm) nm.value = user.name || '';
      if (em) em.value = user.email || '';
    }
  }

  buildSubjectOptions();
  loadRecentUploads();
  loadCommunityStats();
  checkDraft();
  initScrollBehavior();
  initDragDrop();
  initFormValidation();
  initTagInput();
  initSubjectSelect();

  // char counters
  charCounter('matTitle','titleCounter',120);
  charCounter('matDesc','descCounter',500);
});

// ── SCROLL & NAV ──
function initScrollBehavior() {
  const nav = document.getElementById('navbar');
  const backTop = document.getElementById('backTop');
  window.addEventListener('scroll', () => {
    nav.classList.toggle('scrolled', window.scrollY > 50);
    backTop.classList.toggle('show', window.scrollY > 400);
  }, { passive: true });
  const ham = document.getElementById('hamburger');
  const mob = document.getElementById('mobileMenu');
  if (ham) ham.onclick = () => { ham.classList.toggle('open'); mob.classList.toggle('open'); };
}

// ── CHAR COUNTER ──
function charCounter(inputId, counterId, max) {
  const inp = document.getElementById(inputId);
  const ctr = document.getElementById(counterId);
  if (!inp || !ctr) return;
  const update = () => {
    const len = inp.value.length;
    ctr.textContent = len + ' / ' + max;
    ctr.className = 'char-counter' + (len >= max ? ' over' : len >= max * 0.85 ? ' warn' : '');
  };
  inp.addEventListener('input', update);
  update();
}

// ── FILE DRAG & DROP ──
function initDragDrop() {
  const zone = document.getElementById('dropZone');
  const fileInput = document.getElementById('fileInput');

  zone.addEventListener('dragover', e => { e.preventDefault(); zone.classList.add('drag-over'); });
  zone.addEventListener('dragleave', () => zone.classList.remove('drag-over'));
  zone.addEventListener('drop', e => {
    e.preventDefault();
    zone.classList.remove('drag-over');
    handleFiles([...e.dataTransfer.files]);
  });

  fileInput.addEventListener('change', () => handleFiles([...fileInput.files]));
}

function getFileIcon(name) {
  const ext = name.split('.').pop().toLowerCase();
  const map = { pdf: { icon: '📄', cls: 'pdf' }, doc: { icon: '📝', cls: 'doc' }, docx: { icon: '📝', cls: 'doc' }, ppt: { icon: '📊', cls: 'ppt' }, pptx: { icon: '📊', cls: 'ppt' }, jpg: { icon: '🖼️', cls: 'img' }, jpeg: { icon: '🖼️', cls: 'img' }, png: { icon: '🖼️', cls: 'img' } };
  return map[ext] || { icon: '📎', cls: 'other' };
}

function fmtSize(bytes) {
  if (bytes < 1024) return bytes + ' B';
  if (bytes < 1048576) return (bytes / 1024).toFixed(1) + ' KB';
  return (bytes / 1048576).toFixed(1) + ' MB';
}

const ALLOWED_EXTS = ['pdf','doc','docx','ppt','pptx','jpg','jpeg','png'];
const MAX_SIZE = 50 * 1024 * 1024;

function handleFiles(files) {
  const remaining = 5 - uploadedFiles.length;
  if (remaining <= 0) { showToast('Maximum 5 files allowed'); return; }
  const toAdd = files.slice(0, remaining);
  toAdd.forEach(file => {
    const ext = file.name.split('.').pop().toLowerCase();
    if (!ALLOWED_EXTS.includes(ext)) { showToast('Unsupported file type: ' + file.name); return; }
    if (file.size > MAX_SIZE) { showToast(file.name + ' exceeds 50MB limit'); return; }
    uploadedFiles.push(file);
    renderFileItem(file);
  });
  checkSubmitBtn();
}

function renderFileItem(file) {
  const list = document.getElementById('fileList');
  const { icon, cls } = getFileIcon(file.name);
  const item = document.createElement('div');
  item.className = 'file-item';
  item.id = 'fi-' + file.name.replace(/[^a-z0-9]/gi, '_');
  item.innerHTML = `
    <div class="file-type-icon ${cls}">${icon}</div>
    <div class="file-info">
      <div class="file-name">${file.name}</div>
      <div class="file-size">${fmtSize(file.size)}</div>
    </div>
    <span class="file-status uploading">Queued</span>
    <button class="file-remove" onclick="removeFile('${file.name.replace(/'/g,"\\'")}',this)" title="Remove">✕</button>
    <div class="file-progress" style="width:0%"></div>
  `;
  list.appendChild(item);
  // simulate progress
  let pct = 0;
  const bar = item.querySelector('.file-progress');
  const status = item.querySelector('.file-status');
  const interval = setInterval(() => {
    pct = Math.min(pct + Math.random() * 18 + 4, 100);
    bar.style.width = pct + '%';
    if (pct >= 100) {
      clearInterval(interval);
      status.textContent = 'Ready';
      status.className = 'file-status done';
    }
  }, 180);
}

function removeFile(name, btn) {
  uploadedFiles = uploadedFiles.filter(f => f.name !== name);
  const item = btn.closest('.file-item');
  item.style.opacity = '0';
  item.style.transform = 'scale(.95)';
  item.style.transition = 'all .25s ease';
  setTimeout(() => item.remove(), 250);
  checkSubmitBtn();
}

// ── SUBJECT SELECT ──
function buildSubjectOptions() {
  const container = document.getElementById('subjectOptions');
  if (!container) return;
  SUBJECTS.forEach(s => {
    const opt = document.createElement('div');
    opt.className = 'custom-select-option';
    opt.textContent = s;
    opt.onclick = () => selectSubject(s);
    container.appendChild(opt);
  });
}

function initSubjectSelect() {
  const trigger = document.getElementById('subjectTrigger');
  const dropdown = document.getElementById('subjectDropdown');
  const search = document.getElementById('subjectSearch');

  trigger.onclick = () => {
    const isOpen = dropdown.classList.contains('open');
    dropdown.classList.toggle('open', !isOpen);
    trigger.classList.toggle('open', !isOpen);
    trigger.setAttribute('aria-expanded', !isOpen);
    if (!isOpen) setTimeout(() => search && search.focus(), 50);
  };

  // Close on outside click
  document.addEventListener('click', e => {
    if (!document.getElementById('subjectSelect').contains(e.target)) {
      dropdown.classList.remove('open');
      trigger.classList.remove('open');
    }
  });

  // Search filter
  if (search) {
    search.addEventListener('input', () => {
      const q = search.value.toLowerCase();
      document.querySelectorAll('.custom-select-option').forEach(opt => {
        opt.style.display = opt.textContent.toLowerCase().includes(q) ? '' : 'none';
      });
    });
  }
}

function selectSubject(val) {
  selectedSubject = val;
  document.getElementById('subjectLabel').textContent = val;
  document.getElementById('subjectLabel').style.color = 'var(--clr-white)';
  document.getElementById('subjectValue').value = val;
  document.getElementById('subjectDropdown').classList.remove('open');
  document.getElementById('subjectTrigger').classList.remove('open');
  document.querySelectorAll('.custom-select-option').forEach(o => o.classList.toggle('selected', o.textContent === val));
  document.getElementById('subjectError').classList.remove('show');
  checkSubmitBtn();
}

// ── TAG INPUT ──
function initTagInput() {
  const input = document.getElementById('tagInput');
  const sugBox = document.getElementById('tagSuggestions');

  input.addEventListener('keydown', e => {
    if ((e.key === 'Enter' || e.key === ',') && input.value.trim()) {
      e.preventDefault();
      addTag(input.value.trim());
      input.value = '';
      sugBox.classList.remove('open');
    } else if (e.key === 'Backspace' && !input.value && tags.length) {
      removeTag(tags[tags.length - 1]);
    }
  });

  input.addEventListener('input', () => {
    const q = input.value.toLowerCase().trim();
    if (!q) { sugBox.classList.remove('open'); return; }
    const matches = TAG_SUGGESTIONS.filter(t => t.toLowerCase().includes(q) && !tags.includes(t));
    if (!matches.length) { sugBox.classList.remove('open'); return; }
    sugBox.innerHTML = '';
    matches.slice(0, 6).forEach(t => {
      const item = document.createElement('div');
      item.className = 'tag-suggestion-item';
      item.textContent = t;
      item.onclick = () => { addTag(t); input.value = ''; sugBox.classList.remove('open'); };
      sugBox.appendChild(item);
    });
    sugBox.classList.add('open');
  });

  document.addEventListener('click', e => {
    if (!document.getElementById('tagsWrapper').contains(e.target)) sugBox.classList.remove('open');
  });
}

function addTag(val) {
  if (tags.length >= 10 || tags.includes(val) || !val) return;
  tags.push(val);
  renderTags();
  updateTagsValue();
}

function removeTag(val) {
  tags = tags.filter(t => t !== val);
  renderTags();
  updateTagsValue();
}

function renderTags() {
  const pillsDiv = document.getElementById('tagPills');
  pillsDiv.innerHTML = '';
  tags.forEach(t => {
    const pill = document.createElement('span');
    pill.className = 'tag-pill';
    pill.innerHTML = '#' + t + ' <button type="button" onclick="removeTag(\'' + t.replace(/'/g, "\\'") + '\')" title="Remove tag">✕</button>';
    pillsDiv.appendChild(pill);
  });
}

function updateTagsValue() {
  document.getElementById('tagsValue').value = tags.join(',');
}

// ── VISIBILITY & LICENSE ──
function updateVisCard() {
  const pub = document.querySelector('input[name=visibility][value=public]');
  document.getElementById('visPublic').classList.toggle('selected', pub.checked);
  document.getElementById('visUnlisted').classList.toggle('selected', !pub.checked);
}

function selectLicense(id) {
  document.getElementById('licFree').classList.toggle('selected', id === 'licFree');
  document.getElementById('licAttr').classList.toggle('selected', id === 'licAttr');
  if (id === 'licFree') document.querySelector('input[name=license][value=free]').checked = true;
  else document.querySelector('input[name=license][value=attribution]').checked = true;
}

// ── FORM VALIDATION ──
function initFormValidation() {
  const form = document.getElementById('uploadForm');

  // Real-time validation
  const fields = [
    { id: 'matTitle', errId: 'titleError', validate: v => v.trim().length >= 5, msg: 'Title must be at least 5 characters' },
    { id: 'matType', errId: 'typeError', validate: v => v !== '', msg: 'Please select material type' },
    { id: 'matYear', errId: 'yearError', validate: v => v !== '', msg: 'Please select year/semester' },
    { id: 'uploaderName', errId: 'nameError', validate: v => v.trim().length >= 2, msg: 'Name must be at least 2 characters' },
    { id: 'uploaderEmail', errId: 'emailError', validate: v => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v), msg: 'Please enter a valid email' }
  ];

  fields.forEach(({ id, errId, validate, msg }) => {
    const el = document.getElementById(id);
    if (!el) return;
    el.addEventListener('blur', () => validateField(el, errId, validate, msg));
    el.addEventListener('input', () => { if (el.classList.contains('invalid')) validateField(el, errId, validate, msg); checkSubmitBtn(); });
  });

  form.addEventListener('submit', e => {
    e.preventDefault();
    if (!validateAll()) return;
    startUpload();
  });
}

function validateField(el, errId, validate, msg) {
  const err = document.getElementById(errId);
  const valid = validate(el.value);
  el.classList.toggle('invalid', !valid);
  el.classList.toggle('valid', valid);
  if (err) { err.textContent = msg; err.classList.toggle('show', !valid); }
  return valid;
}

function validateAll() {
  let ok = true;
  const checks = [
    { id: 'matTitle', errId: 'titleError', validate: v => v.trim().length >= 5, msg: 'Title must be at least 5 characters' },
    { id: 'matType', errId: 'typeError', validate: v => v !== '', msg: 'Please select material type' },
    { id: 'matYear', errId: 'yearError', validate: v => v !== '', msg: 'Please select year/semester' },
    { id: 'uploaderName', errId: 'nameError', validate: v => v.trim().length >= 2, msg: 'Please enter your name' },
    { id: 'uploaderEmail', errId: 'emailError', validate: v => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v), msg: 'Please enter a valid email' }
  ];
  checks.forEach(({ id, errId, validate, msg }) => {
    const el = document.getElementById(id);
    if (!validateField(el, errId, validate, msg)) ok = false;
  });
  if (!selectedSubject) {
    document.getElementById('subjectError').classList.add('show');
    ok = false;
  }
  if (uploadedFiles.length === 0) {
    showToast('Please upload at least one file');
    ok = false;
  }
  return ok;
}

function checkSubmitBtn() {
  const btn = document.getElementById('submitBtn');
  const title = document.getElementById('matTitle').value.trim();
  const type = document.getElementById('matType').value;
  const year = document.getElementById('matYear').value;
  const name = document.getElementById('uploaderName').value.trim();
  const email = document.getElementById('uploaderEmail').value.trim();
  const emailOk = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
  const ready = title.length >= 5 && type && year && name.length >= 2 && emailOk && selectedSubject && uploadedFiles.length > 0;
  btn.disabled = !ready;
}

// ── UPLOAD SIMULATION ──
function startUpload() {
  const modal = document.getElementById('uploadModal');
  const progress = document.getElementById('modalProgress');
  const status = document.getElementById('modalStatus');
  const icon = document.getElementById('modalIcon');
  const title = document.getElementById('modalTitle');
  const sub = document.getElementById('modalSub');
  const actions = document.getElementById('modalActions');
  const bar = document.getElementById('modalProgressWrap');

  modal.classList.add('open');
  icon.textContent = '📤';
  title.textContent = 'Uploading...';
  sub.textContent = 'Please wait while we process your material';
  bar.style.display = 'block';
  actions.style.display = 'none';
  progress.style.width = '0%';

  const stages = [
    { pct: 20, text: 'Uploading files...', delay: 600 },
    { pct: 50, text: 'Processing content...', delay: 1200 },
    { pct: 75, text: 'Generating preview...', delay: 1800 },
    { pct: 90, text: 'Saving metadata...', delay: 2400 },
    { pct: 100, text: 'Almost done!', delay: 3000 }
  ];

  stages.forEach(({ pct, text, delay }) => {
    setTimeout(() => {
      progress.style.width = pct + '%';
      document.getElementById('modalStatus').textContent = text;
    }, delay);
  });

  setTimeout(() => {
    icon.textContent = '🎉';
    title.textContent = 'Upload Successful!';
    sub.textContent = 'Your material is now live and helping students!';
    bar.style.display = 'none';
    document.getElementById('modalStatus').textContent = '';
    actions.style.display = 'flex';
    launchConfetti();

    // Save to real NoteNestData
    if (window.NoteNestData && window.NoteNestAuth) {
      const user = window.NoteNestAuth.getUser();
      const newMat = {
        id: 'mat_' + Date.now(),
        title: document.getElementById('matTitle').value.trim(),
        description: document.getElementById('matDesc').value.trim(),
        type: document.getElementById('matType').value,
        subject: selectedSubject || 'General',
        department: "General",
        course: document.getElementById('matExam').value.trim() || 'General',
        semester: document.getElementById('matYear').value,
        year: document.getElementById('matAcYear').value.trim() || 'N/A',
        examType: "Class Notes",
        university: document.getElementById('matUniv').value.trim() || 'Global',
        tags: tags,
        fileFormat: uploadedFiles[0] ? uploadedFiles[0].name.split('.').pop().toUpperCase() : 'PDF',
        fileSize: uploadedFiles[0] ? fmtSize(uploadedFiles[0].size) : '0 MB',
        pages: Math.floor(Math.random() * 50) + 1,
        uploadedBy: user ? user.name : document.getElementById('uploaderName').value.trim(),
        uploaderId: user ? user.id : 'guest',
        uploadDate: new Date().toISOString().split('T')[0],
        downloads: 0,
        views: 0,
        rating: 0,
        ratingCount: 0,
        comments: []
      };
      window.NoteNestData.saveUpload(newMat);
    }

    saveToRecentUploads();
    clearDraft();
  }, 3600);
}

// ── CONFETTI ──
function launchConfetti() {
  const container = document.getElementById('confettiContainer');
  const colors = ['#f5a623','#22a06b','#ff6b6b','#00b4a6','#ffffff','#1a6b4a'];
  for (let i = 0; i < 80; i++) {
    const piece = document.createElement('div');
    piece.className = 'confetti-piece';
    piece.style.left = Math.random() * 100 + 'vw';
    piece.style.background = colors[Math.floor(Math.random() * colors.length)];
    piece.style.width = (Math.random() * 10 + 6) + 'px';
    piece.style.height = (Math.random() * 10 + 6) + 'px';
    piece.style.borderRadius = Math.random() > 0.5 ? '50%' : '2px';
    piece.style.animationDuration = (Math.random() * 2 + 1.5) + 's';
    piece.style.animationDelay = (Math.random() * 1.5) + 's';
    container.appendChild(piece);
  }
  setTimeout(() => container.innerHTML = '', 5000);
}

// ── RESET FORM ──
function resetForm() {
  document.getElementById('uploadModal').classList.remove('open');
  document.getElementById('uploadForm').reset();
  uploadedFiles = [];
  tags = [];
  selectedSubject = '';
  document.getElementById('fileList').innerHTML = '';
  document.getElementById('tagPills').innerHTML = '';
  document.getElementById('tagsValue').value = '';
  document.getElementById('subjectLabel').textContent = 'Select subject...';
  document.getElementById('subjectLabel').style.color = 'var(--clr-gray2)';
  document.getElementById('subjectValue').value = '';
  document.getElementById('submitBtn').disabled = true;
  document.querySelectorAll('.custom-select-option').forEach(o => o.classList.remove('selected'));
  ['licFree','visPublic'].forEach(id => document.getElementById(id).classList.add('selected'));
  ['licAttr','visUnlisted'].forEach(id => document.getElementById(id).classList.remove('selected'));
  checkSubmitBtn();
}

// ── DRAFT ──
function saveDraft() {
  const draft = {
    title: document.getElementById('matTitle').value,
    desc: document.getElementById('matDesc').value,
    subject: selectedSubject,
    type: document.getElementById('matType').value,
    exam: document.getElementById('matExam').value,
    year: document.getElementById('matYear').value,
    acYear: document.getElementById('matAcYear').value,
    univ: document.getElementById('matUniv').value,
    tags: tags,
    name: document.getElementById('uploaderName').value,
    email: document.getElementById('uploaderEmail').value,
    savedAt: new Date().toISOString()
  };
  localStorage.setItem('nn_upload_draft', JSON.stringify(draft));
  showToast('Draft saved successfully!', 'success');
}

function checkDraft() {
  const raw = localStorage.getItem('nn_upload_draft');
  if (!raw) return;
  try {
    const d = JSON.parse(raw);
    if (d.title || d.subject) {
      document.getElementById('draftBanner').style.display = 'flex';
    }
  } catch {}
}

function restoreDraft() {
  const raw = localStorage.getItem('nn_upload_draft');
  if (!raw) return;
  try {
    const d = JSON.parse(raw);
    if (d.title) document.getElementById('matTitle').value = d.title;
    if (d.desc) document.getElementById('matDesc').value = d.desc;
    if (d.subject) selectSubject(d.subject);
    if (d.type) document.getElementById('matType').value = d.type;
    if (d.exam) document.getElementById('matExam').value = d.exam;
    if (d.year) document.getElementById('matYear').value = d.year;
    if (d.acYear) document.getElementById('matAcYear').value = d.acYear;
    if (d.univ) document.getElementById('matUniv').value = d.univ;
    if (d.tags && Array.isArray(d.tags)) { tags = d.tags; renderTags(); updateTagsValue(); }
    if (d.name) document.getElementById('uploaderName').value = d.name;
    if (d.email) document.getElementById('uploaderEmail').value = d.email;
    // update counters
    ['matTitle','matDesc'].forEach(id => document.getElementById(id).dispatchEvent(new Event('input')));
    checkSubmitBtn();
    showToast('Draft restored!', 'success');
  } catch {}
  document.getElementById('draftBanner').style.display = 'none';
}

function dismissDraft() {
  document.getElementById('draftBanner').style.display = 'none';
}

function clearDraft() {
  localStorage.removeItem('nn_upload_draft');
}

// ── RECENT UPLOADS ──
function saveToRecentUploads() {
  const uploads = JSON.parse(localStorage.getItem('nn_recent_uploads') || '[]');
  uploads.unshift({
    title: document.getElementById('matTitle').value || 'Untitled',
    subject: selectedSubject || 'General',
    date: new Date().toLocaleDateString('en-IN', { day: 'numeric', month: 'short', year: 'numeric' }),
    icon: '📄'
  });
  localStorage.setItem('nn_recent_uploads', JSON.stringify(uploads.slice(0, 5)));
  loadRecentUploads();
}

function loadRecentUploads() {
  const uploads = JSON.parse(localStorage.getItem('nn_recent_uploads') || '[]');
  const container = document.getElementById('recentUploads');
  if (!uploads.length) {
    container.innerHTML = '<p style="font-size:.85rem;color:var(--clr-gray2);text-align:center;padding:16px 0">No recent uploads yet.</p>';
    return;
  }
  container.innerHTML = uploads.map(u => `
    <div class="recent-upload-item">
      <div class="ru-thumb">${u.icon}</div>
      <div class="ru-info">
        <div class="ru-name">${u.title}</div>
        <div class="ru-date">${u.date}</div>
      </div>
    </div>
  `).join('');
}

// ── COMMUNITY STATS (mock) ──
function loadCommunityStats() {
  function animateNum(el, target, suffix) {
    let cur = 0;
    const step = target / 40;
    const tick = () => {
      cur = Math.min(cur + step, target);
      el.textContent = Math.floor(cur).toLocaleString() + suffix;
      if (cur < target) requestAnimationFrame(tick);
    };
    requestAnimationFrame(tick);
  }
  const obs = new IntersectionObserver(entries => {
    if (!entries[0].isIntersecting) return;
    obs.disconnect();
    animateNum(document.getElementById('statToday'), 47, '');
    animateNum(document.getElementById('statTotal'), 12840, '');
    animateNum(document.getElementById('statContrib'), 3200, '');
  }, { threshold: 0.3 });
  const statsCard = document.getElementById('statToday');
  if (statsCard) obs.observe(statsCard.closest('.sidebar-card'));
}

// ── TOAST ──
function showToast(msg, type = 'error') {
  const existing = document.getElementById('nn-toast');
  if (existing) existing.remove();
  const toast = document.createElement('div');
  toast.id = 'nn-toast';
  toast.style.cssText = `
    position:fixed;bottom:28px;left:50%;transform:translateX(-50%) translateY(20px);
    background:${type === 'success' ? 'var(--clr-green)' : '#2a1a1a'};
    border:1px solid ${type === 'success' ? 'var(--clr-green-light)' : 'var(--clr-coral)'};
    color:white;padding:12px 24px;border-radius:10px;font-size:.9rem;font-family:var(--ff-body);
    z-index:4000;opacity:0;transition:all .3s ease;white-space:nowrap;
    box-shadow:0 8px 24px rgba(0,0,0,.5);
  `;
  toast.textContent = msg;
  document.body.appendChild(toast);
  requestAnimationFrame(() => { toast.style.opacity = '1'; toast.style.transform = 'translateX(-50%) translateY(0)'; });
  setTimeout(() => { toast.style.opacity = '0'; setTimeout(() => toast.remove(), 300); }, 3000);
}
