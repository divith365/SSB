
/* Tour Explorer JS */
function selectTexPackage(item, panelId) {
  const explorer = item.closest('.tour-explorer');
  explorer.querySelectorAll('.tex-menu-item').forEach(i => i.classList.remove('tex-active'));
  item.classList.add('tex-active');
  explorer.querySelectorAll('.tex-panel').forEach(p => p.classList.remove('tex-panel-active'));
  document.getElementById(panelId).classList.add('tex-panel-active');
}

function selectBlrSub(tab, type) {
  document.querySelectorAll('#pkg-blr .tex-sub-tab').forEach(t => t.classList.remove('tex-sub-active'));
  tab.classList.add('tex-sub-active');
  const hero = document.getElementById('blr-hero');
  const title = hero.querySelector('h2');
  const desc = document.getElementById('blr-desc');
  const tags = document.getElementById('blr-tags');
  const coin = document.getElementById('blr-coin');
  if (type === 'half') {
    hero.style.backgroundImage = "url('https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Vidhana_Soudha_Bangalore_India.jpg/800px-Vidhana_Soudha_Bangalore_India.jpg')";
    title.innerHTML = 'Bangalore <em>Half Day</em> Package<br><span style="font-family:\'Inter\', sans-serif;font-size:0.55em;opacity:0.9;font-weight:500;">ಬೆಂಗಳೂರು <em style="color:#FFD580;font-style:normal;">ಅರ್ಧ ದಿನ</em> ಪ್ಯಾಕೇಜ್</span>';
    desc.innerHTML = 'A curated morning or evening tour covering Bangalore\'s must-see landmarks.<br><span style="font-size:0.9em;opacity:0.75;">ಬೆಂಗಳೂರಿನ ಪ್ರಮುಖ ತಾಣಗಳ ವಿಶೇಷ ದರ್ಶನ.</span>';
    tags.innerHTML = '<span class="tex-place-tag">🛕 Bull Temple · ದೊಡ್ಡ ಗಣಪತಿ</span><span class="tex-place-tag">🌳 Lalbagh · ಲಾಲ್‌ಬಾಗ್</span><span class="tex-place-tag">🏛️ Vidhana Soudha · ವಿಧಾನ ಸೌಧ</span><span class="tex-place-tag">🌿 Cubbon Park · ಕಬ್ಬನ್ ಪಾರ್ಕ್</span>';
    if(coin){ coin.textContent='1a'; coin.className='tex-tab-coin coin-1a'; }
  } else {
    hero.style.backgroundImage = "url('https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/ISKCON_Bangalore.jpg/800px-ISKCON_Bangalore.jpg')";
    title.innerHTML = 'Bangalore <em>Full Day</em> Package<br><span style="font-family:\'Inter\', sans-serif;font-size:0.55em;opacity:0.9;font-weight:500;">ಬೆಂಗಳೂರು <em style="color:#FFD580;font-style:normal;">ಪೂರ್ಣ ದಿನ</em> ಪ್ಯಾಕೇಜ್</span>';
    desc.innerHTML = 'An all-day journey through the Garden City\'s heritage, culture & spiritual sites.<br><span style="font-size:0.9em;opacity:0.75;">ತೋಟಗಳ ನಗರದ ಐತಿಹಾಸಿಕ, ಸಾಂಸ್ಕೃತಿಕ ಮತ್ತು ಆಧ್ಯಾತ್ಮಿಕ ತಾಣಗಳ ಪೂರ್ಣ ದಿನದ ಪ್ರವಾಸ.</span>';
    tags.innerHTML = '<span class="tex-place-tag">🛕 ISKCON Temple · ಇಸ್ಕಾನ್</span><span class="tex-place-tag">🏰 Tippu Palace · ಟಿಪ್ಪು ಅರಮನೆ</span><span class="tex-place-tag">🌳 Lalbagh · ಲಾಲ್‌ಬಾಗ್</span><span class="tex-place-tag">🏛️ Vidhana Soudha · ವಿಧಾನ ಸೌಧ</span><span class="tex-place-tag">⛪ St. Mark\'s · ಸೆಂಟ್ ಮಾರ್ಕ್ಸ್</span>';
    if(coin){ coin.textContent='1b'; coin.className='tex-tab-coin coin-1b'; }
  }
}

const cabRoutes = {
  1: {
    img: 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/Halebeedu_DSW.jpg/800px-Halebeedu_DSW.jpg',
    title: '<em>Heritage</em> Circuit<br><span style="font-family:\'Inter\',sans-serif;font-size:0.55em;opacity:0.8;font-weight:500;"><em style="color:#FFD580;font-style:normal;">ಐತಿಹಾಸಿಕ</em> ಸರ್ಕಿಟ್</span>',
    desc: 'Trace ancient Karnataka\'s golden age through its timeless temples and shrines.<br><span style="font-size:0.9em;opacity:0.75;">ಪ್ರಾಚೀನ ಕರ್ನಾಟಕದ ಸ್ವರ್ಣಯುಗದ ದೇವಾಲಯಗಳ ಮತ್ತು ಪೂಜಾ ಸ್ಥಳಗಳ ದರ್ಶನ.</span>',
    tags: '🛕 Yediyuru · ಯೇದಿಯೂರು|🛕 Adichunchanagiri · ಆದಿಚುಂಚನಗಿರಿ|🕌 Sravanabelagola · ಶ್ರವಣಬೆಳಗೊಳ|🏛️ Belur · ಬೇಲೂರು|🏛️ Halebeedu · ಹಳೇಬೀಡು'
  },
  2: {
    img: 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Nandi_Hills_Sunrise.jpg/800px-Nandi_Hills_Sunrise.jpg',
    title: '<em>Hills & Nature</em> Circuit<br><span style="font-family:\'Inter\',sans-serif;font-size:0.55em;opacity:0.8;font-weight:500;"><em style="color:#FFD580;font-style:normal;">ಬೆಟ್ಟ ಮತ್ತು ಪ್ರಕೃತಿ</em> ಸರ್ಕಿಟ್</span>',
    desc: 'Sunrise, hilltop shrines and serene nature — a refreshing escape from the city.<br><span style="font-size:0.9em;opacity:0.75;">ಸೂರ್ಯೋದಯ, ಬೆಟ್ಟದ ದೇವಾಲಯಗಳು ಮತ್ತು ಪ್ರಶಾಂತ ಪ್ರಕೃತಿ — ನಗರದಿಂದ ಮನೋಲ್ಲಾಸದ ಪ್ರಯಾಣ.</span>',
    tags: '⛰️ Siddagange · ಸಿದ್ಧಗಂಗೆ|🌄 Shivagange · ಶಿವಗಂಗೆ|💧 Namadachilume · ನಾಮದಚಿಲುಮೆ|⛰️ Mandaragiri Hills · ಮಂದರಗಿರಿ|🛕 Goravanahalli Laxmi · ಗೊರವನಹಳ್ಳಿ ಲಕ್ಷ್ಮಿ'
  },
  3: {
    img: 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/Shivanasamudra_Falls.jpg/800px-Shivanasamudra_Falls.jpg',
    title: '<em>Riverside</em> Circuit<br><span style="font-family:\'Inter\',sans-serif;font-size:0.55em;opacity:0.8;font-weight:500;"><em style="color:#FFD580;font-style:normal;">ನದಿ ತಟ</em> ಸರ್ಕಿಟ್</span>',
    desc: 'Rivers, waterfalls, ancient temples and the mystic sands of Talakadu.<br><span style="font-size:0.9em;opacity:0.75;">ನದಿಗಳು, ಜಲಪಾತಗಳು, ಪ್ರಾಚೀನ ದೇವಾಲಯಗಳು ಮತ್ತು ತಲಕಾಡಿನ ರಹಸ್ಯಮಯ ಮರಳು.</span>',
    tags: '🏰 Srirangapatna · ಶ್ರೀರಂಗಪಟ್ಟಣ|💧 Shivanasamudra Bluff · ಶಿವನಸಮುದ್ರ|🛕 Somanatha Temple · ಸೋಮನಾಥ ದೇವಾಲಯ|🏖️ Talakadu · ತಲಕಾಡು'
  }
};
function selectCabRoute(tab, num) {
  document.querySelectorAll('#pkg-cab .tex-sub-tab').forEach(t => t.classList.remove('tex-sub-active'));
  tab.classList.add('tex-sub-active');
  const r = cabRoutes[num];
  document.getElementById('cab-hero').style.backgroundImage = `url('${r.img}')`;
  document.getElementById('cab-title').innerHTML = r.title;
  document.getElementById('cab-desc').innerHTML = r.desc;
  document.getElementById('cab-tags').innerHTML = r.tags.split('|').map(t => `<span class="tex-place-tag">${t}</span>`).join('');
  const coin = document.getElementById('cab-coin');
  const coinMap = {1:'2a',2:'2b',3:'2c'};
  const coinClass = {1:'coin-2a',2:'coin-2b',3:'coin-2c'};
  if(coin){ coin.textContent = coinMap[num]; coin.className = 'tex-tab-coin ' + coinClass[num]; }
}

