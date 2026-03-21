<body>

<!-- NAVBAR (Dashboard View) -->
<header>
  <nav id="navbar">
    <div class="container nav-inner">
      <a href="index.html" class="nav-logo" aria-label="NoteNest home">
        <div class="nav-logo-icon">
          <svg viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8zM14 2v6h6M16 13H8M16 17H8M10 9H8"/></svg>
        </div>
        <span class="nav-logo-text">Note<span>Nest</span></span>
      </a>
      
      <!-- User Menu Dropdown -->
      <div class="user-menu" id="userMenuBtn" onclick="toggleDropdown()">
        <div class="nav-avatar" id="navAvatar">JD</div>
        <span class="nav-username" id="navName">John Doe</span>
        <svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7 10l5 5 5-5z"/></svg>
        
        <div class="user-dropdown" id="userDropdown">
          <a href="#" class="dd-item" onclick="switchTab('dashboard')">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg>
            Dashboard
          </a>
          <a href="#" class="dd-item" onclick="switchTab('uploads')">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="17 8 12 3 7 8"></polyline><line x1="12" y1="3" x2="12" y2="15"></line></svg>
            My Uploads
          </a>
          <a href="#" class="dd-item" onclick="switchTab('bookmarks')">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"></path></svg>
            Saved Materials
          </a>
          <a href="#" class="dd-item" onclick="switchTab('settings')">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="3"></circle><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"></path></svg>
            Settings
          </a>
          <div class="dd-divider"></div>
          <a href="#" class="dd-item dd-logout" onclick="logout()">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"></path><polyline points="16 17 21 12 16 7"></polyline><line x1="21" y1="12" x2="9" y2="12"></line></svg>
            Logout
          </a>
        </div>
      </div>
      
      <button class="hamburger" id="hamburger" aria-label="Toggle menu">
        <span></span><span></span><span></span>
      </button>
    </div>
  </nav>
</header>

