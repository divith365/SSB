const https = require('https');
const fs = require('fs');

const cards = {
  chk: ['Mullayanagiri', 'Kudremukh', 'Sringeri', 'Belur,_Karnataka'],
  crg: ['Abbey_Falls', 'Dubare', 'Raja%27s_Seat', 'Bylakuppe'],
  mys: ['Mysore_Palace', 'Ooty', 'Kodaikanal', 'Wayanad_district'],
  ker: ['Munnar', 'Periyar_National_Park', 'Alappuzha', 'Kovalam'],
  oot: ['Ooty', 'Nilgiri_Mountain_Railway', 'Ooty_Botanical_Gardens', 'Doddabetta'],
  kod: ['Kodaikanal', 'Pillar_Rocks', 'Coaker%27s_Walk', 'Bryant_Park'],
  goa: ['Palolem_Beach', 'Dudhsagar_Falls', 'Aguada_Fort', 'Basilica_of_Bom_Jesus'],
  alp: ['Alappuzha', 'Kumarakom', 'Vembanad', 'Kerala_backwaters']
};

const options = { headers: { 'User-Agent': 'MyApp/2.0' } };

function fetchWiki(title) {
  return new Promise((resolve, reject) => {
    const url = `https://en.wikipedia.org/w/api.php?action=query&titles=${title}&prop=pageimages&pithumbsize=960&format=json`;
    https.get(url, options, (res) => {
      let data = '';
      res.on('data', d => data += d);
      res.on('end', () => {
        try {
          const obj = JSON.parse(data);
          const pages = obj.query.pages;
          for (let p in pages) {
            if (pages[p].thumbnail) return resolve(pages[p].thumbnail.source);
          }
          resolve('NOT_FOUND');
        } catch(e) {
          resolve('JSON_ERROR');
        }
      });
    }).on('error', () => resolve('REQ_ERROR'));
  });
}

async function run() {
  let results = {};
  for (const [card, titles] of Object.entries(cards)) {
    results[card] = [];
    for (let title of titles) {
      let url = await fetchWiki(title);
      results[card].push(url);
      await new Promise(r => setTimeout(r, 200)); // 200ms delay
    }
  }
  fs.writeFileSync('collage_urls.json', JSON.stringify(results, null, 2));
  console.log('Finished writing collage_urls.json');
}

run();
