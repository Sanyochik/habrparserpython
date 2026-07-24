import requests

def parcehabr (count):
    i = 1
    habr = requests.get('https://habr.com/ru/feed/').text
    print("Последние темы с сайта habr.com")
    while i <= count and i <= 17:
        title_start = habr.find('"tm-title__link"')+48
        habr = habr[title_start:]
        title_end = habr.find('</span>')
        title = habr[0:title_end]
        i+=1
        print (f"Название темы: {title}")
parcehabr(30)