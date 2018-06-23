from flask import Flask
from flask import request, Response, jsonify
import random
import string


app = Flask(__name__)

# 请求方式错误
method_err = {
    "code": 301,
    "msg": "请求方式不正确，只支持post请求"
}
# 参数错误
param_err = {
    "code": 302,
    "msg": "请求参数错误，请检查入参"
}
# 余额不足
money_err = {
    "code": 303,
    "msg": "账户余额不足"
}

# 价格错误
price_err = {
    "code": 304,
    "msg": "价格不合法"
}

# 用户不存在
user_err = {
    "code": 305,
    "msg": "该用户不存在"
}

# 成功的信息
success_msg = {
    "code": 200,
    "msg": "支付成功"
}

# 数据库异常
db_err = {
    "code": 306,
    "msg": "数据库错误"
}
@app.route('/pay',methods=['POST','GET'])
def pay():
    if request.method != 'POST':  # 如果不是post请求的话，返回请求类型错误
        return jsonify(method_err)
    else:
        user_id = request.values.get('user_id')
        #使用request.values.get获取到传入的参数，user_id
        price = request.values.get('price')
        list_dic={
            'name':'shen',
            "status_code":200,
            "result":{
                'age':26,
                'sex':'man'
            }
        }
        print(list_dic['result']['age'])
        #list_dic['name']='shen'
        return jsonify(list_dic)

if __name__ == '__main__':
    app.run(debug=True)