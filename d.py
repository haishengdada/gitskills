import threading
import queue
import requests
from lxml import etree
import pymysql
import random
import time


url_a = "https://zz.fang.anjuke.com/loupan/all/p"
url_b = '/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
}
conn = pymysql.connect(host='39.105.8.184', port=3306, user='root', password='xinhu9795', db='yhs', charset='utf8')
cursor = conn.cursor()
for i in range(1, 22):
    url = url_a + str(i) + url_b
    reponses = requests.get(url, headers=headers).content.decode()
    # print(reponses)
    html = etree.HTML(reponses)
    houses_ls = html.xpath("//div[@class='item-mod ']")
    # print(houses_ls)
    # print(len(houses_ls))
    # print(etree.tostring(houses_ls).decode())
    for i in houses_ls:
        title = i.xpath(".//div[@class='infos']/a/h3/span/text()")[0]
        print(title)
        ban_kuai1 = i.xpath(".//div[@class='infos']/a[@class='address']/span/text()")[0]
        ban_kuai = ban_kuai1.split("]")[0].split("[")[1].split()
        b = ''
        for q in ban_kuai:
            b += q
        di_zhi = ban_kuai1.split("]")[1]
        print(b, di_zhi)
        hu_xing = i.xpath(".//div[@class='infos']/a[@class='huxing']/span/text()")
        # print(hu_xing)
        a = ''
        for j in hu_xing:
            a += j
            # bedroom = "insert into house_price(hu_xing) values ('%s')" % (j)
            # cursor.execute(bedroom)
            # conn.commit()
        print(a)
        price2 = i.xpath(".//a[@class='favor-pos']/p/text()")
        if len(price2) != 0:
            price2 = price2[0]
        price1 = i.xpath(".//a[@class='favor-pos']/p/span/text()")
        if len(price1) != 0:
            price1 = price1[0]
        price = str(price2) + str(price1)
        print(price)
        guan_jian_ci = i.xpath(".//div[@class='infos']/a[@class='tags-wrap']/div[@class='tag-panel']/i/text()")
        guan_jian_ci1 = i.xpath(".//div[@class='infos']/a[@class='tags-wrap']/div[@class='tag-panel']/span/text()")
        c = ''
        d = ','
        for w in guan_jian_ci:
            c += w
            c += d
        for e in guan_jian_ci1:
            c += e
            c += d
        print(c)
        houses_item = "insert into house_price(title,ban_kuai,address,price,guan_jian_ci,hu_xing) values ('%s','%s','%s','%s','%s','%s')" % (title, b, di_zhi, price, c, a)
        cursor.execute(houses_item)


print("")