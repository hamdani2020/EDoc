from flask import Flask, render_template, request, session, Response, redirect, url_for, make_response
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

#app.secret_key = 'rushi'

app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///EDoc.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)
app.app_context().push()

class edoc(db.Model):
    sno = db.Column(db.Integer, primary_key=True)   
    name = db.Column(db.String(80), nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(80), nullable=False)
    Age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(50), nullable=False)
    height = db.Column(db.Integer, nullable=False)
    Weight = db.Column(db.Integer, nullable=False)
    bloodgroup = db.Column(db.String(50), nullable=False)

    def __repr__(self) -> str:
        return f"{self.sno} {self.name} {self.phone} {self.email} {self.Age} {self.gender} {self.height} {self.Weight} {self.bloodgroup}"
    

class Appoinment(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    appoinmentname = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    doctor = db.Column(db.String(80), nullable=False)
    message = db.Column(db.String(250), nullable=False)
    def __repr__(self) -> str:
        return f"{self.sno} {self.appoinmentname} {self.email} {self.doctor} {self.message}"
    
class Contact(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    message = db.Column(db.String(250), nullable=False)
    def __repr__(self) -> str:
        return f"{self.sno} {self.name} {self.email} {self.message}"

@app.route('/')
def hello_world():
    # return 'Hello, World!'
    return render_template('index.html')

@app.route('/contact', methods=["GET", "POST"])
def contact():
    # return 'Hello, World!'
    if request.method == 'POST':
        # gender = request.form['gender']
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        rushi = Contact(name=name, email=email, message=message)
        db.session.add(rushi)
        db.session.commit()
    return render_template('return3.html')

@app.route('/form', methods=["GET", "POST"])
def form():
    print("inside function")
    if request.method == 'POST':
        # gender = request.form['gender']
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']
        print(name)
        Age = request.form['Age']
        print(Age)
        gender = request.form['gender']
        print(gender)
        height = request.form['height']
        Weight = request.form['Weight']
        bloodgroup = request.form['bloodgroup']
        print("Entered in loop")
        rusih = edoc(name=name, phone=phone, email=email, Age=Age, gender=gender, height=height, Weight=Weight, bloodgroup=bloodgroup)
        db.session.add(rusih)
        # db.session.commit()   
        print("Executed")
        db.session.commit()
        return render_template('return.html')

    # return 'Hello, World!'
    return render_template('form.html')

@app.route('/login')
def login():
    # return 'Hello, World!'
    # if request.method == "POST":
        

    return render_template('login.html')


@app.route('/videocall')
def videocall():
    # return 'Hello, World!'
    return render_template('videocall.html')

@app.route('/doctinfo1')
def doctinfo1():
    # return 'Hello, World!'
    return render_template('doctinfo1.html')

@app.route('/doctinfo2')
def doctinfo2():
    # return 'Hello, World!'
    return render_template('doctinfo2.html')

@app.route('/doctinfo3')
def doctinfo3():
    # return 'Hello, World!'
    return render_template('doctinfo3.html')

@app.route('/docs')
def docs():
    # return 'Hello, World!'
    return render_template('docs.html')

@app.route('/gmeet')
def gmeet():
    # return 'Hello, World!'
    return render_template('gmeet.html')

@app.route('/appoinment', methods=["GET", "POST"])
def appoinment():
    if request.method == 'POST':
        # gender = request.form['gender']
        appoinmentname = request.form['appoinmentname']
        email = request.form['email']
        doctor = request.form['doctor']
        message = request.form['message']
        bookappoinment = Appoinment(appoinmentname=appoinmentname, email=email, doctor=doctor, message=message)
        db.session.add(bookappoinment)
        # db.session.commit()   
        print("Executed")
        db.session.commit()
        return render_template('return2.html')
    # return 'Hello, World!'
    return render_template('appoinment.html')

if __name__ =="__main__":
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5007)
