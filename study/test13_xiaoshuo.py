# _*_ coding:UTF-8 _*_
import requests
import lxml
from bs4 import BeautifulSoup
'''
if __name__ == '__main__':
    target = 'https://www.bqkan8.com/1_1094/5403177.html'
    req = requests.get(url=target)
    html=req.text
    bf = BeautifulSoup(html)
    texts = bf.find_all('div',class_='showtxt')
    print(texts[0].text.replace('\xa0'*8,'\n\n'))
'''
if __name__ == '__main__':
    target = 'https://www.bqkan8.com/1_1094/'
    req = requests.get(url=target)
    html=req.text
    div = BeautifulSoup(html).find_all('div',class_='listmain')
    print(div[0])