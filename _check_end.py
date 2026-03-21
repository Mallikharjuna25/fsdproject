path = r'c:\Users\kharj\OneDrive\Desktop\fsd project\browse.html'
with open(path, encoding='utf-8') as f:
    c = f.read()

# Find and print lines 800-900 of HTML (footer section)
lines = c.split('\n')
print(f'Total lines: {len(lines)}')
# print last 60 lines
for i, line in enumerate(lines[-60:], len(lines)-60):
    print(f'{i}: {line[:120]}')
