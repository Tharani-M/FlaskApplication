from flask import Flask,render_template,request
from flask import abort
from markupsafe import escape
import json
from db import user,books

app = Flask(__name__)


@app.route('/')
def loginpage():
    return render_template('index.html')

@app.route('/user',methods=["GET","POST"])
def getusers():
    if request.method == "GET":
         return user
    if request.method == "POST":
        request_data = request.get_json()
        
        user.append(request_data)
        return json.dumps(user,indent=2)
    
@app.route('/<email>',methods=["GET","POST"])
def postusers(email):
     global user
     req = request.get_json()
     if request.method == "GET":
          for u in user:
               if u['email'] == email:
               
                    return json.dumps(u,indent=2)

          else:
               abort(404,message="Data is not available")
     if request.method == "POST":
          for u in user:
               if u['email'] == email:
                    u =  req
                    user += req
                    return json.dumps(u,indent=2)
          else:
               abort(404,message="Data is not available")

@app.put('/<email>')
def updateuser(email):
    global user
    req = request.get_json()
    for u in user:
               if u['email'] == email:
                    u.update(req)                  
                    return json.dumps(user,indent=2)
    else:
         abort(404,message="Data is not available")

@app.delete('/<email>')
def deluser(email):
    global user
    for u in user:
               if u['email'] == email:                  
                    user.remove(u)
                    return json.dumps(user,indent=2)
    else:
               abort(404,"Data is not available") 
        
@app.route('/<string:email>')
def getuser(email):
    # print(user)
    # return f'User {escape(email)}'
    # for i in user:ö
    if user['email'] == email:
            return json.dumps(user['usertype'],indent=2)
    
    
# GET,POST,PUT,DELETE requests in books

@app.route('/api/books',methods=['GET','POST'])
def getsetbooks():
      global books
      if request.method == "GET":
            return json.dumps(books,indent=2)
      if request.method == "POST":
            req_book = request.get_json()
            books.append(req_book)
            return json.dumps(books,indent=2)

@app.route('/api/books/<int:book_id>',methods=['GET','POST'])
def specificbooks(book_id):
      global books
      if request.method == 'GET':
             for b in books:
                   if b['book_id'] == book_id:
                         return json.dumps(b,indent=2)
      if request.method == 'POST':
            req_book_up = request.get_json()
            for b in books:
               if b['book_id'] == book_id: 
                        b.update(req_book_up)
                        return  json.dumps(books,indent=2)

@app.put('/api/books/<int:bookid>')
def updatebookinfo(bookid):
      global books
      for b in books:
               if b['book_id'] == bookid: 
                     book_info_up = request.get_json()
                     b.update(book_info_up)
                     return  json.dumps(books,indent=2)

@app.delete('/api/books/<int:bookid>')
def deletebookinfo(bookid):
      global books
      for b in books:
               if b['book_id'] == bookid: 
                     books.remove(b)
                     return  json.dumps(books,indent=2)


    
                      