from flask import Flask,redirect,url_for,render_template,request,jsonify
import pymongo
from flask_pymongo import PyMongo
import bson.json_util
import json
import passlib.hash

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/Details"
mongo = PyMongo(app)

# def connectdb():
#     MONGO_URI = "mongodb://localhost:27017/"
#     client = pymongo.MongoClient(MONGO_URI)
#     db = client['Details']
#     collection = db['coded']
#     return collection


@app.route('/')
def home():
    
    return render_template('index.html')


# # Database connection details (replace with your actual credentials)
# client = pymongo.MongoClient("mongodb://localhost:27017/")  # Connect to MongoDB
# db = client["Details"]  # Replace with your database name
# collection = db["MedicalRecords"]  # Replace with your collection name

def connectdb():
    return collection  # Return the collection object

@app.route('/login', methods=['GET', 'POST'])
def login():
    # collection = connectdb()
    if request.method == 'POST':
        mail = request.form['mail']
        name = request.form['name']
        password = request.form['password']
        user_type = request.form['user_type']

        # Input validation (basic example)
        if not mail or not password or not user_type:
            return render_template('login.html', error="Please fill in all fields.")

        # Secure password comparison (replace with a hashing mechanism)
        # This is a placeholder for illustration, use a secure hashing library like passlib
        # and store hashed passwords in the database.

        if mail in db.coded.find_one({'mail': mail})['mail'] and password == db.coded.find_one({'mail': mail})['password']:
            # Successful login

            return render_template('profile.html', name= name,mail=mail, user_type=user_type)
        else:
            # Invalid credentials
            return render_template('login.html', error="Invalid email or password.")

    return render_template('login.html')


@app.route('/signin',methods=['GET' , 'POST'] )
def signin(): 
    user_data = []
    if request.method=='POST':
        pa = request.form['password']
        hasher = passlib.hash.bcrypt.using(rounds=12)  # Adjust rounds as needed
        hashed_password = hasher.hash(pa) 
        data2 ={ 'nithn' : 'hi' , 'password' :hashed_password ,}

        
        mongo.db.MedicalRecords.insert_one(user_data)
        # return data2,'success'

        # db.coded.insert_one(bson.json_util.dumps(data2))
        
        name = request.form['name']
        password = request.form['password']
        user_type= request.form['user_type']
        mail = request.form['mail']
        data = {'name' : name, 'password': password,'mail': mail,'user_type': user_type}
        user_data.append(data)

        
        # store = db.coded.insert_one(jsonify(data2))
        # print(request.form)
        # user_data = request.form

        # db.coded.insert_many(user_data)
        # # return request.form
        # # for item in data:
        # #     print(data[item])
        # #     return data[item]
            
        # if not name or not mail or not password or not user_type:
        #     return render_template('signin.html', error="Please fill in all fields.")
        
        # user_data = request.form


        # return render_template('signin.html', success="Registration successful!", name=name, mail=mail, user_type=user_type)
    return render_template('signin.html')

@app.route('/appointments')
def appointments():

    return render_template('appointments.html')

@app.route('/profile')
def profile():

    return render_template('profile.html')

@app.route('/healthdetails')
def health_details():
    return render_template("health_details.html")


@app.route('/try',methods=['GET' , 'POST'] )
def sign():
    user_data = []
    if request.method=='POST':
        print(request.form)
        return request.form

if __name__ == '__main__':
    app.run(debug=True)
