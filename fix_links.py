import os
import re

files = ['index.html', 'browse.html', 'upload.html', 'material.html', 'categories.html', 'dashboard.html', 'auth.html']

def fix_html(content, filename):
    # 1. Global link fixes (dumb but effective matching text)
    # Using generic replacements for any hardcoded unlinked or wrong linked stuff
    content = re.sub(r'<a[^>]+href="(?:#|auth\.html|upload\.html|index\.html|browse\.html|categories\.html|dashboard\.html)"[^>]*>\s*Home\s*</a>', r'<a href="index.html">Home</a>', content)
    content = re.sub(r'<a[^>]+href="(?:#|auth\.html|upload\.html|index\.html|browse\.html|categories\.html|dashboard\.html)"[^>]*>\s*Browse.*?\s*</a>', r'<a href="browse.html">Browse</a>', content)
    # Don't accidentally wipe out the "View on Browse" button classes
    
    # 2. Add / Replace the Auth Area in Desktop Nav
    if filename != 'auth.html':
        # Replace the <div class="user-menu"...> or <a href="..." class="btn-nav"...> in nav-inner with <div id="navAuthArea"></div>
        # Looking for the node right before the hamburger
        
        # Dashboard case
        content = re.sub(r'<div class="user-menu"[^>]*>.*?</div>\s*</div>\s*<button class="hamburger"', 
                         r'<div id="navAuthArea"></div>\n      <button class="hamburger"', 
                         content, flags=re.DOTALL)
        
        # Other pages case (btn-nav)
        content = re.sub(r'<a[^>]*class="[^"]*btn-nav[^"]*"[^>]*>.*?</a>\s*<button class="hamburger"', 
                         r'<div id="navAuthArea"></div>\n      <button class="hamburger"', 
                         content, flags=re.DOTALL)
                         
        # 3. Add mobileAuthArea to the mobile menu
        if 'id="mobileAuthArea"' not in content:
            content = re.sub(r'(<div class="mobile-menu"[^>]*>\s*<ul.*?>.*?)(</ul>\s*</div>)',
                             r'\1  <div id="mobileAuthArea"></div>\n  \2',
                             content, flags=re.DOTALL)
                             
        # 4. Inject script before </body>
        if 'src="nav-auth.js"' not in content:
            content = content.replace('</body>', '<script src="nav-auth.js" charset="utf-8"></script>\n</body>')
            
    # Fix the brand back link
    content = re.sub(r'<a href="[^"]*" class="nav-logo"', r'<a href="index.html" class="nav-logo"', content)
    
    # Ensure all href="#" that contains Categories turns into categories.html
    content = re.sub(r'<a href="#"([^>]*)>Categories(.*?)</a>', r'<a href="categories.html"\1>Categories\2</a>', content, flags=re.IGNORECASE)
    
    # Ensure href="#" that contains Browse turns into browse.html
    content = re.sub(r'<a href="#"([^>]*)>Browse(.*?)</a>', r'<a href="browse.html"\1>Browse\2</a>', content, flags=re.IGNORECASE)
    
    # Ensure Dashboard links
    content = re.sub(r'<a href="#"([^>]*)>Dashboard(.*?)</a>', r'<a href="dashboard.html"\1>Dashboard\2</a>', content, flags=re.IGNORECASE)
    return content

for fw in files:
    path = os.path.join(r"c:\Users\kharj\OneDrive\Desktop\fsd project", fw)
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            c = f.read()
        
        new_c = fix_html(c, fw)
        
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_c)
        print(f"Fixed {fw}")
    else:
        print(f"Skipped {fw}")
