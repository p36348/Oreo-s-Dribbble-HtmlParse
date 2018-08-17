from bs4 import BeautifulSoup
import re
import json


def parse_shot(shot):
    print('============ parsing shot ============')
    # print(shot)
    main = shot.find('div', {'class': 'dribbble-shot'})
    _id = re.sub(r'screenshot-', '', shot['id'])
    img = main.find('picture').find('img')['src']
    title = main.find('a', {'class': 'dribbble-over'}).find('strong').string
    comment = main.find('span', {'class': 'comment'}).string
    fav = main.find('li', {'class': 'fav'}).find('a').string
    cmnt = re.sub(r'\n|\s', '', main.find('li', {'class': 'cmnt'}).find('span').string)
    views = main.find('li', {'class': 'views'}).find('span').string
    print(cmnt)
    shot_json = {'img': img,
                 'title': title,
                 'id': _id,
                 'comment': comment,
                 'fav': fav,
                 'views': views,
                 'cmnt': cmnt}
    print('============ parsed shot ============')
    return shot_json


if __name__ == "__main__":
    # html已经保存到了本地
    html = open('resources/dribbble.html', 'r')

    html_page = html.read()

    html.close()

    soup = BeautifulSoup(html_page, 'html.parser')
    img_links = soup.find_all('img')
    dribbble_shots = soup.find_all('li', {'class': r'group'})
    shot_array = list(map(parse_shot, dribbble_shots))

    print(len(shot_array), shot_array)

    result = open('output/shot_array.json', 'w')
    result.write(json.dumps(shot_array))
    result.close()

