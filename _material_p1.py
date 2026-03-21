<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1.0"/>
<meta name="description" content="View and download Complete Organic Chemistry Notes - Unit 1 to 4 on NoteNest."/>
<title>Complete Organic Chemistry Notes — NoteNest</title>
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
body{background:var(--clr-bg);color:var(--clr-white);font-family:var(--ff-body);overflow-x:hidden;line-height:1.6}
::-webkit-scrollbar{width:6px}::-webkit-scrollbar-track{background:#111}::-webkit-scrollbar-thumb{background:var(--clr-green);border-radius:3px}

/* BACK TO TOP */
#backTop{position:fixed;bottom:32px;right:32px;width:44px;height:44px;background:var(--clr-green);border:none;border-radius:50%;cursor:pointer;display:flex;align-items:center;justify-content:center;opacity:0;visibility:hidden;transition:var(--transition);z-index:500;box-shadow:var(--shadow-glow)}
#backTop.show{opacity:1;visibility:visible}
#backTop:hover{background:var(--clr-green-light);transform:translateY(-3px)}
#backTop svg{stroke:white;fill:none;stroke-width:2.5;stroke-linecap:round;stroke-linejoin:round;width:18px;height:18px}

/* UTILITY */
.container{max-width:1200px;margin:0 auto;padding:0 24px}
.btn-amber{background:var(--clr-amber);color:#0d0d0d;font-weight:600;border:none;padding:10px 22px;border-radius:8px;cursor:pointer;font-family:var(--ff-body);font-size:.9rem;transition:var(--transition);text-decoration:none;display:inline-flex;align-items:center;gap:6px;justify-content:center}
.btn-amber:hover{background:var(--clr-amber-dark);transform:translateY(-2px);box-shadow:0 8px 24px rgba(245,166,35,.3)}
.btn-green{background:var(--clr-green);color:white;font-weight:600;border:none;padding:12px 28px;border-radius:8px;cursor:pointer;font-family:var(--ff-body);font-size:1rem;transition:var(--transition);text-decoration:none;display:inline-flex;align-items:center;gap:8px;justify-content:center}
.btn-green:hover{background:var(--clr-green-light);transform:translateY(-2px);box-shadow:var(--shadow-glow)}
.btn-outline{background:transparent;color:var(--clr-white);border:1px solid var(--clr-border);padding:8px 16px;border-radius:6px;cursor:pointer;font-family:var(--ff-body);font-size:.85rem;font-weight:500;transition:var(--transition);text-decoration:none;display:inline-flex;align-items:center;gap:6px;justify-content:center}
.btn-outline:hover{border-color:var(--clr-green-light);color:var(--clr-green-light)}

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

/* BREADCRUMB */
.breadcrumb-wrap{padding:100px 0 24px;border-bottom:1px solid var(--clr-border);background:linear-gradient(to bottom,rgba(26,107,74,.05),transparent)}
.breadcrumb{display:flex;align-items:center;gap:8px;font-size:.85rem;color:var(--clr-gray2);font-family:var(--ff-mono);flex-wrap:wrap}
.breadcrumb a{color:var(--clr-gray);text-decoration:none;transition:var(--transition);display:inline-flex;align-items:center;gap:6px}
.breadcrumb a:hover{color:var(--clr-amber)}
.breadcrumb span.sep{color:var(--clr-gray2)}
.breadcrumb span.current{color:var(--clr-white);white-space:nowrap;overflow:hidden;text-overflow:ellipsis;max-width:300px}
.back-btn{display:inline-flex;align-items:center;gap:6px;color:var(--clr-gray);text-decoration:none;font-size:.85rem;font-weight:500;transition:var(--transition);margin-right:12px;padding-right:12px;border-right:1px solid var(--clr-border)}
.back-btn:hover{color:var(--clr-white);transform:translateX(-3px)}

/* MAIN LAYOUT */
.mat-layout{display:grid;grid-template-columns:1fr 340px;gap:40px;padding:40px 0 80px;align-items:start}

/* LEFT COLUMN — HEADER */
.mat-header{margin-bottom:32px;animation:fadeUp .6s ease both}
.mat-title{font-family:var(--ff-display);font-size:clamp(2rem,4vw,3rem);font-weight:700;line-height:1.2;margin-bottom:16px;color:var(--clr-white)}
.mat-meta-row{display:flex;align-items:center;gap:12px;flex-wrap:wrap;margin-bottom:16px}
.type-badge{display:inline-flex;align-items:center;gap:6px;background:rgba(26,107,74,.15);border:1px solid rgba(26,107,74,.4);padding:4px 12px;border-radius:100px;font-family:var(--ff-mono);font-size:.75rem;color:var(--clr-green-light);letter-spacing:1px}
.meta-pill{font-size:.85rem;color:var(--clr-gray);background:var(--clr-surface);padding:4px 12px;border-radius:6px;border:1px solid var(--clr-border)}
.mat-stats-row{display:flex;align-items:center;gap:20px;font-size:.85rem;color:var(--clr-gray2);margin-bottom:24px;padding-bottom:24px;border-bottom:1px solid var(--clr-border)}
.stat-item{display:flex;align-items:center;gap:6px}
.stat-item span{color:var(--clr-amber)}
.uploader-row{display:flex;align-items:center;gap:12px}
.avatar{width:40px;height:40px;border-radius:50%;background:linear-gradient(135deg,var(--clr-teal),var(--clr-green));display:flex;align-items:center;justify-content:center;font-weight:600;color:white;font-size:1.1rem;flex-shrink:0}
.uploader-info{flex:1}
.uploader-name{font-weight:600;font-size:.95rem;color:var(--clr-white);margin-bottom:2px}
.upload-date{font-size:.75rem;color:var(--clr-gray2);font-family:var(--ff-mono)}

/* DESCRIPTION CARD */
.desc-card{background:var(--clr-surface);border:1px solid var(--clr-border);border-radius:var(--radius-lg);padding:24px;margin-bottom:32px;animation:fadeUp .6s ease both;animation-delay:.1s}
.desc-content{font-size:.95rem;color:var(--clr-white);line-height:1.7;position:relative}
.desc-text{overflow:hidden;max-height:150px;transition:max-height .4s ease}
.desc-text.expanded{max-height:2000px}
.desc-fade{position:absolute;bottom:0;left:0;right:0;height:60px;background:linear-gradient(transparent,var(--clr-surface));pointer-events:none;transition:opacity .3s ease}
.desc-text.expanded + .desc-fade{opacity:0}
.show-more-btn{background:none;border:none;color:var(--clr-amber);font-family:var(--ff-body);font-size:.85rem;font-weight:600;cursor:pointer;margin-top:12px;display:flex;align-items:center;gap:4px;padding:0}
.show-more-btn:hover{text-decoration:underline}

/* PDF PREVIEW */
.preview-card{background:var(--clr-surface);border:1px solid var(--clr-border);border-radius:var(--radius-lg);overflow:hidden;margin-bottom:32px;animation:fadeUp .6s ease both;animation-delay:.2s}
.preview-header{padding:16px 20px;background:var(--clr-surface2);border-bottom:1px solid var(--clr-border);display:flex;align-items:center;justify-content:space-between}
.preview-title{font-size:.9rem;font-weight:600;display:flex;align-items:center;gap:8px}
.preview-title span{font-family:var(--ff-mono);color:var(--clr-gray);font-size:.75rem;font-weight:400}
.preview-controls{display:flex;align-items:center;gap:12px}
.prev-btn,.next-btn,.zoom-btn{background:var(--clr-bg);border:1px solid var(--clr-border);color:var(--clr-white);width:28px;height:28px;border-radius:6px;display:flex;align-items:center;justify-content:center;cursor:pointer;transition:var(--transition);font-size:.9rem}
.prev-btn:hover:not(:disabled),.next-btn:hover:not(:disabled),.zoom-btn:hover{background:var(--clr-border);color:var(--clr-amber)}
.prev-btn:disabled,.next-btn:disabled{opacity:.4;cursor:not-allowed}
.page-counter{font-family:var(--ff-mono);font-size:.8rem;color:var(--clr-gray)}
.preview-body{height:600px;background:#111;position:relative;overflow:hidden;display:flex;align-items:center;justify-content:center}
.pdf-page-wrapper{width:80%;max-width:560px;background:white;aspect-ratio:1/1.414;box-shadow:0 8px 32px rgba(0,0,0,.5);border-radius:4px;transition:transform .3s cubic-bezier(0.2, 0.8, 0.2, 1);position:relative;overflow:hidden;padding:40px}
.pdf-skeleton{width:100%;height:100%;display:flex;flex-direction:column;gap:16px}
.sk-title{width:60%;height:24px;background:#e0e0e0;border-radius:4px}
.sk-line{width:100%;height:12px;background:#f0f0f0;border-radius:4px}
.sk-line.short{width:85%}
.sk-line.half{width:50%}
.sk-box{width:100%;height:180px;background:#f5f5f5;border-radius:4px;margin:12px 0}
.watermark{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font-family:var(--ff-display);font-size:4rem;color:rgba(0,0,0,.04);transform:rotate(-45deg);pointer-events:none;user-select:none;font-weight:900}
.preview-overlay{position:absolute;bottom:0;left:0;right:0;height:40%;background:linear-gradient(transparent,rgba(13,13,13,.95) 80%);display:flex;flex-direction:column;align-items:center;justify-content:flex-end;padding:32px;text-align:center;backdrop-filter:blur(2px)}
.preview-overlay p{font-size:.95rem;color:var(--clr-white);font-weight:500;margin-bottom:16px}

/* COMMENTS */
.comments-section{background:var(--clr-surface);border:1px solid var(--clr-border);border-radius:var(--radius-lg);padding:32px;animation:fadeUp .6s ease both;animation-delay:.3s}
.comments-header{display:flex;align-items:center;justify-content:space-between;margin-bottom:24px}
.comments-header h3{font-family:var(--ff-display);font-size:1.4rem;font-weight:700}
.comments-header span{font-family:var(--ff-mono);font-size:.85rem;color:var(--clr-gray)}
.add-comment{display:flex;gap:16px;margin-bottom:40px;padding-bottom:32px;border-bottom:1px solid var(--clr-border)}
.add-comment .avatar{width:44px;height:44px;background:linear-gradient(135deg,var(--clr-amber),var(--clr-amber-dark))}
.comment-input-box{flex:1}
.rating-input{display:flex;gap:4px;margin-bottom:12px;font-size:1.4rem;color:var(--clr-border);cursor:pointer}
.rating-input span{transition:color .2s ease}
.rating-input span:hover,.rating-input span.active{color:var(--clr-amber)}
.rating-input span.hover{color:var(--clr-amber-dark)}
.comment-textarea{width:100%;background:var(--clr-surface2);border:1px solid var(--clr-border);border-radius:8px;padding:12px 16px;color:var(--clr-white);font-family:var(--ff-body);font-size:.95rem;resize:vertical;min-height:90px;outline:none;transition:var(--transition);margin-bottom:12px}
.comment-textarea:focus{border-color:var(--clr-green-light)}
.comment-list{display:flex;flex-direction:column;gap:24px}
.comment-item{display:flex;gap:16px}
.comment-item .avatar{width:40px;height:40px;font-size:1rem;background:var(--clr-surface2);border:1px solid var(--clr-border);color:var(--clr-gray)}
.comment-body{flex:1}
.comment-meta{display:flex;align-items:center;gap:10px;margin-bottom:4px}
.comment-author{font-weight:600;font-size:.9rem}
.comment-date{font-size:.75rem;color:var(--clr-gray);font-family:var(--ff-mono)}
.comment-stars{color:var(--clr-amber);font-size:.85rem;letter-spacing:1px}
.comment-text{font-size:.9rem;color:var(--clr-white);line-height:1.6;margin-bottom:12px}
.comment-actions{display:flex;align-items:center;gap:16px}
.like-btn{background:none;border:none;color:var(--clr-gray2);font-size:.8rem;cursor:pointer;display:flex;align-items:center;gap:6px;transition:var(--transition);font-family:var(--ff-body);padding:0}
.like-btn:hover{color:var(--clr-white)}
.like-btn.liked{color:var(--clr-coral)}
.like-btn svg{width:14px;height:14px;fill:currentColor}

/* RIGHT COLUMN — SIDEBAR */
.sidebar{position:sticky;top:90px;display:flex;flex-direction:column;gap:24px}

/* DOWNLOAD CARD */
.dl-card{background:linear-gradient(to bottom,var(--clr-surface),rgba(26,107,74,.05));border:1px solid var(--clr-border);border-radius:var(--radius-lg);padding:28px 24px;text-align:center;position:relative;overflow:hidden;animation:fadeUp .6s ease both}
.dl-card::before{content:'';position:absolute;top:0;left:0;right:0;height:3px;background:linear-gradient(90deg,var(--clr-amber),var(--clr-green-light))}
.dl-file-icon{font-size:3rem;margin-bottom:12px;filter:drop-shadow(0 4px 12px rgba(0,0,0,.2))}
.dl-filename{font-weight:600;font-size:1.05rem;margin-bottom:4px;word-break:break-all;line-height:1.3}
.dl-filesize{font-family:var(--ff-mono);font-size:.8rem;color:var(--clr-gray);margin-bottom:24px}
.btn-dl{width:100%;padding:16px;font-size:1.1rem;background:var(--clr-amber);color:#0d0d0d;font-weight:700;border:none;border-radius:10px;cursor:pointer;font-family:var(--ff-body);transition:var(--transition);display:flex;align-items:center;justify-content:center;gap:10px;box-shadow:0 8px 24px rgba(245,166,35,.2)}
.btn-dl:hover{background:var(--clr-amber-dark);transform:translateY(-2px);box-shadow:0 12px 32px rgba(245,166,35,.3)}
.btn-dl:active{transform:translateY(0)}
.dl-stats{font-size:.8rem;color:var(--clr-gray);margin-top:16px;display:flex;align-items:center;justify-content:center;gap:6px}
.dl-stats span{color:var(--clr-white);font-weight:600}
.btn-bookmark{width:100%;padding:12px;margin-top:12px;background:transparent;border:1px solid var(--clr-border);color:var(--clr-white);font-weight:600;border-radius:8px;cursor:pointer;font-family:var(--ff-body);transition:var(--transition);display:flex;align-items:center;justify-content:center;gap:8px}
.btn-bookmark:hover{border-color:var(--clr-green-light);color:var(--clr-green-light);background:rgba(26,107,74,.05)}
.btn-bookmark.active{border-color:var(--clr-green-light);color:var(--clr-green-light);background:rgba(26,107,74,.05)}
.btn-bookmark.active svg{fill:currentColor}
.report-link{display:inline-block;margin-top:20px;font-size:.75rem;color:var(--clr-gray2);text-decoration:underline;cursor:pointer;transition:var(--transition)}
.report-link:hover{color:var(--clr-coral)}

/* INFO CARD */
.info-card{background:var(--clr-surface);border:1px solid var(--clr-border);border-radius:var(--radius-lg);padding:24px;animation:fadeUp .6s ease both;animation-delay:.1s}
.info-card h3{font-family:var(--ff-display);font-size:1.2rem;font-weight:700;margin-bottom:20px;padding-bottom:12px;border-bottom:1px solid var(--clr-border)}
.info-list{display:flex;flex-direction:column;gap:14px}
.info-item{display:flex;justify-content:space-between;align-items:center;font-size:.9rem}
.info-label{color:var(--clr-gray);font-weight:500}
.info-val{color:var(--clr-white);font-weight:600;text-align:right}

/* TAGS CARD */
.tags-card{background:var(--clr-surface);border:1px solid var(--clr-border);border-radius:var(--radius-lg);padding:24px;animation:fadeUp .6s ease both;animation-delay:.2s}
.tags-card h3{font-family:var(--ff-display);font-size:1.1rem;font-weight:700;margin-bottom:16px}
.tag-pills{display:flex;flex-wrap:wrap;gap:8px}
.tag-pill{background:rgba(26,107,74,.1);border:1px solid var(--clr-border);color:var(--clr-gray);padding:4px 12px;border-radius:100px;font-size:.8rem;font-family:var(--ff-mono);text-decoration:none;transition:var(--transition)}
.tag-pill:hover{border-color:var(--clr-green-light);color:var(--clr-green-light);background:rgba(26,107,74,.2)}

/* SHARE CARD */
.share-card{background:var(--clr-surface);border:1px solid var(--clr-border);border-radius:var(--radius-lg);padding:24px;animation:fadeUp .6s ease both;animation-delay:.3s}
.share-card h3{font-family:var(--ff-display);font-size:1.1rem;font-weight:700;margin-bottom:16px}
.share-actions{display:flex;gap:12px}
.btn-copy{flex:1;background:var(--clr-surface2);border:1px solid var(--clr-border);color:var(--clr-white);padding:10px;border-radius:8px;cursor:pointer;font-family:var(--ff-body);font-size:.85rem;font-weight:500;transition:var(--transition);display:flex;align-items:center;justify-content:center;gap:8px}
.btn-copy:hover{border-color:var(--clr-amber);color:var(--clr-amber)}
.btn-social{width:40px;height:40px;background:var(--clr-surface2);border:1px solid var(--clr-border);border-radius:8px;display:flex;align-items:center;justify-content:center;color:var(--clr-white);cursor:pointer;transition:var(--transition);font-size:1.1rem}
.btn-social.wa:hover{background:#25D366;border-color:#25D366;color:white}
.btn-social.tg:hover{background:#0088cc;border-color:#0088cc;color:white}

/* RELATED MATERIALS */
.related-section{margin-top:40px;padding-top:40px;border-top:1px solid var(--clr-border);animation:fadeUp .6s ease both;animation-delay:.4s}
.related-section h3{font-family:var(--ff-display);font-size:1.4rem;font-weight:700;margin-bottom:20px}
.related-list{display:flex;flex-direction:column;gap:16px}
.rel-card{display:flex;flex-direction:column;gap:12px;padding:16px;background:var(--clr-surface2);border:1px solid var(--clr-border);border-radius:12px;transition:var(--transition);text-decoration:none;color:inherit}
.rel-card:hover{border-color:var(--clr-green-light);transform:translateY(-2px);background:var(--clr-surface)}
.rel-type{font-family:var(--ff-mono);font-size:.7rem;color:var(--clr-amber);letter-spacing:1px}
.rel-title{font-weight:600;font-size:.95rem;line-height:1.4;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.rel-meta{display:flex;align-items:center;justify-content:space-between;font-size:.8rem;color:var(--clr-gray)}
.rel-meta span{display:flex;align-items:center;gap:4px}

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

/* TOAST */
#nn-toast{position:fixed;bottom:28px;left:50%;transform:translateX(-50%) translateY(20px);background:var(--clr-green);border:1px solid var(--clr-green-light);color:white;padding:12px 24px;border-radius:10px;font-size:.9rem;font-family:var(--ff-body);z-index:4000;opacity:0;transition:all .3s ease;white-space:nowrap;box-shadow:0 8px 24px rgba(0,0,0,.5);font-weight:500;display:flex;align-items:center;gap:8px}

@keyframes fadeUp{from{opacity:0;transform:translateY(24px)}to{opacity:1;transform:none}}

/* RESPONSIVE */
@media(max-width:1024px){
  .mat-layout{grid-template-columns:1fr;gap:40px}
  .sidebar{position:static}
  .related-section{display:grid;grid-template-columns:1fr 1fr;gap:16px;align-items:start}
  .related-section h3{grid-column:1/-1}
}
@media(max-width:768px){
  .related-section{grid-template-columns:1fr}
  .footer-grid{grid-template-columns:1fr 1fr}
  .mat-title{font-size:2rem}
  .pdf-page-wrapper{width:95%;padding:20px}
}
@media(max-width:600px){
  .nav-links,.nav-cta{display:none}
  .hamburger{display:flex}
  .footer-grid{grid-template-columns:1fr}
  .mat-stats-row{flex-direction:column;align-items:flex-start;gap:12px}
  .add-comment{flex-direction:column}
}
</style>
</head>