const chkRoutes = {
  1: {
    img: 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Mullayanagiri_Peak.jpg/800px-Mullayanagiri_Peak.jpg',
    title: 'Chikkamagalur <em>1N/2D</em><br><span style="font-family:\'Inter\',sans-serif;font-size:0.55em;opacity:0.8;font-weight:500;">ಚಿಕ್ಕಮಗಳೂರು <em style="color:#FFD580;font-style:normal;">೧ರಾ/೨ಹ</em></span>',
    desc: 'A perfect short getaway into the coffee land of Karnataka.<br><span style="font-size:0.9em;opacity:0.75;">ಕರ್ನಾಟಕದ ಕಾಫಿ ನಾಡಿಗೆ ಒಂದು ಅದ್ಭುತ ಕಿರು ಪ್ರವಾಸ.</span>',
    tags: '⛰️ Mullayanagiri · ಮುಳ್ಳಯ್ಯನಗಿರಿ|🌿 Baba Budangiri · ಬಾಬಾ ಬುಡನ್‌ಗಿರಿ|🌊 Jhari Falls · ಝರಿ ಜಲಪಾತ'
  },
  2: {
    img: 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Kudremukh_Peak.jpg/800px-Kudremukh_Peak.jpg',
    title: 'Chikkamagalur <em>2N/3D</em><br><span style="font-family:\'Inter\',sans-serif;font-size:0.55em;opacity:0.8;font-weight:500;">ಚಿಕ್ಕಮಗಳೂರು <em style="color:#FFD580;font-style:normal;">೨ರಾ/೩ಹ</em></span>',
    desc: 'An extended retreat to explore the majestic Western Ghats in full.<br><span style="font-size:0.9em;opacity:0.75;">ಪಶ್ಚಿಮ ಘಟ್ಟಗಳ ಸೌಂದರ್ಯವನ್ನು ಸವಿಯಲು ಸುದೀರ್ಘ ಪ್ರವಾಸ.</span>',
    tags: '⛰️ Mullayanagiri · ಮುಳ್ಳಯ್ಯನಗಿರಿ|🌿 Kemmangundi · ಕೆಮ್ಮಣ್ಣುಗುಂಡಿ|🐅 Bhadra Wildlife · ಭದ್ರಾ ವನ್ಯಜೀವಿ|🌊 Hebbe Falls · ಹೆಬ್ಬೆ ಜಲಪಾತ'
  },
  3: {
    img: 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Sringeri_Vidyashankara_Temple.jpg/800px-Sringeri_Vidyashankara_Temple.jpg',
    title: '<em>Chikkamagalur - Horanadu Sringeri Kalasa</em><br><span style="font-family:\'Inter\',sans-serif;font-size:0.55em;opacity:0.8;font-weight:500;"><em style="color:#FFD580;font-style:normal;">ಚಿಕ್ಕಮಗಳೂರು - ಹೊರನಾಡು ಶೃಂಗೇರಿ ಕಳಸ</em></span>',
    desc: 'A spiritual journey covering the most revered temple towns of Chikkamagalur district.<br><span style="font-size:0.9em;opacity:0.75;">ಚಿಕ್ಕಮಗಳೂರಿನ ಪ್ರಸಿದ್ಧ ಪುಣ್ಯಕ್ಷೇತ್ರಗಳ ಪವಿತ್ರ ದರ್ಶನ.</span>',
    tags: '🛕 Horanadu · ಹೊರನಾಡು|🛕 Sringeri · ಶೃಂಗೇರಿ|🛕 Kalasa · ಕಳಸ|⛰️ Kudremukh · ಕುದುರೆಮುಖ'
  }
};
function selectChkRoute(tab, num) {
  document.querySelectorAll('#pkg-chk .tex-sub-tab').forEach(t => t.classList.remove('tex-sub-active'));
  tab.classList.add('tex-sub-active');
  const r = chkRoutes[num];
  document.getElementById('chk-hero').style.backgroundImage = `url('${r.img}')`;
  document.getElementById('chk-title').innerHTML = r.title;
  document.getElementById('chk-desc').innerHTML = r.desc;
  document.getElementById('chk-tags').innerHTML = r.tags.split('|').map(t => `<span class="tex-place-tag">${t}</span>`).join('');
  const coin = document.getElementById('chk-coin');
  const coinMap = {1:'3a',2:'3b',3:'3c'};
  const coinClass = {1:'coin-3a',2:'coin-3b',3:'coin-3c'};
  if(coin){ coin.textContent = coinMap[num]; coin.className = 'tex-tab-coin ' + coinClass[num]; }
}

