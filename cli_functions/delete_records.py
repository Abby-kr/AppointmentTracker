from models import Doctors,Patients

def delete_doctor(session,search_option):
    while search_option:
        print(" ")
        print("Add new doctor to database.")
        print("Would you like to conitinue?")
        answer = input("Y/n")
        if answer == "Y":
            print(" ")
            print("You have selected the option to delete an individual doctor record from the database.")
        
            print(" ")
            doctor_name = input("Enter doctor's name(e.g Dr.Michael): ")
            doctor_to_delete = session.query(Doctors).filter(Doctors.name == doctor_name).first()
            # = query.first()
            print(" ")
            print(f"{doctor_to_delete}")
            print(" ")
            confirm = input("Confirm if above doctor is to be deleted.(y/n)")
            if confirm  == "y":
                warning = input("WARNING: Selecting Y will delete this doctor from the database. Press y/n to confirm: ")
                if warning == "y" or warning == "Y":
                    session.delete(doctor_to_delete)
                    session.commit()
                    print(" ")
                    print("Doctor record successfully deleted!")
                else:
                    print(" ")
                    print("Doctor record NOT deleted.")
            else:
                print(" ")
                print("Doctor record NOT deleted.")
        else:
            break



def delete_patient(session,search_option):
    while search_option:
        print(" ")
        print("Add new doctor to database.")
        print("Would you like to conitinue?")
        answer = input("Y/n")
        if answer == "Y":
            print(" ")
            print("You have selected the option to delete an individual patient record from the database.")
            print(" ")
            patient_name = input("Enter patient's name(e.g Dr.Michael): ")
            query = session.query(Patients).filter(Patients.name == patient_name).first()
            patient_to_delete = query.first()
            print(" ")
            print(f"{patient_to_delete}")
            print(" ")
            confirm = input("Confirm if above patient is to be deleted.(y/n)")
            if confirm  == "y":
                warning = input("WARNING: Selecting y will delete this patient from the database. Press y/n to confirm: ")
                if warning == "y":
                    session.delete(patient_to_delete)
                    session.commit()
                    print(" ")
                    print("Patient record successfully deleted!")
                else:
                    print(" ")
                    print("Patient record NOT deleted.")
            else:
                print(" ")
                print("Patient record NOT deleted.")
        else:
            break
