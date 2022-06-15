KEYWORDS = ['дизайн', 'фото', 'web', 'python']
HEADERS = {
    'Cookie': '_ym_uid=1639148487334283574; _ym_d=1639149414; _ga=GA1.2.528119004.1639149415; _gid=GA1.2.512914915.1639149415; habr_web_home=ARTICLES_LIST_ALL; hl=ru; fl=ru; _ym_isad=2; __gads=ID=87f529752d2e0de1-221b467103cd00b7:T=1639149409:S=ALNI_MYKvHcaV4SWfZmCb3_wXDx2olu6kw',
    'Accept-Language': 'ru-RU,ru;q=0.9',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Cache-Control': 'max-age=0',
    'If-None-Match': 'W/"37433-+qZyNZhUgblOQJvD5vdmtE4BN6w"',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36',
    'sec-ch-ua-mobile': '?0'
}

import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    ret = requests.get('https://habr.com/ru/all/', headers=HEADERS)
    soup = BeautifulSoup(ret.text, 'html.parser')

    posts = soup.find_all('article')

    for post in posts:
        text_list = sorted(post.text.lower().split(' '))
        if set(text_list).intersection(KEYWORDS) != set():
            post_url = post.find(class_='tm-article-snippet__readmore').get('href')
            post_date = post.find('time').text
            post_title = post.find('h2').text
            print(f'{post_date} - {post_title} - https://habr.com{post_url}')
            
    # Дополнительное задание
    
    print('----------Дополнительное задание----------')
    for post in posts:
        post_url = post.find(class_='tm-article-snippet__readmore').get('href')
        ret_post = requests.get(f'https://habr.com{post_url}', headers=HEADERS)
        soup_post = BeautifulSoup(ret_post.text, 'html.parser')
        article = soup_post.find('article')
        article_text_list = sorted(article.text.lower().split(' '))
        if set(article_text_list).intersection(KEYWORDS) != set():
            article_date = article.find('time').text
            article_title = article.find('h1').text
            print(f'{article_date} - {article_title} - https://habr.com{post_url}')

