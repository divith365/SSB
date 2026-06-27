import sys

with open('/home/arun/SSB/index.html', 'r') as f:
    content = f.read()

# Replace the specific CSS that is breaking the scrolling for pkg-mys and pkg-ker
old_css = """#pkg-mys .tex-sub-tabs, #pkg-ker .tex-sub-tabs {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  overflow: visible;
  height: auto;
}"""

new_css = """#pkg-mys .tex-sub-tabs, #pkg-ker .tex-sub-tabs {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  /* Removed overflow: visible and height: auto to allow scrolling */
}"""

content = content.replace(old_css, new_css)

# Also ensure min-height: 0 on the mobile flex item
mobile_css_old = """    align-content: start;
    overflow-y: auto !important;
    flex: 1 !important;
  }"""

mobile_css_new = """    align-content: start;
    overflow-y: auto !important;
    flex: 1 !important;
    min-height: 0 !important;
  }"""

content = content.replace(mobile_css_old, mobile_css_new)

with open('/home/arun/SSB/index.html', 'w') as f:
    f.write(content)
