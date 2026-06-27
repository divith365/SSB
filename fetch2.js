const https = require('https');

const titles = [
  'Palolem_Beach', 'Dudhsagar_Falls', 'Aguada_Fort', 'Basilica_of_Bom_Jesus',
  'Alappuzha', 'Kumarakom', 'Vembanad', 'Kerala_backwaters'
];

async function run() {
  for (let title of titles) {
    const url = `https://en.wikipedia.org/w/api.php?action=query&titles=${title}&prop=pageimages&pithumbsize=960&format=json`;
    await new Promise(r => {
      https.get(url, { headers: { 'User-Agent': 'MyApp/4.0' } }, res => {
        let data = '';
        res.on('data', d => data += d);
        res.on('end', () => {
          try {
            const obj = JSON.parse(data);
            const pages = obj.query.pages;
            let found = false;
            for (let p in pages) {
              if (pages[p].thumbnail) {
                console.log(`${title}: ${pages[p].thumbnail.source}`);
                found = true;
              }
            }
            if (!found) console.log(`${title}: NOT_FOUND`);
          } catch(e) {
            console.log(`${title}: ERROR`);
          }
          r();
        });
      });
    });
    await new Promise(r => setTimeout(r, 500));
  }
}
run();
