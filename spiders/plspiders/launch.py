import requests
from lxml import etree
import pymongo
from datetime import datetime


if __name__ == "__main__":
    # 获取数据
    url = 'https://soccer.hupu.com/table/England.html'
    strhtml = requests.get(url)
    # print(str(strhtml.content,'utf-8'))
    # 解析数据
    html = etree.HTML(str(strhtml.content,'utf-8'))
    # html = etree.HTML(text)
    # clprint(html)
    result1 = html.xpath('//*[@id="main_table"]/tbody/descendant::tr')
    dictlist = []
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    for index in range(len(result1)):
        # 球队名
        namestr = '//*[@id="main_table"]/tbody/tr['+str(index+1)+']/td['+str(3)+']/a/text()'
        name = html.xpath(namestr)
        # 场次
        scenestr = '//*[@id="main_table"]/tbody/tr['+str(index+1)+']/td['+str(4)+']/text()'
        scene = html.xpath(scenestr)
        # 胜
        winstr = '//*[@id="main_table"]/tbody/tr['+str(index+1)+']/td['+str(5)+']/text()'
        win = html.xpath(winstr)
        # 平
        flatstr = '//*[@id="main_table"]/tbody/tr['+str(index+1)+']/td['+str(6)+']/text()'
        flat = html.xpath(flatstr)
        # 负
        losestr = '//*[@id="main_table"]/tbody/tr['+str(index+1)+']/td['+str(7)+']/text()'
        lose = html.xpath(losestr)
        # 进球
        goalstr = '//*[@id="main_table"]/tbody/tr['+str(index+1)+']/td['+str(8)+']/text()'
        goal = html.xpath(goalstr)
        # 失球
        fumblestr = '//*[@id="main_table"]/tbody/tr['+str(index+1)+']/td['+str(9)+']/text()'
        fumble = html.xpath(fumblestr)
        dict = {
            'name' : name[0],
            'scene' : int(scene[0]),
            'win': int(win[0]),
            'flat': int(flat[0]),
            'lose': int(lose[0]),
            'goal': int(goal[0]),
            'fumble': int(fumble[0]),
            'create_time': now
        }
        dictlist.append(dict)
    #print(dictlist)
    # 保存到数据库中
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["football"]
    mycol = mydb["pl_orign_data"]
    x = mycol.insert_many(dictlist)
    print('保存成功'+str(x))