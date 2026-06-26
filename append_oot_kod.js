const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

const cssToAdd = `
.tex-tab-coin.coin-7a { background: rgba(255,180,60,0.85); color: #1a0f07; }
.tex-tab-coin.coin-7b { background: rgba(100,180,255,0.85); color: #0a1528; }
.tex-tab-coin.coin-7c { background: rgba(80,200,140,0.85); color: #051a10; }
.tex-tab-coin.coin-8a { background: rgba(255,180,60,0.85); color: #1a0f07; }
.tex-tab-coin.coin-8b { background: rgba(100,180,255,0.85); color: #0a1528; }
`;

const htmlToAdd = `
    <!-- Tour Explorer 6: Ooty -->
    <div class="tour-explorer" id="tourExplorer6">
      <div class="tex-left">
        <div class="tex-header">
          <span class="tex-kannada">ಊಟಿ ಪ್ರವಾಸ</span>
          Ooty Packages
        </div>
        <div class="tex-menu-item tex-active" onclick="selectTexPackage(this, 'pkg-oot')">
          <div class="tex-num">7</div>
          <div class="tex-menu-text">
            <strong>Ooty Special</strong>
            <span>ಊಟಿ ಸ್ಪೆಷಲ್</span>
          </div>
          <div class="tex-menu-arrow">➔</div>
        </div>
      </div>
      <div class="tex-right">
        <div class="tex-panel tex-panel-active" id="pkg-oot">
          <div class="tex-panel-hero" id="oot-hero" style="background-image:url('https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Ooty_Lake.jpg/800px-Ooty_Lake.jpg');">
            <div class="tex-panel-hero-overlay"></div>
            <div class="tex-tab-coin coin-7a" id="oot-coin">7a</div>
            <div class="tex-panel-hero-content">
              <h2 id="oot-title">Ooty <em>1N/2D, 2N/3D, 3N/4D</em><br><span style="font-family:'Inter',sans-serif;font-size:0.55em;opacity:0.8;font-weight:500;">ಊಟಿ <em style="color:#FFD580;font-style:normal;">೧ರಾ/೨ಹ, ೨ರಾ/೩ಹ, ೩ರಾ/೪ಹ</em></span></h2>
              <p id="oot-desc">Relax by the Ooty lake and explore the queen of hill stations.<br><span style="font-size:0.9em;opacity:0.75;">ಊಟಿ ಸರೋವರ ಮತ್ತು ಗಿರಿಧಾಮಗಳ ರಾಣಿಯ ಸೌಂದರ್ಯವನ್ನು ಸವಿಯಿರಿ.</span></p>
              <div class="tex-place-tags" id="oot-tags">
                <span class="tex-place-tag">⛰️ Ooty Lake · ಊಟಿ ಸರೋವರ</span>
                <span class="tex-place-tag">🌺 Botanical Garden · ಬೊಟಾನಿಕಲ್ ಗಾರ್ಡನ್</span>
                <span class="tex-place-tag">⛰️ Dodabetta Peak · ದೊಡ್ಡಬೆಟ್ಟ</span>
              </div>
            </div>
          </div>
          <div class="tex-sub-tabs">
            <div class="tex-sub-tab tex-sub-active" onclick="selectOotRoute(this,1)">
              <div class="tex-sub-icon">⛰️</div>
              <div class="tex-sub-info">
                <strong>Ooty 1N/2D, 2N/3D, 3N/4D<br><span style="font-size:0.85em;color:#FFD580;font-weight:500;">ಊಟಿ ೧ರಾ/೨ಹ, ೨ರಾ/೩ಹ, ೩ರಾ/೪ಹ</span></strong>
              </div>
              <div style="position:absolute;bottom:8px;right:10px;width:24px;height:24px;border-radius:50%;background:rgba(255,180,60,0.85);color:#1a0f07;font-size:10px;font-weight:900;display:flex;align-items:center;justify-content:center;box-shadow:0 2px 8px rgba(0,0,0,0.4);">7a</div>
            </div>
            <div class="tex-sub-tab" onclick="selectOotRoute(this,2)">
              <div class="tex-sub-icon">⛵</div>
              <div class="tex-sub-info">
                <strong>Ooty - Kodaikanal 2N/3D, 3N/4D, 4N/5D<br><span style="font-size:0.85em;color:#FFD580;font-weight:500;">ಊಟಿ - ಕೊಡೆಕಾನಲ್ ೨ರಾ/೩ಹ, ೩ರಾ/೪ಹ, ೪ರಾ/೫ಹ</span></strong>
              </div>
              <div style="position:absolute;bottom:8px;right:10px;width:24px;height:24px;border-radius:50%;background:rgba(100,180,255,0.85);color:#0a1528;font-size:10px;font-weight:900;display:flex;align-items:center;justify-content:center;box-shadow:0 2px 8px rgba(0,0,0,0.4);">7b</div>
            </div>
            <div class="tex-sub-tab" onclick="selectOotRoute(this,3)">
              <div class="tex-sub-icon">🍃</div>
              <div class="tex-sub-info">
                <strong>Ooty - Kodaikanal - Munnar 6N/7D<br><span style="font-size:0.85em;color:#FFD580;font-weight:500;">ಊಟಿ - ಕೊಡೆಕಾನಲ್ - ಮುನ್ನಾರ್ ೬ರಾ/೭ಹ</span></strong>
              </div>
              <div style="position:absolute;bottom:8px;right:10px;width:24px;height:24px;border-radius:50%;background:rgba(80,200,140,0.85);color:#051a10;font-size:10px;font-weight:900;display:flex;align-items:center;justify-content:center;box-shadow:0 2px 8px rgba(0,0,0,0.4);">7c</div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Tour Explorer 7: Kodaikanal -->
    <div class="tour-explorer" id="tourExplorer7">
      <div class="tex-left">
        <div class="tex-header">
          <span class="tex-kannada">ಕೊಡೆಕಾನಲ್ ಪ್ರವಾಸ</span>
          Kodaikanal Packages
        </div>
        <div class="tex-menu-item tex-active" onclick="selectTexPackage(this, 'pkg-kod')">
          <div class="tex-num">8</div>
          <div class="tex-menu-text">
            <strong>Kodaikanal Special</strong>
            <span>ಕೊಡೆಕಾನಲ್ ಸ್ಪೆಷಲ್</span>
          </div>
          <div class="tex-menu-arrow">➔</div>
        </div>
      </div>
      <div class="tex-right">
        <div class="tex-panel tex-panel-active" id="pkg-kod">
          <div class="tex-panel-hero" id="kod-hero" style="background-image:url('https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Kodaikanal_Lake.jpg/800px-Kodaikanal_Lake.jpg');">
            <div class="tex-panel-hero-overlay"></div>
            <div class="tex-tab-coin coin-8a" id="kod-coin">8a</div>
            <div class="tex-panel-hero-content">
              <h2 id="kod-title">Kodaikanal <em>1N/2D & 2N/3D</em><br><span style="font-family:'Inter',sans-serif;font-size:0.55em;opacity:0.8;font-weight:500;">ಕೊಡೆಕಾನಲ್ <em style="color:#FFD580;font-style:normal;">೧ರಾ/೨ಹ & ೨ರಾ/೩ಹ</em></span></h2>
              <p id="kod-desc">Experience the princess of hill stations with its star-shaped lake.<br><span style="font-size:0.9em;opacity:0.75;">ಗಿರಿಧಾಮಗಳ ರಾಜಕುಮಾರಿ ಮತ್ತು ನಕ್ಷತ್ರ ಆಕಾರದ ಸರೋವರದ ಸೌಂದರ್ಯ.</span></p>
              <div class="tex-place-tags" id="kod-tags">
                <span class="tex-place-tag">⛵ Kodai Lake · ಕೊಡೆಕಾನಲ್ ಸರೋವರ</span>
                <span class="tex-place-tag">🌲 Pine Forest · ಪೈನ್ ಫಾರೆಸ್ಟ್</span>
                <span class="tex-place-tag">🪨 Pillar Rocks · ಪಿಲ್ಲರ್ ರಾಕ್ಸ್</span>
              </div>
            </div>
          </div>
          <div class="tex-sub-tabs">
            <div class="tex-sub-tab tex-sub-active" onclick="selectKodRoute(this,1)">
              <div class="tex-sub-icon">⛵</div>
              <div class="tex-sub-info">
                <strong>Kodaikanal 1N/2D & 2N/3D<br><span style="font-size:0.85em;color:#FFD580;font-weight:500;">ಕೊಡೆಕಾನಲ್ ೧ರಾ/೨ಹ & ೨ರಾ/೩ಹ</span></strong>
              </div>
              <div style="position:absolute;bottom:8px;right:10px;width:24px;height:24px;border-radius:50%;background:rgba(255,180,60,0.85);color:#1a0f07;font-size:10px;font-weight:900;display:flex;align-items:center;justify-content:center;box-shadow:0 2px 8px rgba(0,0,0,0.4);">8a</div>
            </div>
            <div class="tex-sub-tab" onclick="selectKodRoute(this,2)">
              <div class="tex-sub-icon">🍃</div>
              <div class="tex-sub-info">
                <strong>Kodaikanal - Munnar 4N/5D<br><span style="font-size:0.85em;color:#FFD580;font-weight:500;">ಕೊಡೆಕಾನಲ್ - ಮುನ್ನಾರ್ ೪ರಾ/೫ಹ</span></strong>
              </div>
              <div style="position:absolute;bottom:8px;right:10px;width:24px;height:24px;border-radius:50%;background:rgba(100,180,255,0.85);color:#0a1528;font-size:10px;font-weight:900;display:flex;align-items:center;justify-content:center;box-shadow:0 2px 8px rgba(0,0,0,0.4);">8b</div>
            </div>
          </div>
        </div>
      </div>
    </div>
`;