const crgRoutes = {
  1: {
    img: 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Abbey_Falls_Kodagu.jpg/800px-Abbey_Falls_Kodagu.jpg',
    title: 'Coorg <em>1N/2D & 2N/3D</em><br><span style="font-family:\'Inter\',sans-serif;font-size:0.55em;opacity:0.8;font-weight:500;">ಕೂರ್ಗ್ <em style="color:#FFD580;font-style:normal;">೧ರಾ/೨ಹ & ೨ರಾ/೩ಹ</em></span>',
    desc: 'Escape to the Scotland of India for misty hills and lush coffee estates.<br><span style="font-size:0.9em;opacity:0.75;">ಭಾರತದ ಸ್ಕಾಟ್‌ಲ್ಯಾಂಡ್ ಮಂಜಿನ ಬೆಟ್ಟಗಳು ಮತ್ತು ಕಾಫಿ ತೋಟಗಳ ಅದ್ಭುತ ಪ್ರವಾಸ.</span>',
    tags: '🌊 Abbey Falls · ಅಬ್ಬೆ ಜಲಪಾತ|🐘 Dubare · ದುಬಾರೆ|🌅 Raja\'s Seat · ರಾಜಾ ಸೀಟ್|🛕 Omkareshwara · ಓಂಕಾರೇಶ್ವರ|🕉️ Talakaveri · ತಲಕಾವೇರಿ'
  },
  2: {
    img: 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Nandi_Hills_Sunrise.jpg/800px-Nandi_Hills_Sunrise.jpg',
    title: 'Coorg - Chikkamagalur <em>2N/3D & 3N/4D</em><br><span style="font-family:\'Inter\',sans-serif;font-size:0.55em;opacity:0.8;font-weight:500;">ಕೂರ್ಗ್ - ಚಿಕ್ಕಮಗಳೂರು <em style="color:#FFD580;font-style:normal;">೨ರಾ/೩ಹ & ೩ರಾ/೪ಹ</em></span>',
    desc: 'The ultimate Western Ghats experience covering the best of two beautiful hill stations.<br><span style="font-size:0.9em;opacity:0.75;">ಎರಡು ಸುಂದರ ಗಿರಿಧಾಮಗಳನ್ನು ಒಳಗೊಂಡ ಪಶ್ಚಿಮ ಘಟ್ಟಗಳ ಅದ್ಭುತ ಅನುಭವ.</span>',
    tags: '⛰️ Mullayanagiri · ಮುಳ್ಳಯ್ಯನಗಿರಿ|🌊 Abbey Falls · ಅಬ್ಬೆ ಜಲಪಾತ|🐘 Dubare · ದುಬಾರೆ|🌿 Kemmangundi · ಕೆಮ್ಮಣ್ಣುಗುಂಡಿ'
  }
};
function selectCrgRoute(tab, num) {
  document.querySelectorAll('#pkg-crg .tex-sub-tab').forEach(t => t.classList.remove('tex-sub-active'));
  tab.classList.add('tex-sub-active');
  const r = crgRoutes[num];
  document.getElementById('crg-hero').style.backgroundImage = `url('${r.img}')`;
  document.getElementById('crg-title').innerHTML = r.title;
  document.getElementById('crg-desc').innerHTML = r.desc;
  document.getElementById('crg-tags').innerHTML = r.tags.split('|').map(t => `<span class="tex-place-tag">${t}</span>`).join('');
  const coin = document.getElementById('crg-coin');
  const coinMap = {1:'4a',2:'4b'};
  const coinClass = {1:'coin-4a',2:'coin-4b'};
  if(coin){ coin.textContent = coinMap[num]; coin.className = 'tex-tab-coin ' + coinClass[num]; }
}

