from models import Doctors,Patients

def new_doctor(session,search_option):
    while search_option:
        print(" ")
        print("Add new doctor to database.")
        print("Would you like to conitinue?")
        answer = input("Y/n")
        if answer == "Y":
            print(" ")
            name = input("Enter name(e.g Dr.Michael): ")
            age = input("Enter age: ")
            specialty = input("Enter specialty(e.g Oncology): ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            hospital = input("Enter hospital: ")
            print(" ")
            print(f"Name: {name} | Age: {age} | Specialty: {specialty} | Phone number: {phone_number} | Email: {email} | Hospital: {hospital}")
            print(" ")
            confirm = input("Confirm add above doctor to database? y/n: ")
            if confirm == "y":
                new_doctor = Doctors(name=name,age=age,specialty=specialty,phone_number=phone_number,email=email,hospital=hospital)
                session.add(new_doctor)
                session.commit()
                print(" ")
                print("New doctor successfully added to database.")
            elif confirm == "n":
                print(" ")
                print("Doctor has not been added to database.")
            else:
                print (" ")
                print("Invalid entry. Please enter y/n.")
        else:
            break



def new_patient(session,search_option):
    while search_option:
        print(" ")
        print("Add new doctor to database.")
        print("Would you like to conitinue?")
        answer = input("Y/n")
        if answer == "Y":
            print(" ")
            print("Add new patient to database.")
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
                new_patient = Patients(name=name,age=age,gender=gender,phone_number=phone_number,email=email,insurance_provider=insurance_provider)
                session.add(new_patient)
                session.commit()
                print(" ")
                print("New patient successfully added to database.")
            elif confirm == "n":
                print(" ")
                print("Patient has not been added to database.")
            else:
                print (" ")
                print("Invalid entry. Please enter y/n.")
