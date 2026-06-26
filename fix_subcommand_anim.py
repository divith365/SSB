with open('/home/arun/SSB/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add animation for sub-tabs
sub_tab_anim_css = """
@keyframes texSubFadeIn {
  from { opacity: 0; transform: translateX(20px); }
  to { opacity: 1; transform: translateX(0); }
}
.tex-panel.tex-panel-active .tex-sub-tab {
  animation: texSubFadeIn 0.4s cubic-bezier(0.4, 0, 0.2, 1) forwards;
  opacity: 0;
}
.tex-panel.tex-panel-active .tex-sub-tab.tex-sub-active {
  animation: none;
  opacity: 1;
}
.tex-panel.tex-panel-active .tex-sub-tab:nth-child(1) { animation-delay: 0.05s; }
.tex-panel.tex-panel-active .tex-sub-tab:nth-child(2) { animation-delay: 0.1s; }
.tex-panel.tex-panel-active .tex-sub-tab:nth-child(3) { animation-delay: 0.15s; }
.tex-panel.tex-panel-active .tex-sub-tab:nth-child(4) { animation-delay: 0.2s; }
.tex-panel.tex-panel-active .tex-sub-tab:nth-child(5) { animation-delay: 0.25s; }
"""

# Wait, if .tex-sub-active has animation: none; opacity: 1, it won't animate on load but it will just be visible.
# But actually, I CAN animate it using a wrapper or just let it snap into place.
# Better yet, don't use transform in the animation, use margin-left.
sub_tab_anim_css_better = """
@keyframes texSubFadeIn {
  from { opacity: 0; padding-left: 40px; }
  to { opacity: 1; padding-left: 20px; }
}
.tex-panel.tex-panel-active .tex-sub-tab {
  animation: texSubFadeIn 0.4s cubic-bezier(0.4, 0, 0.2, 1) forwards;
  opacity: 0;
}
.tex-panel.tex-panel-active .tex-sub-tab:nth-child(1) { animation-delay: 0.05s; }
.tex-panel.tex-panel-active .tex-sub-tab:nth-child(2) { animation-delay: 0.1s; }
.tex-panel.tex-panel-active .tex-sub-tab:nth-child(3) { animation-delay: 0.15s; }
.tex-panel.tex-panel-active .tex-sub-tab:nth-child(4) { animation-delay: 0.2s; }
.tex-panel.tex-panel-active .tex-sub-tab:nth-child(5) { animation-delay: 0.25s; }
.tex-panel.tex-panel-active .tex-sub-tab:nth-child(6) { animation-delay: 0.3s; }
"""

# Inject before closing style tag if not already injected
if "texSubFadeIn" not in html:
    html = html.replace('</style>', sub_tab_anim_css_better + '\n</style>')

with open('/home/arun/SSB/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Subcommand animation added.")