const mysRoutes = {
  1: {
    img: 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/Mysore_Palace_Morning.jpg/800px-Mysore_Palace_Morning.jpg',
    title: 'Mysore <em>Full Day Sightseeing</em><br><span style="font-family:\'Inter\',sans-serif;font-size:0.55em;opacity:0.8;font-weight:500;">ಮೈಸೂರು <em style="color:#FFD580;font-style:normal;">ಪೂರ್ಣ ದಿನದ ದರ್ಶನ</em></span>',
    desc: 'Explore the City of Palaces and its royal heritage.<br><span style="font-size:0.9em;opacity:0.75;">ಅರಮನೆಗಳ ನಗರ ಮತ್ತು ಅದರ ರಾಜಮನೆತನದ ಪರಂಪರೆಯನ್ನು ಅನ್ವೇಷಿಸಿ.</span>',
    tags: '🏰 Mysore Palace · ಮೈಸೂರು ಅರಮನೆ|🐅 Zoo · ಮೃಗಾಲಯ|🌸 Brindavan Gardens · ಬೃಂದಾವನ ಉದ್ಯಾನವನ'
  },
  2: {
    img: 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Ooty_Lake.jpg/800px-Ooty_Lake.jpg',
    title: 'Mysore - Ooty <em>1N/2D</em><br><span style="font-family:\'Inter\',sans-serif;font-size:0.55em;opacity:0.8;font-weight:500;">ಮೈಸೂರು - ಊಟಿ <em style="color:#FFD580;font-style:normal;">೧ರಾ/೨ಹ</em></span>',
    desc: 'A quick getaway combining heritage with the queen of hill stations.<br><span style="font-size:0.9em;opacity:0.75;">ಪರಂಪರೆ ಮತ್ತು ಗಿರಿಧಾಮಗಳ ರಾಣಿಯ ಅದ್ಭುತ ಸಂಗಮ.</span>',
    tags: '🏰 Mysore Palace · ಮೈಸೂರು ಅರಮನೆ|⛰️ Ooty Lake · ಊಟಿ ಸರೋವರ|🌺 Botanical Garden · ಬೊಟಾನಿಕಲ್ ಗಾರ್ಡನ್'
  },
  3: {
    img: 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Nilgiri_Mountain_Railway_Ooty.jpg/800px-Nilgiri_Mountain_Railway_Ooty.jpg',
    title: 'Mysore Ooty Coonoor <em>2N/3D</em><br><span style="font-family:\'Inter\',sans-serif;font-size:0.55em;opacity:0.8;font-weight:500;">ಮೈಸೂರು ಊಟಿ ಕೂನೂರು <em style="color:#FFD580;font-style:normal;">೨ರಾ/೩ಹ</em></span>',
    desc: 'The classic Nilgiris experience with a touch of royal Mysore.<br><span style="font-size:0.9em;opacity:0.75;">ಮೈಸೂರಿನ ರಾಜವೈಭವದೊಂದಿಗೆ ನೀಲಗಿರಿಯ ಅದ್ಭುತ ಅನುಭವ.</span>',
    tags: '🚂 Toy Train · ಟಾಯ್ ಟ್ರೈನ್|🌿 Sims Park · ಸಿಮ್ಸ್ ಪಾರ್ಕ್|⛰️ Dolphin Nose · ಡಾಲ್ಫಿನ್ ನೋಸ್'
  },
  4: {
    img: 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/Pine_Forest_Ooty.jpg/800px-Pine_Forest_Ooty.jpg',
    title: 'Mysore - Ooty Coonoor Filmy Chakkar <em>3N/4D & 4N/5D</em><br><span style="font-family:\'Inter\',sans-serif;font-size:0.55em;opacity:0.8;font-weight:500;">ಮೈಸೂರು - ಊಟಿ ಕೂನೂರು ಫಿಲ್ಮಿ ಚಕ್ಕರ್ <em style="color:#FFD580;font-style:normal;">೩ರಾ/೪ಹ & ೪ರಾ/೫ಹ</em></span>',
    desc: 'Visit iconic shooting locations hidden within the Nilgiris.<br><span style="font-size:0.9em;opacity:0.75;">ನೀಲಗಿರಿಯಲ್ಲಿರುವ ಪ್ರಸಿದ್ಧ ಸಿನಿಮಾ ಚಿತ್ರೀಕರಣ ಸ್ಥಳಗಳ ಭೇಟಿ.</span>',
    tags: '🎬 Shooting Point · ಶೂಟಿಂಗ್ ಪಾಯಿಂಟ್|🌲 Pine Forest · ಪೈನ್ ಫಾರೆಸ್ಟ್|⛰️ Dodabetta Peak · ದೊಡ್ಡಬೆಟ್ಟ'
  },
  5: {
    img: 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Kodaikanal_Lake.jpg/800px-Kodaikanal_Lake.jpg',
    title: 'Mysore - Ooty - Kodaikanal<br><span style="font-family:\'Inter\',sans-serif;font-size:0.55em;opacity:0.8;font-weight:500;">ಮೈಸೂರು - ಊಟಿ - ಕೊಡೆಕಾನಲ್</span>',
    desc: 'The ultimate Southern hill station trio for a memorable vacation.<br><span style="font-size:0.9em;opacity:0.75;">ದಕ್ಷಿಣ ಭಾರತದ ಮೂರು ಪ್ರಮುಖ ಗಿರಿಧಾಮಗಳ ಸುಂದರ ಪ್ರವಾಸ.</span>',
    tags: '⛵ Kodai Lake · ಕೊಡೆಕಾನಲ್ ಸರೋವರ|🌲 Pine Forest · ಪೈನ್ ಫಾರೆಸ್ಟ್|🪨 Pillar Rocks · ಪಿಲ್ಲರ್ ರಾಕ್ಸ್'
  },
  6: {
    img: 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/66/Edakkal_Caves.jpg/800px-Edakkal_Caves.jpg',
    title: 'Mysore Ooty Wayanad <em>5N/6D, 2N/3D, 3N/4D</em><br><span style="font-family:\'Inter\',sans-serif;font-size:0.55em;opacity:0.8;font-weight:500;">ಮೈಸೂರು ಊಟಿ ವಯನಾಡ್ <em style="color:#FFD580;font-style:normal;">೫ರಾ/೬ಹ, ೨ರಾ/೩ಹ, ೩ರಾ/೪ಹ</em></span>',
    desc: 'Explore the diverse landscapes from palaces to Nilgiris and Wayanad forests.<br><span style="font-size:0.9em;opacity:0.75;">ಅರಮನೆ, ನೀಲಗಿರಿ ಮತ್ತು ವಯನಾಡ್ ಕಾಡುಗಳ ವೈವಿಧ್ಯಮಯ ಪ್ರವಾಸ.</span>',
    tags: '🐘 Wayanad Wildlife · ವಯನಾಡ್ ವನ್ಯಜೀವಿ|⛰️ Edakkal Caves · ಎಡಕಲ್ ಗುಹೆಗಳು|🌊 Soochipara Falls · ಸೂಚಿಪಾರ ಜಲಪಾತ'
  },
  7: {
    img: 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Dubare_Elephant_Camp.jpg/800px-Dubare_Elephant_Camp.jpg',
    title: 'Mysore - Coorg <em>2N/3D & 3N/4D</em><br><span style="font-family:\'Inter\',sans-serif;font-size:0.55em;opacity:0.8;font-weight:500;">ಮೈಸೂರು - ಕೂರ್ಗ್ <em style="color:#FFD580;font-style:normal;">೨ರಾ/೩ಹ & ೩ರಾ/೪ಹ</em></span>',
    desc: 'A perfect blend of culture, wildlife, and natural beauty.<br><span style="font-size:0.9em;opacity:0.75;">ಸಂಸ್ಕೃತಿ, ವನ್ಯಜೀವಿ ಮತ್ತು ಪ್ರಕೃತಿ ಸೌಂದರ್ಯದ ಅದ್ಭುತ ಸಂಗಮ.</span>',
    tags: '🐘 Dubare Camp · ದುಬಾರೆ ಆನೆ ಶಿಬಿರ|🌊 Abbey Falls · ಅಬ್ಬೆ ಜಲಪಾತ|🏯 Golden Temple · ಸುವರ್ಣ ದೇವಾಲಯ'
  },
  8: {
    img: 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Wayanad_Banasura_Sagar_Dam.jpg/800px-Wayanad_Banasura_Sagar_Dam.jpg',
    title: 'Mysore - Coorg - Wayanad <em>5N/6D</em><br><span style="font-family:\'Inter\',sans-serif;font-size:0.55em;opacity:0.8;font-weight:500;">ಮೈಸೂರು - ಕೂರ್ಗ್ - ವಯನಾಡ್ <em style="color:#FFD580;font-style:normal;">೫ರಾ/೬ಹ</em></span>',
    desc: 'Experience the ultimate nature circuit from Coorg to the hills of Wayanad.<br><span style="font-size:0.9em;opacity:0.75;">ಕೂರ್ಗಿನಿಂದ ವಯನಾಡಿನ ಗಿರಿಧಾಮಗಳವರೆಗೆ ಪ್ರಕೃತಿಯ ಮಡಿಲಲ್ಲಿ ಅದ್ಭುತ ಪ್ರವಾಸ.</span>',
    tags: '🐘 Dubare Camp · ದುಬಾರೆ ಆನೆ ಶಿಬಿರ|🌊 Abbey Falls · ಅಬ್ಬೆ ಜಲಪಾತ|🌿 Banasura Dam · ಬಾಣಾಸುರ ಅಣೆಕಟ್ಟು'
  },
  9: {
    img: 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/66/Edakkal_Caves.jpg/800px-Edakkal_Caves.jpg',
    title: 'Mysore Wayanad <em>2N/3D & 3N/4D</em><br><span style="font-family:\'Inter\',sans-serif;font-size:0.55em;opacity:0.8;font-weight:500;">ಮೈಸೂರು ವಯನಾಡ್ <em style="color:#FFD580;font-style:normal;">೨ರಾ/೩ಹ & ೩ರಾ/೪ಹ</em></span>',
    desc: 'A quick dive into the lush green forests and caves of Wayanad.<br><span style="font-size:0.9em;opacity:0.75;">ವಯನಾಡಿನ ಹಚ್ಚ ಹಸಿರಿನ ಕಾಡುಗಳು ಮತ್ತು ಗುಹೆಗಳಿಗೆ ಒಂದು ಕಿರು ಪ್ರವಾಸ.</span>',
    tags: '⛰️ Edakkal Caves · ಎಡಕಲ್ ಗುಹೆಗಳು|🌊 Soochipara Falls · ಸೂಚಿಪಾರ ಜಲಪಾತ|🐘 Wayanad Wildlife · ವಯನಾಡ್ ವನ್ಯಜೀವಿ'
  },
  10: {
    img: 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Meenakshi_Amman_Temple_Madurai.jpg/800px-Meenakshi_Amman_Temple_Madurai.jpg',
    title: 'Mysore Ooty Kodai Madurai Rameswaram Kanyakumari <em>6N/7D & 7N/8D</em><br><span style="font-family:\'Inter\',sans-serif;font-size:0.55em;opacity:0.8;font-weight:500;">ಮೈಸೂರು ಊಟಿ ಕೊಡೆಕಾನಲ್ ಮದುರೈ ರಾಮೇಶ್ವರಂ ಕನ್ಯಾಕುಮಾರಿ <em style="color:#FFD580;font-style:normal;">೬ರಾ/೭ಹ & ೭ರಾ/೮ಹ</em></span>',
    desc: 'The ultimate Southern India grand tour from palaces to the southern tip of India.<br><span style="font-size:0.9em;opacity:0.75;">ಅರಮನೆಗಳಿಂದ ಹಿಡಿದು ಭಾರತದ ದಕ್ಷಿಣ ತುದಿಯವರೆಗಿನ ಅಂತಿಮ ಮಹಾ ಪ್ರವಾಸ.</span>',
    tags: '🛕 Madurai Meenakshi · ಮದುರೈ ಮೀನಾಕ್ಷಿ|🌊 Kanyakumari · ಕನ್ಯಾಕುಮಾರಿ|🛕 Rameswaram · ರಾಮೇಶ್ವರಂ'
  }
};
function selectMysRoute(tab, num) {
  document.querySelectorAll('#pkg-mys .tex-sub-tab').forEach(t => t.classList.remove('tex-sub-active'));
  tab.classList.add('tex-sub-active');
  const r = mysRoutes[num];
  document.getElementById('mys-hero').style.backgroundImage = `url('${r.img}')`;
  document.getElementById('mys-title').innerHTML = r.title;
  document.getElementById('mys-desc').innerHTML = r.desc;
  document.getElementById('mys-tags').innerHTML = r.tags.split('|').map(t => `<span class="tex-place-tag">${t}</span>`).join('');
  const coin = document.getElementById('mys-coin');
  const coinMap = {1:'5a',2:'5b',3:'5c',4:'5d',5:'5e',6:'5f',7:'5g',8:'5h',9:'5i',10:'5j'};
  const coinClass = {1:'coin-5a',2:'coin-5b',3:'coin-5c',4:'coin-5d',5:'coin-5e',6:'coin-5f',7:'coin-5g',8:'coin-5h',9:'coin-5i',10:'coin-5j'};
  if(coin){ coin.textContent = coinMap[num]; coin.className = 'tex-tab-coin ' + coinClass[num]; }
}


