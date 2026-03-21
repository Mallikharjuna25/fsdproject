<body>

<!-- BACK TO TOP -->
<button id="backTop" aria-label="Back to top" onclick="window.scrollTo({top:0,behavior:'smooth'})">
  <svg viewBox="0 0 24 24"><path d="M12 19V5M5 12l7-7 7 7"/></svg>
</button>

<!-- NAVBAR -->
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
        <li><a href="browse.html" class="active">Browse</a></li>
        <li><a href="upload.html">Upload</a></li>
        <li><a href="#">Categories</a></li>
        <li><a href="#">About</a></li>
      </ul>
      <a href="upload.html" class="btn-amber nav-cta">Upload ↑</a>
      <button class="hamburger" id="hamburger" aria-label="Toggle menu" title="Menu">
        <span></span><span></span><span></span>
      </button>
    </div>
    <div class="mobile-menu" id="mobileMenu">
      <ul>
        <li><a href="index.html">Home</a></li>
        <li><a href="browse.html">Browse</a></li>
        <li><a href="upload.html">Upload</a></li>
        <li><a href="#">Categories</a></li>
        <li><a href="#">About</a></li>
      </ul>
      <a href="upload.html" class="btn-amber">Upload ↑</a>
    </div>
  </nav>
</header>

<!-- BREADCRUMB -->
<div class="breadcrumb-wrap">
  <div class="container">
    <div class="breadcrumb">
      <a href="browse.html" class="back-btn" title="Go back to Browse">← Back to Browse</a>
      <a href="index.html">Home</a>
      <span class="sep">›</span>
      <a href="browse.html">Browse</a>
      <span class="sep">›</span>
      <a href="browse.html?subject=Chemistry">Chemistry</a>
      <span class="sep">›</span>
      <span class="current">Complete Organic Chemistry Notes - Unit 1 to 4</span>
    </div>
  </div>
</div>

