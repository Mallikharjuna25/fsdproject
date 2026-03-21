<body>

<!-- NAVBAR (Category View) -->
<header>
  <nav id="navbar">
    <div class="container nav-inner">
      <a href="index.html" class="nav-logo" aria-label="NoteNest home">
        <div class="nav-logo-icon">
          <svg viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8zM14 2v6h6M16 13H8M16 17H8M10 9H8"/></svg>
        </div>
        <span class="nav-logo-text">Note<span>Nest</span></span>
      </a>
      
      <ul class="nav-links">
        <li><a href="index.html">Home</a></li>
        <li><a href="browse.html">Browse</a></li>
        <li><a href="categories.html" class="active">Categories</a></li>
        <li><a href="dashboard.html">Dashboard</a></li>
      </ul>
      
      <a href="upload.html" class="btn-nav">
        Upload<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="17 8 12 3 7 8"></polyline><line x1="12" y1="3" x2="12" y2="15"></line></svg>
      </a>
      
      <button class="hamburger" id="hamburger" aria-label="Toggle menu">
        <span></span><span></span><span></span>
      </button>
    </div>
  </nav>

  <!-- Mobile Menu -->
  <div class="mobile-menu" id="mobileMenu">
    <ul>
      <li><a href="index.html">Home</a></li>
      <li><a href="browse.html">Browse All</a></li>
      <li><a href="categories.html">Categories</a></li>
      <li><a href="dashboard.html">Dashboard</a></li>
      <li><a href="upload.html" style="color:var(--clr-amber)">Upload Material</a></li>
    </ul>
  </div>
</header>

