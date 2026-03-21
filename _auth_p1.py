<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1.0"/>
<meta name="description" content="Login or Sign Up to NoteNest - The best platform for students to share knowledge."/>
<title>Login / Sign Up — NoteNest</title>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700;900&family=DM+Sans:wght@300;400;500;600&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet"/>
<style>
:root{
  --clr-bg:#0d0d0d;--clr-surface:#1a1a1a;--clr-surface2:#1e1e1e;--clr-border:#2a2a2a;
  --clr-green:#1a6b4a;--clr-green-light:#22a06b;--clr-green-glow:rgba(26,107,74,.35);
  --clr-amber:#f5a623;--clr-amber-dark:#c4821a;--clr-coral:#ff6b6b;--clr-teal:#00b4a6;
  --clr-white:#ffffff;--clr-gray:#a0a0a0;--clr-gray2:#6a6a6a;
  --ff-display:'Playfair Display',serif;--ff-body:'DM Sans',sans-serif;--ff-mono:'JetBrains Mono',monospace;
  --radius:12px;--radius-lg:24px;--shadow-glow:0 0 24px var(--clr-green-glow);--transition:.3s ease;
}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
body{background:var(--clr-bg);color:var(--clr-white);font-family:var(--ff-body);line-height:1.6;overflow-x:hidden}
::-webkit-scrollbar{width:6px}::-webkit-scrollbar-track{background:#111}::-webkit-scrollbar-thumb{background:var(--clr-green);border-radius:3px}

/* MAIN LAYOUT */
.auth-layout{display:flex;min-height:100vh}

/* LEFT PANEL — BRANDING */
.auth-left{flex:1;background:radial-gradient(circle at top left,rgba(26,107,74,.2),transparent 50%),radial-gradient(circle at bottom right,rgba(245,166,35,.1),transparent 50%),var(--clr-surface);border-right:1px solid var(--clr-border);padding:48px;display:flex;flex-direction:column;justify-content:space-between;position:relative;overflow:hidden}
.auth-left::before{content:'';position:absolute;inset:0;background-image:url("data:image/svg+xml,%3Csvg width='40' height='40' viewBox='0 0 40 40' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M20 20.5a.5.5 0 1 1 0-1 .5.5 0 0 1 0 1zm10 10.5a.5.5 0 1 1 0-1 .5.5 0 0 1 0 1zm-20 0a.5.5 0 1 1 0-1 .5.5 0 0 1 0 1z' fill='%23ffffff' fill-opacity='0.03' fill-rule='evenodd'/%3E%3C/svg%3E");pointer-events:none}
.brand-header{position:relative;z-index:10}
.nav-logo{display:inline-flex;align-items:center;gap:12px;text-decoration:none;margin-bottom:24px}
.nav-logo-icon{width:44px;height:44px;background:linear-gradient(135deg,var(--clr-green),var(--clr-green-light));border-radius:12px;display:flex;align-items:center;justify-content:center}
.nav-logo-icon svg{fill:white;width:24px;height:24px}
.nav-logo-text{font-family:var(--ff-display);font-size:1.8rem;font-weight:700;color:var(--clr-white);letter-spacing:.5px}
.nav-logo-text span{color:var(--clr-amber)}
.tagline{font-size:1.4rem;color:var(--clr-gray);max-width:340px;line-height:1.4;font-family:var(--ff-display)}

/* ANIMATED FLOATING CARDS */
.floating-cards{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);width:400px;height:400px;z-index:5}
.f-card{position:absolute;background:rgba(26,26,26,.8);backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px);border:1px solid rgba(255,255,255,.1);border-radius:16px;padding:20px;width:280px;box-shadow:0 24px 48px rgba(0,0,0,.4);animation:float 6s ease-in-out infinite}
.f-card.c1{top:10%;left:0;animation-delay:0s;z-index:3;transform:rotate(-5deg)}
.f-card.c2{top:45%;right:-10%;animation-delay:-2s;z-index:2;transform:rotate(4deg)}
.f-card.c3{bottom:5%;left:15%;animation-delay:-4s;z-index:1;transform:rotate(-2deg)}
.fc-type{display:inline-block;padding:4px 10px;background:rgba(26,107,74,.2);color:var(--clr-green-light);font-size:.75rem;font-family:var(--ff-mono);border-radius:4px;margin-bottom:12px}
.fc-title{font-weight:600;font-size:1rem;color:white;margin-bottom:8px}
.fc-meta{font-size:.8rem;color:var(--clr-gray);display:flex;justify-content:space-between}

