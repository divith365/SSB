const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

const cssToAdd = `
.tex-tab-coin.coin-6a { background: rgba(255,180,60,0.85); color: #1a0f07; }
.tex-tab-coin.coin-6b { background: rgba(100,180,255,0.85); color: #0a1528; }
.tex-tab-coin.coin-6c { background: rgba(80,200,140,0.85); color: #051a10; }
.tex-tab-coin.coin-6d { background: rgba(255,180,60,0.85); color: #1a0f07; }
.tex-tab-coin.coin-6e { background: rgba(100,180,255,0.85); color: #0a1528; }
.tex-tab-coin.coin-6f { background: rgba(80,200,140,0.85); color: #051a10; }
.tex-tab-coin.coin-6g { background: rgba(255,180,60,0.85); color: #1a0f07; }
.tex-tab-coin.coin-6h { background: rgba(100,180,255,0.85); color: #0a1528; }
.tex-tab-coin.coin-6i { background: rgba(80,200,140,0.85); color: #051a10; }
`;

const htmlToAdd = `
    <!-- Tour Explorer 5: Kerala Special -->
    <div class="tour-explorer" id="tourExplorer5">
      <div class="tex-left">
        <div class="tex-header">
          <span class="tex-kannada">ಕೇರಳ ಪ್ರವಾಸ</span>
          Kerala Packages
        </div>
        <div class="tex-menu-item tex-active" onclick="selectTexPackage(this, 'pkg-ker')">
          <div class="tex-num">6</div>
          <div class="tex-menu-text">
            <strong>Kerala Special</strong>
            <span>ಕೇರಳ ಸ್ಪೆಷಲ್</span>
          </div>
          <div class="tex-menu-arrow">➔</div>
        </div>
      </div>
      <div class="tex-right">
        <!-- Package 6: Kerala -->
        <div class="tex-panel tex-panel-active" id="pkg-ker">
          <div class="tex-panel-hero" id="ker-hero" style="background-image:url('https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Munnar_hillstation.jpg/800px-Munnar_hillstation.jpg');">
            <div class="tex-panel-hero-overlay"></div>
            <div class="tex-tab-coin coin-6a" id="ker-coin">6a</div>
            <div class="tex-panel-hero-content">
              <h2 id="ker-title">Munnar <em>2N/3D</em><br><span style="font-family:'Inter',sans-serif;font-size:0.55em;opacity:0.8;font-weight:500;">ಮುನ್ನಾರ್ <em style="color:#FFD580;font-style:normal;">೨ರಾ/೩ಹ</em></span></h2>
              <p id="ker-desc">Escape into the endless tea plantations and misty mountains of Munnar.<br><span style="font-size:0.9em;opacity:0.75;">ಮುನ್ನಾರ್‌ನ ಚಹಾ ತೋಟಗಳು ಮತ್ತು ಮಂಜಿನ ಬೆಟ್ಟಗಳ ಸೌಂದರ್ಯವನ್ನು ಸವಿಯಿರಿ.</span></p>
              <div class="tex-place-tags" id="ker-tags">
                <span class="tex-place-tag">🍃 Tea Gardens · ಚಹಾ ತೋಟಗಳು</span>
                <span class="tex-place-tag">⛰️ Mattupetty Dam · ಮಾಟ್ಟುಪೆಟ್ಟಿ ಆಣೆಕಟ್ಟು</span>
                <span class="tex-place-tag">🌺 Echo Point · ಎಕೋ ಪಾಯಿಂಟ್</span>
              </div>
            </div>
          </div>
          <div class="tex-sub-tabs">
            <div class="tex-sub-tab tex-sub-active" onclick="selectKerRoute(this,1)">
              <div class="tex-sub-icon">🍃</div>
              <div class="tex-sub-info">
                <strong>Munnar 2N/3D<br><span style="font-size:0.85em;color:#FFD580;font-weight:500;">ಮುನ್ನಾರ್ ೨ರಾ/೩ಹ</span></strong>
              </div>
              <div style="position:absolute;bottom:8px;right:10px;width:24px;height:24px;border-radius:50%;background:rgba(255,180,60,0.85);color:#1a0f07;font-size:10px;font-weight:900;display:flex;align-items:center;justify-content:center;box-shadow:0 2px 8px rgba(0,0,0,0.4);">6a</div>
            </div>
            <div class="tex-sub-tab" onclick="selectKerRoute(this,2)">
              <div class="tex-sub-icon">🐘</div>
              <div class="tex-sub-info">
                <strong>Wayanad 1N/2D & 2N/3D<br><span style="font-size:0.85em;color:#FFD580;font-weight:500;">ವಯನಾಡ್ ೧ರಾ/೨ಹ & ೨ರಾ/೩ಹ</span></strong>
              </div>
              <div style="position:absolute;bottom:8px;right:10px;width:24px;height:24px;border-radius:50%;background:rgba(100,180,255,0.85);color:#0a1528;font-size:10px;font-weight:900;display:flex;align-items:center;justify-content:center;box-shadow:0 2px 8px rgba(0,0,0,0.4);">6b</div>
            </div>
            <div class="tex-sub-tab" onclick="selectKerRoute(this,3)">
              <div class="tex-sub-icon">🐅</div>
              <div class="tex-sub-info">
                <strong>Munnar - Thekkady 2N/3D<br><span style="font-size:0.85em;color:#FFD580;font-weight:500;">ಮುನ್ನಾರ್ - ತೆಕ್ಕಡಿ ೨ರಾ/೩ಹ</span></strong>
              </div>
              <div style="position:absolute;bottom:8px;right:10px;width:24px;height:24px;border-radius:50%;background:rgba(80,200,140,0.85);color:#051a10;font-size:10px;font-weight:900;display:flex;align-items:center;justify-content:center;box-shadow:0 2px 8px rgba(0,0,0,0.4);">6c</div>
            </div>
            <div class="tex-sub-tab" onclick="selectKerRoute(this,4)">
              <div class="tex-sub-icon">⛵</div>
              <div class="tex-sub-info">
                <strong>Munnar Thekkady Alleppey 3N/4D & 4N/5D<br><span style="font-size:0.85em;color:#FFD580;font-weight:500;">ಮುನ್ನಾರ್ ತೆಕ್ಕಡಿ ಅಲೆಪ್ಪಿ ೩ರಾ/೪ಹ & ೪ರಾ/೫ಹ</span></strong>
              </div>
              <div style="position:absolute;bottom:8px;right:10px;width:24px;height:24px;border-radius:50%;background:rgba(255,180,60,0.85);color:#1a0f07;font-size:10px;font-weight:900;display:flex;align-items:center;justify-content:center;box-shadow:0 2px 8px rgba(0,0,0,0.4);">6d</div>
            </div>
            <div class="tex-sub-tab" onclick="selectKerRoute(this,5)">
              <div class="tex-sub-icon">🛶</div>
              <div class="tex-sub-info">
                <strong>Munnar - Alleppey 2N/3D & 3N/4D<br><span style="font-size:0.85em;color:#FFD580;font-weight:500;">ಮುನ್ನಾರ್ - ಅಲೆಪ್ಪಿ ೨ರಾ/೩ಹ & ೩ರಾ/೪ಹ</span></strong>
              </div>
              <div style="position:absolute;bottom:8px;right:10px;width:24px;height:24px;border-radius:50%;background:rgba(100,180,255,0.85);color:#0a1528;font-size:10px;font-weight:900;display:flex;align-items:center;justify-content:center;box-shadow:0 2px 8px rgba(0,0,0,0.4);">6e</div>
            </div>
            <div class="tex-sub-tab" onclick="selectKerRoute(this,6)">
              <div class="tex-sub-icon">🏖️</div>
              <div class="tex-sub-info">
                <strong>Munnar Alleppey Kovalam 4N/5D<br><span style="font-size:0.85em;color:#FFD580;font-weight:500;">ಮುನ್ನಾರ್ ಅಲೆಪ್ಪಿ ಕೋವಲಂ ೪ರಾ/೫ಹ</span></strong>
              </div>
              <div style="position:absolute;bottom:8px;right:10px;width:24px;height:24px;border-radius:50%;background:rgba(80,200,140,0.85);color:#051a10;font-size:10px;font-weight:900;display:flex;align-items:center;justify-content:center;box-shadow:0 2px 8px rgba(0,0,0,0.4);">6f</div>
            </div>
            <div class="tex-sub-tab" onclick="selectKerRoute(this,7)">
              <div class="tex-sub-icon">🌴</div>
              <div class="tex-sub-info">
                <strong>Munnar Thekkady Alleppey Trivandrum 5N/6D<br><span style="font-size:0.85em;color:#FFD580;font-weight:500;">ಮುನ್ನಾರ್ ತೆಕ್ಕಡಿ ಅಲೆಪ್ಪಿ ತಿರುವನಂತಪುರಂ ೫ರಾ/೬ಹ</span></strong>
              </div>
              <div style="position:absolute;bottom:8px;right:10px;width:24px;height:24px;border-radius:50%;background:rgba(255,180,60,0.85);color:#1a0f07;font-size:10px;font-weight:900;display:flex;align-items:center;justify-content:center;box-shadow:0 2px 8px rgba(0,0,0,0.4);">6g</div>
            </div>
            <div class="tex-sub-tab" onclick="selectKerRoute(this,8)">
              <div class="tex-sub-icon">🛕</div>
              <div class="tex-sub-info">
                <strong>Trivandrum 1N/2D<br><span style="font-size:0.85em;color:#FFD580;font-weight:500;">ತಿರುವನಂತಪುರಂ ೧ರಾ/೨ಹ</span></strong>
              </div>
              <div style="position:absolute;bottom:8px;right:10px;width:24px;height:24px;border-radius:50%;background:rgba(100,180,255,0.85);color:#0a1528;font-size:10px;font-weight:900;display:flex;align-items:center;justify-content:center;box-shadow:0 2px 8px rgba(0,0,0,0.4);">6h</div>
            </div>
            <div class="tex-sub-tab" onclick="selectKerRoute(this,9)">
              <div class="tex-sub-icon">🌊</div>
              <div class="tex-sub-info">
                <strong>Trivandrum - Kanyakumari 2N/3D<br><span style="font-size:0.85em;color:#FFD580;font-weight:500;">ತಿರುವನಂತಪುರಂ - ಕನ್ಯಾಕುಮಾರಿ ೨ರಾ/೩ಹ</span></strong>
              </div>
              <div style="position:absolute;bottom:8px;right:10px;width:24px;height:24px;border-radius:50%;background:rgba(80,200,140,0.85);color:#051a10;font-size:10px;font-weight:900;display:flex;align-items:center;justify-content:center;box-shadow:0 2px 8px rgba(0,0,0,0.4);">6i</div>
            </div>
          </div>
        </div>
      </div>
    </div>
`;