<main>
  <!-- PAGE HEADER -->
  <section class="page-hero">
    <div class="container">
      <h1 class="hero-title reveal">Explore All Categories</h1>
      <p class="section-subtitle reveal" style="animation-delay:0.1s;max-width:600px;margin-left:auto;margin-right:auto">Filter by material type, department, or specific exams to find exactly what you need to succeed.</p>
      
      <div class="hero-search reveal" style="animation-delay:0.2s">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
        <input type="text" id="catSearch" placeholder="Search categories, subjects, or exams..." onkeyup="filterCategories()">
      </div>
    </div>
  </section>

  <!-- POPULAR SUBJECTS THIS WEEK -->
  <section class="container" style="padding-bottom:80px">
    <h2 class="section-title reveal" style="font-size:1.6rem">Trending This Week 🔥</h2>
    <div class="trending-week reveal" style="margin-top:24px">
      
      <a href="browse.html" class="tw-card cat-item" data-text="calculus integration derivatives math">
        <span class="tw-rank">1</span>
        <div class="tw-info">
          <div class="tw-title">Calculus II (Integration)</div>
          <div class="tw-bar-bg"><div class="tw-bar-fill" style="width:85%"></div></div>
          <div class="tw-meta"><span>1,204 downloads</span><span>Maths</span></div>
        </div>
      </a>
      
      <a href="browse.html" class="tw-card cat-item" data-text="object oriented programming java">
        <span class="tw-rank">2</span>
        <div class="tw-info">
          <div class="tw-title">OOPs with Java</div>
          <div class="tw-bar-bg"><div class="tw-bar-fill" style="width:70%"></div></div>
          <div class="tw-meta"><span>890 downloads</span><span>CSE</span></div>
        </div>
      </a>
      
      <a href="browse.html" class="tw-card cat-item" data-text="organic chemistry reactions">
        <span class="tw-rank">3</span>
        <div class="tw-info">
          <div class="tw-title">Organic Chem Reactions</div>
          <div class="tw-bar-bg"><div class="tw-bar-fill" style="width:55%"></div></div>
          <div class="tw-meta"><span>542 downloads</span><span>Science</span></div>
        </div>
      </a>
      
      <a href="browse.html" class="tw-card cat-item" data-text="marketing management business">
        <span class="tw-rank">4</span>
        <div class="tw-info">
          <div class="tw-title">Marketing Management</div>
          <div class="tw-bar-bg"><div class="tw-bar-fill" style="width:40%"></div></div>
          <div class="tw-meta"><span>410 downloads</span><span>Commerce</span></div>
        </div>
      </a>
      
    </div>
  </section>

  <!-- MATERIAL TYPES -->
  <section class="container" style="padding-bottom:80px">
    <h2 class="section-title reveal">Material Types</h2>
    <p class="section-subtitle reveal">Browse by format.</p>
    
    <div class="type-grid">
      <a href="browse.html" class="type-card reveal cat-item" data-text="notes handwritten lectures class">
        <div class="tc-icon">📝</div>
        <h3 class="tc-title">Handwritten Notes</h3>
        <p class="tc-desc">Top-quality notes taken by university toppers.</p>
        <span class="tc-count">4,520 files</span>
      </a>
      <a href="browse.html" class="type-card reveal cat-item" data-text="model papers previous years exams">
        <div class="tc-icon">📄</div>
        <h3 class="tc-title">Model Papers</h3>
        <p class="tc-desc">Test your knowledge with practice setups.</p>
        <span class="tc-count">1,890 files</span>
      </a>
      <a href="browse.html" class="type-card reveal cat-item" data-text="question past exams university">
        <div class="tc-icon">❓</div>
        <h3 class="tc-title">Question Papers</h3>
        <p class="tc-desc">Past year university questions to prepare.</p>
        <span class="tc-count">8,402 files</span>
      </a>
      <a href="browse.html" class="type-card reveal cat-item" data-text="assignments solutions homework">
        <div class="tc-icon">📌</div>
        <h3 class="tc-title">Assignments</h3>
        <p class="tc-desc">Solved assignments for reference.</p>
        <span class="tc-count">2,105 files</span>
      </a>
      <a href="browse.html" class="type-card reveal cat-item" data-text="lab records experiments practicals">
        <div class="tc-icon">🔬</div>
        <h3 class="tc-title">Lab Records</h3>
        <p class="tc-desc">Complete practical logs and manuals.</p>
        <span class="tc-count">945 files</span>
      </a>
      <a href="browse.html" class="type-card reveal cat-item" data-text="textbooks references reading books">
        <div class="tc-icon">📚</div>
        <h3 class="tc-title">Textbooks</h3>
        <p class="tc-desc">Reference books and digital materials.</p>
        <span class="tc-count">1,120 files</span>
      </a>
      <a href="browse.html" class="type-card reveal cat-item" data-text="cheat sheets summaries formulas mind maps">
        <div class="tc-icon">⚡</div>
        <h3 class="tc-title">Cheat Sheets</h3>
        <p class="tc-desc">Quick summaries and formula sheets.</p>
        <span class="tc-count">640 files</span>
      </a>
      <a href="browse.html" class="type-card reveal cat-item" data-text="presentations ppt slides seminars project">
        <div class="tc-icon">💻</div>
        <h3 class="tc-title">Presentations</h3>
        <p class="tc-desc">Slide decks and seminar materials.</p>
        <span class="tc-count">890 files</span>
      </a>
    </div>
  </section>

  <!-- BY DEPARTMENT (ACCORDION) -->
  <section class="container" style="padding-bottom:120px">
    <h2 class="section-title reveal">Browse by Department</h2>
    <p class="section-subtitle reveal">Expand down your field of study.</p>

    <div class="dept-accordion">
      <!-- Engineering -->
      <div class="dept-item reveal cat-item" data-text="engineering cse ece civil mech eee btech">
        <div class="dept-header" onclick="toggleAccordion(this)">
          <div class="dh-left">
            <div class="dh-icon"><svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2l3 5h-6z"/><path d="M5 22h14a2 2 0 002-2v-4H3v4a2 2 0 002 2z"/><path d="M3 16h18"/><path d="M5 12h14"/></svg></div>
            <div>
              <h3 class="dh-title">Engineering & Technology</h3>
              <p class="dh-meta">Explore CSE, ECE, Civil, Mechanical, IT</p>
            </div>
          </div>
          <svg class="dh-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>
        </div>
        <div class="dept-body">
          <div class="dept-content">
            <div class="subject-row">
              <a href="browse.html" class="subject-card">
                <div class="sc-header"><span class="sc-icon">💻</span><span class="sc-count">4K+ files</span></div>
                <h4 class="sc-title">Computer Science & Engineering</h4>
                <div class="sc-link">View Notes <span>→</span></div>
              </a>
              <a href="browse.html" class="subject-card">
                <div class="sc-header"><span class="sc-icon">⚙️</span><span class="sc-count">2K+ files</span></div>
                <h4 class="sc-title">Mechanical Engineering</h4>
                <div class="sc-link">View Notes <span>→</span></div>
              </a>
              <a href="browse.html" class="subject-card">
                <div class="sc-header"><span class="sc-icon">🏗️</span><span class="sc-count">1.5K+ files</span></div>
                <h4 class="sc-title">Civil Engineering</h4>
                <div class="sc-link">View Notes <span>→</span></div>
              </a>
              <a href="browse.html" class="subject-card">
                <div class="sc-header"><span class="sc-icon">🔌</span><span class="sc-count">2.8K+ files</span></div>
                <h4 class="sc-title">Electronics & Comm. (ECE)</h4>
                <div class="sc-link">View Notes <span>→</span></div>
              </a>
            </div>
          </div>
        </div>
      </div>

      <!-- Sciences -->
      <div class="dept-item reveal cat-item" data-text="sciences physics chemistry mathematics biology bsc">
        <div class="dept-header" onclick="toggleAccordion(this)">
          <div class="dh-left">
            <div class="dh-icon"><svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19.79 5A2 2 0 0 0 18 4H6a2 2 0 0 0-1.79 1l-3.32 6.64A2 2 0 0 0 1 12.5V20a2 2 0 0 0 2 2h18a2 2 0 0 0 2-2v-7.5a2 2 0 0 0-.11-.86l-3.3-6.64z"/><path d="M15 4v6l4 2.5"/></svg></div>
            <div>
              <h3 class="dh-title">Fundamental Sciences</h3>
              <p class="dh-meta">Physics, Chemistry, Maths, Biology</p>
            </div>
          </div>
          <svg class="dh-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>
        </div>
        <div class="dept-body">
          <div class="dept-content">
            <div class="subject-row">
              <a href="browse.html" class="subject-card">
                <div class="sc-header"><span class="sc-icon">🧲</span><span class="sc-count">1.2K+ files</span></div>
                <h4 class="sc-title">Advanced Physics</h4>
                <div class="sc-link">View Notes <span>→</span></div>
              </a>
              <a href="browse.html" class="subject-card">
                <div class="sc-header"><span class="sc-icon">⚗️</span><span class="sc-count">980 files</span></div>
                <h4 class="sc-title">Organic & Inorganic Chemistry</h4>
                <div class="sc-link">View Notes <span>→</span></div>
              </a>
              <a href="browse.html" class="subject-card">
                <div class="sc-header"><span class="sc-icon">📐</span><span class="sc-count">2.4K+ files</span></div>
                <h4 class="sc-title">Applied Mathematics & Stats</h4>
                <div class="sc-link">View Notes <span>→</span></div>
              </a>
            </div>
          </div>
        </div>
      </div>
      
      <!-- Management -->
      <div class="dept-item reveal cat-item" data-text="commerce management business bba mba accounting economics finance">
        <div class="dept-header" onclick="toggleAccordion(this)">
          <div class="dh-left">
            <div class="dh-icon"><svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/></svg></div>
            <div>
              <h3 class="dh-title">Commerce & Management</h3>
              <p class="dh-meta">MBA, BBA, Accounting, Marketing</p>
            </div>
          </div>
          <svg class="dh-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>
        </div>
        <div class="dept-body">
          <div class="dept-content">
            <div class="subject-row">
              <a href="browse.html" class="subject-card">
                <div class="sc-header"><span class="sc-icon">📈</span><span class="sc-count">1.1K+ files</span></div>
                <h4 class="sc-title">Business Analytics</h4>
                <div class="sc-link">View Notes <span>→</span></div>
              </a>
              <a href="browse.html" class="subject-card">
                <div class="sc-header"><span class="sc-icon">💼</span><span class="sc-count">850 files</span></div>
                <h4 class="sc-title">Accounting & Finance</h4>
                <div class="sc-link">View Notes <span>→</span></div>
              </a>
              <a href="browse.html" class="subject-card">
                <div class="sc-header"><span class="sc-icon">📱</span><span class="sc-count">620 files</span></div>
                <h4 class="sc-title">Digital Marketing</h4>
                <div class="sc-link">View Notes <span>→</span></div>
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- BY EXAM TYPE -->
  <section class="container" style="padding-bottom:100px">
    <h2 class="section-title reveal">Competitive Exams</h2>
    <p class="section-subtitle reveal">Targeted preparation material for standard tests.</p>
    
    <div class="exam-grid">
      <a href="browse.html" class="exam-card reveal cat-item" data-text="gate engineering graduate aptitude test">
        <div class="ec-badge">G</div>
        <div class="ec-info">
          <h3 class="ec-title">GATE Preparation</h3>
          <p class="ec-desc">Previous papers, core notes, and test series for PG engineering.</p>
        </div>
      </a>
      <a href="browse.html" class="exam-card reveal cat-item" data-text="jee joint entrance exam subjective physics maths chemistry">
        <div class="ec-badge">J</div>
        <div class="ec-info">
          <h3 class="ec-title">JEE Mains & Advanced</h3>
          <p class="ec-desc">Formulas, solutions, and mock tests for UG admissions.</p>
        </div>
      </a>
      <a href="browse.html" class="exam-card reveal cat-item" data-text="neet medical mbbs entrance biology">
        <div class="ec-badge">N</div>
        <div class="ec-info">
          <h3 class="ec-title">NEET Medical</h3>
          <p class="ec-desc">Biology roadmaps, chemistry charts, and question banks.</p>
        </div>
      </a>
      <a href="browse.html" class="exam-card reveal cat-item" data-text="upsc civil services ia as history geography aptitude">
        <div class="ec-badge" style="color:#00b4a6">U</div>
        <div class="ec-info">
          <h3 class="ec-title">UPSC Civil Services</h3>
          <p class="ec-desc">Current affairs, polity notes, and general studies.</p>
        </div>
      </a>
      <a href="browse.html" class="exam-card reveal cat-item" data-text="cat mba admission quantitative verbal logic">
        <div class="ec-badge" style="color:#ff6b6b">C</div>
        <div class="ec-info">
          <h3 class="ec-title">CAT / MBA</h3>
          <p class="ec-desc">Quantitative aptitude, logical reasoning cheatsheets.</p>
        </div>
      </a>
      <a href="browse.html" class="exam-card reveal cat-item" data-text="ielts gre toefl english abroad study">
        <div class="ec-badge" style="color:white">I</div>
        <div class="ec-info">
          <h3 class="ec-title">IELTS / GRE</h3>
          <p class="ec-desc">Vocabulary lists, essay templates, and practice listening.</p>
        </div>
      </a>
    </div>
  </section>

  <!-- TRENDING TAG CLOUD -->
  <section class="container" style="padding-bottom:120px">
    <h2 class="section-title reveal">Trending Search Tags</h2>
    <p class="section-subtitle reveal">What the community is searching for right now.</p>
    
    <div class="cloud-container reveal">
      <div class="tags-wrapper" id="tagCloud">
        <!-- Rendered via JS -->
      </div>
    </div>
  </section>
