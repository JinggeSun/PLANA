from flask import Flask,render_template,jsonify
import json
import pymongo
from bson import json_util


app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')


@app.route("/list",methods=['GET'])
def data_list():

    mycol = mongodb()

    q1={"create_time":{"$gt" : '2020-03-10 00:00:00'}}   
    l1=list(mycol.find(q1))
    print(l1)
    data = {'data': l1}
    return json_util.dumps(data)

    #return jsonify(l1)

def mongodb():
     # 从数据库中获取数据
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["football"]
    mycol = mydb["pl_orign_data"]
    return mycol


if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=8080)
