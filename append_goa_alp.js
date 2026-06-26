const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

const cssToAdd = `
.tex-tab-coin.coin-9a { background: rgba(255,180,60,0.85); color: #1a0f07; }
.tex-tab-coin.coin-10a { background: rgba(100,180,255,0.85); color: #0a1528; }
`;

const htmlToAdd = `
    <!-- Tour Explorer 8: Goa -->
    <div class="tour-explorer" id="tourExplorer8">
      <div class="tex-left">
        <div class="tex-header">
          <span class="tex-kannada">ಗೋವಾ ಪ್ರವಾಸ</span>
          Goa Packages
        </div>
        <div class="tex-menu-item tex-active" onclick="selectTexPackage(this, 'pkg-goa')">
          <div class="tex-num">9</div>
          <div class="tex-menu-text">
            <strong>Goa Special</strong>
            <span>ಗೋವಾ ಸ್ಪೆಷಲ್</span>
          </div>
          <div class="tex-menu-arrow">➔</div>
        </div>
      </div>
      <div class="tex-right">
        <div class="tex-panel tex-panel-active" id="pkg-goa">
          <div class="tex-panel-hero" id="goa-hero" style="background-image:url('https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Palolem_Beach_Goa_India.jpg/800px-Palolem_Beach_Goa_India.jpg');">
            <div class="tex-panel-hero-overlay"></div>
            <div class="tex-tab-coin coin-9a" id="goa-coin">9a</div>
            <div class="tex-panel-hero-content">
              <h2 id="goa-title">Goa Package <em>3N/4D</em><br><span style="font-family:'Inter',sans-serif;font-size:0.55em;opacity:0.8;font-weight:500;">ಗೋವಾ ಪ್ಯಾಕೇಜ್ <em style="color:#FFD580;font-style:normal;">೩ರಾ/೪ಹ</em></span></h2>
              <p id="goa-desc">Explore the sun-kissed beaches, historic churches, and vibrant culture of Goa.<br><span style="font-size:0.9em;opacity:0.75;">ಗೋವಾದ ಸುಂದರ ಕಡಲತೀರಗಳು, ಚರ್ಚ್‌ಗಳು ಮತ್ತು ಸಂಸ್ಕೃತಿಯ ಅದ್ಭುತ ಪ್ರವಾಸ.</span></p>
              <div class="tex-place-tags" id="goa-tags">
                <span class="tex-place-tag">🏖️ Beaches · ಕಡಲತೀರಗಳು</span>
                <span class="tex-place-tag">⛪ Churches · ಚರ್ಚ್‌ಗಳು</span>
                <span class="tex-place-tag">🌴 Fort Aguada · ಅಗುಡಾ ಕೋಟೆ</span>
              </div>
            </div>
          </div>
          <div class="tex-sub-tabs">
            <div class="tex-sub-tab tex-sub-active" onclick="selectGoaRoute(this,1)">
              <div class="tex-sub-icon">🏖️</div>
              <div class="tex-sub-info">
                <strong>Goa Package 3N/4D<br><span style="font-size:0.85em;color:#FFD580;font-weight:500;">ಗೋವಾ ಪ್ಯಾಕೇಜ್ ೩ರಾ/೪ಹ</span></strong>
              </div>
              <div style="position:absolute;bottom:8px;right:10px;width:24px;height:24px;border-radius:50%;background:rgba(255,180,60,0.85);color:#1a0f07;font-size:10px;font-weight:900;display:flex;align-items:center;justify-content:center;box-shadow:0 2px 8px rgba(0,0,0,0.4);">9a</div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Tour Explorer 9: Alleppey -->
    <div class="tour-explorer" id="tourExplorer9">
      <div class="tex-left">
        <div class="tex-header">
          <span class="tex-kannada">ಅಲೆಪ್ಪಿ ಮತ್ತು ಕೊಚ್ಚಿ</span>
          Alleppey Packages
        </div>
        <div class="tex-menu-item tex-active" onclick="selectTexPackage(this, 'pkg-alp')">
          <div class="tex-num">10</div>
          <div class="tex-menu-text">
            <strong>Alleppey Houseboat</strong>
            <span>ಅಲೆಪ್ಪಿ ಹೌಸ್‌ಬೋಟ್</span>
          </div>
          <div class="tex-menu-arrow">➔</div>
        </div>
      </div>
      <div class="tex-right">
        <div class="tex-panel tex-panel-active" id="pkg-alp">
          <div class="tex-panel-hero" id="alp-hero" style="background-image:url('https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Alleppey_Houseboat.jpg/800px-Alleppey_Houseboat.jpg');">
            <div class="tex-panel-hero-overlay"></div>
            <div class="tex-tab-coin coin-10a" id="alp-coin">10a</div>
            <div class="tex-panel-hero-content">
              <h2 id="alp-title">Alleppey Houseboat - Cochin <em>1N/2D</em><br><span style="font-family:'Inter',sans-serif;font-size:0.55em;opacity:0.8;font-weight:500;">ಅಲೆಪ್ಪಿ ಹೌಸ್‌ಬೋಟ್ - ಕೊಚ್ಚಿ <em style="color:#FFD580;font-style:normal;">೧ರಾ/೨ಹ</em></span></h2>
              <p id="alp-desc">A peaceful backwater cruise in Alleppey followed by the rich heritage of Cochin.<br><span style="font-size:0.9em;opacity:0.75;">ಅಲೆಪ್ಪಿಯ ಪ್ರಶಾಂತ ಹಿನ್ನೀರಿನ ವಿಹಾರ ಮತ್ತು ಕೊಚ್ಚಿಯ ಶ್ರೀಮಂತ ಪರಂಪರೆಯ ಪ್ರವಾಸ.</span></p>
              <div class="tex-place-tags" id="alp-tags">
                <span class="tex-place-tag">⛵ Houseboat · ಹೌಸ್‌ಬೋಟ್</span>
                <span class="tex-place-tag">🛶 Backwaters · ಹಿನ್ನೀರು</span>
                <span class="tex-place-tag">🏰 Fort Kochi · ಫೋರ್ಟ್ ಕೊಚ್ಚಿ</span>
              </div>
            </div>
          </div>
          <div class="tex-sub-tabs">
            <div class="tex-sub-tab tex-sub-active" onclick="selectAlpRoute(this,1)">
              <div class="tex-sub-icon">⛵</div>
              <div class="tex-sub-info">
                <strong>Alleppey Houseboat - Cochin 1N/2D<br><span style="font-size:0.85em;color:#FFD580;font-weight:500;">ಅಲೆಪ್ಪಿ ಹೌಸ್‌ಬೋಟ್ - ಕೊಚ್ಚಿ ೧ರಾ/೨ಹ</span></strong>
              </div>
              <div style="position:absolute;bottom:8px;right:10px;width:28px;height:24px;border-radius:12px;background:rgba(100,180,255,0.85);color:#0a1528;font-size:10px;font-weight:900;display:flex;align-items:center;justify-content:center;box-shadow:0 2px 8px rgba(0,0,0,0.4);">10a</div>
            </div>
          </div>
        </div>
      </div>
    </div>
`;

