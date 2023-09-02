from bs4 import BeautifulSoup
import json
import requests

def parse_table(right_div_content_p):
    table = right_div_content_p.find('table', attrs={'id': 'beast'})
    table_rows = table.find_all('tr')

    name = table_rows[0].find('td').text.strip()

    second_row = table_rows[1]
    second_row_tds = second_row.find_all('td')
    image_url = second_row_tds[0].find('img').get('src')
    location = table.find('table').find('td').text.strip()

    last_row = table_rows[-1]
    detail_row_last_row_tds = last_row.find_all('td')
    note = detail_row_last_row_tds[0].text.split('Note:')[-1].strip()
    
    detail_table = table_rows[1].find('table')
    detail_rows = detail_table.find_all('tr')

    stats = {}
    loot = []

    detail_row_third_row = detail_rows[2]
    detail_row_third_row_tds = detail_row_third_row.find_all('td')
    stats['lv'] = int(detail_row_third_row_tds[0].text.strip())
    stats['hp'] = int(detail_row_third_row_tds[1].text.strip())
    stats['pwr'] = int(detail_row_third_row_tds[2].text.strip())
    stats['skl'] = int(detail_row_third_row_tds[3].text.strip())
    stats['def'] = int(detail_row_third_row_tds[4].text.strip())
    stats['spd'] = int(detail_row_third_row_tds[5].text.strip())
    stats['mgc'] = int(detail_row_third_row_tds[6].text.strip())
    stats['luk'] = int(detail_row_third_row_tds[7].text.strip())

    loot.append({
        'item': detail_row_third_row_tds[8].text.strip(),
        'rate': detail_row_third_row_tds[9].text.strip()
    })

    detail_rows_fourth_row = detail_rows[3]
    detail_rows_fourth_row_tds = detail_rows_fourth_row.find_all('td')
    loot.append({
        'item': detail_rows_fourth_row_tds[8].text.strip(),
        'rate': detail_rows_fourth_row_tds[9].text.strip()
    })

    detail_row_fifth_row = detail_rows[4]
    detail_row_fifth_row_tds = detail_row_fifth_row.find_all('td')
    bits = int(detail_row_fifth_row_tds[0].text.strip())

    weakness = []
    for i in range(1, 7):
        weakness.append({
            'element': detail_rows_fourth_row_tds[i].find('img').get('src').split('_')[1].replace('.gif', ''),
            'value': detail_row_fifth_row_tds[i].text.strip(),
            'image_url': detail_rows_fourth_row_tds[i].find('img').get('src')
        })

    
    loot.append({
        'item': detail_row_fifth_row_tds[8].text.strip(),
        'rate': detail_row_fifth_row_tds[9].text.strip()
    })
    
    result = {
        'name': name,
        'image_url': image_url,
        'location': location,
        'stats': stats,
        'bits': bits,
        'weakness': weakness,
        'loot': loot,
        'notes': note
    }
    
    return result

def parse_scraper(html):
    soup = BeautifulSoup(html, 'html.parser')
    right = soup.find('div', attrs={'class': 'right'})
    right_divs = right.find_all('div' , attrs={'class': 'content'})

    result = []

    right_div_content_normal = right_divs[3] # normal monster
    right_div_content_indent = right_div_content_normal.find('div', attrs={'class': 'indent'})
    right_div_content_indent_p = right_div_content_indent.find_all('p')
    for el in right_div_content_indent_p:
        result.append(parse_table(el))

    right_div_content_boss = right_divs[4] # boss monster
    right_div_content_indent = right_div_content_boss.find('div', attrs={'class': 'indent'})
    right_div_content_indent_p = right_div_content_indent.find_all('p')
    for el in right_div_content_indent_p:
        result.append(parse_table(el))


    return result


url = 'https://suikosource.com/games/gs1/guides/bestiary.php'

html = requests.get(url).content
result = parse_scraper(html)
json = json.dumps(result, indent=4) 
with open('suikoden_bestiary.json', 'w') as f:
    f.write(json)
