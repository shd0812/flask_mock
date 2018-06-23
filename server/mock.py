import json
from flask import Flask
from flask import request, make_response,jsonify
app = Flask(__name__)
users_dict = {}
@app.route('/',methods=['GET','POST'])
def home():
    return 'Hello world!'
@app.route('/api/users/<int:uid>', methods=['GET'])
def get_user(uid):
    print('看看%s' %uid)
    user = users_dict.get(uid)
    print(user,users_dict)
    if user :
        success = True
        status_code = 200


    else:
        success = False
        status_code = 404
    result = {
        'success': success,
        'data': user
    }
    response = make_response(json.dumps(result),status_code)
    response.headers["Content-Type"] = "application/json"
    print('返回结果%s' %response.data)
    return response

@app.route('/api/users/<int:uid>', methods=['POST'])
def create_user(uid):
    user = request.get_json()

    print(user)
    if uid not in users_dict:
        result = {
            'success': True,
            'msg': "user created successfully."
        }
        status_code = 201
        users_dict[uid] = user
    else:
        result = {
            'success': False,
            'msg': "user already existed."
        }
        status_code = 500
    print(users_dict)
    response = make_response(json.dumps(result), status_code)
    print(response)
    response.headers["Content-Type"] = "application/json"
    return response

@app.route('/api/users/<int:uid>', methods=['PUT'])
def update_user(uid):
    user = users_dict.get(uid, {})
    if user:
        user = request.get_json()
        success = True
        status_code = 200
    else:
        success = False
        status_code = 404
    result = {
        'success': success,
        'data': user
    }
    response = make_response(json.dumps(result), status_code)
    response.headers["Content-Type"] = "application/json"
    return response

if __name__ =='__main__':
    app.run(debug=True)