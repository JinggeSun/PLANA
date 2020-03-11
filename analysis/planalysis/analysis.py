import pymongo
from datetime import datetime
import alg


if __name__ == "__main__":
    # 从数据库中获取数据
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["football"]
    mycol = mydb["pl_orign_data"]
    # 获取当天的数据
    q1={"create_time":{"$gt" : '2020-03-10 00:00:00'}}   
    l1=list(mycol.find(q1))

    l2 = []

    for data in l1:
        _id = data['_id']
        name  = data['name']
        scene = data['scene']
        win = data['win']
        flat = data['flat']
        lose = data['lose']
        goal = data['goal']
        fumble = data['fumble']
        #调用算法
        datadb = {}
        datadb['_id'] = _id
        datadb['win_goal'] = alg.win_goal_alg(goal,fumble)
        datadb['avg_goal'] = alg.avg_goal_agl(goal,scene)  
        datadb['avg_fumble'] = alg.avg_fumble_agl(fumble,scene)
        datadb['avg_total'] = alg.avg_total_alg(datadb['avg_goal'],datadb['avg_fumble'])
        datadb['integral'] = alg.integral_alg(win,flat,lose)
        datadb['avg_integral'] = alg.avg_integral_alg(datadb['integral'],scene)
        l2.append(datadb)
    #调用排名算法
    result_list = alg.rank_alg(l2)
    print(result_list)
    for data in result_list:
        # 根据id更新
        myquery = { "_id": data['_id'] }
        result = mycol.update_one(myquery, {'$set': data}, True)  