<div class="dash-layout">
  
  <!-- SIDEBAR NAVIGATION -->
  <aside class="sidebar">
    <div class="sb-profile">
      <div class="sb-avatar-wrap">
        <div class="sb-avatar" id="sbAvatarText">JD</div>
        <img id="sbAvatarImg" style="display:none;position:absolute;top:4px;left:4px;width:72px;height:72px;border-radius:50%;object-fit:cover" alt="Avatar">
      </div>
      <div class="sb-name" id="sbName">John Doe</div>
      <div class="sb-email" id="sbEmail">john@university.edu</div>
      <button class="btn-outline" style="width:100%" onclick="switchTab('settings')">Edit Profile</button>
      
      <div class="prog-container" id="profileProg" style="display:none">
        <div class="prog-header"><span>Profile Completion</span><span>65%</span></div>
        <div class="prog-track"><div class="prog-fill"></div></div>
      </div>
    </div>
    
    <nav class="sb-nav">
      <a href="#" class="sb-link active" data-tab="dashboard">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><rect x="3" y="3" width="7" height="7"></rect><rect x="14" y="3" width="7" height="7"></rect><rect x="14" y="14" width="7" height="7"></rect><rect x="3" y="14" width="7" height="7"></rect></svg>
        Overview
      </a>
      <a href="#" class="sb-link" data-tab="uploads">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="17 8 12 3 7 8"></polyline><line x1="12" y1="3" x2="12" y2="15"></line></svg>
        My Uploads
      </a>
      <a href="#" class="sb-link" data-tab="bookmarks">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"></path></svg>
        Bookmarks
      </a>
      <a href="#" class="sb-link" data-tab="downloads">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><polyline points="8 17 12 21 16 17"></polyline><line x1="12" y1="12" x2="12" y2="21"></line><path d="M20.88 18.09A5 5 0 0 0 18 9h-1.26A8 8 0 1 0 3 16.29"></path></svg>
        History
      </a>
      <a href="#" class="sb-link" data-tab="notifications">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"></path><path d="M13.73 21a2 2 0 0 1-3.46 0"></path></svg>
        Notifications
        <span class="badge" id="notifBadge">3</span>
      </a>
      <a href="#" class="sb-link" data-tab="settings" style="margin-top:auto">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><circle cx="12" cy="12" r="3"></circle><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"></path></svg>
        Settings
      </a>
    </nav>
  </aside>

  <!-- MAIN CONTENT -->
  <main class="main-content">
    
    <!-- TAB: DASHBOARD (OVERVIEW) -->
    <div id="tab-dashboard" class="tab-pane active">
      <div class="page-header">
        <div>
          <h1 class="page-title" id="welcomeMsg">Good morning, John! 🎓</h1>
          <p class="page-subtitle">Here's what's happening with your study materials today.</p>
        </div>
        <a href="upload.html" class="btn-amber">Upload Material</a>
      </div>

      <div class="stat-grid">
        <div class="s-card amber">
          <div class="sc-header">
            <span class="sc-label">Total Uploads</span>
            <div class="sc-icon"><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="17 8 12 3 7 8"></polyline><line x1="12" y1="3" x2="12" y2="15"></line></svg></div>
          </div>
          <div class="sc-value">14</div>
          <div class="sc-trend trend-up">↑ 2 this month</div>
        </div>
        <div class="s-card">
          <div class="sc-header">
            <span class="sc-label">Downloads Received</span>
            <div class="sc-icon"><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg></div>
          </div>
          <div class="sc-value">1,208</div>
          <div class="sc-trend trend-up">↑ 15% vs last week</div>
        </div>
        <div class="s-card">
          <div class="sc-header">
            <span class="sc-label">Saved Materials</span>
            <div class="sc-icon"><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"></path></svg></div>
          </div>
          <div class="sc-value">42</div>
          <div class="sc-trend trend-neu">− No change</div>
        </div>
        <div class="s-card">
          <div class="sc-header">
            <span class="sc-label">Profile Views</span>
            <div class="sc-icon"><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path><circle cx="12" cy="12" r="3"></circle></svg></div>
          </div>
          <div class="sc-value">385</div>
          <div class="sc-trend trend-up">↑ 24 this week</div>
        </div>
      </div>

      <div class="dash-sections">
        <!-- Activity Chart Box -->
        <div class="section-box" style="display:flex;flex-direction:column">
          <div class="box-header">
            <span class="box-title">Upload Activity (6 Months)</span>
          </div>
          <div class="chart-container" id="activityChart">
            <!-- Bars injected by JS -->
          </div>
        </div>
        
        <!-- Recent Box -->
        <div class="section-box">
          <div class="box-header">
            <span class="box-title">Recent Activity</span>
            <a href="#" onclick="switchTab('downloads')" class="box-link">View all</a>
          </div>
          <div class="mini-list" id="recentActivityList">
            <!-- Injected by JS -->
          </div>
        </div>
      </div>
    </div>


    <!-- TAB: MY UPLOADS -->
    <div id="tab-uploads" class="tab-pane">
      <div class="page-header">
        <div>
          <h1 class="page-title">My Uploads</h1>
          <p class="page-subtitle">Manage the study materials you've shared with the community.</p>
        </div>
        <a href="upload.html" class="btn-amber">Upload New</a>
      </div>

      <div class="toolbar">
        <div class="search-bar">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
          <input type="text" placeholder="Search your uploads..." onkeyup="filterUploads(this.value)">
        </div>
        <select class="filter-dropdown" onchange="filterStatus(this.value)">
          <option value="all">All Statuses</option>
          <option value="pub">Published</option>
          <option value="drf">Draft</option>
        </select>
      </div>

      <div class="mat-grid" id="uploadsGrid">
        <!-- Populated via JS -->
      </div>
    </div>


    <!-- TAB: BOOKMARKS -->
    <div id="tab-bookmarks" class="tab-pane">
      <div class="page-header">
        <div>
          <h1 class="page-title">Saved Materials</h1>
          <p class="page-subtitle">Your personal library of bookmarked notes and papers.</p>
        </div>
        <a href="browse.html" class="btn-outline">Browse More</a>
      </div>

      <div class="mat-grid" id="bookmarksGrid">
        <!-- Populated via JS -->
      </div>
    </div>


    <!-- TAB: DOWNLOAD HISTORY -->
    <div id="tab-downloads" class="tab-pane">
      <div class="page-header">
        <div>
          <h1 class="page-title">Download History</h1>
          <p class="page-subtitle">Keep track of the files you've downloaded.</p>
        </div>
        <button class="btn-outline" style="color:var(--clr-coral);border-color:var(--clr-border)" onclick="clearDownloads()">Clear History</button>
      </div>

      <div class="list-view" id="downloadsList">
        <!-- Populated via JS -->
      </div>
    </div>


    <!-- TAB: NOTIFICATIONS -->
    <div id="tab-notifications" class="tab-pane">
      <div class="page-header">
        <div>
          <h1 class="page-title">Notifications</h1>
          <p class="page-subtitle">Updates on your uploads and community interactions.</p>
        </div>
        <button class="btn-outline" onclick="markAllRead()">Mark all as read ✓</button>
      </div>

      <div class="list-view" id="notificationsList">
        <!-- Populated via JS -->
      </div>
    </div>


    <!-- TAB: SETTINGS -->
    <div id="tab-settings" class="tab-pane">
      <div class="page-header">
        <div>
          <h1 class="page-title">Account Settings</h1>
          <p class="page-subtitle">Manage your profile information and preferences.</p>
        </div>
      </div>

      <form onsubmit="saveProfileSettings(event)">
        <!-- Profile Section -->
        <div class="settings-section">
          <h3>Public Profile</h3>
          <div class="avatar-upload-wrap">
            <label class="av-preview" id="avatarPreviewLabel">
              <img id="avatarPreviewImg" src="" alt="Avatar Preview">
              <input type="file" id="avatarUpload" accept="image/*" onchange="previewAvatar(event)">
            </label>
            <div>
              <p style="font-weight:600;margin-bottom:4px">Profile Picture</p>
              <p style="color:var(--clr-gray);font-size:.85rem;margin-bottom:8px">Recommended size: 200x200px (JPG, PNG)</p>
              <label for="avatarUpload" class="btn-outline" style="padding:6px 12px;font-size:.8rem">Change Photo</label>
            </div>
          </div>

          <div class="set-row">
            <div class="set-group">
              <label for="setFullName">Full Name *</label>
              <input type="text" id="setFullName" class="set-control" required>
            </div>
            <div class="set-group">
              <label for="setUsername">Username Handle (Public)</label>
              <input type="text" id="setUsername" class="set-control" placeholder="@username">
            </div>
          </div>
          
          <div class="set-group" style="margin-bottom:20px">
            <label for="setBio">Short Bio / Description</label>
            <textarea id="setBio" class="set-control" rows="3" placeholder="Tell students about yourself..."></textarea>
          </div>

          <div class="set-row">
            <div class="set-group">
              <label for="setUni">University / College</label>
              <input type="text" id="setUni" class="set-control" placeholder="e.g. Stanford University">
            </div>
            <div class="set-group">
              <label for="setCourse">Course / Branch</label>
              <input type="text" id="setCourse" class="set-control" placeholder="e.g. B.Tech Computer Science">
            </div>
          </div>
          <button type="submit" class="btn-amber">Save Profile Changes</button>
        </div>
      </form>

      <!-- Preferences -->
      <div class="settings-section">
        <h3>Email & Notifications</h3>
        
        <div class="toggle-wrap">
          <div class="toggle-info">
            <strong>Download Alerts</strong>
            <span>Email me when someone downloads my material</span>
          </div>
          <label class="switch">
            <input type="checkbox" checked>
            <span class="slider"></span>
          </label>
        </div>
        
        <div class="toggle-wrap">
          <div class="toggle-info">
            <strong>New Comments</strong>
            <span>Notify me of new reviews or comments</span>
          </div>
          <label class="switch">
            <input type="checkbox" checked>
            <span class="slider"></span>
          </label>
        </div>
        
        <div class="toggle-wrap" style="border-bottom:none">
          <div class="toggle-info">
            <strong>NoteNest Newsletter</strong>
            <span>Receive weekly updates and feature announcements</span>
          </div>
          <label class="switch">
            <input type="checkbox">
            <span class="slider"></span>
          </label>
        </div>
      </div>

      <!-- Danger Zone -->
      <div class="settings-section" style="border-color:rgba(255,107,107,.3)">
        <h3 style="color:var(--clr-coral);border-color:rgba(255,107,107,.3)">Danger Zone</h3>
        <p style="color:var(--clr-gray);font-size:.9rem;margin-bottom:16px">Once you delete your account, there is no going back. Please be certain. All your uploaded materials and bookmarks will be permanently deleted.</p>
        <button class="btn-danger" onclick="confirmDeleteAccount()">Delete Account</button>
      </div>

    </div>

  </main>
</div>

<!-- DELETE MODAL -->
<div class="modal-back" id="deleteModal">
  <div class="modal">
    <h3>Delete Material?</h3>
    <p>Are you sure you want to permanently delete this material? This action cannot be undone.</p>
    <div class="modal-actions">
      <button class="btn-outline" onclick="closeDeleteModal()">Cancel</button>
      <button class="btn-danger" id="confirmDelBtn">Delete Permanently</button>
    </div>
  </div>
</div>

<!-- SCRIPTS -->
<script src="dashboard.js" charset="utf-8"></script>
</body>
</html>
