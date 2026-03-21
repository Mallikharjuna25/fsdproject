path = r'c:\Users\kharj\OneDrive\Desktop\fsd project\browse.html'
with open(path, encoding='utf-8') as f:
    c = f.read()

# Check key element IDs
ids_to_check = ['filtersDesktop', 'sidebarInner', 'mobileFilterBtn', 'filterOverlay', 
                'sidebarDrawer', 'drawerClose', 'activeChips', 'resultCount', 
                'sortSelect', 'gridViewBtn', 'listViewBtn', 'resultsGrid',
                'emptyState', 'pagination', 'pageBtns', 'perPageSelect',
                'searchInput', 'searchBtn', 'filterCount', 'clearAllDesktop',
                'applyDesktop', 'clearDesktop', 'hamburger', 'mobileMenu', 'navbar', 'backTop']

print("HTML ID checks:")
for id_ in ids_to_check:
    found = f'id="{id_}"' in c
    print(f"  {id_}: {'OK' if found else 'MISSING'}")