const kerRoutes = {
  1: {
    img: 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Munnar_hillstation.jpg/800px-Munnar_hillstation.jpg',
    title: 'Munnar <em>2N/3D</em><br><span style="font-family:\'Inter\',sans-serif;font-size:0.55em;opacity:0.8;font-weight:500;">ಮುನ್ನಾರ್ <em style="color:#FFD580;font-style:normal;">೨ರಾ/೩ಹ</em></span>',
    desc: 'Escape into the endless tea plantations and misty mountains of Munnar.<br><span style="font-size:0.9em;opacity:0.75;">ಮುನ್ನಾರ್‌ನ ಚಹಾ ತೋಟಗಳು ಮತ್ತು ಮಂಜಿನ ಬೆಟ್ಟಗಳ ಸೌಂದರ್ಯವನ್ನು ಸವಿಯಿರಿ.</span>',
    tags: '🍃 Tea Gardens · ಚಹಾ ತೋಟಗಳು|⛰️ Mattupetty Dam · ಮಾಟ್ಟುಪೆಟ್ಟಿ ಆಣೆಕಟ್ಟು|🌺 Echo Point · ಎಕೋ ಪಾಯಿಂಟ್'
  },
  2: {
    img: 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/66/Edakkal_Caves.jpg/800px-Edakkal_Caves.jpg',
    title: 'Wayanad <em>1N/2D & 2N/3D</em><br><span style="font-family:\'Inter\',sans-serif;font-size:0.55em;opacity:0.8;font-weight:500;">ವಯನಾಡ್ <em style="color:#FFD580;font-style:normal;">೧ರಾ/೨ಹ & ೨ರಾ/೩ಹ</em></span>',
    desc: 'A nature lover\'s paradise featuring ancient caves, waterfalls, and wildlife.<br><span style="font-size:0.9em;opacity:0.75;">ಪ್ರಾಚೀನ ಗುಹೆಗಳು, ಜಲಪಾತಗಳು ಮತ್ತು ವನ್ಯಜೀವಿಗಳ ಪ್ರಕೃತಿ ಪ್ರೇಮಿಗಳ ಸ್ವರ್ಗ.</span>',
    tags: '🐘 Wayanad Wildlife · ವಯನಾಡ್ ವನ್ಯಜೀವಿ|⛰️ Edakkal Caves · ಎಡಕಲ್ ಗುಹೆಗಳು|🌊 Soochipara Falls · ಸೂಚಿಪಾರ ಜಲಪಾತ'
  },
  3: {
    img: 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Periyar_National_Park.jpg/800px-Periyar_National_Park.jpg',
    title: 'Munnar - Thekkady <em>2N/3D</em><br><span style="font-family:\'Inter\',sans-serif;font-size:0.55em;opacity:0.8;font-weight:500;">ಮುನ್ನಾರ್ - ತೆಕ್ಕಡಿ <em style="color:#FFD580;font-style:normal;">೨ರಾ/೩ಹ</em></span>',
    desc: 'Combine the hills of Munnar with the thrilling wildlife of Thekkady.<br><span style="font-size:0.9em;opacity:0.75;">ಮುನ್ನಾರ್‌ನ ಬೆಟ್ಟಗಳು ಮತ್ತು ತೆಕ್ಕಡಿಯ ವನ್ಯಜೀವಿಗಳ ಅದ್ಭುತ ಸಂಗಮ.</span>',
    tags: '🍃 Tea Gardens · ಚಹಾ ತೋಟಗಳು|🐅 Periyar Wildlife · ಪೆರಿಯಾರ್ ವನ್ಯಜೀವಿ|🐘 Elephant Ride · ಆನೆ ಸವಾರಿ'
  },
  4: {
    img: 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Alleppey_Houseboat.jpg/800px-Alleppey_Houseboat.jpg',
    title: 'Munnar Thekkady Alleppey <em>3N/4D & 4N/5D</em><br><span style="font-family:\'Inter\',sans-serif;font-size:0.55em;opacity:0.8;font-weight:500;">ಮುನ್ನಾರ್ ತೆಕ್ಕಡಿ ಅಲೆಪ್ಪಿ <em style="color:#FFD580;font-style:normal;">೩ರಾ/೪ಹ & ೪ರಾ/೫ಹ</em></span>',
    desc: 'The complete Kerala triangle from hills to wildlife and serene backwaters.<br><span style="font-size:0.9em;opacity:0.75;">ಬೆಟ್ಟಗಳು, ವನ್ಯಜೀವಿ ಮತ್ತು ಹಿನ್ನೀರಿನ ಸಂಪೂರ್ಣ ಕೇರಳ ತ್ರಿಕೋನ ಪ್ರವಾಸ.</span>',
    tags: '🍃 Tea Gardens · ಚಹಾ ತೋಟಗಳು|🐅 Periyar Wildlife · ಪೆರಿಯಾರ್ ವನ್ಯಜೀವಿ|⛵ Houseboat · ಹೌಸ್‌ಬೋಟ್'
  },
  5: {
    img: 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Kerala_Backwaters.jpg/800px-Kerala_Backwaters.jpg',
    title: 'Munnar - Alleppey <em>2N/3D & 3N/4D</em><br><span style="font-family:\'Inter\',sans-serif;font-size:0.55em;opacity:0.8;font-weight:500;">ಮುನ್ನಾರ್ - ಅಲೆಪ್ಪಿ <em style="color:#FFD580;font-style:normal;">೨ರಾ/೩ಹ & ೩ರಾ/೪ಹ</em></span>',
    desc: 'A romantic escape pairing misty mountains with tranquil backwater cruising.<br><span style="font-size:0.9em;opacity:0.75;">ಮಂಜಿನ ಬೆಟ್ಟಗಳು ಮತ್ತು ಪ್ರಶಾಂತ ಹಿನ್ನೀರಿನ ವಿಹಾರದ ಸುಂದರ ಪ್ರವಾಸ.</span>',
    tags: '⛰️ Munnar Hills · ಮುನ್ನಾರ್ ಬೆಟ್ಟಗಳು|🛶 Backwaters · ಹಿನ್ನೀರು|⛵ Houseboat · ಹೌಸ್‌ಬೋಟ್'
  },
  6: {
    img: 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Kovalam_Beach.jpg/800px-Kovalam_Beach.jpg',
    title: 'Munnar Alleppey Kovalam <em>4N/5D</em><br><span style="font-family:\'Inter\',sans-serif;font-size:0.55em;opacity:0.8;font-weight:500;">ಮುನ್ನಾರ್ ಅಲೆಪ್ಪಿ ಕೋವಲಂ <em style="color:#FFD580;font-style:normal;">೪ರಾ/೫ಹ</em></span>',
    desc: 'Hills, backwaters, and beaches – experience the finest diversity of Kerala.<br><span style="font-size:0.9em;opacity:0.75;">ಬೆಟ್ಟಗಳು, ಹಿನ್ನೀರು ಮತ್ತು ಕಡಲತೀರಗಳು – ಕೇರಳದ ಅತ್ಯುತ್ತಮ ವೈವಿಧ್ಯಮಯ ಅನುಭವ.</span>',
    tags: '🍃 Tea Gardens · ಚಹಾ ತೋಟಗಳು|⛵ Houseboat · ಹೌಸ್‌ಬೋಟ್|🏖️ Kovalam Beach · ಕೋವಲಂ ಕಡಲತೀರ'
  },
  7: {
    img: 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Padmanabhaswamy_Temple_Trivandrum.jpg/800px-Padmanabhaswamy_Temple_Trivandrum.jpg',
    title: 'Munnar Thekkady Alleppey Trivandrum <em>5N/6D</em><br><span style="font-family:\'Inter\',sans-serif;font-size:0.55em;opacity:0.8;font-weight:500;">ಮುನ್ನಾರ್ ತೆಕ್ಕಡಿ ಅಲೆಪ್ಪಿ ತಿರುವನಂತಪುರಂ <em style="color:#FFD580;font-style:normal;">೫ರಾ/೬ಹ</em></span>',
    desc: 'The grand Kerala expedition ending with the cultural heritage of Trivandrum.<br><span style="font-size:0.9em;opacity:0.75;">ತಿರುವನಂತಪುರಂನ ಸಾಂಸ್ಕೃತಿಕ ಪರಂಪರೆಯೊಂದಿಗೆ ಅಂತ್ಯಗೊಳ್ಳುವ ಭವ್ಯ ಕೇರಳ ಪ್ರವಾಸ.</span>',
    tags: '⛵ Houseboat · ಹೌಸ್‌ಬೋಟ್|🏖️ Kovalam Beach · ಕೋವಲಂ ಕಡಲತೀರ|🛕 Padmanabhaswamy · ಪದ್ಮನಾಭಸ್ವಾಮಿ'
  },
  8: {
    img: 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Napier_Museum_Trivandrum.jpg/800px-Napier_Museum_Trivandrum.jpg',
    title: 'Trivandrum <em>1N/2D</em><br><span style="font-family:\'Inter\',sans-serif;font-size:0.55em;opacity:0.8;font-weight:500;">ತಿರುವನಂತಪುರಂ <em style="color:#FFD580;font-style:normal;">೧ರಾ/೨ಹ</em></span>',
    desc: 'Discover the rich history, museums, and temples of Kerala\'s capital city.<br><span style="font-size:0.9em;opacity:0.75;">ಕೇರಳದ ರಾಜಧಾನಿಯ ಶ್ರೀಮಂತ ಇತಿಹಾಸ, ವಸ್ತುಸಂಗ್ರಹಾಲಯಗಳು ಮತ್ತು ದೇವಾಲಯಗಳ ದರ್ಶನ.</span>',
    tags: '🛕 Padmanabhaswamy · ಪದ್ಮನಾಭಸ್ವಾಮಿ|🏛️ Napier Museum · ನೇಪಿಯರ್ ಮ್ಯೂಸಿಯಂ|🏖️ Kovalam Beach · ಕೋವಲಂ ಕಡಲತೀರ'
  },
  9: {
    img: 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Vivekananda_Rock_Memorial.jpg/800px-Vivekananda_Rock_Memorial.jpg',
    title: 'Trivandrum - Kanyakumari <em>2N/3D</em><br><span style="font-family:\'Inter\',sans-serif;font-size:0.55em;opacity:0.8;font-weight:500;">ತಿರುವನಂತಪುರಂ - ಕನ್ಯಾಕುಮಾರಿ <em style="color:#FFD580;font-style:normal;">೨ರಾ/೩ಹ</em></span>',
    desc: 'From the capital of Kerala to the majestic southern tip of India.<br><span style="font-size:0.9em;opacity:0.75;">ಕೇರಳದ ರಾಜಧಾನಿಯಿಂದ ಭಾರತದ ಭವ್ಯ ದಕ್ಷಿಣ ತುದಿಯವರೆಗಿನ ಪ್ರವಾಸ.</span>',
    tags: '🛕 Padmanabhaswamy · ಪದ್ಮನಾಭಸ್ವಾಮಿ|🌊 Vivekananda Rock · ವಿವೇಕಾನಂದ ರಾಕ್|🌅 Sunset Point · ಸೂರ್ಯಾಸ್ತ ವೀಕ್ಷಣೆ'
  }
};
function selectKerRoute(tab, num) {
  document.querySelectorAll('#pkg-ker .tex-sub-tab').forEach(t => t.classList.remove('tex-sub-active'));
  tab.classList.add('tex-sub-active');
  const r = kerRoutes[num];
  document.getElementById('ker-hero').style.backgroundImage = `url('${r.img}')`;
  document.getElementById('ker-title').innerHTML = r.title;
  document.getElementById('ker-desc').innerHTML = r.desc;
  document.getElementById('ker-tags').innerHTML = r.tags.split('|').map(t => `<span class="tex-place-tag">${t}</span>`).join('');
  const coin = document.getElementById('ker-coin');
  const coinMap = {1:'6a',2:'6b',3:'6c',4:'6d',5:'6e',6:'6f',7:'6g',8:'6h',9:'6i'};
  const coinClass = {1:'coin-6a',2:'coin-6b',3:'coin-6c',4:'coin-6d',5:'coin-6e',6:'coin-6f',7:'coin-6g',8:'coin-6h',9:'coin-6i'};
  if(coin){ coin.textContent = coinMap[num]; coin.className = 'tex-tab-coin ' + coinClass[num]; }
}


