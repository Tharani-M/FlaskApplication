from flask import Flask,render_template,request
from markupsafe import escape

app = Flask(__name__)
user={"fname":'def_fname1',
      'lname':'def_lname1',
      'email': 'def_email1@gmail.com',
      'phone_number':'12345565',
      'password':'ks1',
      'usertype':'seller'}
#       {"fname":'def_fname2',
#       'lname':'def_lname2',
#       'email': 'def_email2@gmail.com',
#       'phone_number':'12345565',
#       'password':'ks2',
#       'usertype':['seller','buyer']},
#       {"fname":'def_fname3',
#       'lname':'def_lname3',
#       'email': 'def_email3',
#       'phone_number':'12345565',
#       'password':'ks3',
#       'usertype':'seller'} 
# ]

@app.route('/')
def getusers():
    return render_template('index.html')

@app.route('/user',methods=["GET","POST"])
def users():
    if request.method == "POST":
        # user['fname']= request.form['first_name']
        # user['lname'] = request.form['last_name']
        # user['email'] = request.form['email']
        # user['phone_number'] = request.form['phone']
        # user['password']= request.form['password']
        # user['usertype'] = request.form['usertype']
        request_data = request.get_json()
        user['fname']=request_data['first_name']
        user['lname'] = request_data['last_name']
        user['email'] =request_data['email']
        user['phone_number'] = request_data['phone']
        user['password']= request_data['password']
        user['usertype'] = request_data['usertype']
        return render_template('loggedin.html',u= request_data)
    
@app.route('/<string:email>')
def getuser(email):
    # print(user)
    # return f'User {escape(email)}'
    # for i in user:ö
    if user['email'] == email:
            return user['usertype']