const jsToAdd = `
const goaRoutes = {
  1: {
    img: 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Palolem_Beach_Goa_India.jpg/800px-Palolem_Beach_Goa_India.jpg',
    title: 'Goa Package <em>3N/4D</em><br><span style="font-family:\\'Inter\\',sans-serif;font-size:0.55em;opacity:0.8;font-weight:500;">ಗೋವಾ ಪ್ಯಾಕೇಜ್ <em style="color:#FFD580;font-style:normal;">೩ರಾ/೪ಹ</em></span>',
    desc: 'Explore the sun-kissed beaches, historic churches, and vibrant culture of Goa.<br><span style="font-size:0.9em;opacity:0.75;">ಗೋವಾದ ಸುಂದರ ಕಡಲತೀರಗಳು, ಚರ್ಚ್‌ಗಳು ಮತ್ತು ಸಂಸ್ಕೃತಿಯ ಅದ್ಭುತ ಪ್ರವಾಸ.</span>',
    tags: '🏖️ Beaches · ಕಡಲತೀರಗಳು|⛪ Churches · ಚರ್ಚ್‌ಗಳು|🌴 Fort Aguada · ಅಗುಡಾ ಕೋಟೆ'
  }
};
function selectGoaRoute(tab, num) {
  document.querySelectorAll('#pkg-goa .tex-sub-tab').forEach(t => t.classList.remove('tex-sub-active'));
  tab.classList.add('tex-sub-active');
  const r = goaRoutes[num];
  document.getElementById('goa-hero').style.backgroundImage = \`url('\${r.img}')\`;
  document.getElementById('goa-title').innerHTML = r.title;
  document.getElementById('goa-desc').innerHTML = r.desc;
  document.getElementById('goa-tags').innerHTML = r.tags.split('|').map(t => \`<span class="tex-place-tag">\${t}</span>\`).join('');
  const coin = document.getElementById('goa-coin');
  const coinMap = {1:'9a'};
  const coinClass = {1:'coin-9a'};
  if(coin){ coin.textContent = coinMap[num]; coin.className = 'tex-tab-coin ' + coinClass[num]; }
}

const alpRoutes = {
  1: {
    img: 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Alleppey_Houseboat.jpg/800px-Alleppey_Houseboat.jpg',
    title: 'Alleppey Houseboat - Cochin <em>1N/2D</em><br><span style="font-family:\\'Inter\\',sans-serif;font-size:0.55em;opacity:0.8;font-weight:500;">ಅಲೆಪ್ಪಿ ಹೌಸ್‌ಬೋಟ್ - ಕೊಚ್ಚಿ <em style="color:#FFD580;font-style:normal;">೧ರಾ/೨ಹ</em></span>',
    desc: 'A peaceful backwater cruise in Alleppey followed by the rich heritage of Cochin.<br><span style="font-size:0.9em;opacity:0.75;">ಅಲೆಪ್ಪಿಯ ಪ್ರಶಾಂತ ಹಿನ್ನೀರಿನ ವಿಹಾರ ಮತ್ತು ಕೊಚ್ಚಿಯ ಶ್ರೀಮಂತ ಪರಂಪರೆಯ ಪ್ರವಾಸ.</span>',
    tags: '⛵ Houseboat · ಹೌಸ್‌ಬೋಟ್|🛶 Backwaters · ಹಿನ್ನೀರು|🏰 Fort Kochi · ಫೋರ್ಟ್ ಕೊಚ್ಚಿ'
  }
};
function selectAlpRoute(tab, num) {
  document.querySelectorAll('#pkg-alp .tex-sub-tab').forEach(t => t.classList.remove('tex-sub-active'));
  tab.classList.add('tex-sub-active');
  const r = alpRoutes[num];
  document.getElementById('alp-hero').style.backgroundImage = \`url('\${r.img}')\`;
  document.getElementById('alp-title').innerHTML = r.title;
  document.getElementById('alp-desc').innerHTML = r.desc;
  document.getElementById('alp-tags').innerHTML = r.tags.split('|').map(t => \`<span class="tex-place-tag">\${t}</span>\`).join('');
  const coin = document.getElementById('alp-coin');
  const coinMap = {1:'10a'};
  const coinClass = {1:'coin-10a'};
  if(coin){ coin.textContent = coinMap[num]; coin.className = 'tex-tab-coin ' + coinClass[num]; }
}
`;

html = html.replace('.tex-tab-coin.coin-8b { background: rgba(100,180,255,0.85); color: #0a1528; }', '.tex-tab-coin.coin-8b { background: rgba(100,180,255,0.85); color: #0a1528; }\n' + cssToAdd);
html = html.replace('<!-- Tour 3 -->', htmlToAdd + '\n    <!-- Tour 3 -->');
html = html.replace('</script>\n</body>', jsToAdd + '\n</script>\n</body>');

fs.writeFileSync('index.html', html);
console.log('Appended Goa and Alleppey widgets');
