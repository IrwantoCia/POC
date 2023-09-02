# BEST RECORD 47.08,96 Seconds
from bs4 import BeautifulSoup
import json
import requests

def parse_table(head_gear_table_rows, is_body_gear=False, is_shield=False, is_acc=False):
    result = []
    for i in range(1, len(head_gear_table_rows)):
        tds = head_gear_table_rows[i].find_all('td')
        shop = ''
        treasure = ''
        loot = ''

        if is_body_gear or is_acc:
            if 'Shop:' in tds[8].text:
                shop = tds[8].text.split('Shop:')[-1].split('Treasure:')[0].strip()
            if 'Treasure:' in tds[8].text:
                treasure = tds[8].text.split('Treasure:')[-1].split('Loot:')[0].strip()
            if 'Loot:' in tds[8].text:
                loot = tds[8].text.split('Loot:')[-1].strip()
        elif is_shield:
            if 'Shop:' in tds[5].text:
                shop = tds[5].text.split('Shop:')[-1].split('Treasure:')[0].strip()
            if 'Treasure:' in tds[5].text:
                treasure = tds[5].text.split('Treasure:')[-1].split('Loot:')[0].strip()
            if 'Loot:' in tds[5].text:
                loot = tds[5].text.split('Loot:')[-1].strip()
        else:
            if 'Shop:' in tds[6].text:
                shop = tds[6].text.split('Shop:')[-1].split('Treasure:')[0].strip()
            if 'Treasure:' in tds[6].text:
                treasure = tds[6].text.split('Treasure:')[-1].split('Loot:')[0].strip()
            if 'Loot:' in tds[6].text:
                loot = tds[6].text.split('Loot:')[-1].strip()


        wear = []
        if not is_shield:
            if tds[2].text.strip() != '':
                wear.append(tds[2].text.strip())

            if tds[3].text.strip() != '':
                wear.append(tds[3].text.strip())

            if is_body_gear or is_acc:
                if tds[4].text.strip() != '':
                    wear.append(tds[4].text.strip())
                if tds[5].text.strip() != '':
                    wear.append(tds[5].text.strip())
        else:
            if tds[2].text.strip() != '':
                wear.append(tds[2].text.strip())


        if is_body_gear or is_acc:
            result.append({
                'name': tds[0].text.strip(),
                'bits': int(tds[1].text.strip()),
                'wear': wear,
                'def': int(tds[6].text.strip()),
                'effect': tds[7].text.strip(),
                'source': {
                    'shop': shop,
                    'loot': loot,
                    'treasure': treasure, 
                    }

                })
        elif is_shield:
            result.append({
                'name': tds[0].text.strip(),
                'bits': int(tds[1].text.strip()),
                'wear': wear,
                'def': int(tds[3].text.strip()),
                'effect': tds[4].text.strip(),
                'source': {
                    'shop': shop,
                    'loot': loot,
                    'treasure': treasure, 
                    }

                })
        else:
            result.append({
                'name': tds[0].text.strip(),
                'bits': int(tds[1].text.strip()),
                'wear': wear,
                'def': int(tds[4].text.strip()),
                'effect': tds[5].text.strip(),
                'source': {
                    'shop': shop,
                    'loot': loot,
                    'treasure': treasure, 
                    }
                })

    return result

def parse_character_wearable(character_wearable_list_divs):
    result = []
    character_wearable_table = character_wearable_list_divs[0].find('table') 
    character_wearable_table_rows = character_wearable_table.find_all('tr')

    for i in range(1, len(character_wearable_table_rows)):
        tds = character_wearable_table_rows[i].find_all('td')
        start = 0

        for _ in range(3):
            wear = []
            for j in range(start+1, start+5):
                if tds[j].text.strip() != '':
                    wear.append(tds[j].text.strip())

            result.append({
                'name': tds[start].text.strip(),
                'image_url': tds[start].find('img')['src'],
                'classes': wear,
                })

            start += 5
    return result

def parse_armor(armor_list_divs):
    head_gear_table = armor_list_divs[0].find('table')
    head_gear_table_rows = head_gear_table.find_all('tr')

    body_gear_table = armor_list_divs[1].find('table')
    body_gear_table_rows = body_gear_table.find_all('tr')

    shield_table = armor_list_divs[2].find('table')
    shield_table_rows = shield_table.find_all('tr')

    acc_table = armor_list_divs[3].find('table')
    acc_table_rows = acc_table.find_all('tr')

    result = []
    result.append(parse_table(head_gear_table_rows))
    result.append(parse_table(body_gear_table_rows, True))
    result.append(parse_table(shield_table_rows, False, True))
    result.append(parse_table(acc_table_rows, False, False, True))

    return result

def parse_scraper(html):
    soup = BeautifulSoup(html, 'html.parser')
    right = soup.find('div', attrs={'class': 'right'})
    right_divs = right.find_all('div' , attrs={'class': 'content'})

    character_wearable_list = right_divs[5]
    character_wearable_list_divs = character_wearable_list.find_all('div', attrs={'class': 'indent'})

    armor_list = right_divs[1]
    armor_list_divs = armor_list.find_all('div', attrs={'class': 'indent'})

    result = {
            "armor": parse_armor(armor_list_divs),
            "character": parse_character_wearable(character_wearable_list_divs)
            } 
    return result



url = 'https://suikosource.com/games/gs1/guides/armor.php'

html = requests.get(url).content
result = parse_scraper(html)

#json_armor = json.dumps(result['armor'], indent=4) 
#with open('suikoden_armor.json', 'w') as f:
#    f.write(json_armor)

print(len(result['character']))
json_character_armor = json.dumps(result['character'], indent=4) 
with open('suikoden_character_armor.json', 'w') as f:
    f.write(json_character_armor)

