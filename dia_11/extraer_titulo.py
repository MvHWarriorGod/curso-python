import bs4
import requests

resultado = requests.get('https://escueladirecta-blog.blogspot.com/')

soup = bs4.BeautifulSoup(resultado.text, 'lxml')

print(soup.select('title')[0].getText())