const ootRoutes = {
  1: {
    img: 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Ooty_Lake.jpg/800px-Ooty_Lake.jpg',
    title: 'Ooty <em>1N/2D, 2N/3D, 3N/4D</em><br><span style="font-family:\'Inter\',sans-serif;font-size:0.55em;opacity:0.8;font-weight:500;">ಊಟಿ <em style="color:#FFD580;font-style:normal;">೧ರಾ/೨ಹ, ೨ರಾ/೩ಹ, ೩ರಾ/೪ಹ</em></span>',
    desc: 'Relax by the Ooty lake and explore the queen of hill stations.<br><span style="font-size:0.9em;opacity:0.75;">ಊಟಿ ಸರೋವರ ಮತ್ತು ಗಿರಿಧಾಮಗಳ ರಾಣಿಯ ಸೌಂದರ್ಯವನ್ನು ಸವಿಯಿರಿ.</span>',
    tags: '⛰️ Ooty Lake · ಊಟಿ ಸರೋವರ|🌺 Botanical Garden · ಬೊಟಾನಿಕಲ್ ಗಾರ್ಡನ್|⛰️ Dodabetta Peak · ದೊಡ್ಡಬೆಟ್ಟ'
  },
  2: {
    img: 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Kodaikanal_Lake.jpg/800px-Kodaikanal_Lake.jpg',
    title: 'Ooty - Kodaikanal <em>2N/3D, 3N/4D, 4N/5D</em><br><span style="font-family:\'Inter\',sans-serif;font-size:0.55em;opacity:0.8;font-weight:500;">ಊಟಿ - ಕೊಡೆಕಾನಲ್ <em style="color:#FFD580;font-style:normal;">೨ರಾ/೩ಹ, ೩ರಾ/೪ಹ, ೪ರಾ/೫ಹ</em></span>',
    desc: 'The best of Tamil Nadu\'s hill stations in one memorable trip.<br><span style="font-size:0.9em;opacity:0.75;">ತಮಿಳುನಾಡಿನ ಅತ್ಯುತ್ತಮ ಗಿರಿಧಾಮಗಳ ಸುಂದರ ಪ್ರವಾಸ.</span>',
    tags: '⛰️ Ooty Lake · ಊಟಿ ಸರೋವರ|⛵ Kodai Lake · ಕೊಡೆಕಾನಲ್ ಸರೋವರ|🪨 Pillar Rocks · ಪಿಲ್ಲರ್ ರಾಕ್ಸ್'
  },
  3: {
    img: 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Munnar_hillstation.jpg/800px-Munnar_hillstation.jpg',
    title: 'Ooty - Kodaikanal - Munnar <em>6N/7D</em><br><span style="font-family:\'Inter\',sans-serif;font-size:0.55em;opacity:0.8;font-weight:500;">ಊಟಿ - ಕೊಡೆಕಾನಲ್ - ಮುನ್ನಾರ್ <em style="color:#FFD580;font-style:normal;">೬ರಾ/೭ಹ</em></span>',
    desc: 'An extended journey through South India\'s most iconic mountain ranges.<br><span style="font-size:0.9em;opacity:0.75;">ದಕ್ಷಿಣ ಭಾರತದ ಪ್ರಮುಖ ಗಿರಿಧಾಮಗಳ ಮೂಲಕ ಸುದೀರ್ಘ ಪ್ರವಾಸ.</span>',
    tags: '⛰️ Ooty Lake · ಊಟಿ ಸರೋವರ|⛵ Kodai Lake · ಕೊಡೆಕಾನಲ್ ಸರೋವರ|🍃 Tea Gardens · ಚಹಾ ತೋಟಗಳು'
  }
};
function selectOotRoute(tab, num) {
  document.querySelectorAll('#pkg-oot .tex-sub-tab').forEach(t => t.classList.remove('tex-sub-active'));
  tab.classList.add('tex-sub-active');
  const r = ootRoutes[num];
  document.getElementById('oot-hero').style.backgroundImage = `url('${r.img}')`;
  document.getElementById('oot-title').innerHTML = r.title;
  document.getElementById('oot-desc').innerHTML = r.desc;
  document.getElementById('oot-tags').innerHTML = r.tags.split('|').map(t => `<span class="tex-place-tag">${t}</span>`).join('');
  const coin = document.getElementById('oot-coin');
  const coinMap = {1:'7a',2:'7b',3:'7c'};
  const coinClass = {1:'coin-7a',2:'coin-7b',3:'coin-7c'};
  if(coin){ coin.textContent = coinMap[num]; coin.className = 'tex-tab-coin ' + coinClass[num]; }
}

