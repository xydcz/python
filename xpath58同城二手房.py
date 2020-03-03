from lxml import etree
import requests

if __name__ == "__main__":
    url = 'https://wh.58.com/jianghan/chuzu/'
    #url = 'https://wh.58.com/ershoufang/'
    header = {
        "User-Agent": "Mozilla/5.0 (Windows 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
        }  

    page_text = requests.get(url=url,headers=header).text

    #数据解析
    tree = etree.HTML(page_text)
    #存储的房间列表对象
    #li_list = tree.xpath('//ul[@class="house-list-wrap"]/li')
    li_list = tree.xpath('//ul[@class="house-list"]/li')
    fp = open('./58tc.txt','w',encoding='utf-8')
    for li in li_list:
        #fp.write(li.xpath('./div[2]/h2/a/text()')[0])
        print(li.xpath('./div[2]/h2/a/text()')[0])

