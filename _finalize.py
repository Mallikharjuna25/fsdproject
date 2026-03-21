path = r'c:\Users\kharj\OneDrive\Desktop\fsd project\browse.html'
closing = '\n<script src="browse.js"></script>\n</body>\n</html>\n'
with open(path, 'a', encoding='utf-8') as f:
    f.write(closing)
import os
print('Done, final size:', os.path.getsize(path))
