window.Toast = {
  container: null,
  
  _init() {
    if (!this.container) {
      this.container = document.createElement('div')
      this.container.id = 'toast-container'
      this.container.style.cssText = `
        position:fixed; bottom:24px; right:24px; 
        z-index:9999; display:flex; flex-direction:column; 
        gap:10px; pointer-events:none;`
      document.body.appendChild(this.container)
    }
  },
  
  show(message, type='success', duration=3000) {
    this._init()
    const colors = {
      success: '#22c77a',
      error: '#e05555',
      info: '#f5a623',
      warning: '#f5a623'
    }
    const icons = {
      success: '✓',
      error: '✕',
      info: 'ℹ',
      warning: '⚠'
    }
    const toast = document.createElement('div')
    toast.style.cssText = `
      background:#1c1c1c; color:#fff; padding:14px 18px;
      border-radius:10px; border-left:4px solid ${colors[type]||colors.success};
      font-family:'DM Sans',sans-serif; font-size:14px;
      display:flex; align-items:center; gap:10px;
      box-shadow:0 4px 20px rgba(0,0,0,0.5);
      pointer-events:all; cursor:pointer;
      animation: slideInToast 0.3s ease;
      max-width:320px;`
    toast.innerHTML = `
      <span style="color:${colors[type]};font-weight:bold">${icons[type]}</span>
      <span>${message}</span>`
    toast.onclick = () => toast.remove()
    this.container.appendChild(toast)
    setTimeout(() => {
      toast.style.animation = 'slideOutToast 0.3s ease forwards'
      setTimeout(() => toast.remove(), 300)
    }, duration)
  },
  
  success(msg) { this.show(msg,'success') },
  error(msg) { this.show(msg,'error') },
  info(msg) { this.show(msg,'info') },
  warning(msg) { this.show(msg,'warning') }
}

// Add keyframes to document
const styleEl = document.createElement('style')
styleEl.textContent = `
  @keyframes slideInToast { from{transform:translateX(120%);opacity:0} to{transform:translateX(0);opacity:1} }
  @keyframes slideOutToast { from{transform:translateX(0);opacity:1} to{transform:translateX(120%);opacity:0} }
`
document.head.appendChild(styleEl)
