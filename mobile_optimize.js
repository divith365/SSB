const fs = require('fs');
let html = fs.readFileSync('/home/arun/SSB/index.html', 'utf8');

const regex = /\.tex-panel \{ flex-direction: column !important; \}/;
const replacement = `.tex-panel { 
    flex-direction: column !important; 
    width: 95% !important; 
    max-width: 100% !important; 
    aspect-ratio: auto !important; 
    height: 90vh !important; 
    max-height: 90vh !important; 
    border-radius: 16px !important; 
  }
  .tex-panel-hero { 
    flex: 0 0 45% !important; 
    height: 45% !important; 
    min-height: 200px !important;
  }
  .tex-sub-tabs { 
    flex: 1 !important; 
    overflow-y: auto !important; 
  }`;

if (regex.test(html)) {
  html = html.replace(regex, replacement);
  fs.writeFileSync('/home/arun/SSB/index.html', html, 'utf8');
  console.log('Mobile optimizations applied!');
} else {
  console.log('Regex failed.');
}
