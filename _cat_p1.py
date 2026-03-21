<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1.0"/>
<meta name="description" content="Explore study materials by categories, departments, subjects, and exams on NoteNest."/>
<title>All Categories — NoteNest</title>
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

::-webkit-scrollbar{width:8px;height:8px}
::-webkit-scrollbar-track{background:#111}
::-webkit-scrollbar-thumb{background:var(--clr-border);border-radius:4px}
::-webkit-scrollbar-thumb:hover{background:var(--clr-green)}

/* UTILITY */
.container{max-width:1200px;margin:0 auto;padding:0 24px}
.section{padding:80px 0}
.section-title{font-family:var(--ff-display);font-size:2.2rem;font-weight:700;margin-bottom:8px;color:var(--clr-white)}
.section-subtitle{color:var(--clr-gray);font-size:1.05rem;margin-bottom:40px}

/* NAVBAR */
nav{background:rgba(13,13,13,.95);backdrop-filter:blur(20px);border-bottom:1px solid var(--clr-border);padding:14px 0;position:sticky;top:0;z-index:1000}
.nav-inner{display:flex;align-items:center;justify-content:space-between}
.nav-logo{display:flex;align-items:center;gap:10px;text-decoration:none}
.nav-logo-icon{width:36px;height:36px;background:linear-gradient(135deg,var(--clr-green),var(--clr-green-light));border-radius:10px;display:flex;align-items:center;justify-content:center}
.nav-logo-icon svg{fill:white;width:20px;height:20px}
.nav-logo-text{font-family:var(--ff-display);font-size:1.4rem;font-weight:700;color:var(--clr-white)}
.nav-logo-text span{color:var(--clr-amber)}
.nav-links{display:flex;align-items:center;gap:32px;list-style:none}
.nav-links a{text-decoration:none;color:var(--clr-gray);font-size:.95rem;font-weight:500;transition:var(--transition);position:relative}
.nav-links a:hover,.nav-links a.active{color:var(--clr-white)}
.nav-links a.active::after{content:'';position:absolute;bottom:-18px;left:0;width:100%;height:2px;background:var(--clr-amber)}
.btn-nav{background:var(--clr-amber);color:#0d0d0d!important;font-weight:600;padding:8px 20px;border-radius:8px;display:flex;align-items:center;gap:6px}
.btn-nav:hover{background:var(--clr-amber-dark);transform:translateY(-2px);box-shadow:0 8px 24px rgba(245,166,35,.3)}

/* PAGE HEADER */
.page-hero{padding:60px 0 40px;text-align:center;position:relative}
.page-hero::before{content:'';position:absolute;top:0;left:50%;transform:translateX(-50%);width:100vw;height:100%;background:radial-gradient(circle at top,rgba(26,107,74,.15),transparent 70%);z-index:-1}
.hero-title{font-family:var(--ff-display);font-size:3.5rem;font-weight:700;margin-bottom:16px;background:linear-gradient(to right,var(--clr-white),var(--clr-gray));-webkit-background-clip:text;color:transparent}
.hero-search{max-width:600px;margin:32px auto 0;position:relative}
.hero-search input{width:100%;background:var(--clr-surface);border:1px solid var(--clr-border);padding:18px 24px 18px 54px;border-radius:var(--radius-lg);font-size:1.1rem;color:var(--clr-white);font-family:var(--ff-body);transition:var(--transition);box-shadow:0 8px 32px rgba(0,0,0,.4)}
.hero-search input:focus{outline:none;border-color:var(--clr-green-light);box-shadow:var(--shadow-glow)}
.hero-search svg{position:absolute;left:20px;top:50%;transform:translateY(-50%);color:var(--clr-gray);width:22px;height:22px}

/* MATERIAL TYPES (4x2 GRID) */
.type-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:24px}
.type-card{background:var(--clr-surface);border:1px solid var(--clr-border);border-radius:var(--radius-lg);padding:32px 24px;text-align:center;transition:var(--transition);position:relative;overflow:hidden;text-decoration:none;color:inherit;cursor:pointer}
.type-card::before{content:'';position:absolute;inset:0;background:linear-gradient(135deg,rgba(26,107,74,.1),transparent);opacity:0;transition:var(--transition)}
.type-card:hover{border-color:var(--clr-green-light);transform:translateY(-8px);box-shadow:var(--shadow-glow)}
.type-card:hover::before{opacity:1}
.tc-icon{width:64px;height:64px;margin:0 auto 20px;background:var(--clr-surface2);border-radius:16px;display:flex;align-items:center;justify-content:center;font-size:32px;transition:transform .4s cubic-bezier(0.4, 0, 0.2, 1)}
.type-card:hover .tc-icon{transform:scale(1.15) rotate(5deg);background:rgba(26,107,74,.2)}
.tc-title{font-family:var(--ff-display);font-size:1.3rem;font-weight:700;margin-bottom:8px;color:var(--clr-white)}
.tc-desc{font-size:.9rem;color:var(--clr-gray);margin-bottom:16px;line-height:1.4}
.tc-count{font-size:.8rem;font-family:var(--ff-mono);color:var(--clr-amber);background:rgba(245,166,35,.1);padding:4px 12px;border-radius:100px;display:inline-block}

/* BROWSE BY DEPARTMENT (ACCORDION) */
.dept-accordion{display:flex;flex-direction:column;gap:16px}
.dept-item{background:var(--clr-surface);border:1px solid var(--clr-border);border-radius:var(--radius-lg);overflow:hidden;transition:var(--transition)}
.dept-item.active{border-color:var(--clr-gray2);background:var(--clr-surface2)}
.dept-header{padding:24px 32px;display:flex;align-items:center;justify-content:space-between;cursor:pointer;user-select:none}
.dh-left{display:flex;align-items:center;gap:16px}
.dh-icon{width:48px;height:48px;background:rgba(26,107,74,.1);color:var(--clr-green-light);border-radius:12px;display:flex;align-items:center;justify-content:center}
.dh-title{font-family:var(--ff-display);font-size:1.4rem;font-weight:700;color:var(--clr-white)}
.dh-meta{font-size:.9rem;color:var(--clr-gray);font-family:var(--ff-mono)}
.dh-arrow{width:24px;height:24px;color:var(--clr-gray);transition:transform .3s ease}
.dept-item.active .dh-arrow{transform:rotate(180deg);color:var(--clr-white)}
.dept-item.active .dh-icon{background:var(--clr-green);color:white}

.dept-body{max-height:0;overflow:hidden;transition:max-height .5s cubic-bezier(0, 1, 0, 1);background:var(--clr-bg)}
.dept-item.active .dept-body{max-height:1000px;transition:max-height .5s ease-in}
.dept-content{padding:24px 32px 32px}
.subject-row{display:flex;gap:20px;overflow-x:auto;padding-bottom:16px;scroll-snap-type:x mandatory}
.subject-card{min-width:260px;background:var(--clr-surface);border:1px solid var(--clr-border);padding:24px;border-radius:16px;text-decoration:none;color:inherit;transition:var(--transition);scroll-snap-align:start;display:flex;flex-direction:column}
.subject-card:hover{border-color:var(--clr-amber);transform:translateY(-4px);background:var(--clr-surface2)}
.sc-header{display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:12px}
.sc-icon{font-size:24px}
.sc-count{font-size:.75rem;font-family:var(--ff-mono);color:var(--clr-gray);background:var(--clr-surface2);padding:2px 8px;border-radius:100px}
.subject-card:hover .sc-count{background:rgba(245,166,35,.15);color:var(--clr-amber)}
.sc-title{font-weight:700;font-size:1.1rem;margin-bottom:8px;line-height:1.3}
.sc-link{margin-top:auto;font-size:.85rem;color:var(--clr-green-light);font-weight:600;display:flex;align-items:center;gap:4px;transition:gap .2s}
.subject-card:hover .sc-link{gap:8px}

/* EXAM TYPE GRID */
.exam-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:24px}
.exam-card{background:linear-gradient(135deg,var(--clr-surface),rgba(26,107,74,.05));border:1px solid var(--clr-border);border-radius:16px;padding:24px;display:flex;align-items:center;gap:20px;text-decoration:none;color:inherit;transition:var(--transition);position:relative;overflow:hidden}
.exam-card::after{content:'';position:absolute;top:0;right:0;width:100px;height:100%;background:linear-gradient(90deg,transparent,rgba(255,255,255,.02));transform:skewX(-15deg);transition:transform .5s ease}
.exam-card:hover::after{transform:skewX(-15deg) translateX(150px)}
.exam-card:hover{border-color:var(--clr-green-light);background:linear-gradient(135deg,var(--clr-surface2),rgba(26,107,74,.1))}
.ec-badge{width:56px;height:56px;background:var(--clr-surface2);border-radius:12px;display:flex;align-items:center;justify-content:center;font-family:var(--ff-display);font-weight:900;font-size:1.2rem;color:var(--clr-amber);border:1px solid var(--clr-border)}
.ec-info{flex:1}
.ec-title{font-size:1.2rem;font-weight:700;margin-bottom:4px}
.ec-desc{font-size:.85rem;color:var(--clr-gray)}

