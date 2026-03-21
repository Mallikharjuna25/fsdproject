path = r'c:\Users\kharj\OneDrive\Desktop\fsd project\browse.html'
with open(path, encoding='utf-8') as f:
    content = f.read()

# Insert card-anim keyframe CSS just before </style>
card_anim_css = """
@keyframes cardIn{from{opacity:0;transform:translateY(20px)}to{opacity:1;transform:none}}
.card-anim{animation:cardIn .5s ease both}
"""

# Find </style> to insert before it
idx = content.rfind('</style>')
if idx != -1:
    content = content[:idx] + card_anim_css + content[idx:]
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print('CSS inserted, new size:', len(content))
else:
    print('ERROR: </style> not found')
