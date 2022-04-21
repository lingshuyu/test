import os
import urllib.request

def get_page(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36')
    response= urllib.request.urlopen(url)
    html= response.read().decode('utf-8')

    a=html.find('current-comment-page')+23
    b=html.find(']',a)
    print(html[a:b])
def find_imgs(url):
    pass

def save_imgs(folder,img_addrs):
    pass

def download_mm(folder='ooxx',pages=10):
    os.mkdir(folder)
    os.chdir(folder)

    url='http://jandan.net/ooxx'
    page_num = int(get_page(url))

    for i in range(pages):
        page_num -= i
        page_url=url+'pages_'+str(page_num)+'#comment'
        img_addrs = find_imgs(page_url)
        save_imgs(folder,img_addrs)

    if __name__ == '__main__':
        download_mm()