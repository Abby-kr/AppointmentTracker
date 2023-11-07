from models import Doctors, Patients, Appointments

def query_doctors(session,search_option):
    print(" ")
    print("You have selected the option to search doctor records")
    while search_option:
        print(" ")
        print("How would you like to search for the doctor(s)?")
        print("a)By name")
        print("b)By specialty")
        print("c)By hosital")
        print(" ")
        search_filter = input("Enter your option: ")
        if search_filter == "Q":
            break
        elif search_filter == "A" or search_filter =="a":
            doctor_name = input("Enter name(e.g Dr.Michael): ")
            doctor_by_name(session,doctor_name)
        elif search_filter == "B" or search_filter =="b":
            doctor_specialty = input("Enter specialty(eg Gynaecology): ")
            doctors_by_specialty(session,doctor_specialty)
        elif search_filter == "C" or search_filter =="c":
            doctor_hospital = input("Enter hospital name(eg St.John's hospital): ")
            doctors_by_hospital(session,doctor_hospital)

def get_doctors(session):
    return [doctor for doctor in session.query(Doctors)]

def doctor_by_name(session,name):
    return session.query(Doctors).filter(Doctors.name == name).first()

def doctors_by_specialty(session,specialty):
    return [doctor for doctor in session.query(Doctors).filter(Doctors.specialty == specialty)]

def doctors_by_hospital(session,hospital):
    return [doctor for doctor in session.query(Doctors).filter(Doctors.hospital == hospital)]


def query_patients(session,search_option):
    print(" ")
    print("You have selected the option to search patient records")
    print(" ")
    print("How would you like to search for the patient(s)?")
    print("a)By name")
    print("b)By age")
    print("c)By gender")
    print(" ")
    search_filter = input("Enter your option: ")
    while search_option:
        if search_filter == "A" or search_filter =="a":
            patient_name = input("Enter name: ")
            patient_by_name(session,patient_name)
        elif search_filter == "B" or search_filter =="b":
            patient_age = input("Enter age: ")
            patient_by_age(session,patient_age)
        elif search_filter == "C" or search_filter =="c":
            patient_gender = input("Enter gender: ")
            patient_by_gender(session,patient_gender)
        elif search_filter == "Q" or search_filter =="q":
            break
        else:
            print("Invalid option entered. Please select from the list of options or press Q to exit.")

def get_patients(session):
    print([patient for patient in session.query(Patients)])

def patient_by_name(session,name):
    print(session.query(Patients).filter(Patients.name == name).first())

def patient_by_age(session,age):
    print([patient for patient in session.query(Patients).filter(Patients.age ==age)])

def patient_by_gender(session,gender):
    print([patient for patient in session.query(Patients).filter(Patients.gender ==gender)])

def query_appointments(session,search_option):
    print(" ")
    print("You have selected the option to search appointment records")
    while search_option:
        print(" ")
        print("How would you like to search for the appointment(s)?")
        print("a)By name")
        print("b)By date")
        print("c)By time")
        print(" ")
        search_filter = input("Enter your option: ")
        if search_filter == "Q" or search_filter == "q":
            break
        elif search_filter == "A" or search_filter =="a":
            patient_name = input("Enter name: ")
            patient_by_name(session,patient_name)
        elif search_filter == "B" or search_filter =="b":
            appointment_date = input("Enter date of appointment: ")
            appt_by_date(session,appointment_date)
        elif search_filter == "C" or search_filter =="c":
            appointment_time = input("Enter time of appointment: ")
            appt_by_time(session,appointment_time)

def get_patients(session):
    return [appt for appt in session.query(Appointments)]


def appt_by_date(session,appointment_date):
    return [appt for appt in session.query(Appointments).filter(Appointments.date == appointment_date)]

def appt_by_time(session,appointment_time):
    return [appt for appt in session.query(Patients).filter(Appointments.time == appointment_time)]
