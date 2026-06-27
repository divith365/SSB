const fs = require('fs');
let html = fs.readFileSync('/home/arun/SSB/index.html', 'utf8');

// Fix undefined in CSS
const validImgs = [
  'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Abbey_Falls_Kodagu.jpg/800px-Abbey_Falls_Kodagu.jpg',
  'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/Mysore_Palace_Morning.jpg/800px-Mysore_Palace_Morning.jpg',
  'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Ooty_Lake.jpg/800px-Ooty_Lake.jpg',
  'https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/Pine_Forest_Ooty.jpg/800px-Pine_Forest_Ooty.jpg',
  'https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Dubare_Elephant_Camp.jpg/800px-Dubare_Elephant_Camp.jpg',
  'https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Munnar_hillstation.jpg/800px-Munnar_hillstation.jpg',
  'https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Alleppey_Houseboat.jpg/800px-Alleppey_Houseboat.jpg'
];

html = html.replace(/url\('undefined'\)/g, () => `url('${validImgs[Math.floor(Math.random() * validImgs.length)]}')`);

fs.writeFileSync('/home/arun/SSB/index.html', html, 'utf8');
console.log('Fixed undefined URLs!');
