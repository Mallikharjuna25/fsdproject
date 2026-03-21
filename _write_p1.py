path = r'c:\Users\kharj\OneDrive\Desktop\fsd project\browse.html'

html_head = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1.0"/>
<meta name="description" content="Browse thousands of study notes, model papers, question papers and more on NoteNest — free forever."/>
<title>Browse Materials — NoteNest</title>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700;900&family=DM+Sans:wght@300;400;500;600&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet"/>
<style>
:root{--clr-bg:#0d0d0d;--clr-surface:#1a1a1a;--clr-surface2:#1e1e1e;--clr-border:#2a2a2a;--clr-green:#1a6b4a;--clr-green-light:#22a06b;--clr-green-glow:rgba(26,107,74,.35);--clr-amber:#f5a623;--clr-amber-dark:#c4821a;--clr-coral:#ff6b6b;--clr-white:#ffffff;--clr-gray:#a0a0a0;--clr-gray2:#6a6a6a;--ff-display:'Playfair Display',serif;--ff-body:'DM Sans',sans-serif;--ff-mono:'JetBrains Mono',monospace;--radius:12px;--radius-lg:20px;--shadow-glow:0 0 24px var(--clr-green-glow);--transition:.3s ease}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{background:var(--clr-bg);color:var(--clr-white);font-family:var(--ff-body);overflow-x:hidden;line-height:1.6}
::-webkit-scrollbar{width:6px}::-webkit-scrollbar-track{background:#111}::-webkit-scrollbar-thumb{background:var(--clr-green);border-radius:3px}
.container{max-width:1200px;margin:0 auto;padding:0 24px}
.fade-in{opacity:0;transform:translateY(20px);transition:opacity .6s ease,transform .6s ease}
.fade-in.visible{opacity:1;transform:none}
#backTop{position:fixed;bottom:32px;right:32px;width:44px;height:44px;background:var(--clr-green);border:none;border-radius:50%;cursor:pointer;display:flex;align-items:center;justify-content:center;opacity:0;visibility:hidden;transition:var(--transition);z-index:500;box-shadow:var(--shadow-glow)}
#backTop.show{opacity:1;visibility:visible}
#backTop:hover{background:var(--clr-green-light);transform:translateY(-3px)}
#backTop svg{fill:white;width:18px;height:18px}
nav{position:fixed;top:0;left:0;right:0;z-index:1000;padding:20px 0;transition:var(--transition)}
nav.scrolled{background:rgba(13,13,13,.9);backdrop-filter:blur(20px);border-bottom:1px solid var(--clr-border);padding:14px 0}
.nav-inner{display:flex;align-items:center;justify-content:space-between}
.nav-logo{display:flex;align-items:center;gap:10px;text-decoration:none}
.nav-logo-icon{width:36px;height:36px;background:linear-gradient(135deg,var(--clr-green),var(--clr-green-light));border-radius:10px;display:flex;align-items:center;justify-content:center}
.nav-logo-icon svg{fill:white;width:20px;height:20px}
.nav-logo-text{font-family:var(--ff-display);font-size:1.4rem;font-weight:700;color:var(--clr-white)}
.nav-logo-text span{color:var(--clr-amber)}
.nav-links{display:flex;align-items:center;gap:32px;list-style:none}
.nav-links a{text-decoration:none;color:var(--clr-gray);font-size:.9rem;font-weight:500;transition:var(--transition);position:relative}
.nav-links a::after{content:'';position:absolute;bottom:-4px;left:0;width:0;height:2px;background:var(--clr-amber);transition:var(--transition)}
.nav-links a:hover{color:var(--clr-white)}.nav-links a:hover::after,.nav-links a.active::after{width:100%}
.nav-links a.active{color:var(--clr-white)}
.btn-amber{background:var(--clr-amber);color:#0d0d0d;font-weight:600;border:none;padding:10px 22px;border-radius:8px;cursor:pointer;font-family:var(--ff-body);font-size:.9rem;transition:var(--transition);text-decoration:none;display:inline-flex;align-items:center;gap:6px}
.btn-amber:hover{background:var(--clr-amber-dark);transform:translateY(-2px);box-shadow:0 8px 24px rgba(245,166,35,.3)}
.hamburger{display:none;flex-direction:column;gap:5px;background:none;border:none;cursor:pointer;padding:4px}
.hamburger span{display:block;width:24px;height:2px;background:var(--clr-white);border-radius:2px;transition:var(--transition)}
.hamburger.open span:nth-child(1){transform:translateY(7px) rotate(45deg)}
.hamburger.open span:nth-child(2){opacity:0}
.hamburger.open span:nth-child(3){transform:translateY(-7px) rotate(-45deg)}
.mobile-menu{display:none;position:absolute;top:100%;left:0;right:0;background:rgba(13,13,13,.97);backdrop-filter:blur(20px);border-bottom:1px solid var(--clr-border);padding:24px}
.mobile-menu.open{display:block}
.mobile-menu ul{list-style:none;display:flex;flex-direction:column;gap:20px}
.mobile-menu ul a{text-decoration:none;color:var(--clr-gray);font-size:1.1rem;font-weight:500;transition:var(--transition)}
.mobile-menu ul a:hover{color:var(--clr-amber)}
.mobile-menu .btn-amber{margin-top:16px;width:100%;justify-content:center}
.page-hero{padding:140px 24px 60px;text-align:center;position:relative;overflow:hidden;background:linear-gradient(180deg,rgba(26,107,74,.07) 0%,transparent 100%)}
.page-hero::before{content:'';position:absolute;width:700px;height:350px;background:radial-gradient(ellipse,var(--clr-green-glow) 0%,transparent 70%);top:40%;left:50%;transform:translate(-50%,-50%);pointer-events:none}
.page-hero h1{font-family:var(--ff-display);font-size:clamp(2.2rem,5vw,3.8rem);font-weight:900;letter-spacing:-.02em;margin-bottom:12px;position:relative}
.page-hero h1 span{color:var(--clr-amber)}
.page-hero .sub{color:var(--clr-gray);font-size:clamp(.95rem,1.8vw,1.1rem);margin-bottom:32px;position:relative}
.search-wrap{max-width:680px;margin:0 auto 24px;position:relative}
.search-wrap input{width:100%;padding:16px 64px 16px 22px;background:var(--clr-surface);border:1px solid var(--clr-border);border-radius:var(--radius-lg);color:var(--clr-white);font-family:var(--ff-body);font-size:1rem;outline:none;transition:var(--transition)}
.search-wrap input::placeholder{color:var(--clr-gray2)}
.search-wrap input:focus{border-color:var(--clr-green-light);box-shadow:0 0 0 3px rgba(34,160,107,.15)}
.search-wrap button{position:absolute;right:8px;top:50%;transform:translateY(-50%);background:var(--clr-amber);border:none;border-radius:10px;width:44px;height:44px;cursor:pointer;display:flex;align-items:center;justify-content:center;transition:var(--transition)}
.search-wrap button:hover{background:var(--clr-amber-dark)}
.search-wrap button svg{stroke:var(--clr-bg);fill:none;width:18px;height:18px;stroke-width:2.5;stroke-linecap:round;stroke-linejoin:round}
.popular-tags{display:flex;flex-wrap:wrap;gap:8px;justify-content:center;max-width:680px;margin:0 auto;position:relative}
.pop-tag{background:rgba(26,107,74,.1);border:1px solid rgba(26,107,74,.25);color:var(--clr-green-light);padding:6px 14px;border-radius:100px;font-size:.8rem;font-weight:500;cursor:pointer;transition:var(--transition)}
.pop-tag:hover,.pop-tag.active{background:var(--clr-green);color:white;border-color:var(--clr-green)}
.browse-layout{display:grid;grid-template-columns:260px 1fr;gap:28px;padding:40px 0 80px;align-items:start}
.filter-sidebar{background:var(--clr-surface);border:1px solid var(--clr-border);border-radius:var(--radius-lg);padding:24px;position:sticky;top:90px;max-height:calc(100vh - 110px);overflow-y:auto}
.filter-sidebar::-webkit-scrollbar{width:4px}.filter-sidebar::-webkit-scrollbar-thumb{background:var(--clr-border);border-radius:2px}
.sidebar-header{display:flex;align-items:center;justify-content:space-between;margin-bottom:20px}
.sidebar-header h3{font-family:var(--ff-display);font-size:1.1rem;font-weight:700}
.clear-all-btn{font-size:.78rem;color:var(--clr-amber);background:none;border:none;cursor:pointer;font-family:var(--ff-body);font-weight:500;transition:var(--transition)}
.clear-all-btn:hover{color:var(--clr-amber-dark)}
.filter-group{border-bottom:1px solid var(--clr-border);padding:14px 0}
.filter-group:last-of-type{border-bottom:none}
.filter-group-header{display:flex;align-items:center;justify-content:space-between;cursor:pointer;user-select:none}
.filter-group-header span:first-child{font-size:.88rem;font-weight:600;color:var(--clr-white)}
.fg-arrow{font-size:.7rem;color:var(--clr-gray);transition:var(--transition)}
.filter-group.open .fg-arrow{transform:rotate(180deg);color:var(--clr-amber)}
.filter-group-body{display:none;margin-top:12px;gap:10px;flex-direction:column}
.filter-group.open .filter-group-body{display:flex}
.filter-check{display:flex;align-items:center;gap:10px;cursor:pointer;font-size:.84rem;color:var(--clr-gray);transition:var(--transition)}
.filter-check:hover{color:var(--clr-white)}
.filter-check input[type=checkbox]{accent-color:var(--clr-green-light);width:15px;height:15px;cursor:pointer;flex-shrink:0}
.subject-search{width:100%;padding:8px 12px;background:rgba(255,255,255,.05);border:1px solid var(--clr-border);border-radius:8px;color:var(--clr-white);font-family:var(--ff-body);font-size:.82rem;outline:none;margin-bottom:6px}
.subject-search:focus{border-color:var(--clr-green-light)}
.filter-actions{display:flex;gap:10px;margin-top:18px}
.apply-btn{flex:1;padding:10px;background:var(--clr-green);color:white;border:none;border-radius:8px;cursor:pointer;font-family:var(--ff-body);font-weight:600;font-size:.88rem;transition:var(--transition)}
.apply-btn:hover{background:var(--clr-green-light)}
.clear-btn{padding:10px 14px;background:transparent;color:var(--clr-gray);border:1px solid var(--clr-border);border-radius:8px;cursor:pointer;font-family:var(--ff-body);font-size:.88rem;transition:var(--transition)}
.clear-btn:hover{border-color:var(--clr-coral);color:var(--clr-coral)}
.mobile-filter-btn{display:none;align-items:center;gap:8px;padding:10px 18px;background:var(--clr-surface);border:1px solid var(--clr-border);border-radius:10px;color:var(--clr-white);font-family:var(--ff-body);font-size:.9rem;cursor:pointer;margin-bottom:16px;transition:var(--transition)}
.mobile-filter-btn:hover{border-color:var(--clr-green-light)}
.filter-overlay{display:none;position:fixed;inset:0;background:rgba(0,0,0,.7);z-index:800;backdrop-filter:blur(4px)}
.filter-overlay.open{display:block}
.sidebar-drawer{position:fixed;left:0;top:0;bottom:0;width:290px;background:var(--clr-surface);z-index:900;padding:24px;overflow-y:auto;transform:translateX(-100%);transition:transform .35s ease}
.sidebar-drawer.open{transform:translateX(0)}
.drawer-close{position:absolute;top:16px;right:16px;background:none;border:none;color:var(--clr-gray);cursor:pointer;font-size:1.4rem;line-height:1;padding:4px}
.active-chips{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:16px;min-height:0}
.chip{display:inline-flex;align-items:center;gap:6px;padding:5px 12px;background:rgba(26,107,74,.15);border:1px solid rgba(26,107,74,.4);border-radius:100px;font-size:.78rem;color:var(--clr-green-light);font-family:var(--ff-mono)}
.chip button{background:none;border:none;color:var(--clr-green-light);cursor:pointer;font-size:.9rem;line-height:1;padding:0;transition:var(--transition)}
.chip button:hover{color:var(--clr-coral)}
.results-topbar{display:flex;align-items:center;justify-content:space-between;gap:12px;margin-bottom:20px;flex-wrap:wrap}
.results-count{font-size:.9rem;color:var(--clr-gray)}
.results-count strong{color:var(--clr-white)}
.topbar-right{display:flex;align-items:center;gap:12px}
.sort-select,.per-page-select{padding:8px 14px;background:var(--clr-surface);border:1px solid var(--clr-border);border-radius:8px;color:var(--clr-white);font-family:var(--ff-body);font-size:.84rem;outline:none;cursor:pointer;transition:var(--transition)}
.sort-select:focus,.per-page-select:focus{border-color:var(--clr-green-light)}
.view-toggle{display:flex;border:1px solid var(--clr-border);border-radius:8px;overflow:hidden}
.view-btn{padding:8px 12px;background:transparent;border:none;cursor:pointer;display:flex;align-items:center;transition:var(--transition)}
.view-btn svg{stroke:var(--clr-gray);fill:none;width:16px;height:16px;stroke-width:2;stroke-linecap:round;stroke-linejoin:round;transition:var(--transition)}
.view-btn.active{background:var(--clr-green)}.view-btn.active svg{stroke:white}
#resultsGrid{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}
#resultsGrid.list-view{grid-template-columns:1fr}
.mat-card{background:var(--clr-surface);border:1px solid var(--clr-border);border-radius:var(--radius-lg);padding:20px;transition:var(--transition);position:relative;display:flex;flex-direction:column;gap:12px}
.mat-card:hover{transform:translateY(-5px);box-shadow:0 16px 48px rgba(0,0,0,.6),0 0 0 1px var(--clr-green-light)}
.mat-thumb{height:110px;background:linear-gradient(135deg,rgba(26,107,74,.12),rgba(26,107,74,.04));border-radius:10px;display:flex;align-items:center;justify-content:center;position:relative;overflow:hidden;flex-shrink:0}
.mat-thumb-icon{font-size:2.8rem;opacity:.85}
.mat-badge{font-family:var(--ff-mono);font-size:.68rem;font-weight:600;padding:3px 8px;border-radius:5px;position:absolute;top:8px;right:8px;letter-spacing:.5px}
.mat-badge.pdf{background:rgba(255,107,107,.15);color:var(--clr-coral);border:1px solid rgba(255,107,107,.3)}
.mat-badge.doc{background:rgba(34,160,107,.15);color:var(--clr-green-light);border:1px solid rgba(34,160,107,.3)}
.mat-badge.ppt{background:rgba(245,166,35,.15);color:var(--clr-amber);border:1px solid rgba(245,166,35,.3)}
.mat-badge.img{background:rgba(0,180,166,.15);color:#00b4a6;border:1px solid rgba(0,180,166,.3)}
.mat-card-body{display:flex;flex-direction:column;gap:10px;flex:1}
.mat-title{font-family:var(--ff-display);font-size:.95rem;font-weight:700;line-height:1.35;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.mat-tags{display:flex;flex-wrap:wrap;gap:6px}
.mat-tag{font-size:.72rem;padding:3px 9px;background:rgba(255,255,255,.05);border:1px solid var(--clr-border);border-radius:100px;color:var(--clr-gray)}
.mat-desc{font-size:.82rem;color:var(--clr-gray2);display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.mat-uploader{display:flex;align-items:center;gap:6px;font-size:.78rem;color:var(--clr-gray2)}
.mat-avatar{width:20px;height:20px;border-radius:50%;background:linear-gradient(135deg,var(--clr-green),var(--clr-green-light));display:flex;align-items:center;justify-content:center;font-size:.55rem;font-weight:700;color:white;flex-shrink:0}
.mat-rating-row{display:flex;align-items:center;justify-content:space-between}
.mat-stars{color:var(--clr-amber);font-size:.82rem;letter-spacing:.5px}
.mat-dl-count{font-size:.75rem;color:var(--clr-gray2);display:flex;align-items:center;gap:4px}
.mat-dl-count svg{stroke:var(--clr-gray2);fill:none;width:13px;height:13px;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}
.mat-actions{display:flex;gap:8px;margin-top:auto}
.mat-download-btn{flex:1;padding:9px;background:var(--clr-amber);color:#0d0d0d;border:none;border-radius:8px;cursor:pointer;font-family:var(--ff-body);font-weight:600;font-size:.82rem;transition:var(--transition);display:flex;align-items:center;justify-content:center;gap:5px}
.mat-download-btn:hover{background:var(--clr-amber-dark);transform:translateY(-1px)}
.mat-bookmark-btn{width:36px;height:36px;background:transparent;border:1px solid var(--clr-border);border-radius:8px;cursor:pointer;display:flex;align-items:center;justify-content:center;transition:var(--transition);padding:0;flex-shrink:0}
.mat-bookmark-btn svg{stroke:var(--clr-gray);fill:none;width:15px;height:15px;stroke-width:2;stroke-linecap:round;stroke-linejoin:round;transition:var(--transition)}
.mat-bookmark-btn.saved svg{stroke:var(--clr-amber);fill:var(--clr-amber)}
.mat-bookmark-btn:hover{border-color:var(--clr-amber)}
#resultsGrid.list-view .mat-card{flex-direction:row;gap:16px;align-items:flex-start}
#resultsGrid.list-view .mat-thumb{width:90px;height:90px}
#emptyState{text-align:center;padding:80px 24px;display:none}
#emptyState svg{width:80px;height:80px;stroke:var(--clr-border);fill:none;stroke-width:1.5;stroke-linecap:round;stroke-linejoin:round;margin:0 auto 20px;display:block}
#emptyState h3{font-family:var(--ff-display);font-size:1.5rem;margin-bottom:8px}
#emptyState p{color:var(--clr-gray);margin-bottom:20px}
.empty-clear-btn{padding:10px 24px;background:var(--clr-green);color:white;border:none;border-radius:8px;cursor:pointer;font-family:var(--ff-body);font-weight:600;transition:var(--transition)}
.empty-clear-btn:hover{background:var(--clr-green-light)}
.pagination{display:flex;align-items:center;justify-content:space-between;margin-top:40px;flex-wrap:wrap;gap:12px}
.page-btns{display:flex;gap:6px;align-items:center}
.page-btn{min-width:38px;height:38px;padding:0 8px;border:1px solid var(--clr-border);background:transparent;color:var(--clr-gray);border-radius:8px;cursor:pointer;font-family:var(--ff-body);font-size:.88rem;transition:var(--transition);display:flex;align-items:center;justify-content:center}
.page-btn svg{stroke:currentColor;fill:none;width:15px;height:15px;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}
.page-btn:hover{border-color:var(--clr-green-light);color:var(--clr-white)}
.page-btn.active{background:var(--clr-green);border-color:var(--clr-green);color:white;font-weight:600}
.page-btn:disabled{opacity:.3;cursor:not-allowed;pointer-events:none}
.per-page-row{display:flex;align-items:center;gap:10px;font-size:.84rem;color:var(--clr-gray)}
footer{background:var(--clr-surface);border-top:1px solid var(--clr-border);padding:60px 0 0}
.footer-grid{display:grid;grid-template-columns:1.8fr 1fr 1fr 1fr;gap:40px;padding-bottom:48px}
.footer-brand p{color:var(--clr-gray);font-size:.88rem;line-height:1.7;margin-top:14px;max-width:260px}
.footer-socials{display:flex;gap:12px;margin-top:20px}
.soc-btn{width:36px;height:36px;background:rgba(255,255,255,.05);border:1px solid var(--clr-border);border-radius:8px;display:flex;align-items:center;justify-content:center;transition:var(--transition);text-decoration:none}
.soc-btn:hover{background:var(--clr-green);border-color:var(--clr-green)}
.soc-btn svg{fill:var(--clr-gray);width:15px;height:15px;transition:var(--transition)}
.soc-btn:hover svg{fill:white}
.footer-col h4{font-family:var(--ff-display);font-size:1rem;font-weight:700;margin-bottom:18px}
.footer-col ul{list-style:none;display:flex;flex-direction:column;gap:12px}
.footer-col ul a{text-decoration:none;color:var(--clr-gray);font-size:.88rem;transition:var(--transition)}
.footer-col ul a:hover{color:var(--clr-amber)}
.footer-bottom{border-top:1px solid var(--clr-border);padding:24px 0;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:12px}
.footer-bottom p{color:var(--clr-gray2);font-size:.82rem}
.footer-bottom span{font-family:var(--ff-mono);font-size:.75rem;color:var(--clr-green-light)}
@media(max-width:1024px){#resultsGrid{grid-template-columns:repeat(2,1fr)}.browse-layout{grid-template-columns:230px 1fr}}
@media(max-width:768px){.nav-links,.nav-cta{display:none}.hamburger{display:flex}.browse-layout{grid-template-columns:1fr}.filter-sidebar{display:none}.mobile-filter-btn{display:flex}.footer-grid{grid-template-columns:1fr 1fr;gap:32px}}
@media(max-width:480px){#resultsGrid,#resultsGrid.list-view .mat-card{grid-template-columns:1fr;flex-direction:column}.footer-grid{grid-template-columns:1fr}.pagination{flex-direction:column;align-items:flex-start}}
</style>
</head>"""

with open(path, 'w', encoding='utf-8') as f:
    f.write(html_head)

import os
print('Part 1 written, size:', os.path.getsize(path))
