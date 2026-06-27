import re

with open("index.html", "r") as f:
    content = f.read()

card_11_12_html = """
    <!-- Card 11: North India Packages -->
    <div class="tour-explorer" id="tourExplorer10" onclick="selectTexPackage(this, 'pkg-north')">
      <div class="tex-left">
        <div class="tex-header">
          <span class="tex-eyebrow">North India Packages<br>ಉತ್ತರ ಭಾರತ ಪ್ಯಾಕೇಜ್‌ಗಳು</span>
          <h3>Special Tours<br><span style="font-family:'Inter',sans-serif;font-size:0.7em;font-weight:500;opacity:0.75;">ವಿಶೇಷ ಪ್ರವಾಸಗಳು</span></h3>
        </div>
        <div class="tex-menu-item" data-pkg="pkg-north" style="--bg-img: url('images/hero/north_1.webp');">
          <div class="tex-num">11</div>
          <div class="tex-menu-text">
            <strong>North India Tours</strong>
            <span>ಉತ್ತರ ಭಾರತ ಪ್ರವಾಸ</span>
          </div>
        </div>
      </div>
      <div class="tex-right" id="texModalOverlay10" onclick="this.classList.remove('modal-open'); document.body.style.overflow=''; event.stopPropagation();">
        <div class="tex-panel" id="pkg-north" onclick="event.stopPropagation();">
          <button onclick="document.getElementById('texModalOverlay10').classList.remove('modal-open'); document.body.style.overflow='';" style="position: absolute; top: 15px; right: 15px; background: rgba(0,0,0,0.8); border: 2px solid rgba(255,255,255,0.8); color: white; width: 28px; height: 28px; border-radius: 50%; font-size: 16px; cursor: pointer; z-index: 10100; display: flex; align-items: center; justify-content: center; transition: 0.2s;">&times;</button>
          <!-- Hero only, no sub-tabs for this card -->
          <div class="tex-panel-hero bg-collage-north" id="north-hero" style="flex: 1 1 100% !important; height: 100% !important; min-height: 100% !important; border-radius: 16px;">
            <div class="tex-panel-hero-overlay"></div>
            <div class="tex-panel-hero-content" style="bottom: 10%; padding: 30px;">
              <h2 id="north-title">North India <em>Special</em><br><span style="font-family:'Inter',sans-serif;font-size:0.55em;opacity:0.8;font-weight:500;">ಉತ್ತರ ಭಾರತ <em style="color:#FFD580;font-style:normal;">ವಿಶೇಷ</em></span></h2>
              <p id="north-desc">Experience the vibrant culture, history, and beauty of North India.<br><span style="font-size:0.9em;opacity:0.75;">ಉತ್ತರ ಭಾರತದ ರೋಮಾಂಚಕ ಸಂಸ್ಕೃತಿ, ಇತಿಹಾಸ ಮತ್ತು ಸೌಂದರ್ಯವನ್ನು ಅನುಭವಿಸಿ.</span></p>
              <div class="tex-place-tags" id="north-tags">
                <span class="tex-place-tag">📍 Delhi & Agra</span>
                <span class="tex-place-tag">📍 Jaipur</span>
                <span class="tex-place-tag">📍 Udaipur</span>
                <span class="tex-place-tag">📍 Varanasi</span>
                <span class="tex-place-tag">📍 Amritsar</span>
                <span class="tex-place-tag">📍 Shimla</span>
                <span class="tex-place-tag">📍 Kashmir</span>
                <span class="tex-place-tag">📍 Manali</span>
                <span class="tex-place-tag">📍 Ayodhya</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Card 12: Hotel Stay Info (Non-Clickable) -->
    <div class="tour-explorer" id="tourExplorer11" style="cursor: default;">
      <div class="tex-left">
        <div class="tex-header">
          <span class="tex-eyebrow">Hotel Accommodation<br>ಹೋಟೆಲ್ ವಸತಿ</span>
          <h3>Stay Options<br><span style="font-family:'Inter',sans-serif;font-size:0.7em;font-weight:500;opacity:0.75;">ಉಳಿದುಕೊಳ್ಳುವ ಆಯ್ಕೆಗಳು</span></h3>
        </div>
        <div class="tex-menu-item" style="--bg-img: url('images/hero/slide_15.webp'); border-bottom: none; cursor: default;">
          <div class="tex-num" style="background: var(--saffron);">🏨</div>
          <div class="tex-menu-text">
            <strong>We Provide Tour packages with:</strong>
            <span style="font-size:12px; margin-top:8px; line-height:1.6; color: rgba(255,255,255,0.9);">
              <span style="color:#50C88C;">✔</span> Deluxe Hotel Stay<br>
              <span style="color:#50C88C;">✔</span> Semi Deluxe Stay<br>
              <span style="color:#50C88C;">✔</span> Star Hotel Stay
            </span>
          </div>
        </div>
      </div>
    </div>
"""

target = '<div style="text-align:center;margin-top:36px;">'
if target in content:
    content = content.replace("      </div>\n  " + target, card_11_12_html + "\n      </div>\n  " + target)
    print("Replaced successfully")
else:
    print("Target not found!")

with open("index.html", "w") as f:
    f.write(content)