const kodRoutes = {
  1: {
    img: 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Kodaikanal_Lake.jpg/800px-Kodaikanal_Lake.jpg',
    title: 'Kodaikanal <em>1N/2D & 2N/3D</em><br><span style="font-family:\'Inter\',sans-serif;font-size:0.55em;opacity:0.8;font-weight:500;">ಕೊಡೆಕಾನಲ್ <em style="color:#FFD580;font-style:normal;">೧ರಾ/೨ಹ & ೨ರಾ/೩ಹ</em></span>',
    desc: 'Experience the princess of hill stations with its star-shaped lake.<br><span style="font-size:0.9em;opacity:0.75;">ಗಿರಿಧಾಮಗಳ ರಾಜಕುಮಾರಿ ಮತ್ತು ನಕ್ಷತ್ರ ಆಕಾರದ ಸರೋವರದ ಸೌಂದರ್ಯ.</span>',
    tags: '⛵ Kodai Lake · ಕೊಡೆಕಾನಲ್ ಸರೋವರ|🌲 Pine Forest · ಪೈನ್ ಫಾರೆಸ್ಟ್|🪨 Pillar Rocks · ಪಿಲ್ಲರ್ ರಾಕ್ಸ್'
  },
  2: {
    img: 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Munnar_hillstation.jpg/800px-Munnar_hillstation.jpg',
    title: 'Kodaikanal - Munnar <em>4N/5D</em><br><span style="font-family:\'Inter\',sans-serif;font-size:0.55em;opacity:0.8;font-weight:500;">ಕೊಡೆಕಾನಲ್ - ಮುನ್ನಾರ್ <em style="color:#FFD580;font-style:normal;">೪ರಾ/೫ಹ</em></span>',
    desc: 'Journey through the high ranges connecting Tamil Nadu to Kerala.<br><span style="font-size:0.9em;opacity:0.75;">ತಮಿಳುನಾಡು ಮತ್ತು ಕೇರಳವನ್ನು ಸಂಪರ್ಕಿಸುವ ಗಿರಿಧಾಮಗಳ ಪ್ರವಾಸ.</span>',
    tags: '⛵ Kodai Lake · ಕೊಡೆಕಾನಲ್ ಸರೋವರ|🍃 Tea Gardens · ಚಹಾ ತೋಟಗಳು|🌺 Echo Point · ಎಕೋ ಪಾಯಿಂಟ್'
  }
};
function selectKodRoute(tab, num) {
  document.querySelectorAll('#pkg-kod .tex-sub-tab').forEach(t => t.classList.remove('tex-sub-active'));
  tab.classList.add('tex-sub-active');
  const r = kodRoutes[num];
  document.getElementById('kod-hero').style.backgroundImage = `url('${r.img}')`;
  document.getElementById('kod-title').innerHTML = r.title;
  document.getElementById('kod-desc').innerHTML = r.desc;
  document.getElementById('kod-tags').innerHTML = r.tags.split('|').map(t => `<span class="tex-place-tag">${t}</span>`).join('');
  const coin = document.getElementById('kod-coin');
  const coinMap = {1:'8a',2:'8b'};
  const coinClass = {1:'coin-8a',2:'coin-8b'};
  if(coin){ coin.textContent = coinMap[num]; coin.className = 'tex-tab-coin ' + coinClass[num]; }
}


