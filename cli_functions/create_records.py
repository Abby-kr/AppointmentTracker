from models import Doctors,Patients

def new_doctor(session,search_option):
    print(" ")
    print("Add new doctor to database.")
    while search_option:
        print(" ")
        name = input("Enter name(e.g Dr.Michael): ")
        age = input("Ener age: ")
        specialty = input("Enter specialty(e.g Oncology): ")
        phone_number = input("Enter phone number: ")
        email = input("Enter email: ")
        hospital = input("Enter hospital: ")
        print(" ")
        print(f"Name: {name} | Age: {age} | Specialty: {specialty} | Phone number: {phone_number} | Email: {email} | Hospital: {hospital}")
        print(" ")
        confirm = input("Confirm add above doctor to database? y/n: ")
        if confirm == "y":
            add_doctor(session,Doctors(name=name,age=age,specialty=specialty,phone_number=phone_number,email=email,hospital=hospital))
            print(" ")
            print("New doctor successfully added to database.")
        elif confirm == "n":
            print(" ")
            print("Doctor has not been added to database.")
        else:
            print (" ")
            print("Invalid entry. Please enter y/n.")


def add_doctor(session, doctor):
    session.add(doctor)
    session.commit()

def new_patient(session,search_option):
    print(" ")
    print("Add new patient to database.")
    while search_option:
        print(" ")
        name = input("Enter name(e.g Dr.Michael): ")
        age = input("Ener age: ")
        gender = input("Enter gender(Male/Female): ")
        phone_number = input("Enter phone number: ")
        email = input("Enter email: ")
        insurance_provider = input("Enter insurance provider: ")
        print(" ")
        print(f"Name: {name} | Age: {age} | Gender: {gender} | Phone number: {phone_number} | Email: {email} | Insurance provider: {insurance_provider}")
        print(" ")
        confirm = input("Confirm add above patient to database? y/n: ")
        if confirm == "y":
            add_patient(session,Patients(name=name,age=age,gender=gender,phone_number=phone_number,email=email,insurance_provider=insurance_provider))
            print(" ")
            print("New patient successfully added to database.")
        elif confirm == "n":
            print(" ")
            print("Patient has not been added to database.")
        else:
            print (" ")
            print("Invalid entry. Please enter y/n.")


def add_patient(session, patient):
    session.add(patient)
    session.commit()