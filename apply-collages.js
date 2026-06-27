const fs = require('fs');
let html = fs.readFileSync('/home/arun/SSB/index.html', 'utf8');

const regex = /(chk|crg|mys|ker|oot|kod|goa|alp)Routes = \{([\s\S]*?)\n\};/g;
let cardImages = {};
let match;
while ((match = regex.exec(html)) !== null) {
  const card = match[1];
  const body = match[2];
  const imgRegex = /img:\s*'([^']+)'/g;
  let imgs = [];
  let imgMatch;
  while ((imgMatch = imgRegex.exec(body)) !== null) {
    imgs.push(imgMatch[1]);
  }
  cardImages[card] = imgs;
}

// Fallback logic to grab 4 distinct images from the existing set without external API calls
const fallbacks = {
  chk: [cardImages.chk[0], cardImages.chk[1], cardImages.chk[2], cardImages.crg[0]], // Abbey falls
  crg: [cardImages.crg[0], cardImages.crg[1], cardImages.mys[0], cardImages.mys[11]], // Mysore, Dubare
  mys: [cardImages.mys[0], cardImages.mys[1], cardImages.mys[14], cardImages.mys[4]], // Mysore, Ooty, Meenakshi, Kodaikanal
  ker: [cardImages.ker[0], cardImages.ker[2], cardImages.ker[3], cardImages.ker[5]], // Munnar, Periyar, Alleppey, Kovalam
  oot: [cardImages.oot[0], cardImages.oot[2], cardImages.mys[2], cardImages.mys[3]], // Ooty Lake, Munnar, Nilgiri train, Pine Forest
  kod: [cardImages.kod[0], cardImages.kod[1], cardImages.mys[4], cardImages.mys[5]], // Kodaikanal, Munnar, Kodaikanal Lake, Edakkal
  goa: [cardImages.goa[0], cardImages.ker[5], cardImages.ker[4], cardImages.goa[0]], // Palolem, Kovalam, Backwaters
  alp: [cardImages.alp[0], cardImages.ker[4], cardImages.ker[0], cardImages.ker[3]]  // Alleppey, Backwaters, Munnar
};

let css = '';
for (let c in fallbacks) {
  const imgs = fallbacks[c].map(i => `url('${i}')`).join(',\n    ');
  css += `
.bg-collage-${c} {
  background-image: 
    ${imgs};
  background-position: top left, top right, bottom left, bottom right;
  background-size: 50.5% 50.5%, 50.5% 50.5%, 50.5% 50.5%, 50.5% 50.5%;
  background-repeat: no-repeat;
}
`;
}

// 1. Add CSS
html = html.replace('</style>', css + '\n</style>');

// 2. Add classes to html heroes
const cards = ['chk', 'crg', 'mys', 'ker', 'oot', 'kod', 'goa', 'alp'];
for (let c of cards) {
  const heroRegex = new RegExp(`<div class="tex-panel-hero" id="${c}-hero" style="background-image:url[^>]*>`);
  html = html.replace(heroRegex, `<div class="tex-panel-hero bg-collage-${c}" id="${c}-hero">`);
  
  // 3. Update select*Route logic in JS
  const funcRegex = new RegExp(`function select${c.charAt(0).toUpperCase() + c.slice(1)}Route\\(tab, num\\) \\{\\s*[\\s\\S]*?const r = ${c}Routes\\[num\\];\\s*document\\.getElementById\\('${c}-hero'\\)\\.style\\.backgroundImage = \\\`url\\('\\$\\{r\\.img\\}'\\)\\\`;`);
  
  const funcRepl = `function select${c.charAt(0).toUpperCase() + c.slice(1)}Route(tab, num) {
  document.querySelectorAll('#pkg-${c} .tex-sub-tab').forEach(t => t.classList.remove('tex-sub-active'));
  tab.classList.add('tex-sub-active');
  const r = ${c}Routes[num];
  const hero = document.getElementById('${c}-hero');
  if (num === 1) {
    hero.className = 'tex-panel-hero bg-collage-${c}';
    hero.style.backgroundImage = '';
  } else {
    hero.className = 'tex-panel-hero';
    hero.style.backgroundImage = \`url('\${r.img}')\`;
    hero.style.backgroundPosition = 'center center';
    hero.style.backgroundSize = 'cover';
  }`;
  
  html = html.replace(funcRegex, funcRepl);
}

fs.writeFileSync('/home/arun/SSB/index.html', html, 'utf8');
console.log('Successfully applied collages for Cards 3-10!');