const jsToAdd = `
const kerRoutes = {
  1: {
    img: 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Munnar_hillstation.jpg/800px-Munnar_hillstation.jpg',
    title: 'Munnar <em>2N/3D</em><br><span style="font-family:\\'Inter\\',sans-serif;font-size:0.55em;opacity:0.8;font-weight:500;">ಮುನ್ನಾರ್ <em style="color:#FFD580;font-style:normal;">೨ರಾ/೩ಹ</em></span>',
    desc: 'Escape into the endless tea plantations and misty mountains of Munnar.<br><span style="font-size:0.9em;opacity:0.75;">ಮುನ್ನಾರ್‌ನ ಚಹಾ ತೋಟಗಳು ಮತ್ತು ಮಂಜಿನ ಬೆಟ್ಟಗಳ ಸೌಂದರ್ಯವನ್ನು ಸವಿಯಿರಿ.</span>',
    tags: '🍃 Tea Gardens · ಚಹಾ ತೋಟಗಳು|⛰️ Mattupetty Dam · ಮಾಟ್ಟುಪೆಟ್ಟಿ ಆಣೆಕಟ್ಟು|🌺 Echo Point · ಎಕೋ ಪಾಯಿಂಟ್'
  },
  2: {
    img: 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/66/Edakkal_Caves.jpg/800px-Edakkal_Caves.jpg',
    title: 'Wayanad <em>1N/2D & 2N/3D</em><br><span style="font-family:\\'Inter\\',sans-serif;font-size:0.55em;opacity:0.8;font-weight:500;">ವಯನಾಡ್ <em style="color:#FFD580;font-style:normal;">೧ರಾ/೨ಹ & ೨ರಾ/೩ಹ</em></span>',
    desc: 'A nature lover\\'s paradise featuring ancient caves, waterfalls, and wildlife.<br><span style="font-size:0.9em;opacity:0.75;">ಪ್ರಾಚೀನ ಗುಹೆಗಳು, ಜಲಪಾತಗಳು ಮತ್ತು ವನ್ಯಜೀವಿಗಳ ಪ್ರಕೃತಿ ಪ್ರೇಮಿಗಳ ಸ್ವರ್ಗ.</span>',
    tags: '🐘 Wayanad Wildlife · ವಯನಾಡ್ ವನ್ಯಜೀವಿ|⛰️ Edakkal Caves · ಎಡಕಲ್ ಗುಹೆಗಳು|🌊 Soochipara Falls · ಸೂಚಿಪಾರ ಜಲಪಾತ'
  },
  3: {
    img: 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Periyar_National_Park.jpg/800px-Periyar_National_Park.jpg',
    title: 'Munnar - Thekkady <em>2N/3D</em><br><span style="font-family:\\'Inter\\',sans-serif;font-size:0.55em;opacity:0.8;font-weight:500;">ಮುನ್ನಾರ್ - ತೆಕ್ಕಡಿ <em style="color:#FFD580;font-style:normal;">೨ರಾ/೩ಹ</em></span>',
    desc: 'Combine the hills of Munnar with the thrilling wildlife of Thekkady.<br><span style="font-size:0.9em;opacity:0.75;">ಮುನ್ನಾರ್‌ನ ಬೆಟ್ಟಗಳು ಮತ್ತು ತೆಕ್ಕಡಿಯ ವನ್ಯಜೀವಿಗಳ ಅದ್ಭುತ ಸಂಗಮ.</span>',
    tags: '🍃 Tea Gardens · ಚಹಾ ತೋಟಗಳು|🐅 Periyar Wildlife · ಪೆರಿಯಾರ್ ವನ್ಯಜೀವಿ|🐘 Elephant Ride · ಆನೆ ಸವಾರಿ'
  },
  4: {
    img: 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Alleppey_Houseboat.jpg/800px-Alleppey_Houseboat.jpg',
    title: 'Munnar Thekkady Alleppey <em>3N/4D & 4N/5D</em><br><span style="font-family:\\'Inter\\',sans-serif;font-size:0.55em;opacity:0.8;font-weight:500;">ಮುನ್ನಾರ್ ತೆಕ್ಕಡಿ ಅಲೆಪ್ಪಿ <em style="color:#FFD580;font-style:normal;">೩ರಾ/೪ಹ & ೪ರಾ/೫ಹ</em></span>',
    desc: 'The complete Kerala triangle from hills to wildlife and serene backwaters.<br><span style="font-size:0.9em;opacity:0.75;">ಬೆಟ್ಟಗಳು, ವನ್ಯಜೀವಿ ಮತ್ತು ಹಿನ್ನೀರಿನ ಸಂಪೂರ್ಣ ಕೇರಳ ತ್ರಿಕೋನ ಪ್ರವಾಸ.</span>',
    tags: '🍃 Tea Gardens · ಚಹಾ ತೋಟಗಳು|🐅 Periyar Wildlife · ಪೆರಿಯಾರ್ ವನ್ಯಜೀವಿ|⛵ Houseboat · ಹೌಸ್‌ಬೋಟ್'
  },
  5: {
    img: 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Kerala_Backwaters.jpg/800px-Kerala_Backwaters.jpg',
    title: 'Munnar - Alleppey <em>2N/3D & 3N/4D</em><br><span style="font-family:\\'Inter\\',sans-serif;font-size:0.55em;opacity:0.8;font-weight:500;">ಮುನ್ನಾರ್ - ಅಲೆಪ್ಪಿ <em style="color:#FFD580;font-style:normal;">೨ರಾ/೩ಹ & ೩ರಾ/೪ಹ</em></span>',
    desc: 'A romantic escape pairing misty mountains with tranquil backwater cruising.<br><span style="font-size:0.9em;opacity:0.75;">ಮಂಜಿನ ಬೆಟ್ಟಗಳು ಮತ್ತು ಪ್ರಶಾಂತ ಹಿನ್ನೀರಿನ ವಿಹಾರದ ಸುಂದರ ಪ್ರವಾಸ.</span>',
    tags: '⛰️ Munnar Hills · ಮುನ್ನಾರ್ ಬೆಟ್ಟಗಳು|🛶 Backwaters · ಹಿನ್ನೀರು|⛵ Houseboat · ಹೌಸ್‌ಬೋಟ್'
  },
  6: {
    img: 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Kovalam_Beach.jpg/800px-Kovalam_Beach.jpg',
    title: 'Munnar Alleppey Kovalam <em>4N/5D</em><br><span style="font-family:\\'Inter\\',sans-serif;font-size:0.55em;opacity:0.8;font-weight:500;">ಮುನ್ನಾರ್ ಅಲೆಪ್ಪಿ ಕೋವಲಂ <em style="color:#FFD580;font-style:normal;">೪ರಾ/೫ಹ</em></span>',
    desc: 'Hills, backwaters, and beaches – experience the finest diversity of Kerala.<br><span style="font-size:0.9em;opacity:0.75;">ಬೆಟ್ಟಗಳು, ಹಿನ್ನೀರು ಮತ್ತು ಕಡಲತೀರಗಳು – ಕೇರಳದ ಅತ್ಯುತ್ತಮ ವೈವಿಧ್ಯಮಯ ಅನುಭವ.</span>',
    tags: '🍃 Tea Gardens · ಚಹಾ ತೋಟಗಳು|⛵ Houseboat · ಹೌಸ್‌ಬೋಟ್|🏖️ Kovalam Beach · ಕೋವಲಂ ಕಡಲತೀರ'
  },
  7: {
    img: 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Padmanabhaswamy_Temple_Trivandrum.jpg/800px-Padmanabhaswamy_Temple_Trivandrum.jpg',
    title: 'Munnar Thekkady Alleppey Trivandrum <em>5N/6D</em><br><span style="font-family:\\'Inter\\',sans-serif;font-size:0.55em;opacity:0.8;font-weight:500;">ಮುನ್ನಾರ್ ತೆಕ್ಕಡಿ ಅಲೆಪ್ಪಿ ತಿರುವನಂತಪುರಂ <em style="color:#FFD580;font-style:normal;">೫ರಾ/೬ಹ</em></span>',
    desc: 'The grand Kerala expedition ending with the cultural heritage of Trivandrum.<br><span style="font-size:0.9em;opacity:0.75;">ತಿರುವನಂತಪುರಂನ ಸಾಂಸ್ಕೃತಿಕ ಪರಂಪರೆಯೊಂದಿಗೆ ಅಂತ್ಯಗೊಳ್ಳುವ ಭವ್ಯ ಕೇರಳ ಪ್ರವಾಸ.</span>',
    tags: '⛵ Houseboat · ಹೌಸ್‌ಬೋಟ್|🏖️ Kovalam Beach · ಕೋವಲಂ ಕಡಲತೀರ|🛕 Padmanabhaswamy · ಪದ್ಮನಾಭಸ್ವಾಮಿ'
  },
  8: {
    img: 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Napier_Museum_Trivandrum.jpg/800px-Napier_Museum_Trivandrum.jpg',
    title: 'Trivandrum <em>1N/2D</em><br><span style="font-family:\\'Inter\\',sans-serif;font-size:0.55em;opacity:0.8;font-weight:500;">ತಿರುವನಂತಪುರಂ <em style="color:#FFD580;font-style:normal;">೧ರಾ/೨ಹ</em></span>',
    desc: 'Discover the rich history, museums, and temples of Kerala\\'s capital city.<br><span style="font-size:0.9em;opacity:0.75;">ಕೇರಳದ ರಾಜಧಾನಿಯ ಶ್ರೀಮಂತ ಇತಿಹಾಸ, ವಸ್ತುಸಂಗ್ರಹಾಲಯಗಳು ಮತ್ತು ದೇವಾಲಯಗಳ ದರ್ಶನ.</span>',
    tags: '🛕 Padmanabhaswamy · ಪದ್ಮನಾಭಸ್ವಾಮಿ|🏛️ Napier Museum · ನೇಪಿಯರ್ ಮ್ಯೂಸಿಯಂ|🏖️ Kovalam Beach · ಕೋವಲಂ ಕಡಲತೀರ'
  },
  9: {
    img: 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Vivekananda_Rock_Memorial.jpg/800px-Vivekananda_Rock_Memorial.jpg',
    title: 'Trivandrum - Kanyakumari <em>2N/3D</em><br><span style="font-family:\\'Inter\\',sans-serif;font-size:0.55em;opacity:0.8;font-weight:500;">ತಿರುವನಂತಪುರಂ - ಕನ್ಯಾಕುಮಾರಿ <em style="color:#FFD580;font-style:normal;">೨ರಾ/೩ಹ</em></span>',
    desc: 'From the capital of Kerala to the majestic southern tip of India.<br><span style="font-size:0.9em;opacity:0.75;">ಕೇರಳದ ರಾಜಧಾನಿಯಿಂದ ಭಾರತದ ಭವ್ಯ ದಕ್ಷಿಣ ತುದಿಯವರೆಗಿನ ಪ್ರವಾಸ.</span>',
    tags: '🛕 Padmanabhaswamy · ಪದ್ಮನಾಭಸ್ವಾಮಿ|🌊 Vivekananda Rock · ವಿವೇಕಾನಂದ ರಾಕ್|🌅 Sunset Point · ಸೂರ್ಯಾಸ್ತ ವೀಕ್ಷಣೆ'
  }
};
function selectKerRoute(tab, num) {
  document.querySelectorAll('#pkg-ker .tex-sub-tab').forEach(t => t.classList.remove('tex-sub-active'));
  tab.classList.add('tex-sub-active');
  const r = kerRoutes[num];
  document.getElementById('ker-hero').style.backgroundImage = \`url('\${r.img}')\`;
  document.getElementById('ker-title').innerHTML = r.title;
  document.getElementById('ker-desc').innerHTML = r.desc;
  document.getElementById('ker-tags').innerHTML = r.tags.split('|').map(t => \`<span class="tex-place-tag">\${t}</span>\`).join('');
  const coin = document.getElementById('ker-coin');
  const coinMap = {1:'6a',2:'6b',3:'6c',4:'6d',5:'6e',6:'6f',7:'6g',8:'6h',9:'6i'};
  const coinClass = {1:'coin-6a',2:'coin-6b',3:'coin-6c',4:'coin-6d',5:'coin-6e',6:'coin-6f',7:'coin-6g',8:'coin-6h',9:'coin-6i'};
  if(coin){ coin.textContent = coinMap[num]; coin.className = 'tex-tab-coin ' + coinClass[num]; }
}
`;

html = html.replace('.tex-tab-coin.coin-5j { background: rgba(255,180,60,0.85); color: #1a0f07; }', '.tex-tab-coin.coin-5j { background: rgba(255,180,60,0.85); color: #1a0f07; }\n' + cssToAdd);
html = html.replace('<!-- Tour 3 -->', htmlToAdd + '\n    <!-- Tour 3 -->');
html = html.replace('</script>\n</body>', jsToAdd + '\n</script>\n</body>');

fs.writeFileSync('index.html', html);
console.log('Appended Kerala widget');
