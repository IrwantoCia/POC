import json
from bs4 import BeautifulSoup

html_content = """
<!-- content for the page goes here. -->
<div class="right">
    <div class="content" id="title">
        <div class="head"><a href="/games/gs1/">Suikoden</a>: <a href="/games/gs1/guides/">Guides</a>: <a href="/games/gs1/guides/antiques.php">Antiques Listing</a></div>
        The locations and prices of the various pots, paintings, and ornaments.
        <div class="footer"><a href="/games/gs1/">Suikoden</a>: <a href="/games/gs1/guides/">Guides</a>: <a href="/games/gs1/guides/antiques.php">Antiques Listing</a> by Kuromimi</div>
    </div>

    <div class="content">
        <div class="head">Pots and Urns</div>
        Black Urn: 20,000 bits<div class="indent">Kalekka: Dropped by Hawk Man </div>
        <p>Blue Dragon Urn: 8,000 bits<div class="indent">Neclord's Castle: Dropped by Larvae </div>
        <p>Celadon Urn: 10,000 bits<div class="indent">Gregminster Area: Dropped by BonBon </div>
        <p>Failure Urn: 10 bits<div class="indent">Gregminster Area: Dropped by BonBon<br>Lepant's Mansion: Dropped by Robot Soldier<br>Lepant's Mansion: Dropped by Slot Man<br>Kalekka: Dropped by Hawk Man<br>Neclord's Castle: Dropped by Larvae</div>
        <p>Fine Bone China: 60,000 bits<div class="indent">Neclord's Castle: Dropped by Larvae </div>
        <p>Nameless Urn: 0 bits (special item)<div class="indent"> Scarleticia Area: Dropped by Holly Fairy </div>
        <p>Octopus Urn: 500 bits<div class="indent">Gregminster Area: Dropped by BonBon<br>Found at Tigerwolf Mountain </div>
        <p>Persian Lamp: 7,500 bits<div class="indent">Lepant's Mansion: Dropped by Robot Soldier<br>Lepant's Mansion: Dropped by Slot Man</div>
        <p>Vase: 2,500 bits<div class="indent">Lepant's Mansion: Dropped by Robot Soldier<br>Lepant's Mansion: Dropped by Slot Man<br>Found at Seifu Mountain</div>
        <p>Wide Urn: 4,000 bits<div class="indent">Kalekka: Dropped by Hawk Man</div>
    </div>

    <div class="content">
        <div class="head">Ornaments</div>
        Bonsai: 25,000 bits<div class="indent">Soniere Prison: Dropped by Red Slime<br>Moravia Castle: Dropped by Whip Master </div>
        <p>Chinese Dish: 6,000 bits<div class="indent">Soniere Prison: Dropped by Red Slime </div>
        <p>Goddess Statue: 100,000 bits<div class="indent">Moravia Castle: Dropped by Whip Master </div>
        <p>Hex Doll: 60 bits<div class="indent">Seika Area: Dropped by Killer Rabbit<br>Soniere Prison: Dropped by Red Slime<br>Dragon Knights' Domain/Seek Valley: Dropped by Ivy<br>Moravia Castle: Dropped by Whip Master<br>Found in Grady's Mansion<br>Found in Kraze's Residence </div>
        <p>Japanese Dish: 3,000 bits<div class="indent">Seika Area: Dropped by Killer Rabbit </div>
        <p>Knight Statue: 30,000 bits<div class="indent">Dragon Knights' Domain/Seek Valley: Dropped by Ivy </div>
        <p>Opal Stone: 0 bits<div class="indent"> (special item)<br> Soniere Prison: Dropped by Nightmare </div>
        <p>Peeing Boy: 16,000 bits<div class="indent">Seika Area: Dropped by Killer Rabbit<br>Dragon Knights' Domain/Seek Valley: Dropped by Ivy</div>
    </div>

    <div class="content">
        <div class="head">Paintings</div>
        Beauties of Nature: 200,000 bits<div class="indent">Gregminster Area: Dropped by Orc </div>
        <p>Flower Painting: 7,000 bits<div class="indent">Great Forest: Dropped by Holly Boy<br>Dwarf Trail: Dropped by Eagle Man<br>Found in Kalekka </div>
        <p>Graffiti: 100 bits<div class="indent">Great Forest: Dropped by Holly Boy<br>Dwarf Trail: Dropped by Eagle Man<br>Cave of the Past: Dropped by Banshee<br>Gregminster Area: Dropped by Orc</div>
        <p>Landscape Painting: 40,000 bits<div class="indent">Cave of the Past: Dropped by Banshee</div>
        <p>Lover's Garden: 29,000 bits<div class="indent">Great Forest: Dropped by Holly Boy<br>Dwarf Trail: Dropped by Eagle Man<br>Gregminster Area: Dropped by Orc </div>
    </div>
</div>
"""

soup = BeautifulSoup(html_content, 'html.parser')

antiques = []
contents = soup.find_all("div", class_="content")

for content in contents:
    head = content.find("div", class_="head").text.strip()
    items = content.find_all("p")

    for item in items:
        name, price = item.text.split(":")[0].strip(), int(item.text.split(":")[1].split(" ")[1].replace(",", ""))
        sources = [source.strip() for source in item.find("div", class_="indent").find_all(text=True) if source.strip()]

        antique = {
            "name": name,
            "price": price,
            "sources": sources
        }

        antiques.append(antique)

data = {
    "antiques": antiques
}

json_data = json.dumps(data, indent=4)
print(json_data)

with open("suikoden.json", "w") as json_file:
    json_file.write(json_data)
