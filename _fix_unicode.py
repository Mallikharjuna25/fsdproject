import re

# Fix browse.js - replace Unicode chars that may cause charset issues
path = r'c:\Users\kharj\OneDrive\Desktop\fsd project\browse.js'
with open(path, encoding='utf-8') as f:
    content = f.read()

# Replace en-dashes with regular hyphens in data strings (only in title/desc strings)
# The en-dash character is '\u2013'
content = content.replace('\u2013', '-')

# Replace em-dashes too (just in case)
content = content.replace('\u2014', '-')

# Replace the star characters in rating labels with ASCII equivalents
# '4\u2605 & above' -> '4+ rating'... no, keep stars but check
# Actually the filter comparison uses exact string match, so keep them consistent
# The \u2605 ★ and \u2606 ☆ are in the stars() return, but those are GENERATED in JS
# The FILTER_GROUPS options has '4\u2605 & above' - let's check
print('Has en-dash:', '\u2013' in content)
print('Has star:', '\u2605' in content)
print('Has em-dash:', '\u2014' in content)

# Check how many replacements were needed for en-dash
orig_count = content.count('\u2013')
print(f'En-dash count after replace: {orig_count}')

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

import os
print('Done. Size:', os.path.getsize(path))
