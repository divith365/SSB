const fs = require('fs');

let html = fs.readFileSync('/home/arun/SSB/index.html', 'utf8');

const cards = ['blr', 'cab', 'chk', 'crg', 'mys', 'ker', 'oot', 'kod', 'goa', 'alp'];

for (let c of cards) {
  const regex = new RegExp(
    `if \\(num === 1\\) \\{\\s*hero\\.className = 'tex-panel-hero bg-collage-${c}';\\s*hero\\.style\\.backgroundImage = '';\\s*\\} else \\{\\s*hero\\.className = 'tex-panel-hero';\\s*hero\\.style\\.backgroundImage = \\\`url\\('\\$\\{r\\.img\\}'\\)\\\`;\\s*hero\\.style\\.backgroundPosition = 'center center';\\s*hero\\.style\\.backgroundSize = 'cover';\\s*\\}`,
    'g'
  );
  
  const replacement = `hero.className = 'tex-panel-hero bg-collage-${c}';\n  hero.style.backgroundImage = '';`;
  
  html = html.replace(regex, replacement);
}

fs.writeFileSync('/home/arun/SSB/index.html', html, 'utf8');
console.log('Updated all routing functions to always show collage backgrounds!');
