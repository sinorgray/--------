import requests
from bs4 import BeautifulSoup

url = 'https://qiita.com/tags?page='
pageLength = 10
rank = 0
for page in range(pageLength):
    req = requests.get(url+str(page))                    #・・・①
    soup = BeautifulSoup(req.content, "html.parser")     #・・・②
    tagsData = soup.findAll('div',class_='TagList__item')#・・・③
    for tagData in tagsData:
        rank +=1
        count = tagData.get('data-count')                #・・・④
        tagText = tagData.text                           #・・・⑤
        print(rank,'位：',tagText,'  ',count,'件')