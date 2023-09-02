from bs4 import BeautifulSoup
import json
import requests

def parse_scraper(html):
    soup = BeautifulSoup(html, 'html.parser')
    right = soup.find('div', attrs={'class': 'right'})
    table = right.find('table' , attrs={'id': 'sg'})
    trs = table.find_all('tr')

    result = []
    start = 0
    while start < len(trs):
        # every character occupies 7 rows
        mini_result = {}

        for i in range(7):
            tds = trs[start+i].find_all('td')

            if i == 0:
                mini_result['name'] = tds[0].text.strip()
                continue

            key = tds[0].text.strip().lower()
            if 'lv' in key:
                key = key.split(' ')[1].strip().lower()
                mini_result[key] = {
                        'pwr': tds[1].text.strip(),
                        'skl': tds[2].text.strip(),
                        'def': tds[3].text.strip(),
                        'spd': tds[4].text.strip(),
                        'mgc': tds[5].text.strip(),
                        'luk': tds[6].text.strip(),
                        'hp': tds[7].text.strip(),
                        }

        result.append(mini_result)
        start += 7

    return result

url = 'https://suikosource.com/games/gs1/guides/statgrowth.php'

html = requests.get(url).content
result = parse_scraper(html)

json_stats = j = json.dumps(result, indent=4) 
with open('suikoden_stats.json', 'w') as f:
    f.write(json_stats)

