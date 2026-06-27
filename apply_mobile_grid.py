import sys

with open('/home/arun/SSB/index.html', 'r') as f:
    content = f.read()

mobile_grid_css = """
/* Make all sub-tabs grid for mobile only (like mys/ker cards) */
@media (max-width: 768px) {
  .tex-sub-tabs {
    display: grid !important;
    grid-template-columns: repeat(2, 1fr) !important;
    overflow: visible !important;
    height: auto !important;
  }
  .tex-sub-tab {
    min-width: 0 !important;
    width: auto !important;
    border-bottom: 1px solid rgba(255,255,255,0.06) !important;
    border-right: 1px solid rgba(255,255,255,0.06) !important;
  }
}
@media (max-width: 480px) {
  .tex-sub-tabs {
    grid-template-columns: 1fr !important;
  }
}
</style>
"""

content = content.replace("</style>", mobile_grid_css)

with open('/home/arun/SSB/index.html', 'w') as f:
    f.write(content)