/* TRENDING TAG CLOUD */
.cloud-container{background:var(--clr-surface);border:1px solid var(--clr-border);border-radius:var(--radius-lg);padding:60px 40px;position:relative;overflow:hidden;min-height:400px;display:flex;align-items:center;justify-content:center}
.tags-wrapper{position:relative;width:100%;height:100%;display:flex;flex-wrap:wrap;align-items:center;justify-content:center;gap:16px;perspective:1000px}
.cloud-tag{display:inline-block;color:var(--clr-gray);text-decoration:none;font-family:var(--ff-mono);transition:var(--transition);position:relative;animation:floatTag 6s ease-in-out infinite alternate}
.cloud-tag:hover{color:var(--clr-amber);transform:scale(1.1)!important;z-index:10;text-shadow:0 0 12px rgba(245,166,35,.4)}
/* Specific classes for randomizing animation delays via JS */
.del-1{animation-delay:0s}.del-2{animation-delay:-1s}.del-3{animation-delay:-2s}.del-4{animation-delay:-3s}.del-5{animation-delay:-4s}

/* POPULAR SUBJECTS THIS WEEK (Horizontal list) */
.trending-week{display:flex;gap:20px;overflow-x:auto;padding-bottom:16px;scroll-snap-type:x mandatory}
.tw-card{min-width:280px;background:var(--clr-surface);border:1px solid var(--clr-border);border-radius:12px;padding:20px;scroll-snap-align:start;display:flex;align-items:center;gap:16px;text-decoration:none;color:inherit;transition:var(--transition)}
.tw-card:hover{background:var(--clr-surface2);border-color:var(--clr-green-light)}
.tw-rank{font-family:var(--ff-display);font-size:1.8rem;font-weight:900;color:var(--clr-border);-webkit-text-stroke:1px var(--clr-gray2)}
.tw-info{flex:1}
.tw-title{font-weight:600;font-size:1rem;margin-bottom:8px}
.tw-bar-bg{height:6px;background:var(--clr-bg);border-radius:3px;overflow:hidden;position:relative}
.tw-bar-fill{height:100%;background:linear-gradient(90deg,var(--clr-green),var(--clr-green-light));border-radius:3px}
.tw-meta{font-size:.75rem;color:var(--clr-gray);margin-top:8px;font-family:var(--ff-mono);display:flex;justify-content:space-between}