.stats-bar{position:relative;z-index:10;display:flex;gap:32px;padding-top:32px;border-top:1px solid rgba(255,255,255,.05);margin-top:auto}
.stat{display:flex;flex-direction:column;gap:4px}
.stat span{font-family:var(--ff-display);font-size:1.6rem;font-weight:700;color:var(--clr-white)}
.stat p{font-size:.85rem;color:var(--clr-gray)}

/* RIGHT PANEL — AUTH FORMS */
.auth-right{flex:1;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:40px 24px;position:relative}
.auth-container{width:100%;max-width:440px;background:var(--clr-surface);border:1px solid var(--clr-border);border-radius:var(--radius-lg);padding:40px;position:relative;overflow:hidden;box-shadow:0 24px 64px rgba(0,0,0,.5)}

/* TABS */
.auth-tabs{display:flex;margin-bottom:32px;border-bottom:2px solid var(--clr-surface2);position:relative}
.tab-btn{flex:1;background:none;border:none;color:var(--clr-gray);font-family:var(--ff-body);font-size:1.1rem;font-weight:600;padding:12px 0;cursor:pointer;transition:color .3sease;position:relative;z-index:2}
.tab-btn.active{color:var(--clr-white)}
.tab-indicator{position:absolute;bottom:-2px;left:0;height:2px;width:50%;background:var(--clr-amber);transition:transform .4s cubic-bezier(0.4, 0, 0.2, 1);z-index:3}
.auth-tabs.signup-active .tab-indicator{transform:translateX(100%)}

/* FORM CONTAINER */
.forms-wrapper{position:relative;min-height:420px;transition:height .4s ease}
.form-section{position:absolute;top:0;left:0;width:100%;transition:all .5s cubic-bezier(0.4, 0, 0.2, 1);opacity:0;visibility:hidden;transform:translateY(20px)}
.form-section.active{opacity:1;visibility:visible;transform:translateY(0);position:relative}

/* FORM ELEMENTS */
.form-group{margin-bottom:20px;position:relative}
.form-group label{display:block;font-size:.85rem;font-weight:500;color:var(--clr-gray);margin-bottom:8px}
.input-wrapper{position:relative;display:flex;align-items:center}
.form-control{width:100%;background:var(--clr-surface2);border:1px solid var(--clr-border);color:var(--clr-white);padding:14px 16px;border-radius:10px;font-family:var(--ff-body);font-size:1rem;transition:var(--transition);outline:none}
.form-control:focus{border-color:var(--clr-green-light);box-shadow:0 0 0 3px rgba(26,107,74,.15)}
.form-control.error{border-color:var(--clr-coral)}
.input-icon{position:absolute;left:16px;color:var(--clr-gray2);pointer-events:none;display:flex;align-items:center}
.form-control.with-icon{padding-left:46px}
.view-btn{position:absolute;right:16px;background:none;border:none;color:var(--clr-gray2);cursor:pointer;display:flex;align-items:center;padding:4px}
.view-btn:hover{color:var(--clr-white)}
.error-msg{color:var(--clr-coral);font-size:.8rem;margin-top:6px;display:none}

