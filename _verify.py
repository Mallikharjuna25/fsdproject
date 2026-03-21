path = r'c:\Users\kharj\OneDrive\Desktop\fsd project\browse.html'
with open(path, encoding='utf-8') as f:
    c = f.read()

# check all key sections
checks = [
    ('navbar', 'id="navbar"'),
    ('page hero', 'class="page-hero"'),
    ('search input', 'id="searchInput"'),
    ('popular tags', 'class="pop-tag"'),
    ('filter sidebar', 'class="filter-sidebar"'),
    ('filtersDesktop', 'id="filtersDesktop"'),
    ('results grid', 'id="resultsGrid"'),
    ('empty state', 'id="emptyState"'),
    ('pagination', 'id="pagination"'),
    ('footer grid', 'class="footer-grid"'),
    ('footer bottom', 'class="footer-bottom"'),
    ('browse.js link', 'src="browse.js"'),
    ('closing tags', '</html>'),
]

print(f'File size: {len(c)} bytes')
for name, pattern in checks:
    print(f'  {name}: {"OK" if pattern in c else "MISSING"}')
    
# count mat-card occurrences  
print(f'\nFilter groups in CSS: {c.count(".filter-group")}')
print(f'mat-card in CSS: {c.count(".mat-card{")}')
