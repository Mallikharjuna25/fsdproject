path = r'c:\Users\kharj\OneDrive\Desktop\fsd project\browse.html'
with open(path, encoding='utf-8') as f:
    content = f.read()

# Fix the script tag to include charset
old = '<script src="browse.js"></script>'
new = '<script src="browse.js" charset="utf-8"></script>'
content = content.replace(old, new)

# Also fix the rating filter display values in browse.js
# Remove Unicode characters from browse.html's pop-tag buttons (they use text, not emoji in JS)
with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
print('Fixed script charset. Done.')
