from flask import Flask,render_template

app = Flask(__name__)
app.secret_key = '123'
from server.mock import home
app.register_blueprint(home,url_prefix='/home')

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=1314,debug=True)
