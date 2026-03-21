// ── DOM ELEMENTS
const searchInput = document.getElementById('catSearch');

// ── INIT
document.addEventListener('DOMContentLoaded', () => {
  initTagCloud();
  initScrollAnimations();
});

// ── LIVE SEARCH FILTER
function filterCategories() {
  const query = searchInput.value.toLowerCase().trim();
  const items = document.querySelectorAll('.cat-item');
  
  items.forEach(item => {
    // We check the data-text attribute which contains keywords plus the visible text
    const textData = item.getAttribute('data-text') || '';
    const visibleText = item.textContent.toLowerCase();
    
    if (textData.includes(query) || visibleText.includes(query)) {
      item.classList.remove('hidden-item');
      
      // If it's a department accordion, we might want to expand it if it matches
      if(query.length > 2 && item.classList.contains('dept-item')) {
        item.classList.add('active');
      } else if (query.length === 0 && item.classList.contains('dept-item')) {
        item.classList.remove('active'); // collapse when search cleared
      }
      
    } else {
      item.classList.add('hidden-item');
      // If we hide a department, ensure it's collapsed so it doesn't look weird if shown later
      if(item.classList.contains('dept-item')) {
        item.classList.remove('active');
      }
    }
  });
}

// ── ACCORDION TOGGLE
function toggleAccordion(element) {
  const parentItem = element.closest('.dept-item');
  
  // Optional: Close others first (uncomment for strict accordion behavior)
  /*
  document.querySelectorAll('.dept-item').forEach(item => {
    if(item !== parentItem) item.classList.remove('active');
  });
  */
  
  parentItem.classList.toggle('active');
}

// ── TRENDING TAG CLOUD MOCK DATA
const tagData = [
  { text: 'engineering', weight: 4 },
  { text: 'medical', weight: 3 },
  { text: 'physics', weight: 8 },
  { text: 'calculus', weight: 10 },
  { text: 'programming', weight: 7 },
  { text: 'mba notes', weight: 4 },
  { text: 'gate 2024', weight: 9 },
  { text: 'neet papers', weight: 8 },
  { text: 'organic chemistry', weight: 6 },
  { text: 'data structures', weight: 9 },
  { text: 'algorithms', weight: 7 },
  { text: 'business', weight: 3 },
  { text: 'finance', weight: 5 },
  { text: 'thermodynamics', weight: 6 },
  { text: 'history', weight: 2 }
];

function initTagCloud() {
  const container = document.getElementById('tagCloud');
  if(!container) return;
  
  container.innerHTML = '';
  
  tagData.forEach(tag => {
    // Calculate font size based on weight (min 1rem, max 2.5rem)
    const fontSize = 0.8 + (tag.weight * 0.15); 
    
    // Calculate opacity based on weight
    const opacity = 0.4 + (tag.weight * 0.06);
    
    // Pick a random animation delay class
    const delayClass = `del-${Math.floor(Math.random() * 5) + 1}`;
    
    const a = document.createElement('a');
    a.href = `browse.html?q=${encodeURIComponent(tag.text)}`;
    a.className = `cloud-tag ${delayClass}`;
    a.textContent = `#${tag.text}`;
    a.style.fontSize = `${fontSize}rem`;
    a.style.opacity = opacity;
    
    // Some tags can be colored amber for pop
    if(tag.weight > 8) {
      a.style.color = 'var(--clr-amber)';
      a.style.opacity = '1';
    }
    
    container.appendChild(a);
  });
}

// ── SCROLL ANIMATIONS (Intersection Observer)
function initScrollAnimations() {
  const revealElements = document.querySelectorAll('.reveal');
  
  const observerOptions = {
    root: null,
    rootMargin: '0px 0px -50px 0px', // Trigger slightly before it comes into view
    threshold: 0.1
  };
  
  const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if(entry.isIntersecting) {
        entry.target.classList.add('active');
        observer.unobserve(entry.target); // Optional: Stop observing once revealed
      }
    });
  }, observerOptions);
  
  revealElements.forEach(el => observer.observe(el));
}
