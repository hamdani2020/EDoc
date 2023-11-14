from hospital import app,db
from flask import render_template,request,redirect,url_for,flash
from hospital.models import Doctor,Patient,Appointment_Dates
from hospital.forms import UpdateDoctor,UpdatePatient,AddDoctor
from wtforms import SubmitField,DateField,TimeField
from wtforms_sqlalchemy.fields import QuerySelectField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired

def doc():
    '''
    Returns the Doctor query in the rep form
    '''
    return Doctor.query

def patient_():
    '''
    returns patient query in the rep form
    
    '''
    return Patient.query

class Appt(FlaskForm):
    '''
    Used Flaskforms module for Booking appointments
    '''
    Doctor = QuerySelectField("Doctor's Name",query_factory=doc,allow_blank='False')
    Patient = QuerySelectField("Patient's Name",query_factory=patient_,allow_blank='False')
    Date = DateField("Appointment Date",format="%Y-%m-%d",validators=(DataRequired(),))
    Time = TimeField("Appointment Time",validators=(DataRequired(),))
    Submit = SubmitField()


@app.route('/')
def home():
    '''
    Returns the home page of the web application
    '''
    return render_template('home.html')


@app.route('/patient')
def patient():
    '''
    Returns all the patients in the Patients database
    '''
    items = Patient.query.all()
    return render_template('patient.html',items=items)


@app.route('/updatepatient/<int:id>',methods=['GET','POST'])
def update_patient(id):
    '''
    Updating info about the patient using POST
    Including the unique id of the specific patient in the parameters to update
    '''
    form = UpdatePatient()
    patientupdate = Patient.query.get(id)
    if request.method == "POST":
        patientupdate.Email = request.form['email']
        patientupdate.Number = request.form['number']
        patientupdate.Address = request.form['address']
        patientupdate.Prescription_info = request.form['prescription']
        db.session.commit()  #Save changes to the db
        flash("Patient Updated Successfully!")
        return render_template("updatepatient.html",form=form,patientupdate=patientupdate)
    return render_template("updatepatient.html",form=form,patientupdate=patientupdate)

@app.route('/addpatient',methods=['GET','POST'])
def addpatient():
    '''
    Addint new patient into the database
    '''
    form = UpdatePatient()
    if form.validate_on_submit():
        patient = Patient(First_Name=form.firstname.data, Last_Name=form.lastname.data, Email=form.email.data, Number=form.number.data, Address=form.address.data, Prescription_info=form.prescription.data)
        db.session.add(patient)
        db.session.commit()
        flash("Patient Succesfully Added!")
        return redirect(url_for("patient"))
    return render_template("addpatient.html",form=form)
    
@app.route('/deletepatient/<int:id>',methods=['GET','POST'])
def deletepatient(id):
    '''
    deleting patient from database
    '''
    patient = Patient.query.get(id)
    db.session.delete(patient)
    db.session.commit()
    flash("Patient Successfully Deleted")
    return redirect(url_for('patient'))


@app.route('/doctor')
def doctor():
    '''
    Returns the doctors in the Doctor database
    '''
    items = Doctor.query.all()
    return render_template('doctor.html',items=items)

@app.route('/adddoctor',methods=['GET','POST'])
def adddoctor():
    '''
    Adds new Doctors to the db
    '''
    form = AddDoctor()
    if form.validate_on_submit():
        doctor = Doctor(First_Name=form.firstname.data, Last_Name=form.lastname.data,Number=form.number.data, Address=form.address.data)
        db.session.add(doctor)
        db.session.commit()
        flash("Doctor Succesfully Added!")
        return redirect(url_for("doctor"))
    return render_template("adddoctor.html",form=form)

@app.route('/updatedoctor/<int:id>',methods=['GET','POST'])
def update_doctor(id):
    '''
    Parmeters: id of the specific doctor user wants to update
    Updates Doctors to the db
    '''
    form = UpdateDoctor()
    doctorupdate = Doctor.query.get(id)
    if request.method == "POST":
        doctorupdate.Number = request.form['number']
        doctorupdate.Address = request.form['address']
        db.session.commit()
        flash("Patient Updated Successfully!")
        return render_template("updatedoctor.html",form=form,doctorupdate=doctorupdate)
    return render_template("updatedoctor.html",form=form,doctorupdate=doctorupdate)

@app.route('/deletedoctor/<int:id>',methods=['GET','POST'])
def deletedoctor(id):
    '''
    Parameter: id of specific doctor user wants to delete
    Used to delete doctor from the database
    '''
    doctor = Doctor.query.get(id)
    db.session.delete(doctor)
    db.session.commit()
    flash("Doctor Successfully Deleted")
    return redirect(url_for('doctor'))

@app.route('/appointment')
def appointment():
    '''
    Returns all the appointment query in the database
    '''
    items = Appointment_Dates.query.all()
    return render_template('appointment.html',items=items)

@app.route('/deleteappointment/<int:id>',methods=['GET','POST'])
def deleteappointment(id):
    '''
    Parameter: unique id of the appointment user wants to delete 
    Used to delete the appointment form database
    '''
    appt = Appointment_Dates.query.get(id)
    db.session.delete(appt)
    db.session.commit()
    flash("Doctor Successfully Deleted")
    return redirect(url_for('appointment'))

@app.route('/addappointment',methods=['GET','POST'])
def addappointment():
    '''
    Adding appointment to the Appointment_Dates database 
    Returning to the main appointment page to see commited changes
    '''
    form = Appt()
    if form.validate_on_submit():
        Doctor = '{}'.format(form.Doctor.data)
        Patient = '{}'.format(form.Patient.data)
        Time = request.form['Time']
        Date = request.form['Date']
        appt = Appointment_Dates(Doctor=Doctor,Patient=Patient,Time=Time,Date=Date)
        db.session.add(appt)
        db.session.commit()
        flash("Appointment Succesfully Booked!")
        return redirect(url_for("appointment"))
    return render_template("addappointment.html",form=form)
