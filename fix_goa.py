import sys

with open('/home/arun/SSB/index.html', 'r') as f:
    content = f.read()

old_goa = """.bg-collage-goa {
  background-image:
    url('https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/Palolem_Beach%2C_South_Goa.jpg/960px-Palolem_Beach%2C_South_Goa.jpg'),
    url('https://upload.wikimedia.org/wikipedia/commons/thumb/0/0b/Doodhsagar_Fall.jpg/960px-Doodhsagar_Fall.jpg'),
    url('https://upload.wikimedia.org/wikipedia/commons/thumb/a/ad/Fort_aguada.jpg/960px-Fort_aguada.jpg'),
    url('https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Front_Elevation_of_Basilica_of_Bom_Jesus.jpg/960px-Front_Elevation_of_Basilica_of_Bom_Jesus.jpg');"""

new_goa = """.bg-collage-goa {
  background-image:
    url('https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/Palolem_Beach%2C_South_Goa.jpg/960px-Palolem_Beach%2C_South_Goa.jpg'),
    url('images/hero/slide_12.webp'),
    url('images/hero/slide_13.webp'),
    url('images/hero/slide_14.webp');"""

content = content.replace(old_goa, new_goa)

with open('/home/arun/SSB/index.html', 'w') as f:
    f.write(content)