<!-- MAIN CONTENT -->
<main class="container">
  <div class="mat-layout">

    <!-- LEFT COLUMN -->
    <div class="main-column">
      
      <!-- Header Section -->
      <section class="mat-header">
        <div class="mat-meta-row">
          <span class="type-badge">📝 Notes</span>
          <span class="meta-pill">Chemistry</span>
          <span class="meta-pill">Sem 3</span>
          <span class="meta-pill">2023-24</span>
        </div>
        <h1 class="mat-title">Complete Organic Chemistry Notes - Unit 1 to 4</h1>
        
        <div class="mat-stats-row">
          <div class="stat-item">👁 <span>1,240</span> views</div>
          <div class="stat-item">⬇ <span>892</span> downloads</div>
          <div class="stat-item">★ <span>4.7</span> (128 ratings)</div>
        </div>

        <div class="uploader-row">
          <div class="avatar">AS</div>
          <div class="uploader-info">
            <h3 class="uploader-name">Ananya Sharma</h3>
            <div class="upload-date">Uploaded on 12 Oct 2023</div>
          </div>
          <button class="btn-outline" style="padding:6px 14px;font-size:.8rem" onclick="toggleFollow(this)">Follow</button>
        </div>
      </section>

      <!-- Description Card -->
      <section class="desc-card">
        <div class="desc-content" id="descContent">
          <div class="desc-text" id="descText">
            <p>These are comprehensive handwritten notes covering Units 1 through 4 of Organic Chemistry for 2nd Year B.Sc. students (Semester 3).</p>
            <br>
            <p><strong>Topics Covered:</strong></p>
            <ul style="margin-left:20px;margin-top:8px">
              <li>Unit 1: Stereochemistry - Isomerism, Enantiomers, Diastereomers, R/S Configuration.</li>
              <li>Unit 2: Aliphatic Hydrocarbons - Alkanes, Alkenes, Alkynes (Preparation and properties).</li>
              <li>Unit 3: Aromatic Hydrocarbons - Benzene structure, Electrophilic aromatic substitution.</li>
              <li>Unit 4: Alkyl and Aryl Halides - SN1, SN2, E1, E2 mechanisms.</li>
            </ul>
            <br>
            <p>These notes include important reaction mechanisms, named reactions, and solved previous year questions at the end of every unit. Specifically tailored for the latest university syllabus. Highly recommended for quick revision before mid-semester and final exams.</p>
          </div>
          <div class="desc-fade" id="descFade"></div>
        </div>
        <button class="show-more-btn" id="showMoreBtn" onclick="toggleDesc()">Show More ↓</button>
      </section>

      <!-- PDF Preview -->
      <section class="preview-card" id="previewSection">
        <div class="preview-header">
          <div class="preview-title">
            📄 Document Preview <span>(24 pages)</span>
          </div>
          <div class="preview-controls">
            <button class="zoom-btn" onclick="zoomPreview(-0.1)" title="Zoom Out">−</button>
            <button class="zoom-btn" onclick="zoomPreview(0.1)" title="Zoom In">+</button>
            <div style="width:1px;height:16px;background:var(--clr-border);margin:0 8px"></div>
            <button class="prev-btn" id="prevPageBtn" onclick="changePage(-1)" disabled>◀</button>
            <span class="page-counter">Page <span id="currentPage">1</span> of 2</span>
            <button class="next-btn" id="nextPageBtn" onclick="changePage(1)">▶</button>
          </div>
        </div>
        <div class="preview-body">
          <div class="pdf-page-wrapper" id="pdfPageWrapper">
            <div class="pdf-skeleton">
              <div class="sk-title" style="margin-bottom:20px;height:28px"></div>
              <div class="sk-line"></div>
              <div class="sk-line"></div>
              <div class="sk-line short"></div>
              <div class="sk-box"></div>
              <div class="sk-line"></div>
              <div class="sk-line"></div>
              <div class="sk-line half"></div>
            </div>
            <div class="watermark">NOTENEST</div>
          </div>
          <div class="preview-overlay">
            <p>Preview limited to 2 pages.</p>
            <button class="btn-amber" onclick="startDownload()">Download full PDF for free</button>
          </div>
        </div>
      </section>

      <!-- Reviews & Comments -->
      <section class="comments-section">
        <div class="comments-header">
          <h3>Reviews &amp; Comments</h3>
          <span>12 Comments</span>
        </div>

        <!-- Add Comment -->
        <div class="add-comment">
          <div class="avatar">You</div>
          <div class="comment-input-box">
            <div class="rating-input" id="ratingInput" onmouseleave="resetRating()">
              <span onmouseover="hoverRating(1)" onclick="setRating(1)">★</span>
              <span onmouseover="hoverRating(2)" onclick="setRating(2)">★</span>
              <span onmouseover="hoverRating(3)" onclick="setRating(3)">★</span>
              <span onmouseover="hoverRating(4)" onclick="setRating(4)">★</span>
              <span onmouseover="hoverRating(5)" onclick="setRating(5)">★</span>
            </div>
            <textarea class="comment-textarea" id="commentText" placeholder="What did you think of this material? Did it help you?"></textarea>
            <div style="display:flex;justify-content:flex-end">
              <button class="btn-green" onclick="submitComment()" style="padding:10px 24px">Post Review</button>
            </div>
          </div>
        </div>

        <!-- Comment List -->
        <div class="comment-list" id="commentList">
          <div class="comment-item">
            <div class="avatar">RS</div>
            <div class="comment-body">
              <div class="comment-meta">
                <span class="comment-author">Rahul Singh</span>
                <span class="comment-stars">★★★★★</span>
                <span class="comment-date">2 days ago</span>
              </div>
              <p class="comment-text">These notes are a lifesaver! The SN1/SN2 mechanism explanations are super clear. Thanks for sharing Ananya.</p>
              <div class="comment-actions">
                <button class="like-btn" onclick="toggleLike(this)"><svg viewBox="0 0 24 24"><path d="M14 9V5a3 3 0 00-3-3l-4 9v11h11.28a2 2 0 002-1.7l1.38-9a2 2 0 00-2-2.3zM7 22H4a2 2 0 01-2-2v-7a2 2 0 012-2h3"/></svg> <span class="like-count">14</span></button>
                <button class="like-btn" title="Reply">Reply</button>
              </div>
            </div>
          </div>
          
          <div class="comment-item">
            <div class="avatar">MK</div>
            <div class="comment-body">
              <div class="comment-meta">
                <span class="comment-author">Meera Kapoor</span>
                <span class="comment-stars">★★★★☆</span>
                <span class="comment-date">1 week ago</span>
              </div>
              <p class="comment-text">Good notes, covers entirely the 3rd sem syllabus. Hand writing is a bit small but readable. Really helpful for my midterms!</p>
              <div class="comment-actions">
                <button class="like-btn" onclick="toggleLike(this)"><svg viewBox="0 0 24 24"><path d="M14 9V5a3 3 0 00-3-3l-4 9v11h11.28a2 2 0 002-1.7l1.38-9a2 2 0 00-2-2.3zM7 22H4a2 2 0 01-2-2v-7a2 2 0 012-2h3"/></svg> <span class="like-count">8</span></button>
                <button class="like-btn" title="Reply">Reply</button>
              </div>
            </div>
          </div>
          
          <div class="comment-item">
            <div class="avatar">VP</div>
            <div class="comment-body">
              <div class="comment-meta">
                <span class="comment-author">Varun Patel</span>
                <span class="comment-stars">★★★★★</span>
                <span class="comment-date">3 weeks ago</span>
              </div>
              <p class="comment-text">Best organic chemistry notes on this platform. The previous year solved questions at the end of Unit 2 really helped me pass.</p>
              <div class="comment-actions">
                <button class="like-btn" onclick="toggleLike(this)"><svg viewBox="0 0 24 24"><path d="M14 9V5a3 3 0 00-3-3l-4 9v11h11.28a2 2 0 002-1.7l1.38-9a2 2 0 00-2-2.3zM7 22H4a2 2 0 01-2-2v-7a2 2 0 012-2h3"/></svg> <span class="like-count">32</span></button>
                <button class="like-btn" title="Reply">Reply</button>
              </div>
            </div>
          </div>
        </div>
        
        <button class="btn-outline" style="width:100%;margin-top:24px" onclick="this.innerHTML='Loading...';setTimeout(()=>this.innerHTML='No more comments to load',800)">Load more comments</button>
      </section>

    </div>

    <!-- RIGHT COLUMN (SIDEBAR) -->
    <aside class="sidebar">
      
      <!-- Download Card -->
      <div class="dl-card">
        <div class="dl-file-icon">📄</div>
        <h2 class="dl-filename">Organic_Chem_Sem3_Complete_Ananya.pdf</h2>
        <div class="dl-filesize">Size: 14.2 MB • Format: PDF</div>
        <button class="btn-dl" id="dlBtn" onclick="startDownload()">
          <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
          Download Now
        </button>
        <div class="dl-stats">
          <span>✓</span> Free to use • Requires attribution
        </div>
        <button class="btn-bookmark" id="bookmarkBtn" onclick="toggleBookmark()">
          <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"></path></svg>
          Save for later
        </button>
        <a class="report-link" onclick="showToast('Thank you. We will review this file.','success')">Report this file</a>
      </div>

      <!-- Info Card -->
      <div class="info-card">
        <h3>Material Details</h3>
        <div class="info-list">
          <div class="info-item">
            <span class="info-label">Format</span>
            <span class="info-val" style="font-family:var(--ff-mono)">PDF</span>
          </div>
          <div class="info-item">
            <span class="info-label">Pages</span>
            <span class="info-val" style="font-family:var(--ff-mono)">24</span>
          </div>
          <div class="info-item">
            <span class="info-label">Subject</span>
            <span class="info-val">Chemistry</span>
          </div>
          <div class="info-item">
            <span class="info-label">Material Type</span>
            <span class="info-val">Notes</span>
          </div>
          <div class="info-item">
            <span class="info-label">University</span>
            <span class="info-val">JNTUA</span>
          </div>
          <div class="info-item">
            <span class="info-label">Language</span>
            <span class="info-val">English</span>
          </div>
          <div class="info-item">
            <span class="info-label">Last Updated</span>
            <span class="info-val" style="font-family:var(--ff-mono);font-size:.8rem">15 Oct 2023</span>
          </div>
        </div>
      </div>

      <!-- Tags Card -->
      <div class="tags-card">
        <h3>Tags</h3>
        <div class="tag-pills">
          <a href="browse.html?tag=chemistry" class="tag-pill">#chemistry</a>
          <a href="browse.html?tag=organic" class="tag-pill">#organic</a>
          <a href="browse.html?tag=jntua" class="tag-pill">#jntua</a>
          <a href="browse.html?tag=sem3" class="tag-pill">#sem3</a>
          <a href="browse.html?tag=bsc" class="tag-pill">#bsc</a>
          <a href="browse.html?tag=notes" class="tag-pill">#notes</a>
          <a href="browse.html?tag=sn1sn2" class="tag-pill">#sn1sn2</a>
        </div>
      </div>

      <!-- Share Card -->
      <div class="share-card">
        <h3>Share this material</h3>
        <div class="share-actions">
          <button class="btn-copy" onclick="copyLink()">
            <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
            Copy Link
          </button>
          <button class="btn-social wa" title="Share on WhatsApp" onclick="window.open('https://api.whatsapp.com/send?text=Check out this awesome chemistry material on NoteNest: '+window.location.href, '_blank')">
            <svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51a12.8 12.8 0 0 0-.57-.01c-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 0 1 2.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 0 0-3.48-8.413Z"/></svg>
          </button>
          <button class="btn-social tg" title="Share on Telegram" onclick="window.open('https://t.me/share/url?url='+window.location.href+'&text=Complete Organic Chemistry Notes on NoteNest', '_blank')">
            <svg viewBox="0 0 24 24" width="18" height="18" fill="currentColor"><path d="M11.944 0A12 12 0 0 0 0 12a12 12 0 0 0 12 12 12 12 0 0 0 12-12A12 12 0 0 0 12 0a12 12 0 0 0-.056 0zm4.962 7.224c.1-.002.321.023.465.14a.506.506 0 0 1 .171.325c.016.093.036.306.02.472-.18 1.898-.962 6.502-1.36 8.627-.168.9-.499 1.201-.82 1.23-.696.065-1.225-.46-1.9-.902-1.056-.693-1.653-1.124-2.678-1.8-1.185-.78-.417-1.21.258-1.91.177-.184 3.247-2.977 3.307-3.23.007-.032.014-.15-.056-.212s-.174-.041-.249-.024c-.106.024-1.793 1.14-5.061 3.345-.48.33-.913.49-1.302.48-.428-.008-1.252-.241-1.865-.44-.752-.245-1.349-.374-1.297-.789.027-.216.325-.437.893-.663 3.498-1.524 5.83-2.529 6.998-3.014 3.332-1.386 4.025-1.627 4.476-1.635z"/></svg>
          </button>
        </div>
      </div>

    </aside>

  </div>

  <!-- RELATED MATERIALS -->
  <section class="related-section">
    <h3>Related Materials</h3>
    <div class="related-list">
      <a href="material.html" class="rel-card">
        <div>
          <span class="rel-type">Model Paper</span>
          <div class="rel-title">Organic Chemistry 2022 Final Exam Paper with Solutions</div>
        </div>
        <div class="rel-meta">
          <span>👁 840</span>
          <span>⬇ 450</span>
          <span>★ 4.8</span>
        </div>
      </a>
      <a href="material.html" class="rel-card">
        <div>
          <span class="rel-type">Notes</span>
          <div class="rel-title">Thermodynamics and Kinetic Theory Fundamentals</div>
        </div>
        <div class="rel-meta">
          <span>👁 1,120</span>
          <span>⬇ 720</span>
          <span>★ 4.9</span>
        </div>
      </a>
      <a href="material.html" class="rel-card">
        <div>
          <span class="rel-type">Cheat Sheet</span>
          <div class="rel-title">All Organic Chemistry Name Reactions List</div>
        </div>
        <div class="rel-meta">
          <span>👁 2,450</span>
          <span>⬇ 1,890</span>
          <span>★ 5.0</span>
        </div>
      </a>
      <a href="material.html" class="rel-card">
        <div>
          <span class="rel-type">Lab Report</span>
          <div class="rel-title">Titration and Volumetric Analysis Record</div>
        </div>
        <div class="rel-meta">
          <span>👁 530</span>
          <span>⬇ 120</span>
          <span>★ 4.2</span>
        </div>
      </a>
    </div>
  </section>
