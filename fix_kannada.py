import sys

with open('/home/arun/SSB/index.html', 'r') as f:
    content = f.read()

# Replacements
replacements = [
    ('ಕೂರ್ಗ್ ಪ್ಯಾಕೇಜ್‌ಗಳು', 'ಕೊಡಗು ಪ್ಯಾಕೇಜ್‌ಗಳು'),
    ('<span>ಕೂರ್ಗ್</span>', '<span>ಕೊಡಗು</span>'),
    ('ಕೂರ್ಗ್ <em style="color:#FFD580;font-style:normal;"> & </em>', 'ಕೊಡಗು'),
    ('ಕೂರ್ಗ್ - ಚಿಕ್ಕಮಗಳೂರು <em style="color:#FFD580;font-style:normal;"> & </em>', 'ಕೊಡಗು - ಚಿಕ್ಕಮಗಳೂರು'),
    ('ಮೈಸೂರು - ಕೂರ್ಗ್ <em style="color:#FFD580;font-style:normal;"> & </em>', 'ಮೈಸೂರು - ಕೊಡಗು'),
    ('ಮೈಸೂರು - ಕೂರ್ಗ್ - ವಯನಾಡ್ <em style="color:#FFD580;font-style:normal;"></em>', 'ಮೈಸೂರು - ಕೊಡಗು - ವಯನಾಡ್'),
    ('ಊಟಿ, ಕೊಡೈ, ಮುನ್ನಾರ್, ಕೂರ್ಗ್, ಕೂನೂರ್', 'ಊಟಿ, ಕೊಡೈ, ಮುನ್ನಾರ್, ಕೊಡಗು, ಕೂನೂರ್')
]

for old, new in replacements:
    content = content.replace(old, new)

with open('/home/arun/SSB/index.html', 'w') as f:
    f.write(content)
