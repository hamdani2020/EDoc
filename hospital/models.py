from hospital import db


class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    First_Name = db.Column(db.String(length = 50), nullable=False)
    Last_Name = db.Column(db.String(length = 50), nullable=False)
    Email = db.Column(db.String(length = 50), nullable=False, unique = True)
    Number = db.Column(db.String(length = 50), nullable=False, unique = True)
    Address = db.Column(db.String(length = 50), nullable=False, unique =  True)
    Prescription_info = db.Column(db.String(length = 1050), nullable=False, unique = False)
    
    def __init__(self,First_Name,Last_Name,Email,Number,Address,Prescription_info):
        self.First_Name = First_Name
        self.Last_Name = Last_Name
        self.Email = Email
        self.Number = Number
        self.Address = Address
        self.Prescription_info = Prescription_info

    def __repr__(self):
        return "{} {}".format(self.First_Name,self.Last_Name) 

class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    First_Name = db.Column(db.String(length = 50), nullable=False)
    Last_Name = db.Column(db.String(length = 50), nullable=False)
    Number = db.Column(db.String(length = 50), nullable=False, unique = True)
    Address = db.Column(db.String(length = 50), nullable=False, unique = True)

    def __init__(self,First_Name,Last_Name,Number,Address):
        self.First_Name = First_Name
        self.Last_Name = Last_Name
        self.Number = Number
        self.Address = Address

    def __repr__(self):
        return "{} {}".format(self.First_Name,self.Last_Name) 

class Appointment_Dates(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Doctor = db.Column(db.String(length = 50), nullable=False)
    Patient = db.Column(db.String(length = 50), nullable=False)
    Time = db.Column(db.String(length = 20), nullable=False)
    Date = db.Column(db.String(length = 20), nullable=False)


    def __init__(self,Doctor,Patient,Time,Date):
        self.Doctor = Doctor
        self.Patient = Patient
        self.Time = Time
        self.Date = Date

db.create_all()