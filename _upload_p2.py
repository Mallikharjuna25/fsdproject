p2 = r'''<body>

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
        <li><a href="browse.html">Browse</a></li>
        <li><a href="upload.html" class="active">Upload</a></li>
        <li><a href="#">Categories</a></li>
        <li><a href="#">About</a></li>
      </ul>
      <a href="upload.html" class="btn-amber nav-cta">Upload ↑</a>
      <button class="hamburger" id="hamburger" aria-label="Toggle menu" aria-expanded="false">
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

<!-- PAGE HEADER -->
<section class="page-header">
  <div class="page-header-glow"></div>
  <div class="container">
    <div class="breadcrumb">
      <a href="index.html">Home</a>
      <span>›</span>
      <span style="color:var(--clr-amber)">Upload</span>
    </div>
    <h1>Share Your <em>Study Material</em></h1>
    <p>Help thousands of students by uploading your notes, papers &amp; resources</p>
  </div>
</section>

<!-- DRAFT BANNER (hidden by default) -->
<div class="container">
  <div class="draft-banner" id="draftBanner" style="display:none">
    <span>📝</span>
    <span>You have a saved draft. Would you like to restore it?</span>
    <button onclick="restoreDraft()">Restore Draft</button>
    <button onclick="dismissDraft()" style="background:transparent;border:1px solid rgba(34,160,107,.4);color:var(--clr-green-light);margin-left:6px">Dismiss</button>
  </div>
</div>

<!-- MAIN CONTENT -->
<main class="container" style="padding-top:24px;padding-bottom:80px">
  <div class="upload-layout">

    <!-- === FORM === -->
    <div>
      <form id="uploadForm" novalidate>

        <!-- STEP 1: FILE UPLOAD -->
        <div class="form-card" style="margin-bottom:24px">
          <div class="form-section">
            <div class="form-section-header">
              <div class="step-badge">1</div>
              <div>
                <h2>File Upload</h2>
                <p>Drop your files here or browse to select (up to 5 files, max 50MB each)</p>
              </div>
            </div>
            <!-- Drop Zone -->
            <div class="drop-zone" id="dropZone">
              <input type="file" id="fileInput" multiple accept=".pdf,.doc,.docx,.ppt,.pptx,.jpg,.jpeg,.png" aria-label="Select files"/>
              <span class="drop-zone-icon">📂</span>
              <h3>Drag &amp; Drop your files here</h3>
              <p>Supports PDF, DOC, DOCX, PPT, PPTX, JPG, PNG</p>
              <button type="button" class="btn-green" style="pointer-events:none">Browse Files</button>
              <div class="formats">
                <span class="format-pill">PDF</span>
                <span class="format-pill">DOC</span>
                <span class="format-pill">DOCX</span>
                <span class="format-pill">PPT</span>
                <span class="format-pill">PPTX</span>
                <span class="format-pill">JPG</span>
                <span class="format-pill">PNG</span>
                <span class="format-pill">Max 50MB</span>
              </div>
            </div>
            <!-- File List -->
            <div class="file-list" id="fileList"></div>
          </div>
        </div>

        <!-- STEP 2: MATERIAL DETAILS -->
        <div class="form-card" style="margin-bottom:24px">
          <div class="form-section">
            <div class="form-section-header">
              <div class="step-badge">2</div>
              <div>
                <h2>Material Details</h2>
                <p>Help students find your material easily with clear metadata</p>
              </div>
            </div>

            <div class="field-group">
              <label for="matTitle">Title <span class="req">*</span></label>
              <div class="field-wrapper">
                <input type="text" id="matTitle" name="matTitle" placeholder="e.g. Complete Organic Chemistry Notes - Unit 1 to 4" maxlength="120" required autocomplete="off"/>
              </div>
              <div class="char-counter" id="titleCounter">0 / 120</div>
              <div class="field-error" id="titleError">Please enter a descriptive title</div>
            </div>

            <div class="field-group">
              <label for="matDesc">Description</label>
              <textarea id="matDesc" name="matDesc" placeholder="Briefly describe what this material covers, key topics, how it helps students, which exam or course it suits..." maxlength="500"></textarea>
              <div class="char-counter" id="descCounter">0 / 500</div>
            </div>

            <div class="field-group">
              <label>Subject <span class="req">*</span></label>
              <div class="custom-select" id="subjectSelect">
                <div class="custom-select-trigger" id="subjectTrigger" tabindex="0" role="combobox" aria-expanded="false" aria-haspopup="listbox">
                  <span id="subjectLabel" style="color:var(--clr-gray2)">Select subject...</span>
                  <span class="arrow">▾</span>
                </div>
                <div class="custom-select-dropdown" id="subjectDropdown">
                  <div class="custom-select-search">
                    <input type="text" id="subjectSearch" placeholder="Search subjects..." autocomplete="off" aria-label="Search subjects"/>
                  </div>
                  <div id="subjectOptions"></div>
                </div>
                <input type="hidden" id="subjectValue" name="subject" required/>
              </div>
              <div class="field-error" id="subjectError">Please select a subject</div>
            </div>

            <div class="field-row">
              <div class="field-group" style="margin-bottom:0">
                <label for="matType">Material Type <span class="req">*</span></label>
                <select id="matType" name="matType" required>
                  <option value="">Select type...</option>
                  <option>Notes</option>
                  <option>Model Paper</option>
                  <option>Question Paper</option>
                  <option>Assignment</option>
                  <option>Lab Report</option>
                  <option>Textbook</option>
                  <option>Cheat Sheet</option>
                  <option>Other</option>
                </select>
                <div class="field-error" id="typeError">Please select material type</div>
              </div>
              <div class="field-group" style="margin-bottom:0">
                <label for="matExam">Exam / Course</label>
                <input type="text" id="matExam" name="matExam" placeholder="e.g. B.Tech, GATE, UPSC, JEE..."/>
              </div>
            </div>

            <div class="field-row" style="margin-top:20px">
              <div class="field-group" style="margin-bottom:0">
                <label for="matYear">Year / Semester <span class="req">*</span></label>
                <select id="matYear" name="matYear" required>
                  <option value="">Select...</option>
                  <optgroup label="Year">
                    <option>1st Year</option><option>2nd Year</option>
                    <option>3rd Year</option><option>4th Year</option>
                  </optgroup>
                  <optgroup label="Semester">
                    <option>Sem 1</option><option>Sem 2</option><option>Sem 3</option>
                    <option>Sem 4</option><option>Sem 5</option><option>Sem 6</option>
                    <option>Sem 7</option><option>Sem 8</option>
                  </optgroup>
                  <optgroup label="Other">
                    <option>Not Applicable</option>
                  </optgroup>
                </select>
                <div class="field-error" id="yearError">Please select year or semester</div>
              </div>
              <div class="field-group" style="margin-bottom:0">
                <label for="matAcYear">Academic Year</label>
                <input type="text" id="matAcYear" name="matAcYear" placeholder="e.g. 2024-25"/>
              </div>
            </div>

            <div class="field-group" style="margin-top:20px;margin-bottom:0">
              <label for="matUniv">University / College <span style="font-size:.78rem;color:var(--clr-gray2)">(optional)</span></label>
              <input type="text" id="matUniv" name="matUniv" placeholder="e.g. JNTUA, Anna University, Delhi University..."/>
            </div>
          </div>
        </div>

        <!-- STEP 3: TAGS & VISIBILITY -->
        <div class="form-card" style="margin-bottom:24px">
          <div class="form-section">
            <div class="form-section-header">
              <div class="step-badge">3</div>
              <div>
                <h2>Tags &amp; Visibility</h2>
                <p>Control how and who can find your material</p>
              </div>
            </div>

            <div class="field-group">
              <label>Tags <span style="font-size:.78rem;color:var(--clr-gray2)">(max 10, press Enter to add)</span></label>
              <div class="tags-input-wrapper" id="tagsWrapper">
                <div id="tagPills"></div>
                <input type="text" id="tagInput" class="tags-input" placeholder="Type a tag and press Enter..." autocomplete="off"/>
                <div class="tag-suggestions" id="tagSuggestions"></div>
              </div>
              <input type="hidden" id="tagsValue" name="tags"/>
            </div>

            <div class="field-group">
              <label>Visibility</label>
              <div class="visibility-options">
                <label class="visibility-card selected" id="visPublic">
                  <input type="radio" name="visibility" value="public" checked onchange="updateVisCard()"/>
                  <div class="vis-icon">🌍</div>
                  <h4>Public</h4>
                  <p>Visible to everyone on Browse</p>
                </label>
                <label class="visibility-card" id="visUnlisted">
                  <input type="radio" name="visibility" value="unlisted" onchange="updateVisCard()"/>
                  <div class="vis-icon">🔗</div>
                  <h4>Unlisted</h4>
                  <p>Only accessible via direct link</p>
                </label>
              </div>
            </div>

            <div class="field-group">
              <div class="toggle-row">
                <div class="toggle-info">
                  <h4>Allow Comments</h4>
                  <p>Let students ask questions or give feedback</p>
                </div>
                <label class="toggle-switch">
                  <input type="checkbox" id="allowComments" name="allowComments" checked/>
                  <span class="toggle-slider"></span>
                </label>
              </div>
            </div>

            <div class="field-group">
              <label style="margin-bottom:10px;display:block">License</label>
              <div class="license-options">
                <label class="license-card selected" id="licFree" onclick="selectLicense('licFree')">
                  <input type="radio" name="license" value="free" checked/>
                  <div class="check" id="checkFree"></div>
                  <h4>Free to Use</h4>
                  <p>Anyone can download and use without restrictions</p>
                </label>
                <label class="license-card" id="licAttr" onclick="selectLicense('licAttr')">
                  <input type="radio" name="license" value="attribution"/>
                  <div class="check" id="checkAttr"></div>
                  <h4>Attribution Required</h4>
                  <p>Credit the uploader when sharing or using</p>
                </label>
              </div>
            </div>
          </div>
        </div>

        <!-- STEP 4: UPLOADER INFO -->
        <div class="form-card" style="margin-bottom:24px">
          <div class="form-section">
            <div class="form-section-header">
              <div class="step-badge">4</div>
              <div>
                <h2>Your Info</h2>
                <p>Let others know who shared this material</p>
              </div>
            </div>

            <div class="field-row">
              <div class="field-group" style="margin-bottom:0">
                <label for="uploaderName">Your Name <span class="req">*</span></label>
                <div class="field-wrapper">
                  <input type="text" id="uploaderName" name="uploaderName" placeholder="e.g. Ananya Sharma" required autocomplete="name"/>
                </div>
                <div class="field-error" id="nameError">Name is required</div>
              </div>
              <div class="field-group" style="margin-bottom:0">
                <label for="uploaderEmail">Email <span class="req">*</span></label>
                <div class="field-wrapper">
                  <input type="email" id="uploaderEmail" name="uploaderEmail" placeholder="you@example.com" required autocomplete="email"/>
                </div>
                <div class="field-error" id="emailError">Please enter a valid email</div>
              </div>
            </div>

            <div style="background:rgba(26,107,74,.08);border:1px solid rgba(34,160,107,.2);border-radius:10px;padding:16px;margin-top:20px;display:flex;align-items:center;gap:14px">
              <span style="font-size:1.6rem">🎓</span>
              <div>
                <p style="font-size:.88rem;font-weight:500;margin-bottom:3px">Want to track all your uploads?</p>
                <p style="font-size:.82rem;color:var(--clr-gray)">Create a free NoteNest account to manage uploads, see statistics, and build your contributor profile.</p>
              </div>
              <a href="#" style="margin-left:auto;white-space:nowrap;font-size:.85rem;color:var(--clr-amber);font-weight:600;text-decoration:none;padding:8px 16px;border:1px solid var(--clr-amber);border-radius:7px;transition:var(--transition)" onmouseover="this.style.background='rgba(245,166,35,.1)'" onmouseout="this.style.background='transparent'">Create Account</a>
            </div>
          </div>
        </div>

        <!-- SUBMIT -->
        <div class="submit-section" style="background:var(--clr-surface);border:1px solid var(--clr-border);border-radius:var(--radius-lg);padding:32px">
          <button type="submit" class="submit-btn" id="submitBtn" disabled>
            <span>📤</span> Upload &amp; Share
          </button>
          <p class="submit-hint">By uploading, you confirm you own the rights to share this material.</p>
          <button type="button" class="save-draft-btn" onclick="saveDraft()">💾 Save as Draft</button>
        </div>

      </form>
    </div>

    <!-- === SIDEBAR === -->
    <aside class="upload-sidebar">

      <!-- Guidelines -->
      <div class="sidebar-card">
        <h3><span>📋</span> Upload Guidelines</h3>
        <div class="guideline-item">
          <div class="gi-icon gi-ok">✓</div>
          <span>Original notes or materials you created or own</span>
        </div>
        <div class="guideline-item">
          <div class="gi-icon gi-ok">✓</div>
          <span>Scanned textbooks with proper rights</span>
        </div>
        <div class="guideline-item">
          <div class="gi-icon gi-ok">✓</div>
          <span>University question papers &amp; model papers</span>
        </div>
        <div class="guideline-item">
          <div class="gi-icon gi-ok">✓</div>
          <span>Lab manuals, cheat sheets, summaries</span>
        </div>
        <div class="guideline-item">
          <div class="gi-icon gi-no">✗</div>
          <span>Commercial textbooks without permission</span>
        </div>
        <div class="guideline-item">
          <div class="gi-icon gi-no">✗</div>
          <span>Plagiarised or copied content</span>
        </div>
        <div class="guideline-item">
          <div class="gi-icon gi-no">✗</div>
          <span>Spam, irrelevant, or low-quality files</span>
        </div>
      </div>

      <!-- Tips -->
      <div class="sidebar-card">
        <h3><span>💡</span> Tips for Good Uploads</h3>
        <div class="tip-item">Use a clear, descriptive title with exam year or edition</div>
        <div class="tip-item">Add relevant tags to increase discoverability</div>
        <div class="tip-item">Write a short description explaining key topics covered</div>
        <div class="tip-item">PDF format gets the highest downloads</div>
        <div class="tip-item">Include the university name for better filtering</div>
      </div>

      <!-- Recent Uploads -->
      <div class="sidebar-card">
        <h3><span>🕐</span> Your Recent Uploads</h3>
        <div id="recentUploads">
          <p style="font-size:.85rem;color:var(--clr-gray2);text-align:center;padding:16px 0">No recent uploads yet.</p>
        </div>
      </div>

      <!-- Community Stats -->
      <div class="sidebar-card">
        <h3><span>📊</span> Community Stats</h3>
        <div class="stat-row">
          <span>Uploaded today</span>
          <span class="stat-val" id="statToday">—</span>
        </div>
        <div class="stat-row">
          <span>Total materials</span>
          <span class="stat-val" id="statTotal">—</span>
        </div>
        <div class="stat-row">
          <span>Active contributors</span>
          <span class="stat-val" id="statContrib">—</span>
        </div>
      </div>
    </aside>
  </div>
</main>

<!-- UPLOAD PROGRESS MODAL -->
<div class="modal-overlay" id="uploadModal">
  <div class="modal-box">
    <span class="modal-icon" id="modalIcon">📤</span>
    <h2 class="modal-title" id="modalTitle">Uploading...</h2>
    <p class="modal-sub" id="modalSub">Please wait while we process your material</p>
    <div class="upload-progress-bar" id="modalProgressWrap">
      <div class="upload-progress-fill" id="modalProgress"></div>
    </div>
    <p class="upload-status-text" id="modalStatus">Preparing files...</p>
    <div class="modal-actions" id="modalActions" style="display:none">
      <a href="browse.html" class="btn-amber">View on Browse</a>
      <button type="button" onclick="resetForm()" style="background:var(--clr-surface2);color:var(--clr-white);border:1px solid var(--clr-border)">Upload Another</button>
    </div>
  </div>
</div>

<!-- CONFETTI CONTAINER -->
<div class="confetti-container" id="confettiContainer"></div>

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

<script src="upload.js" charset="utf-8"></script>
</body>
</html>
'''

with open(r'c:\Users\kharj\OneDrive\Desktop\fsd project\upload.html','a',encoding='utf-8') as f:
    f.write(p2)
print('Part 2 done, total size:', __import__('os').path.getsize(r'c:\Users\kharj\OneDrive\Desktop\fsd project\upload.html'))
