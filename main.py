# from https://www.geeksforgeeks.org/setting-up-google-cloud-sql-with-flask/


import os

from flask import Flask, request, make_response
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

PASSWORD = "testtest"
PUBLIC_IP_ADDRESS = "34.80.17.223"
DBNAME = "dances"
PROJECT_ID = "gcp-mysql-python"
INSTANCE_NAME = "gcp-mysql-python:asia-east1:gcp-mysql"

# configuration
app.config["SECRET_KEY"] = "yoursecretkey"
# app.config["SQLALCHEMY_DATABASE_URI"]= f"mysql + mysqldb://root:{PASSWORD}@{PUBLIC_IP_ADDRESS}/{DBNAME}?unix_socket =/cloudsql/{PROJECT_ID}:{INSTANCE_NAME}"
app.config["SQLALCHEMY_DATABASE_URI"]= f"mysql://root:{PASSWORD}@{PUBLIC_IP_ADDRESS}/{DBNAME}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]= True

db = SQLAlchemy(app)


# User ORM for SQLAlchemy
class Dances(db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    dances = db.Column(db.String(50), nullable = False)
 
@app.route('/add', methods =['POST'])
def add():
    dance = request.form.get('dance')
 
    # checking if user already exists
    dance = Dances.query.filter_by(dances = dance).first()
 
    if not dance:
        try:
            # creating Users object
            user = Dances(
                name = name,
                email = email
            )
            # adding the fields to users table
            db.session.add(user)
            db.session.commit()
            # response
            responseObject = {
                'status' : 'success',
                'message': 'Successfully registered.'
            }
 
            return make_response(responseObject, 200)
        except:
            responseObject = {
                'status' : 'fail',
                'message': 'Some error occured !!'
            }
 
            return make_response(responseObject, 400)
         
    else:
        # if user already exists then send status as fail
        responseObject = {
            'status' : 'fail',
            'message': 'User already exists !!'
        }
 
        return make_response(responseObject, 403)
 
@app.route('/view')
def view():
    # fetches all the users
    dances = Dances.query.all()
    # response list consisting user details
    response = list()
 
    for dance in dances:
        response.append({
            "name" : dance.dances,
        })
 
    return make_response({
        'status' : 'success',
        'message': response
    }, 200)

@app.route('/')
def home():
    return ("hello please view my fances")
 
 
if __name__ == "__main__":
    # serving the app directly
    app.run()


# @app.route("/")
# def hello_world():
#     name = os.environ.get("NAME", "World")
#     return "Hello {}!".format(name)

# @app.route("/<username>")
# def hello(username):
#     return "Hello {}!".format(username)


# if __name__ == "__main__":
#     app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))