/* FOOTER */
footer{background:var(--clr-surface);border-top:1px solid var(--clr-border);padding:60px 0 24px;margin-top:40px}
.ft-grid{display:grid;grid-template-columns:2fr 1fr 1fr 1fr;gap:40px;margin-bottom:60px}
.ft-brand .nav-logo{margin-bottom:16px}
.ft-desc{color:var(--clr-gray);font-size:.95rem;max-width:300px}
.ft-title{font-family:var(--ff-display);font-size:1.2rem;font-weight:700;margin-bottom:20px;color:var(--clr-white)}
.ft-links{list-style:none;display:flex;flex-direction:column;gap:12px}
.ft-links a{color:var(--clr-gray);text-decoration:none;transition:var(--transition);font-size:.95rem}
.ft-links a:hover{color:var(--clr-amber);transform:translateX(4px);display:inline-block}
.ft-bottom{text-align:center;padding-top:24px;border-top:1px solid var(--clr-border);color:var(--clr-gray2);font-size:.9rem}

/* ANIMATIONS */
@keyframes floatTag{
  0%{transform:translateY(0) scale(1)}
  50%{transform:translateY(-10px) scale(1.05)}
  100%{transform:translateY(5px) scale(.95)}
}
.reveal{opacity:0;transform:translateY(30px);transition:all .8s cubic-bezier(0.4, 0, 0.2, 1)}
.reveal.active{opacity:1;transform:translateY(0)}
.hidden-item{display:none!important}

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

@media(max-width:900px){
  .type-grid{grid-template-columns:repeat(2,1fr)}
  .ft-grid{grid-template-columns:1fr 1fr;gap:32px}
}
@media(max-width:768px){
  .nav-links,.btn-nav{display:none}
  .hamburger{display:flex}
  .hero-title{font-size:2.5rem}
  .dh-title{font-size:1.2rem}
  .dept-header{padding:20px}
  .dept-content{padding:20px}
}
@media(max-width:500px){
  .type-grid{grid-template-columns:1fr}
  .exam-grid{grid-template-columns:1fr}
  .ft-grid{grid-template-columns:1fr}
  .cloud-container{padding:30px 20px}
}
</style>
</head>