</main>

<!-- FOOTER -->
<footer>
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <a href="index.html" class="nav-logo" style="margin-bottom:0">
          <div class="nav-logo-icon"><svg viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8zM14 2v6h6"/></svg></div>
          <span class="nav-logo-text">Note<span>Nest</span></span>
        </a>
        <p>A free platform for students to share &amp; discover study materials. Open-source. Ad-free. Forever.</p>
      </div>
      <div class="footer-col">
        <h4>Platform</h4>
        <ul>
          <li><a href="browse.html">Browse Materials</a></li>
          <li><a href="upload.html">Upload Notes</a></li>
          <li><a href="#">How It Works</a></li>
          <li><a href="#">FAQ</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Categories</h4>
        <ul>
          <li><a href="#">Notes</a></li>
          <li><a href="#">Question Papers</a></li>
          <li><a href="#">Model Papers</a></li>
          <li><a href="#">Lab Reports</a></li>
          <li><a href="#">Cheat Sheets</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Contact</h4>
        <ul>
          <li><a href="mailto:hello@notenest.io">hello@notenest.io</a></li>
          <li><a href="#">Report an Issue</a></li>
          <li><a href="#">Privacy Policy</a></li>
          <li><a href="#">Terms of Service</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <p>© 2025 NoteNest. Made with ♥ for students everywhere.</p>
      <span>// open-source · free-forever</span>
    </div>
  </div>
</footer>

<script src="material.js" charset="utf-8"></script>
</body>
</html>
