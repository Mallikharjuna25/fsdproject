<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1.0"/>
<meta name="description" content="NoteNest User Dashboard - Manage your uploads, bookmarks, and account settings."/>
<title>Dashboard — NoteNest</title>
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
  --radius:12px;--radius-lg:20px;--shadow-glow:0 0 24px var(--clr-green-glow);--transition:.3s ease;
}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{background:var(--clr-bg);color:var(--clr-white);font-family:var(--ff-body);line-height:1.6;overflow-x:hidden}
::-webkit-scrollbar{width:6px}::-webkit-scrollbar-track{background:#111}::-webkit-scrollbar-thumb{background:var(--clr-green);border-radius:3px}

/* UTILITY */
.container{max-width:1200px;margin:0 auto;padding:0 24px}
.btn-amber{background:var(--clr-amber);color:#0d0d0d;font-weight:600;border:none;padding:10px 22px;border-radius:8px;cursor:pointer;font-family:var(--ff-body);font-size:.9rem;transition:var(--transition);text-decoration:none;display:inline-flex;align-items:center;gap:6px;justify-content:center}
.btn-amber:hover{background:var(--clr-amber-dark);transform:translateY(-2px);box-shadow:0 8px 24px rgba(245,166,35,.3)}
.btn-green{background:var(--clr-green);color:white;font-weight:600;border:none;padding:10px 22px;border-radius:8px;cursor:pointer;font-family:var(--ff-body);font-size:.9rem;transition:var(--transition);text-decoration:none;display:inline-flex;align-items:center;gap:8px;justify-content:center}
.btn-green:hover{background:var(--clr-green-light);transform:translateY(-2px);box-shadow:var(--shadow-glow)}
.btn-outline{background:var(--clr-surface);color:var(--clr-white);border:1px solid var(--clr-border);padding:8px 16px;border-radius:8px;cursor:pointer;font-family:var(--ff-body);font-size:.85rem;font-weight:500;transition:var(--transition);text-decoration:none;display:inline-flex;align-items:center;gap:6px;justify-content:center}
.btn-outline:hover{border-color:var(--clr-amber);color:var(--clr-amber)}
.btn-danger{background:transparent;color:var(--clr-coral);border:1px solid rgba(255,107,107,.3);padding:8px 16px;border-radius:8px;cursor:pointer;font-family:var(--ff-body);font-size:.85rem;font-weight:500;transition:var(--transition);display:inline-flex;align-items:center;gap:6px}
.btn-danger:hover{background:rgba(255,107,107,.1);border-color:var(--clr-coral)}

/* NAVBAR (Modified for Auth state) */
nav{background:rgba(13,13,13,.95);backdrop-filter:blur(20px);border-bottom:1px solid var(--clr-border);padding:14px 0;position:sticky;top:0;z-index:1000}
.nav-inner{display:flex;align-items:center;justify-content:space-between}
.nav-logo{display:flex;align-items:center;gap:10px;text-decoration:none}
.nav-logo-icon{width:36px;height:36px;background:linear-gradient(135deg,var(--clr-green),var(--clr-green-light));border-radius:10px;display:flex;align-items:center;justify-content:center}
.nav-logo-icon svg{fill:white;width:20px;height:20px}
.nav-logo-text{font-family:var(--ff-display);font-size:1.4rem;font-weight:700;color:var(--clr-white)}
.nav-logo-text span{color:var(--clr-amber)}
.nav-links{display:flex;align-items:center;gap:32px;list-style:none}
.nav-links a{text-decoration:none;color:var(--clr-gray);font-size:.9rem;font-weight:500;transition:var(--transition)}
.nav-links a:hover{color:var(--clr-white)}

/* USER DROPDOWN */
.user-menu{position:relative;display:flex;align-items:center;gap:12px;cursor:pointer;padding:4px 8px;border-radius:30px;transition:var(--transition);border:1px solid transparent}
.user-menu:hover{background:var(--clr-surface);border-color:var(--clr-border)}
.nav-avatar{width:32px;height:32px;border-radius:50%;background:linear-gradient(135deg,var(--clr-amber),var(--clr-amber-dark));color:#0d0d0d;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:.9rem}
.nav-username{font-size:.9rem;font-weight:600;color:var(--clr-white)}
.user-dropdown{position:absolute;top:calc(100% + 10px);right:0;width:200px;background:var(--clr-surface);border:1px solid var(--clr-border);border-radius:12px;padding:8px 0;box-shadow:0 12px 32px rgba(0,0,0,.5);opacity:0;visibility:hidden;transform:translateY(10px);transition:var(--transition);z-index:2000}
.user-menu.active .user-dropdown{opacity:1;visibility:visible;transform:translateY(0)}
.dd-item{display:flex;align-items:center;gap:10px;padding:10px 16px;color:var(--clr-gray);text-decoration:none;font-size:.9rem;transition:var(--transition)}
.dd-item:hover{background:var(--clr-surface2);color:var(--clr-white)}
.dd-item svg{width:16px;height:16px}
.dd-divider{height:1px;background:var(--clr-border);margin:8px 0}
.dd-logout{color:var(--clr-coral)}
.dd-logout:hover{color:var(--clr-coral);background:rgba(255,107,107,.05)}

/* DASHBOARD LAYOUT */
.dash-layout{display:flex;min-height:calc(100vh - 65px);position:relative}

/* SIDEBAR */
.sidebar{width:260px;background:var(--clr-surface);border-right:1px solid var(--clr-border);display:flex;flex-direction:column;position:sticky;top:65px;height:calc(100vh - 65px);overflow-y:auto;z-index:100;flex-shrink:0}
.sb-profile{padding:32px 24px;text-align:center;border-bottom:1px solid var(--clr-border)}
.sb-avatar-wrap{position:relative;width:80px;height:80px;margin:0 auto 16px;border-radius:50%;padding:4px;background:linear-gradient(135deg,var(--clr-green-light),var(--clr-amber));display:flex;align-items:center;justify-content:center}
.sb-avatar{width:100%;height:100%;border-radius:50%;background:var(--clr-surface2);color:var(--clr-white);display:flex;align-items:center;justify-content:center;font-family:var(--ff-display);font-size:2rem;font-weight:700;overflow:hidden}
.sb-avatar img{width:100%;height:100%;object-fit:cover}
.sb-name{font-family:var(--ff-display);font-size:1.2rem;font-weight:700;margin-bottom:4px}
.sb-email{font-size:.8rem;color:var(--clr-gray);font-family:var(--ff-mono);margin-bottom:16px}
.sb-nav{padding:24px 16px;display:flex;flex-direction:column;gap:8px;flex:1}
.sb-link{display:flex;align-items:center;gap:12px;padding:12px 16px;color:var(--clr-gray);text-decoration:none;font-size:.95rem;font-weight:500;border-radius:8px;transition:all .2s ease;border-left:3px solid transparent}
.sb-link svg{width:18px;height:18px;stroke-width:2.5}
.sb-link:hover{background:var(--clr-surface2);color:var(--clr-white)}
.sb-link.active{background:linear-gradient(90deg,rgba(26,107,74,.15),transparent);color:var(--clr-green-light);border-left-color:var(--clr-amber)}
.sb-link.active svg{stroke:var(--clr-green-light)}
.badge{background:var(--clr-coral);color:white;font-size:.7rem;font-family:var(--ff-mono);font-weight:700;padding:2px 8px;border-radius:100px;margin-left:auto}
.badge.hidden{display:none}

/* MAIN CONTENT AREA */
.main-content{flex:1;padding:40px;background:var(--clr-bg);overflow-x:hidden}
.tab-pane{display:none;animation:fadeUp .4s ease both}
.tab-pane.active{display:block}
.page-header{margin-bottom:32px;display:flex;align-items:flex-end;justify-content:space-between;flex-wrap:wrap;gap:16px}
.page-title{font-family:var(--ff-display);font-size:2rem;font-weight:700;color:var(--clr-white)}
.page-subtitle{color:var(--clr-gray);font-size:.95rem;margin-top:6px}

/* DASHBOARD OVERVIEW (TAB 1) */
.stat-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:24px;margin-bottom:40px}
.s-card{background:var(--clr-surface);border:1px solid var(--clr-border);border-radius:var(--radius-lg);padding:24px;display:flex;flex-direction:column;position:relative;overflow:hidden}
.s-card::before{content:'';position:absolute;top:0;left:0;right:0;height:2px;background:linear-gradient(90deg,var(--clr-green),transparent)}
.s-card.amber::before{background:linear-gradient(90deg,var(--clr-amber),transparent)}
.sc-header{display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:16px;color:var(--clr-gray)}
.sc-icon{width:40px;height:40px;border-radius:10px;background:var(--clr-surface2);display:flex;align-items:center;justify-content:center;color:var(--clr-green-light)}
.s-card.amber .sc-icon{color:var(--clr-amber)}
.sc-value{font-family:var(--ff-display);font-size:2.5rem;font-weight:700;line-height:1;margin-bottom:8px;color:var(--clr-white)}
.sc-label{font-size:.9rem;color:var(--clr-gray);font-weight:500}
.sc-trend{font-size:.8rem;font-family:var(--ff-mono);display:flex;align-items:center;gap:4px;margin-top:12px;padding-top:12px;border-top:1px solid var(--clr-border)}
.trend-up{color:var(--clr-green-light)}.trend-down{color:var(--clr-coral)}.trend-neu{color:var(--clr-gray)}

.dash-sections{display:grid;grid-template-columns:2fr 1fr;gap:32px}
.section-box{background:var(--clr-surface);border:1px solid var(--clr-border);border-radius:var(--radius-lg);padding:24px}
.box-header{display:flex;justify-content:space-between;align-items:center;margin-bottom:20px}
.box-title{font-family:var(--ff-display);font-size:1.2rem;font-weight:700}
.box-link{font-size:.85rem;color:var(--clr-amber);text-decoration:none}
.box-link:hover{text-decoration:underline}

/* CHART MOCKUP (CSS BAR CHART) */
.chart-container{height:200px;display:flex;align-items:flex-end;gap:12px;padding:20px 0 0;border-bottom:1px solid var(--clr-border);position:relative}
.chart-bar-group{flex:1;display:flex;justify-content:center;gap:6px;position:relative;height:100%;align-items:flex-end}
.c-bar{width:16px;border-radius:4px 4px 0 0;position:relative;transition:var(--transition);cursor:pointer;animation:growUp 1s cubic-bezier(0.2, 0.8, 0.2, 1) both}
.c-bar.up{background:var(--clr-green-light);transform-origin:bottom}
.c-bar.dn{background:var(--clr-border);transform-origin:bottom}
.c-bar:hover{filter:brightness(1.2)}
.c-label{position:absolute;bottom:-24px;font-size:.7rem;color:var(--clr-gray);font-family:var(--ff-mono);text-align:center;width:100%}

/* MINI LISTS */
.mini-list{display:flex;flex-direction:column;gap:12px}
.mini-item{display:flex;align-items:center;gap:12px;padding:12px;background:var(--clr-surface2);border-radius:10px;border:1px solid transparent;transition:var(--transition);text-decoration:none;color:inherit}
.mini-item:hover{border-color:var(--clr-border);background:var(--clr-bg)}
.mi-icon{width:36px;height:36px;background:rgba(26,107,74,.1);color:var(--clr-green-light);border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:1.1rem;flex-shrink:0}
.mi-info{flex:1;min-width:0}
.mi-title{font-weight:600;font-size:.9rem;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;margin-bottom:2px}
.mi-meta{font-size:.75rem;color:var(--clr-gray);font-family:var(--ff-mono)}

/* PROGRESS BAR */
.prog-container{margin-top:16px}
.prog-header{display:flex;justify-content:space-between;font-size:.85rem;margin-bottom:8px}
.prog-track{height:8px;background:var(--clr-surface2);border-radius:4px;overflow:hidden}
.prog-fill{height:100%;background:linear-gradient(90deg,var(--clr-amber),var(--clr-amber-dark));width:65%;border-radius:4px}

/* TAB 2 & 3: GRID LISTINGS (UPLOADS & BOOKMARKS) */
.toolbar{display:flex;gap:16px;margin-bottom:24px;flex-wrap:wrap}
.search-bar{flex:1;min-width:200px;position:relative}
.search-bar input{width:100%;background:var(--clr-surface);border:1px solid var(--clr-border);color:var(--clr-white);padding:10px 16px 10px 40px;border-radius:8px;font-family:var(--ff-body);font-size:.9rem;outline:none;transition:var(--transition)}
.search-bar input:focus{border-color:var(--clr-green-light)}
.search-bar svg{position:absolute;left:14px;top:50%;transform:translateY(-50%);color:var(--clr-gray);width:16px;height:16px}
.filter-dropdown{background:var(--clr-surface);border:1px solid var(--clr-border);color:var(--clr-white);padding:10px 16px;border-radius:8px;font-family:var(--ff-body);font-size:.9rem;outline:none;cursor:pointer}

.mat-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:24px}
.mat-card{background:var(--clr-surface);border:1px solid var(--clr-border);border-radius:16px;padding:20px;display:flex;flex-direction:column;transition:var(--transition);position:relative}
.mat-card:hover{border-color:var(--clr-green-light);transform:translateY(-4px);box-shadow:0 12px 24px rgba(0,0,0,.3)}
.mc-status{position:absolute;top:20px;right:20px;font-size:.7rem;font-family:var(--ff-mono);padding:2px 8px;border-radius:100px;font-weight:600}
.mc-status.pub{background:rgba(26,107,74,.15);color:var(--clr-green-light)}
.mc-status.drf{background:rgba(245,166,35,.15);color:var(--clr-amber)}
.mc-type{font-size:.75rem;font-family:var(--ff-mono);color:var(--clr-gray);margin-bottom:8px}
.mc-title{font-weight:700;font-size:1.05rem;line-height:1.4;margin-bottom:12px;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.mc-stats{display:flex;gap:16px;font-size:.8rem;color:var(--clr-gray);margin-bottom:20px;padding-bottom:16px;border-bottom:1px solid var(--clr-border)}
.mc-stats span{display:flex;align-items:center;gap:4px}
.mc-actions{display:flex;gap:8px;margin-top:auto}

/* LIST VIEWS (DOWNLOADS & NOTIF) */
.list-view{display:flex;flex-direction:column;gap:12px}
.list-row{background:var(--clr-surface);border:1px solid var(--clr-border);border-radius:12px;padding:16px 20px;display:flex;align-items:center;gap:20px;transition:var(--transition)}
.list-row:hover{border-color:var(--clr-gray2)}
.lr-icon{width:40px;height:40px;background:var(--clr-surface2);border-radius:10px;display:flex;align-items:center;justify-content:center;color:var(--clr-gray)}
.lr-icon.dl{color:var(--clr-amber)}
.lr-icon.noti{color:var(--clr-green-light)}
.list-row.unread{border-left:3px solid var(--clr-amber);background:rgba(245,166,35,.03)}
.lr-content{flex:1}
.lr-title{font-weight:600;font-size:.95rem;margin-bottom:4px}
.lr-desc{font-size:.85rem;color:var(--clr-gray)}
.lr-meta{font-family:var(--ff-mono);font-size:.75rem;color:var(--clr-gray2);min-width:100px;text-align:right}

/* SETTINGS FORM */
.settings-section{background:var(--clr-surface);border:1px solid var(--clr-border);border-radius:var(--radius-lg);padding:32px;margin-bottom:32px}
.settings-section h3{font-family:var(--ff-display);font-size:1.4rem;margin-bottom:24px;padding-bottom:16px;border-bottom:1px solid var(--clr-border)}
.set-row{display:flex;gap:24px;margin-bottom:20px}
.set-group{flex:1}
.set-group label{display:block;font-size:.85rem;font-weight:500;color:var(--clr-gray);margin-bottom:8px}
.set-control{width:100%;background:var(--clr-surface2);border:1px solid var(--clr-border);color:var(--clr-white);padding:12px 16px;border-radius:8px;font-family:var(--ff-body);font-size:.95rem;outline:none;transition:var(--transition)}
.set-control:focus{border-color:var(--clr-green-light)}
.avatar-upload-wrap{display:flex;align-items:center;gap:24px;margin-bottom:32px}
.av-preview{width:100px;height:100px;border-radius:50%;background:var(--clr-surface2);border:2px dashed var(--clr-border);display:flex;align-items:center;justify-content:center;overflow:hidden;position:relative;cursor:pointer}
.av-preview img{width:100%;height:100%;object-fit:cover;display:none}
.av-preview::after{content:'+';position:absolute;font-size:2rem;color:var(--clr-gray);transition:var(--transition)}
.av-preview:hover::after{color:var(--clr-white);transform:scale(1.2)}
.av-preview.has-img::after{display:none}
input[type="file"]{display:none}

/* TOGGLES */
.toggle-wrap{display:flex;align-items:center;justify-content:space-between;padding:16px 0;border-bottom:1px solid var(--clr-border)}
.toggle-info strong{display:block;font-size:.95rem;margin-bottom:4px}
.toggle-info span{font-size:.85rem;color:var(--clr-gray)}
.switch{position:relative;display:inline-block;width:44px;height:24px}
.switch input{display:none}
.slider{position:absolute;cursor:pointer;top:0;left:0;right:0;bottom:0;background-color:var(--clr-surface2);transition:.4s;border-radius:34px;border:1px solid var(--clr-border)}
.slider:before{position:absolute;content:"";height:18px;width:18px;left:2px;bottom:2px;background-color:var(--clr-gray);transition:.4s;border-radius:50%}
input:checked + .slider{background-color:var(--clr-green-light);border-color:var(--clr-green-light)}
input:checked + .slider:before{transform:translateX(20px);background-color:white}

/* TOAST & MODAL */
#nn-toast{position:fixed;bottom:28px;left:50%;transform:translateX(-50%) translateY(20px);background:var(--clr-green);border:1px solid var(--clr-green-light);color:white;padding:12px 24px;border-radius:10px;font-size:.9rem;font-family:var(--ff-body);z-index:4000;opacity:0;transition:all .3s ease;white-space:nowrap;box-shadow:0 8px 24px rgba(0,0,0,.5);font-weight:500;display:flex;align-items:center;gap:8px}

.modal-back{position:fixed;inset:0;background:rgba(0,0,0,.8);backdrop-filter:blur(5px);z-index:3000;display:flex;align-items:center;justify-content:center;opacity:0;visibility:hidden;transition:var(--transition)}
.modal-back.show{opacity:1;visibility:visible}
.modal{background:var(--clr-surface);border:1px solid var(--clr-border);border-radius:var(--radius-lg);padding:32px;width:90%;max-width:400px;transform:translateY(20px);transition:transform .3s ease}
.modal-back.show .modal{transform:translateY(0)}
.modal h3{font-family:var(--ff-display);font-size:1.4rem;margin-bottom:12px}
.modal p{color:var(--clr-gray);font-size:.95rem;margin-bottom:24px}
.modal-actions{display:flex;gap:12px;justify-content:flex-end}

@keyframes fadeUp{from{opacity:0;transform:translateY(15px)}to{opacity:1;transform:none}}
@keyframes growUp{from{transform:scaleY(0)}to{transform:scaleY(1)}}

/* RESPONSIVE */
.hamburger{display:none;flex-direction:column;gap:5px;background:none;border:none;cursor:pointer;padding:4px}
.hamburger span{display:block;width:24px;height:2px;background:var(--clr-white);border-radius:2px;transition:var(--transition)}
.hamburger.open span:nth-child(1){transform:translateY(7px) rotate(45deg)}
.hamburger.open span:nth-child(2){opacity:0}
.hamburger.open span:nth-child(3){transform:translateY(-7px) rotate(-45deg)}
.mobile-menu{display:none;position:absolute;top:100%;left:0;right:0;background:rgba(13,13,13,.97);backdrop-filter:blur(20px);border-bottom:1px solid var(--clr-border);padding:24px}
.mobile-menu.open{display:block}
.mobile-menu ul{list-style:none;display:flex;flex-direction:column;gap:20px}
.mobile-menu ul a{text-decoration:none;color:var(--clr-gray);font-size:1.1rem;font-weight:500}

@media(max-width:1024px){
  .dash-layout{flex-direction:column}
  .sidebar{width:100%;height:auto;position:static;flex-direction:row;align-items:center;padding:16px 24px;border-right:none;border-bottom:1px solid var(--clr-border);overflow-x:auto}
  .sb-profile{display:none} /* hide profile header in top bar mode */
  .sb-nav{flex-direction:row;padding:0;gap:8px}
  .sb-link{white-space:nowrap;padding:8px 16px;border-left:none;border-bottom:3px solid transparent}
  .sb-link.active{background:var(--clr-surface2);border-bottom-color:var(--clr-amber)}
  .dash-sections{grid-template-columns:1fr}
}
@media(max-width:600px){
  .nav-links{display:none}
  .hamburger{display:flex}
  .user-menu{display:none} /* Handle mobile via hamburger instead */
  .main-content{padding:24px 16px}
  .set-row{flex-direction:column;gap:16px}
  .list-row{flex-direction:column;align-items:flex-start;gap:12px;position:relative}
  .lr-meta{position:absolute;top:16px;right:20px}
}
</style>
</head>
