p1 = r'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1.0"/>
<meta name="description" content="Upload your study materials to NoteNest and help thousands of students."/>
<title>Upload Material — NoteNest</title>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700;900&family=DM+Sans:wght@300;400;500;600&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet"/>
<style>
:root{
  --clr-bg:#0d0d0d;--clr-surface:#1a1a1a;--clr-surface2:#1e1e1e;--clr-border:#2a2a2a;
  --clr-green:#1a6b4a;--clr-green-light:#22a06b;--clr-green-glow:rgba(26,107,74,.35);
  --clr-amber:#f5a623;--clr-amber-dark:#c4821a;--clr-coral:#ff6b6b;
  --clr-white:#ffffff;--clr-gray:#a0a0a0;--clr-gray2:#6a6a6a;
  --ff-display:'Playfair Display',serif;--ff-body:'DM Sans',sans-serif;--ff-mono:'JetBrains Mono',monospace;
  --radius:12px;--radius-lg:20px;--shadow-glow:0 0 24px var(--clr-green-glow);--transition:.3s ease;
}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{background:var(--clr-bg);color:var(--clr-white);font-family:var(--ff-body);overflow-x:hidden;line-height:1.6}
::-webkit-scrollbar{width:6px}::-webkit-scrollbar-track{background:#111}::-webkit-scrollbar-thumb{background:var(--clr-green);border-radius:3px}

/* BACK TO TOP */
#backTop{position:fixed;bottom:32px;right:32px;width:44px;height:44px;background:var(--clr-green);border:none;border-radius:50%;cursor:pointer;display:flex;align-items:center;justify-content:center;opacity:0;visibility:hidden;transition:var(--transition);z-index:500;box-shadow:var(--shadow-glow)}
#backTop.show{opacity:1;visibility:visible}
#backTop:hover{background:var(--clr-green-light);transform:translateY(-3px)}
#backTop svg{stroke:white;fill:none;stroke-width:2.5;stroke-linecap:round;stroke-linejoin:round;width:18px;height:18px}

/* UTILITY */
.container{max-width:1200px;margin:0 auto;padding:0 24px}
.btn-amber{background:var(--clr-amber);color:#0d0d0d;font-weight:600;border:none;padding:10px 22px;border-radius:8px;cursor:pointer;font-family:var(--ff-body);font-size:.9rem;transition:var(--transition);text-decoration:none;display:inline-flex;align-items:center;gap:6px}
.btn-amber:hover{background:var(--clr-amber-dark);transform:translateY(-2px);box-shadow:0 8px 24px rgba(245,166,35,.3)}
.btn-green{background:var(--clr-green);color:white;font-weight:600;border:none;padding:12px 28px;border-radius:8px;cursor:pointer;font-family:var(--ff-body);font-size:1rem;transition:var(--transition);text-decoration:none;display:inline-flex;align-items:center;gap:8px}
.btn-green:hover{background:var(--clr-green-light);transform:translateY(-2px);box-shadow:var(--shadow-glow)}

/* NAVBAR */
nav{position:fixed;top:0;left:0;right:0;z-index:1000;padding:20px 0;transition:var(--transition)}
nav.scrolled{background:rgba(13,13,13,.88);backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);border-bottom:1px solid var(--clr-border);padding:14px 0}
.nav-inner{display:flex;align-items:center;justify-content:space-between}
.nav-logo{display:flex;align-items:center;gap:10px;text-decoration:none}
.nav-logo-icon{width:36px;height:36px;background:linear-gradient(135deg,var(--clr-green),var(--clr-green-light));border-radius:10px;display:flex;align-items:center;justify-content:center}
.nav-logo-icon svg{fill:white;width:20px;height:20px}
.nav-logo-text{font-family:var(--ff-display);font-size:1.4rem;font-weight:700;color:var(--clr-white)}
.nav-logo-text span{color:var(--clr-amber)}
.nav-links{display:flex;align-items:center;gap:32px;list-style:none}
.nav-links a{text-decoration:none;color:var(--clr-gray);font-size:.9rem;font-weight:500;transition:var(--transition);position:relative}
.nav-links a::after{content:'';position:absolute;bottom:-4px;left:0;width:0;height:2px;background:var(--clr-amber);transition:var(--transition)}
.nav-links a:hover{color:var(--clr-white)}.nav-links a:hover::after{width:100%}
.nav-links a.active{color:var(--clr-white)}.nav-links a.active::after{width:100%}
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

/* PAGE HEADER */
.page-header{padding:120px 0 48px;position:relative;overflow:hidden;text-align:center}
.page-header-glow{position:absolute;width:500px;height:300px;background:radial-gradient(circle,var(--clr-green-glow) 0%,transparent 70%);top:50%;left:50%;transform:translate(-50%,-50%);pointer-events:none}
.breadcrumb{display:flex;align-items:center;gap:8px;font-size:.85rem;color:var(--clr-gray2);justify-content:center;margin-bottom:20px;font-family:var(--ff-mono)}
.breadcrumb a{color:var(--clr-gray);text-decoration:none;transition:var(--transition)}
.breadcrumb a:hover{color:var(--clr-amber)}
.breadcrumb span{color:var(--clr-gray2)}
.page-header h1{font-family:var(--ff-display);font-size:clamp(2rem,4vw,2.8rem);font-weight:700;margin-bottom:12px}
.page-header h1 em{font-style:normal;color:var(--clr-amber)}
.page-header p{color:var(--clr-gray);font-size:1.05rem;max-width:480px;margin:0 auto}

/* DRAFT BANNER */
.draft-banner{background:rgba(26,107,74,.12);border:1px solid rgba(26,107,74,.35);border-radius:10px;padding:14px 20px;display:flex;align-items:center;gap:12px;margin-bottom:24px;font-size:.9rem;color:var(--clr-green-light)}
.draft-banner button{margin-left:auto;background:var(--clr-green);color:white;border:none;padding:6px 14px;border-radius:6px;cursor:pointer;font-size:.82rem;font-family:var(--ff-body);transition:var(--transition)}
.draft-banner button:hover{background:var(--clr-green-light)}

/* MAIN LAYOUT */
.upload-layout{display:grid;grid-template-columns:1fr 320px;gap:32px;padding-bottom:80px;align-items:start}

/* FORM CARD */
.form-card{background:var(--clr-surface);border:1px solid var(--clr-border);border-radius:var(--radius-lg);overflow:hidden}
.form-section{padding:32px;border-bottom:1px solid var(--clr-border)}
.form-section:last-child{border-bottom:none}
.form-section-header{display:flex;align-items:center;gap:14px;margin-bottom:24px}
.step-badge{width:36px;height:36px;border-radius:50%;background:linear-gradient(135deg,var(--clr-green),var(--clr-green-light));display:flex;align-items:center;justify-content:center;font-family:var(--ff-mono);font-size:.85rem;font-weight:600;color:white;flex-shrink:0}
.form-section-header h2{font-family:var(--ff-display);font-size:1.3rem;font-weight:700}
.form-section-header p{font-size:.85rem;color:var(--clr-gray);margin-top:2px}

/* DROP ZONE */
.drop-zone{border:2px dashed var(--clr-border);border-radius:var(--radius);padding:48px 24px;text-align:center;cursor:pointer;transition:var(--transition);position:relative;background:rgba(255,255,255,.01)}
.drop-zone:hover,.drop-zone.drag-over{border-color:var(--clr-green-light);background:rgba(26,107,74,.06);box-shadow:0 0 0 4px rgba(26,107,74,.12)}
.drop-zone-icon{font-size:3rem;margin-bottom:16px;display:block}
.drop-zone h3{font-family:var(--ff-display);font-size:1.2rem;margin-bottom:8px}
.drop-zone p{color:var(--clr-gray);font-size:.9rem;margin-bottom:20px}
.drop-zone input[type=file]{position:absolute;inset:0;opacity:0;cursor:pointer}
.formats{display:flex;flex-wrap:wrap;gap:6px;justify-content:center;margin-top:16px}
.format-pill{background:rgba(255,255,255,.05);border:1px solid var(--clr-border);border-radius:100px;padding:3px 10px;font-size:.75rem;font-family:var(--ff-mono);color:var(--clr-gray)}

/* FILE PREVIEW */
.file-list{display:flex;flex-direction:column;gap:10px;margin-top:16px}
.file-item{display:flex;align-items:center;gap:14px;background:var(--clr-surface2);border:1px solid var(--clr-border);border-radius:10px;padding:14px 16px;position:relative;overflow:hidden}
.file-type-icon{width:40px;height:40px;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:1.2rem;flex-shrink:0}
.file-type-icon.pdf{background:rgba(255,107,107,.12);color:#ff6b6b}
.file-type-icon.doc{background:rgba(26,107,74,.15);color:var(--clr-green-light)}
.file-type-icon.ppt{background:rgba(245,166,35,.12);color:var(--clr-amber)}
.file-type-icon.img{background:rgba(0,180,166,.12);color:#00b4a6}
.file-type-icon.other{background:rgba(160,160,160,.1);color:var(--clr-gray)}
.file-info{flex:1;min-width:0}
.file-name{font-size:.9rem;font-weight:500;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.file-size{font-size:.78rem;color:var(--clr-gray);margin-top:2px;font-family:var(--ff-mono)}
.file-progress{position:absolute;bottom:0;left:0;height:2px;background:var(--clr-green-light);transition:width .4s ease;border-radius:0 2px 2px 0}
.file-remove{background:none;border:none;color:var(--clr-gray2);cursor:pointer;font-size:1.1rem;padding:4px;transition:var(--transition);flex-shrink:0}
.file-remove:hover{color:var(--clr-coral)}
.file-status{font-size:.75rem;font-family:var(--ff-mono);padding:2px 8px;border-radius:100px;margin-left:auto}
.file-status.uploading{background:rgba(245,166,35,.15);color:var(--clr-amber)}
.file-status.done{background:rgba(26,107,74,.15);color:var(--clr-green-light)}

/* FORM FIELDS */
.field-group{display:flex;flex-direction:column;gap:6px;margin-bottom:20px}
.field-group label{font-size:.85rem;font-weight:500;color:var(--clr-gray)}
.field-group label .req{color:var(--clr-coral);margin-left:2px}
.field-group input,.field-group textarea,.field-group select{background:var(--clr-surface2);border:1px solid var(--clr-border);border-radius:8px;padding:12px 14px;color:var(--clr-white);font-family:var(--ff-body);font-size:.95rem;width:100%;outline:none;transition:var(--transition)}
.field-group input:focus,.field-group textarea:focus,.field-group select:focus{border-color:var(--clr-green-light);box-shadow:0 0 0 3px rgba(34,160,107,.12)}
.field-group input.valid{border-color:var(--clr-green-light)}
.field-group input.invalid,.field-group textarea.invalid,.field-group select.invalid{border-color:var(--clr-coral)}
.field-group textarea{resize:vertical;min-height:120px}
.field-group select{cursor:pointer;appearance:none;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 24 24' fill='none' stroke='%23a0a0a0' stroke-width='2'%3E%3Cpath d='M6 9l6 6 6-6'/%3E%3C/svg%3E");background-repeat:no-repeat;background-position:right 12px center;padding-right:40px}
.field-group select option{background:#1a1a1a}
.field-row{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.char-counter{font-size:.75rem;color:var(--clr-gray2);text-align:right;font-family:var(--ff-mono);margin-top:2px}
.char-counter.warn{color:var(--clr-amber)}
.char-counter.over{color:var(--clr-coral)}
.field-error{font-size:.78rem;color:var(--clr-coral);display:none}
.field-error.show{display:block}
.field-valid-icon{position:absolute;right:12px;top:50%;transform:translateY(-50%);color:var(--clr-green-light);font-size:.9rem;pointer-events:none}
.field-wrapper{position:relative}

/* CUSTOM SUBJECT SELECT */
.custom-select{position:relative}
.custom-select-trigger{background:var(--clr-surface2);border:1px solid var(--clr-border);border-radius:8px;padding:12px 40px 12px 14px;cursor:pointer;transition:var(--transition);display:flex;align-items:center;justify-content:space-between;font-size:.95rem;color:var(--clr-white)}
.custom-select-trigger:focus{border-color:var(--clr-green-light)}
.custom-select-trigger.open{border-color:var(--clr-green-light);border-bottom-left-radius:0;border-bottom-right-radius:0}
.custom-select-trigger .arrow{color:var(--clr-gray);transition:var(--transition)}
.custom-select-trigger.open .arrow{transform:rotate(180deg)}
.custom-select-dropdown{display:none;position:absolute;top:100%;left:0;right:0;background:var(--clr-surface2);border:1px solid var(--clr-green-light);border-top:none;border-radius:0 0 8px 8px;z-index:50;max-height:240px;overflow-y:auto}
.custom-select-dropdown.open{display:block}
.custom-select-search{padding:10px 12px;border-bottom:1px solid var(--clr-border)}
.custom-select-search input{background:var(--clr-surface);border:1px solid var(--clr-border);border-radius:6px;padding:8px 12px;color:var(--clr-white);font-family:var(--ff-body);font-size:.85rem;width:100%;outline:none}
.custom-select-search input:focus{border-color:var(--clr-green-light)}
.custom-select-option{padding:10px 14px;cursor:pointer;font-size:.9rem;transition:var(--transition)}
.custom-select-option:hover,.custom-select-option.selected{background:rgba(26,107,74,.15);color:var(--clr-green-light)}

/* TAGS INPUT */
.tags-input-wrapper{background:var(--clr-surface2);border:1px solid var(--clr-border);border-radius:8px;padding:10px 12px;display:flex;flex-wrap:wrap;gap:8px;cursor:text;transition:var(--transition);position:relative;min-height:48px;align-items:center}
.tags-input-wrapper:focus-within{border-color:var(--clr-green-light);box-shadow:0 0 0 3px rgba(34,160,107,.12)}
.tag-pill{display:inline-flex;align-items:center;gap:5px;background:rgba(26,107,74,.2);border:1px solid rgba(34,160,107,.3);color:var(--clr-green-light);padding:3px 10px;border-radius:100px;font-size:.8rem;font-family:var(--ff-mono)}
.tag-pill button{background:none;border:none;cursor:pointer;color:var(--clr-green-light);font-size:.85rem;line-height:1;padding:0;opacity:.7}
.tag-pill button:hover{opacity:1;color:var(--clr-coral)}
.tags-input{border:none;outline:none;background:transparent;color:var(--clr-white);font-family:var(--ff-body);font-size:.9rem;min-width:80px;flex:1}
.tag-suggestions{position:absolute;top:calc(100% + 4px);left:0;right:0;background:var(--clr-surface2);border:1px solid var(--clr-border);border-radius:8px;z-index:40;max-height:160px;overflow-y:auto;display:none;box-shadow:0 8px 24px rgba(0,0,0,.5)}
.tag-suggestions.open{display:block}
.tag-suggestion-item{padding:10px 14px;cursor:pointer;font-size:.9rem;transition:var(--transition)}
.tag-suggestion-item:hover{background:rgba(26,107,74,.15);color:var(--clr-green-light)}

/* TOGGLE SWITCH */
.toggle-row{display:flex;align-items:center;justify-content:space-between;padding:14px 0;border-bottom:1px solid var(--clr-border)}
.toggle-row:last-of-type{border-bottom:none}
.toggle-info h4{font-size:.95rem;font-weight:500;margin-bottom:2px}
.toggle-info p{font-size:.82rem;color:var(--clr-gray)}
.toggle-switch{position:relative;width:48px;height:26px;flex-shrink:0}
.toggle-switch input{opacity:0;width:0;height:0;position:absolute}
.toggle-slider{position:absolute;inset:0;background:var(--clr-border);border-radius:100px;cursor:pointer;transition:var(--transition)}
.toggle-slider::before{content:'';position:absolute;width:20px;height:20px;left:3px;top:3px;background:var(--clr-gray);border-radius:50%;transition:var(--transition)}
.toggle-switch input:checked ~ .toggle-slider{background:var(--clr-green)}
.toggle-switch input:checked ~ .toggle-slider::before{transform:translateX(22px);background:white}

/* LICENSE CARDS */
.license-options{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:4px}
.license-card{border:2px solid var(--clr-border);border-radius:10px;padding:16px;cursor:pointer;transition:var(--transition);position:relative}
.license-card input[type=radio]{position:absolute;opacity:0;width:0;height:0}
.license-card.selected,.license-card:has(input:checked){border-color:var(--clr-green-light);background:rgba(26,107,74,.08)}
.license-card h4{font-size:.9rem;font-weight:600;margin-bottom:4px}
.license-card p{font-size:.78rem;color:var(--clr-gray)}
.license-card .check{width:18px;height:18px;border-radius:50%;border:2px solid var(--clr-border);position:absolute;top:14px;right:14px;transition:var(--transition);background:transparent}
.license-card.selected .check,.license-card:has(input:checked) .check{border-color:var(--clr-green-light);background:var(--clr-green-light)}

/* VISIBILITY */
.visibility-options{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.visibility-card{border:2px solid var(--clr-border);border-radius:10px;padding:16px;cursor:pointer;transition:var(--transition);text-align:center}
.visibility-card input[type=radio]{position:absolute;opacity:0;width:0;height:0}
.visibility-card.selected,.visibility-card:has(input:checked){border-color:var(--clr-amber);background:rgba(245,166,35,.06)}
.visibility-card .vis-icon{font-size:1.8rem;margin-bottom:8px}
.visibility-card h4{font-size:.9rem;font-weight:600;margin-bottom:3px}
.visibility-card p{font-size:.78rem;color:var(--clr-gray)}

/* SUBMIT SECTION */
.submit-section{padding:32px;background:linear-gradient(to bottom,var(--clr-surface),rgba(26,107,74,.05))}
.submit-btn{width:100%;padding:18px;font-size:1.1rem;border-radius:12px;background:var(--clr-amber);color:#0d0d0d;font-weight:700;border:none;cursor:pointer;font-family:var(--ff-body);transition:var(--transition);display:flex;align-items:center;justify-content:center;gap:10px;letter-spacing:.3px}
.submit-btn:hover:not(:disabled){background:var(--clr-amber-dark);transform:translateY(-2px);box-shadow:0 12px 36px rgba(245,166,35,.35)}
.submit-btn:disabled{opacity:.45;cursor:not-allowed;transform:none}
.submit-hint{text-align:center;font-size:.8rem;color:var(--clr-gray2);margin-top:12px}
.save-draft-btn{width:100%;padding:12px;border-radius:10px;background:transparent;border:1px solid var(--clr-border);color:var(--clr-gray);font-family:var(--ff-body);font-size:.9rem;cursor:pointer;transition:var(--transition);margin-top:10px}
.save-draft-btn:hover{border-color:var(--clr-green-light);color:var(--clr-green-light)}

/* SIDEBAR */
.upload-sidebar{display:flex;flex-direction:column;gap:20px;position:sticky;top:90px}
.sidebar-card{background:var(--clr-surface);border:1px solid var(--clr-border);border-radius:var(--radius);padding:24px}
.sidebar-card h3{font-family:var(--ff-display);font-size:1rem;font-weight:700;margin-bottom:16px;display:flex;align-items:center;gap:8px}
.sidebar-card h3 span{font-size:1.1rem}
.guideline-item{display:flex;align-items:flex-start;gap:10px;padding:10px 0;border-bottom:1px solid var(--clr-border);font-size:.85rem}
.guideline-item:last-child{border-bottom:none;padding-bottom:0}
.guideline-item .gi-icon{width:20px;height:20px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:.7rem;flex-shrink:0;margin-top:1px}
.gi-ok{background:rgba(26,107,74,.2);color:var(--clr-green-light)}
.gi-no{background:rgba(255,107,107,.15);color:var(--clr-coral)}
.tip-item{display:flex;align-items:flex-start;gap:8px;font-size:.83rem;padding:6px 0;color:var(--clr-gray)}
.tip-item::before{content:'★';color:var(--clr-amber);flex-shrink:0;font-size:.7rem;margin-top:3px}
.recent-upload-item{display:flex;align-items:center;gap:10px;padding:10px 0;border-bottom:1px solid var(--clr-border);font-size:.83rem}
.recent-upload-item:last-child{border-bottom:none;padding-bottom:0}
.ru-thumb{width:32px;height:32px;border-radius:6px;display:flex;align-items:center;justify-content:center;font-size:.9rem;background:rgba(26,107,74,.15)}
.ru-info{flex:1;min-width:0}
.ru-name{white-space:nowrap;overflow:hidden;text-overflow:ellipsis;font-weight:500}
.ru-date{font-size:.72rem;color:var(--clr-gray2);font-family:var(--ff-mono)}
.stat-row{display:flex;justify-content:space-between;padding:8px 0;border-bottom:1px solid var(--clr-border);font-size:.85rem}
.stat-row:last-child{border-bottom:none}
.stat-row .stat-val{font-family:var(--ff-mono);color:var(--clr-amber);font-weight:600}

/* UPLOAD MODAL */
.modal-overlay{position:fixed;inset:0;background:rgba(0,0,0,.8);backdrop-filter:blur(8px);z-index:2000;display:flex;align-items:center;justify-content:center;opacity:0;visibility:hidden;transition:var(--transition)}
.modal-overlay.open{opacity:1;visibility:visible}
.modal-box{background:var(--clr-surface);border:1px solid var(--clr-border);border-radius:var(--radius-lg);padding:48px 40px;max-width:480px;width:90%;text-align:center;position:relative;transform:scale(.92);transition:var(--transition)}
.modal-overlay.open .modal-box{transform:scale(1)}
.modal-icon{font-size:3.5rem;margin-bottom:20px;display:block}
.modal-title{font-family:var(--ff-display);font-size:1.6rem;font-weight:700;margin-bottom:8px}
.modal-sub{color:var(--clr-gray);font-size:.95rem;margin-bottom:32px}
.upload-progress-bar{height:6px;background:var(--clr-border);border-radius:100px;overflow:hidden;margin:24px 0}
.upload-progress-fill{height:100%;background:linear-gradient(90deg,var(--clr-green),var(--clr-green-light));border-radius:100px;width:0;transition:width .5s ease}
.upload-status-text{font-family:var(--ff-mono);font-size:.85rem;color:var(--clr-green-light);margin-top:8px;min-height:20px}
.modal-actions{display:flex;gap:12px;justify-content:center;margin-top:24px;flex-wrap:wrap}
.modal-actions a,.modal-actions button{padding:12px 24px;border-radius:8px;font-family:var(--ff-body);font-size:.9rem;font-weight:600;cursor:pointer;text-decoration:none;transition:var(--transition)}

/* CONFETTI */
.confetti-container{position:fixed;inset:0;pointer-events:none;z-index:3000;overflow:hidden}
.confetti-piece{position:absolute;width:10px;height:10px;top:-20px;animation:confettiFall linear forwards;border-radius:2px}
@keyframes confettiFall{to{transform:translateY(110vh) rotate(720deg);opacity:0}}

/* FOOTER */
footer{background:var(--clr-surface);border-top:1px solid var(--clr-border);padding:60px 0 0}
.footer-grid{display:grid;grid-template-columns:1.5fr 1fr 1fr 1fr;gap:48px;margin-bottom:48px}
.footer-brand p{color:var(--clr-gray);font-size:.9rem;margin:12px 0 0;max-width:260px;line-height:1.7}
.footer-col h4{font-weight:600;margin-bottom:16px;font-size:.95rem}
.footer-col ul{list-style:none;display:flex;flex-direction:column;gap:10px}
.footer-col ul a{color:var(--clr-gray);text-decoration:none;font-size:.9rem;transition:var(--transition)}
.footer-col ul a:hover{color:var(--clr-amber)}
.footer-bottom{border-top:1px solid var(--clr-border);padding:24px 0;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:12px}
.footer-bottom p{color:var(--clr-gray2);font-size:.85rem}
.footer-bottom span{font-family:var(--ff-mono);font-size:.75rem;color:var(--clr-gray2)}

/* RESPONSIVE */
@media(max-width:900px){
  .upload-layout{grid-template-columns:1fr}
  .upload-sidebar{position:static}
  .field-row{grid-template-columns:1fr}
  .footer-grid{grid-template-columns:1fr 1fr}
}
@media(max-width:600px){
  .nav-links,.nav-cta{display:none}
  .hamburger{display:flex}
  .footer-grid{grid-template-columns:1fr}
  .page-header{padding:100px 0 36px}
  .modal-box{padding:32px 24px}
  .license-options,.visibility-options{grid-template-columns:1fr}
}
@keyframes cardIn{from{opacity:0;transform:translateY(16px)}to{opacity:1;transform:none}}
.form-card,.sidebar-card{animation:cardIn .5s ease both}
</style>
</head>
'''

with open(r'c:\Users\kharj\OneDrive\Desktop\fsd project\upload.html','w',encoding='utf-8') as f:
    f.write(p1)
print('Part 1 done, size:', len(p1))