</main>

<footer>
  <div class="container">
    <div class="ft-grid">
      <div class="ft-brand">
        <a href="index.html" class="nav-logo">
          <div class="nav-logo-icon"><svg viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8zM14 2v6h6"/></svg></div>
          <span class="nav-logo-text">Note<span>Nest</span></span>
        </a>
        <p class="ft-desc">Empowering students by providing a collaborative platform to share, discover, and learn from top-quality study materials globally.</p>
      </div>
      <div>
        <h4 class="ft-title">Platform</h4>
        <ul class="ft-links">
          <li><a href="browse.html">Browse Materials</a></li>
          <li><a href="categories.html">Categories & Subjects</a></li>
          <li><a href="#">Top Contributors</a></li>
          <li><a href="#">University Network</a></li>
        </ul>
      </div>
      <div>
        <h4 class="ft-title">Resources</h4>
        <ul class="ft-links">
          <li><a href="upload.html">Upload Guidelines</a></li>
          <li><a href="#">Copyright Policy</a></li>
          <li><a href="#">FAQ & Support</a></li>
          <li><a href="#">Student Blog</a></li>
        </ul>
      </div>
      <div>
        <h4 class="ft-title">Legal</h4>
        <ul class="ft-links">
          <li><a href="#">Terms of Service</a></li>
          <li><a href="#">Privacy Policy</a></li>
          <li><a href="#">Cookie Settings</a></li>
          <li><a href="#">Contact Us</a></li>
        </ul>
      </div>
    </div>
    <div class="ft-bottom">
      &copy; 2026 NoteNest. Designed for the student community.
    </div>
  </div>
</footer>

<script src="categories.js" charset="utf-8"></script>
</body>
</html>
