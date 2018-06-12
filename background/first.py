from flask import Blueprint,render_template,request,jsonify


one = Blueprint('xnho', __name__)

@one.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')

@one.route('/next', methods=['GET', 'POST'])
def next():
    return '1222'