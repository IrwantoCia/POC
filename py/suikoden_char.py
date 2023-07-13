# BEST RECORD 47.08,96 Seconds
from bs4 import BeautifulSoup
import json
import requests

def parse_scraper(html):
    soup = BeautifulSoup(html, 'html.parser')
    right = soup.find('div', attrs={'class': 'right'})
    table = right.find('table' , attrs={'class': 'namelist'})
    trs = table.find_all('tr')

    result = []
    for i in range(1, len(trs)):
        tds = trs[i].find_all('td')

        name = tds[1].text
        star = tds[2].text
        how_to_recruit = tds[3].text
        optional = False

        if trs[i].get('class') == ['opt']:
            optional = True

        result.append({
            'id': i,
            'name': name,
            'star': star,
            'how_to_recruit': how_to_recruit,
            'optional': optional,
            })

    return result

url = 'https://www.suikosource.com/games/sod.php?pf=S1'

html = requests.get(url).content
result = parse_scraper(html)

json_character = json.dumps(result, indent=4) 
with open('suikoden_character.json', 'w') as f:
    f.write(json_character)

