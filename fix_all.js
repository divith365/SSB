const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

// 1. Fix tex-header for new cards
html = html.replace(
  /<div class="tex-header">\s*<span class="tex-kannada">ಕೇರಳ ಪ್ರವಾಸ<\/span>\s*Kerala Packages\s*<\/div>/g,
  `<div class="tex-header">
          <span class="tex-eyebrow">Kerala Packages<br>ಕೇರಳ ಪ್ಯಾಕೇಜ್‌ಗಳು</span>
          <h3>Kerala Special<br><span style="font-family:'Inter',sans-serif;font-size:0.7em;font-weight:500;opacity:0.75;">ಕೇರಳ ಸ್ಪೆಷಲ್</span></h3>
        </div>`
);

html = html.replace(
  /<div class="tex-header">\s*<span class="tex-kannada">ಊಟಿ ಪ್ರವಾಸ<\/span>\s*Ooty Packages\s*<\/div>/g,
  `<div class="tex-header">
          <span class="tex-eyebrow">Ooty Packages<br>ಊಟಿ ಪ್ಯಾಕೇಜ್‌ಗಳು</span>
          <h3>Ooty Special<br><span style="font-family:'Inter',sans-serif;font-size:0.7em;font-weight:500;opacity:0.75;">ಊಟಿ ಸ್ಪೆಷಲ್</span></h3>
        </div>`
);

html = html.replace(
  /<div class="tex-header">\s*<span class="tex-kannada">ಕೊಡೆಕಾನಲ್ ಪ್ರವಾಸ<\/span>\s*Kodaikanal Packages\s*<\/div>/g,
  `<div class="tex-header">
          <span class="tex-eyebrow">Kodaikanal Packages<br>ಕೊಡೆಕಾನಲ್ ಪ್ಯಾಕೇಜ್‌ಗಳು</span>
          <h3>Kodai Special<br><span style="font-family:'Inter',sans-serif;font-size:0.7em;font-weight:500;opacity:0.75;">ಕೊಡೆಕಾನಲ್ ಸ್ಪೆಷಲ್</span></h3>
        </div>`
);

html = html.replace(
  /<div class="tex-header">\s*<span class="tex-kannada">ಗೋವಾ ಪ್ರವಾಸ<\/span>\s*Goa Packages\s*<\/div>/g,
  `<div class="tex-header">
          <span class="tex-eyebrow">Goa Packages<br>ಗೋವಾ ಪ್ಯಾಕೇಜ್‌ಗಳು</span>
          <h3>Goa Special<br><span style="font-family:'Inter',sans-serif;font-size:0.7em;font-weight:500;opacity:0.75;">ಗೋವಾ ಸ್ಪೆಷಲ್</span></h3>
        </div>`
);

html = html.replace(
  /<div class="tex-header">\s*<span class="tex-kannada">ಅಲೆಪ್ಪಿ ಮತ್ತು ಕೊಚ್ಚಿ<\/span>\s*Alleppey Packages\s*<\/div>/g,
  `<div class="tex-header">
          <span class="tex-eyebrow">Alleppey Packages<br>ಅಲೆಪ್ಪಿ ಪ್ಯಾಕೇಜ್‌ಗಳು</span>
          <h3>Houseboat Stay<br><span style="font-family:'Inter',sans-serif;font-size:0.7em;font-weight:500;opacity:0.75;">ಹೌಸ್‌ಬೋಟ್ ಪ್ರವಾಸ</span></h3>
        </div>`
);

// 2. Remove old cards
// They start at "<!-- Tour 3 -->" and end before "</div>" of the packages grid.
// Let's find the exact string bounds
const startIndex = html.indexOf('<!-- Tour 3 -->');
if (startIndex !== -1) {
  const endIndexStr = '<!-- DESTINATIONS -->';
  const endIndex = html.indexOf(endIndexStr);
  if (endIndex !== -1) {
    // The grid closes before DESTINATIONS
    // Let's slice carefully
    let before = html.substring(0, startIndex);
    let after = html.substring(endIndex);
    // Add back the closing div for packages-grid and section end
    let middle = `  </div>
  <div style="text-align:center;margin-top:36px;">
    <a href="#contact" class="btn-primary" data-t="more_btn">Enquire About Any Package</a>
  </div>
</section>

`;
    html = before + middle + after;
  }
}

fs.writeFileSync('index.html', html);
console.log('Fixed headers and removed old cards');