.row-group{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.form-options{display:flex;align-items:center;justify-content:space-between;margin-bottom:24px}
.checkbox-wrap{display:flex;align-items:center;gap:8px;cursor:pointer;font-size:.85rem;color:var(--clr-gray)}
.checkbox-wrap input{width:16px;height:16px;accent-color:var(--clr-green-light);cursor:pointer}
.forgot-link{font-size:.85rem;color:var(--clr-amber);text-decoration:none;transition:var(--transition)}
.forgot-link:hover{text-decoration:underline}

/* BUTTONS */
.btn-submit{width:100%;background:var(--clr-amber);color:#0d0d0d;border:none;padding:16px;border-radius:12px;font-family:var(--ff-body);font-size:1.05rem;font-weight:700;cursor:pointer;transition:var(--transition);display:flex;align-items:center;justify-content:center;gap:10px;margin-bottom:24px;box-shadow:0 8px 24px rgba(245,166,35,.2)}
.btn-submit:hover{background:var(--clr-amber-dark);transform:translateY(-2px);box-shadow:0 12px 32px rgba(245,166,35,.3)}
.btn-submit:active{transform:translateY(0)}

.divider{display:flex;align-items:center;text-align:center;color:var(--clr-gray2);font-size:.85rem;margin-bottom:24px}
.divider::before,.divider::after{content:'';flex:1;border-bottom:1px solid var(--clr-border)}
.divider span{padding:0 16px}

.btn-google{width:100%;background:var(--clr-surface2);border:1px solid var(--clr-border);color:var(--clr-white);padding:14px;border-radius:12px;font-family:var(--ff-body);font-size:.95rem;font-weight:600;cursor:pointer;transition:var(--transition);display:flex;align-items:center;justify-content:center;gap:12px}
.btn-google:hover{background:var(--clr-surface);border-color:var(--clr-gray2)}
.btn-google svg{width:20px;height:20px}

.auth-footer{text-align:center;margin-top:24px;font-size:.9rem;color:var(--clr-gray)}
.auth-footer a{color:var(--clr-white);font-weight:600;text-decoration:none;cursor:pointer}
.auth-footer a:hover{text-decoration:underline;color:var(--clr-amber)}

/* PASSWORD STRENGTH */
.strength-meter{margin-top:8px;display:flex;gap:6px;height:4px}
.s-bar{flex:1;background:var(--clr-border);border-radius:2px;transition:var(--transition)}
.strength-text{font-size:.75rem;color:var(--clr-gray);margin-top:6px;display:none;justify-content:flex-end}
.meter-weak .s-bar:nth-child(1){background:var(--clr-coral)}
.meter-weak ~ .strength-text{display:flex;color:var(--clr-coral)}
.meter-medium .s-bar:nth-child(1),.meter-medium .s-bar:nth-child(2){background:var(--clr-amber)}
.meter-medium ~ .strength-text{display:flex;color:var(--clr-amber)}
.meter-strong .s-bar{background:var(--clr-green-light)}
.meter-strong ~ .strength-text{display:flex;color:var(--clr-green-light)}

/* FORGOT PASSWORD SLIDE-IN */
.forgot-panel{position:absolute;inset:0;background:var(--clr-surface);z-index:20;padding:40px;transform:translateX(100%);transition:transform .4s cubic-bezier(0.4, 0, 0.2, 1);display:flex;flex-direction:column;justify-content:center}
.forgot-panel.active{transform:translateX(0)}
.back-login{background:none;border:none;color:var(--clr-gray);font-family:var(--ff-body);font-size:.9rem;cursor:pointer;display:inline-flex;align-items:center;gap:6px;margin-bottom:24px;transition:var(--transition)}
.back-login:hover{color:var(--clr-white)}
.forgot-panel h2{font-family:var(--ff-display);font-size:1.8rem;margin-bottom:12px}
.forgot-panel p{color:var(--clr-gray);font-size:.95rem;margin-bottom:32px;line-height:1.5}

/* TOAST */
#nn-toast{position:fixed;bottom:28px;left:50%;transform:translateX(-50%) translateY(20px);background:var(--clr-green);border:1px solid var(--clr-green-light);color:white;padding:12px 24px;border-radius:10px;font-size:.9rem;font-family:var(--ff-body);z-index:4000;opacity:0;transition:all .3s ease;white-space:nowrap;box-shadow:0 8px 24px rgba(0,0,0,.5);font-weight:500;display:flex;align-items:center;gap:8px}

/* SPINNER */
.spinner{width:20px;height:20px;border:3px solid rgba(0,0,0,.2);border-top-color:#0d0d0d;border-radius:50%;animation:spin 1s linear infinite;display:none}
.btn-submit.loading .spinner{display:inline-block}
.btn-submit.loading span{display:none}

@keyframes spin{to{transform:rotate(360deg)}}
@keyframes float{
  0%,100%{transform:translateY(0) rotate(-2deg)}
  50%{transform:translateY(-15px) rotate(1deg)}
}
@keyframes floatAlt{
  0%,100%{transform:translateY(0) rotate(4deg)}
  50%{transform:translateY(-20px) rotate(0deg)}
}

/* RESPONSIVE */
.home-link{position:absolute;top:32px;right:32px;color:var(--clr-gray);text-decoration:none;font-size:.9rem;font-weight:500;display:flex;align-items:center;gap:6px;transition:var(--transition);z-index:100}
.home-link:hover{color:var(--clr-white)}

@media(max-width:1024px){
  .auth-left{padding:32px}
  .floating-cards{display:none}
}
@media(max-width:768px){
  .auth-left{display:none}
  .auth-layout{justify-content:center;background:var(--clr-bg)}
  .auth-container{box-shadow:none;border:none;padding:24px 16px}
  .home-link{top:16px;right:16px}
}
</style>
</head>
