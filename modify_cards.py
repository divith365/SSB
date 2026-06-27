import sys

with open('/home/arun/SSB/index.html', 'r') as f:
    content = f.read()

# Replace the max-width: 600px grid template
old_600px = """@media (max-width: 600px) {
  .tours-grid { grid-template-columns: 1fr; }
}"""

new_600px = """@media (max-width: 600px) {
  .tours-grid { grid-template-columns: 1fr 1fr; gap: 8px; padding-left: 10px; padding-right: 10px; }
}"""

content = content.replace(old_600px, new_600px)


# Replace the max-width: 768px block for the tour-explorer
old_768px = """@media (max-width: 768px) {
  .tour-explorer { flex-direction: column; min-height: auto; }
  .tex-left { width: 100%; border-right: none; border-bottom: 1px solid rgba(255,255,255,0.06); padding: 16px 0; display: flex; flex-direction: row; flex-wrap: nowrap; overflow-x: auto; overflow-y: hidden; -webkit-overflow-scrolling: touch; scrollbar-width: none; }
  .tex-left::-webkit-scrollbar { display: none; }
  .tex-menu-item { flex: 0 0 85%; max-width: 300px; margin: 0 8px; }
  .tex-header { width: 100%; padding: 8px 16px 10px; }"""

new_768px = """@media (max-width: 768px) {
  .tour-explorer { flex-direction: column; min-height: auto; border-radius: 12px; }
  .tex-left { width: 100%; border-right: none; border-bottom: none; padding: 6px; display: flex; flex-direction: column; }
  .tex-left::-webkit-scrollbar { display: none; }
  .tex-menu-item { flex: none; width: 100%; max-width: none; margin: 0; padding: 6px; gap: 8px; }
  .tex-menu-item .tex-num { width: 22px; height: 22px; font-size: 11px; border-radius: 4px; }
  .tex-menu-text strong { font-size: 11px !important; line-height: 1.2 !important; }
  .tex-menu-text span { font-size: 9px !important; line-height: 1.2 !important; margin-top: 2px; }
  .tex-menu-item::after { display: none; }
  .tex-header { width: 100%; padding: 8px 8px 6px; margin-bottom: 4px; }
  .tex-header .tex-eyebrow { font-size: 8px !important; margin-bottom: 2px !important; letter-spacing: 0.5px !important; }
  .tex-header h3 { font-size: 12px !important; line-height: 1.3 !important; }
  .tex-header::before { display: none; }"""

content = content.replace(old_768px, new_768px)

with open('/home/arun/SSB/index.html', 'w') as f:
    f.write(content)