const goaRoutes = {
  1: {
    img: 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Palolem_Beach_Goa_India.jpg/800px-Palolem_Beach_Goa_India.jpg',
    title: 'Goa Package <em>3N/4D</em><br><span style="font-family:\'Inter\',sans-serif;font-size:0.55em;opacity:0.8;font-weight:500;">ಗೋವಾ ಪ್ಯಾಕೇಜ್ <em style="color:#FFD580;font-style:normal;">೩ರಾ/೪ಹ</em></span>',
    desc: 'Explore the sun-kissed beaches, historic churches, and vibrant culture of Goa.<br><span style="font-size:0.9em;opacity:0.75;">ಗೋವಾದ ಸುಂದರ ಕಡಲತೀರಗಳು, ಚರ್ಚ್‌ಗಳು ಮತ್ತು ಸಂಸ್ಕೃತಿಯ ಅದ್ಭುತ ಪ್ರವಾಸ.</span>',
    tags: '🏖️ Beaches · ಕಡಲತೀರಗಳು|⛪ Churches · ಚರ್ಚ್‌ಗಳು|🌴 Fort Aguada · ಅಗುಡಾ ಕೋಟೆ'
  }
};
function selectGoaRoute(tab, num) {
  document.querySelectorAll('#pkg-goa .tex-sub-tab').forEach(t => t.classList.remove('tex-sub-active'));
  tab.classList.add('tex-sub-active');
  const r = goaRoutes[num];
  document.getElementById('goa-hero').style.backgroundImage = `url('${r.img}')`;
  document.getElementById('goa-title').innerHTML = r.title;
  document.getElementById('goa-desc').innerHTML = r.desc;
  document.getElementById('goa-tags').innerHTML = r.tags.split('|').map(t => `<span class="tex-place-tag">${t}</span>`).join('');
  const coin = document.getElementById('goa-coin');
  const coinMap = {1:'9a'};
  const coinClass = {1:'coin-9a'};
  if(coin){ coin.textContent = coinMap[num]; coin.className = 'tex-tab-coin ' + coinClass[num]; }
}

const alpRoutes = {
  1: {
    img: 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Alleppey_Houseboat.jpg/800px-Alleppey_Houseboat.jpg',
    title: 'Alleppey Houseboat - Cochin <em>1N/2D</em><br><span style="font-family:\'Inter\',sans-serif;font-size:0.55em;opacity:0.8;font-weight:500;">ಅಲೆಪ್ಪಿ ಹೌಸ್‌ಬೋಟ್ - ಕೊಚ್ಚಿ <em style="color:#FFD580;font-style:normal;">೧ರಾ/೨ಹ</em></span>',
    desc: 'A peaceful backwater cruise in Alleppey followed by the rich heritage of Cochin.<br><span style="font-size:0.9em;opacity:0.75;">ಅಲೆಪ್ಪಿಯ ಪ್ರಶಾಂತ ಹಿನ್ನೀರಿನ ವಿಹಾರ ಮತ್ತು ಕೊಚ್ಚಿಯ ಶ್ರೀಮಂತ ಪರಂಪರೆಯ ಪ್ರವಾಸ.</span>',
    tags: '⛵ Houseboat · ಹೌಸ್‌ಬೋಟ್|🛶 Backwaters · ಹಿನ್ನೀರು|🏰 Fort Kochi · ಫೋರ್ಟ್ ಕೊಚ್ಚಿ'
  }
};
function selectAlpRoute(tab, num) {
  document.querySelectorAll('#pkg-alp .tex-sub-tab').forEach(t => t.classList.remove('tex-sub-active'));
  tab.classList.add('tex-sub-active');
  const r = alpRoutes[num];
  document.getElementById('alp-hero').style.backgroundImage = `url('${r.img}')`;
  document.getElementById('alp-title').innerHTML = r.title;
  document.getElementById('alp-desc').innerHTML = r.desc;
  document.getElementById('alp-tags').innerHTML = r.tags.split('|').map(t => `<span class="tex-place-tag">${t}</span>`).join('');
  const coin = document.getElementById('alp-coin');
  const coinMap = {1:'10a'};
  const coinClass = {1:'coin-10a'};
  if(coin){ coin.textContent = coinMap[num]; coin.className = 'tex-tab-coin ' + coinClass[num]; }
}

</script>
</body>
