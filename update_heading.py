import re

with open('/home/arun/SSB/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_section = '''    <span class="eyebrow">ನಾವು ನೀಡುವ ಸೇವೆಗಳು &nbsp;•&nbsp; What we offer</span>
    <h2>ಟೂರ್ ವರ್ಗಗಳು <br><span class="sub-name en-font" style="font-size: 0.65em; color: var(--muted);">Tour Categories</span></h2>'''

new_section = '''    <h2>ನಾವು ನೀಡುವ ಸೇವೆಗಳು &nbsp;•&nbsp; What we offer</h2>'''

html = html.replace(old_section, new_section)

with open('/home/arun/SSB/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
