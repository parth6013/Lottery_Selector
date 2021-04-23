from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def hello_world():
    return 'hello,world'

@app.route('/try', methods=['GET', 'POST'])
@cross_origin()
def index():
    number = int(request.json['key'])
    list=request.json['work']
    print(number)
    print(list)
    
    l2=[]
    import random
    while(number>0):
        y=random.choice(list)
        l2.append(y)
        list.remove(y)
        
        number=number-1
    l3={
        "names":l2
    }
    return jsonify(l3)
    

 

# @app.route('/function/n')
# number=int(n)
# def random(number):
#     list=["hello","lolo","bolo"]
#     l2=[]
#     import random
#     while(number>0):
#         y=random.choice(list)
#         l2.append(y)
#         list.remove(y)
        
#         number=number-1
#     l3={
#         "names":l2
#     }
#     return jsonify(l3)



if __name__ == '__main__':
    app.run(debug=True)