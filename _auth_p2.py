<body>

<a href="index.html" class="home-link">
  <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg>
  Back to Home
</a>

<div class="auth-layout">
  
  <!-- LEFT PANEL -->
  <div class="auth-left">
    <div class="brand-header">
      <a href="index.html" class="nav-logo">
        <div class="nav-logo-icon"><svg viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8zM14 2v6h6"/></svg></div>
        <span class="nav-logo-text">Note<span>Nest</span></span>
      </a>
      <h1 class="tagline">Join 10,000+ students sharing knowledge</h1>
    </div>

    <div class="floating-cards">
      <div class="f-card c1">
        <span class="fc-type">📝 Notes</span>
        <div class="fc-title">Advanced Data Structures - Trees & Graphs</div>
        <div class="fc-meta"><span>By Alex Chen</span><span>★ 4.9</span></div>
      </div>
      <div class="f-card c2" style="animation-name:floatAlt">
        <span class="fc-type">📄 Model Paper</span>
        <div class="fc-title">Physics 101 Midterm Questions 2023</div>
        <div class="fc-meta"><span>By Sarah Jenkins</span><span>★ 4.7</span></div>
      </div>
      <div class="f-card c3">
        <span class="fc-type">⚡ Cheat Sheet</span>
        <div class="fc-title">Calculus Derivatives & Integrals Fast Prep</div>
        <div class="fc-meta"><span>By Maya Patel</span><span>★ 5.0</span></div>
      </div>
    </div>

    <div class="stats-bar">
      <div class="stat">
        <span>12K+</span>
        <p>Study Materials</p>
      </div>
      <div class="stat">
        <span>8K+</span>
        <p>Downloads</p>
      </div>
      <div class="stat">
        <span style="color:var(--clr-amber)">Free</span>
        <p>Forever for Students</p>
      </div>
    </div>
  </div>

  <!-- RIGHT PANEL -->
  <div class="auth-right">
    <div class="auth-container">
      
      <!-- Tabs -->
      <div class="auth-tabs" id="authTabs">
        <button class="tab-btn active" onclick="switchTab('login')">Login</button>
        <button class="tab-btn" onclick="switchTab('signup')">Sign Up</button>
        <div class="tab-indicator" id="tabIndicator"></div>
      </div>

      <div class="forms-wrapper" id="formsWrapper">
        
        <!-- LOGIN FORM -->
        <form class="form-section active" id="loginForm" onsubmit="handleLogin(event)">
          <div class="form-group">
            <label for="loginEmail">Email Address</label>
            <div class="input-wrapper">
              <span class="input-icon"><svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg></span>
              <input type="email" id="loginEmail" class="form-control with-icon" placeholder="you@example.com" required>
            </div>
            <div class="error-msg" id="loginEmailError">Please enter a valid email</div>
          </div>

          <div class="form-group">
            <label for="loginPwd">Password</label>
            <div class="input-wrapper">
              <span class="input-icon"><svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg></span>
              <input type="password" id="loginPwd" class="form-control with-icon" placeholder="••••••••" required>
              <button type="button" class="view-btn" onclick="togglePwd('loginPwd')">
                <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path><circle cx="12" cy="12" r="3"></circle></svg>
              </button>
            </div>
          </div>

          <div class="form-options">
            <label class="checkbox-wrap">
              <input type="checkbox" id="rememberMe" checked>
              Remember me
            </label>
            <a href="#" class="forgot-link" onclick="openForgot(event)">Forgot Password?</a>
          </div>

          <button type="submit" class="btn-submit" id="loginBtn">
            <span class="spinner"></span>
            <span>Login</span>
          </button>

          <div class="divider"><span>or complete with</span></div>

          <button type="button" class="btn-google" onclick="simOAuth()">
            <svg viewBox="0 0 24 24"><path d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z" fill="#4285F4"/><path d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z" fill="#34A853"/><path d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z" fill="#FBBC05"/><path d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z" fill="#EA4335"/></svg>
            Continue with Google
          </button>

          <div class="auth-footer">
            Don't have an account? <a onclick="switchTab('signup')">Sign Up</a>
          </div>
        </form>

        <!-- SIGNUP FORM -->
        <form class="form-section" id="signupForm" onsubmit="handleSignup(event)">
          <div class="row-group">
            <div class="form-group">
              <label for="regName">Full Name</label>
              <input type="text" id="regName" class="form-control" placeholder="John Doe" required>
            </div>
            <div class="form-group">
              <label for="regEmail">Email Address</label>
              <input type="email" id="regEmail" class="form-control" placeholder="you@example.com" required>
              <div class="error-msg" id="regEmailError">Invalid email format</div>
            </div>
          </div>

          <div class="form-group">
            <label for="regPwd">Password</label>
            <div class="input-wrapper">
              <input type="password" id="regPwd" class="form-control" placeholder="Create a password" required oninput="checkStrength()">
              <button type="button" class="view-btn" onclick="togglePwd('regPwd')">
                <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path><circle cx="12" cy="12" r="3"></circle></svg>
              </button>
            </div>
            <div class="strength-meter" id="strengthMeter">
              <div class="s-bar"></div><div class="s-bar"></div><div class="s-bar"></div>
            </div>
            <div class="strength-text" id="strengthText">Weak</div>
          </div>

          <div class="form-group">
            <label for="regPwdConfirm">Confirm Password</label>
            <div class="input-wrapper">
              <input type="password" id="regPwdConfirm" class="form-control" placeholder="Repeat password" required oninput="checkMatch()">
              <span class="input-icon" id="matchIcon" style="right:16px;left:auto;color:var(--clr-green-light);display:none">
                <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>
              </span>
            </div>
            <div class="error-msg" id="matchError">Passwords do not match</div>
          </div>

          <div class="row-group">
            <div class="form-group">
              <label for="regUni">University / College <span style="color:var(--clr-gray2);font-weight:400">(Optional)</span></label>
              <input type="text" id="regUni" class="form-control" placeholder="e.g. JNTU">
            </div>
            <div class="form-group">
              <label for="regCourse">Course / Branch</label>
              <input type="text" id="regCourse" class="form-control" placeholder="e.g. B.Tech CS">
            </div>
          </div>

          <div class="form-group" style="margin-bottom:24px">
            <label class="checkbox-wrap">
              <input type="checkbox" required>
              I agree to NoteNest's Terms of Service and Privacy Policy
            </label>
          </div>

          <button type="submit" class="btn-submit" id="signupBtn">
            <span class="spinner"></span>
            <span>Create Account</span>
          </button>

          <div class="divider"><span>or</span></div>

          <button type="button" class="btn-google" onclick="simOAuth()">
            <svg viewBox="0 0 24 24"><path d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z" fill="#4285F4"/><path d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z" fill="#34A853"/><path d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z" fill="#FBBC05"/><path d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z" fill="#EA4335"/></svg>
            Sign up with Google
          </button>

          <div class="auth-footer">
            Already have an account? <a onclick="switchTab('login')">Login</a>
          </div>
        </form>

      </div>

      <!-- FORGOT PASSWORD SLIDE-IN -->
      <div class="forgot-panel" id="forgotPanel">
        <button class="back-login" onclick="closeForgot()">
          <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="19" y1="12" x2="5" y2="12"></line><polyline points="12 19 5 12 12 5"></polyline></svg>
          Back to Login
        </button>
        <h2>Reset Password</h2>
        <p>Enter the email address associated with your account and we'll send you a link to reset your password.</p>
        
        <form onsubmit="handleReset(event)">
          <div class="form-group">
            <label for="resetEmail">Email Address</label>
            <input type="email" id="resetEmail" class="form-control" placeholder="you@example.com" required>
          </div>
          <button type="submit" class="btn-submit" id="resetBtn" style="margin-top:24px">
            <span class="spinner"></span>
            <span>Send Reset Link</span>
          </button>
        </form>
      </div>

    </div>
  </div>
</div>

<script src="auth.js" charset="utf-8"></script>
</body>
</html>