const jsToAdd = `
const ootRoutes = {
  1: {
    img: 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Ooty_Lake.jpg/800px-Ooty_Lake.jpg',
    title: 'Ooty <em>1N/2D, 2N/3D, 3N/4D</em><br><span style="font-family:\\'Inter\\',sans-serif;font-size:0.55em;opacity:0.8;font-weight:500;">ಊಟಿ <em style="color:#FFD580;font-style:normal;">೧ರಾ/೨ಹ, ೨ರಾ/೩ಹ, ೩ರಾ/೪ಹ</em></span>',
    desc: 'Relax by the Ooty lake and explore the queen of hill stations.<br><span style="font-size:0.9em;opacity:0.75;">ಊಟಿ ಸರೋವರ ಮತ್ತು ಗಿರಿಧಾಮಗಳ ರಾಣಿಯ ಸೌಂದರ್ಯವನ್ನು ಸವಿಯಿರಿ.</span>',
    tags: '⛰️ Ooty Lake · ಊಟಿ ಸರೋವರ|🌺 Botanical Garden · ಬೊಟಾನಿಕಲ್ ಗಾರ್ಡನ್|⛰️ Dodabetta Peak · ದೊಡ್ಡಬೆಟ್ಟ'
  },
  2: {
    img: 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Kodaikanal_Lake.jpg/800px-Kodaikanal_Lake.jpg',
    title: 'Ooty - Kodaikanal <em>2N/3D, 3N/4D, 4N/5D</em><br><span style="font-family:\\'Inter\\',sans-serif;font-size:0.55em;opacity:0.8;font-weight:500;">ಊಟಿ - ಕೊಡೆಕಾನಲ್ <em style="color:#FFD580;font-style:normal;">೨ರಾ/೩ಹ, ೩ರಾ/೪ಹ, ೪ರಾ/೫ಹ</em></span>',
    desc: 'The best of Tamil Nadu\\'s hill stations in one memorable trip.<br><span style="font-size:0.9em;opacity:0.75;">ತಮಿಳುನಾಡಿನ ಅತ್ಯುತ್ತಮ ಗಿರಿಧಾಮಗಳ ಸುಂದರ ಪ್ರವಾಸ.</span>',
    tags: '⛰️ Ooty Lake · ಊಟಿ ಸರೋವರ|⛵ Kodai Lake · ಕೊಡೆಕಾನಲ್ ಸರೋವರ|🪨 Pillar Rocks · ಪಿಲ್ಲರ್ ರಾಕ್ಸ್'
  },
  3: {
    img: 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Munnar_hillstation.jpg/800px-Munnar_hillstation.jpg',
    title: 'Ooty - Kodaikanal - Munnar <em>6N/7D</em><br><span style="font-family:\\'Inter\\',sans-serif;font-size:0.55em;opacity:0.8;font-weight:500;">ಊಟಿ - ಕೊಡೆಕಾನಲ್ - ಮುನ್ನಾರ್ <em style="color:#FFD580;font-style:normal;">೬ರಾ/೭ಹ</em></span>',
    desc: 'An extended journey through South India\\'s most iconic mountain ranges.<br><span style="font-size:0.9em;opacity:0.75;">ದಕ್ಷಿಣ ಭಾರತದ ಪ್ರಮುಖ ಗಿರಿಧಾಮಗಳ ಮೂಲಕ ಸುದೀರ್ಘ ಪ್ರವಾಸ.</span>',
    tags: '⛰️ Ooty Lake · ಊಟಿ ಸರೋವರ|⛵ Kodai Lake · ಕೊಡೆಕಾನಲ್ ಸರೋವರ|🍃 Tea Gardens · ಚಹಾ ತೋಟಗಳು'
  }
};
function selectOotRoute(tab, num) {
  document.querySelectorAll('#pkg-oot .tex-sub-tab').forEach(t => t.classList.remove('tex-sub-active'));
  tab.classList.add('tex-sub-active');
  const r = ootRoutes[num];
  document.getElementById('oot-hero').style.backgroundImage = \`url('\${r.img}')\`;
  document.getElementById('oot-title').innerHTML = r.title;
  document.getElementById('oot-desc').innerHTML = r.desc;
  document.getElementById('oot-tags').innerHTML = r.tags.split('|').map(t => \`<span class="tex-place-tag">\${t}</span>\`).join('');
  const coin = document.getElementById('oot-coin');
  const coinMap = {1:'7a',2:'7b',3:'7c'};
  const coinClass = {1:'coin-7a',2:'coin-7b',3:'coin-7c'};
  if(coin){ coin.textContent = coinMap[num]; coin.className = 'tex-tab-coin ' + coinClass[num]; }
}

const kodRoutes = {
  1: {
    img: 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Kodaikanal_Lake.jpg/800px-Kodaikanal_Lake.jpg',
    title: 'Kodaikanal <em>1N/2D & 2N/3D</em><br><span style="font-family:\\'Inter\\',sans-serif;font-size:0.55em;opacity:0.8;font-weight:500;">ಕೊಡೆಕಾನಲ್ <em style="color:#FFD580;font-style:normal;">೧ರಾ/೨ಹ & ೨ರಾ/೩ಹ</em></span>',
    desc: 'Experience the princess of hill stations with its star-shaped lake.<br><span style="font-size:0.9em;opacity:0.75;">ಗಿರಿಧಾಮಗಳ ರಾಜಕುಮಾರಿ ಮತ್ತು ನಕ್ಷತ್ರ ಆಕಾರದ ಸರೋವರದ ಸೌಂದರ್ಯ.</span>',
    tags: '⛵ Kodai Lake · ಕೊಡೆಕಾನಲ್ ಸರೋವರ|🌲 Pine Forest · ಪೈನ್ ಫಾರೆಸ್ಟ್|🪨 Pillar Rocks · ಪಿಲ್ಲರ್ ರಾಕ್ಸ್'
  },
  2: {
    img: 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Munnar_hillstation.jpg/800px-Munnar_hillstation.jpg',
    title: 'Kodaikanal - Munnar <em>4N/5D</em><br><span style="font-family:\\'Inter\\',sans-serif;font-size:0.55em;opacity:0.8;font-weight:500;">ಕೊಡೆಕಾನಲ್ - ಮುನ್ನಾರ್ <em style="color:#FFD580;font-style:normal;">೪ರಾ/೫ಹ</em></span>',
    desc: 'Journey through the high ranges connecting Tamil Nadu to Kerala.<br><span style="font-size:0.9em;opacity:0.75;">ತಮಿಳುನಾಡು ಮತ್ತು ಕೇರಳವನ್ನು ಸಂಪರ್ಕಿಸುವ ಗಿರಿಧಾಮಗಳ ಪ್ರವಾಸ.</span>',
    tags: '⛵ Kodai Lake · ಕೊಡೆಕಾನಲ್ ಸರೋವರ|🍃 Tea Gardens · ಚಹಾ ತೋಟಗಳು|🌺 Echo Point · ಎಕೋ ಪಾಯಿಂಟ್'
  }
};
function selectKodRoute(tab, num) {
  document.querySelectorAll('#pkg-kod .tex-sub-tab').forEach(t => t.classList.remove('tex-sub-active'));
  tab.classList.add('tex-sub-active');
  const r = kodRoutes[num];
  document.getElementById('kod-hero').style.backgroundImage = \`url('\${r.img}')\`;
  document.getElementById('kod-title').innerHTML = r.title;
  document.getElementById('kod-desc').innerHTML = r.desc;
  document.getElementById('kod-tags').innerHTML = r.tags.split('|').map(t => \`<span class="tex-place-tag">\${t}</span>\`).join('');
  const coin = document.getElementById('kod-coin');
  const coinMap = {1:'8a',2:'8b'};
  const coinClass = {1:'coin-8a',2:'coin-8b'};
  if(coin){ coin.textContent = coinMap[num]; coin.className = 'tex-tab-coin ' + coinClass[num]; }
}
`;

html = html.replace('.tex-tab-coin.coin-6i { background: rgba(80,200,140,0.85); color: #051a10; }', '.tex-tab-coin.coin-6i { background: rgba(80,200,140,0.85); color: #051a10; }\n' + cssToAdd);
html = html.replace('<!-- Tour 3 -->', htmlToAdd + '\n    <!-- Tour 3 -->');
html = html.replace('</script>\n</body>', jsToAdd + '\n</script>\n</body>');

fs.writeFileSync('index.html', html);
console.log('Appended Ooty and Kodaikanal widgets');
