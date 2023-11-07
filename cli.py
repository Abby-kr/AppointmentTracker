#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import Session,sessionmaker

from cli_functions.search_database import (query_doctors,query_appointments,query_patients)
from cli_functions.create_records import (new_doctor,new_patient)
from cli_functions.delete_records import (delete_doctor,delete_patient)

db_uri = 'sqlite:///appointments.db'
engine = create_engine(db_uri)
Session = sessionmaker(bind=engine)
session = Session()

class Cli:
    def __init__(self):
        self.session = session

    def main(self):
        user_name = input("Enter Your Name: ")
        while user_name:
            print(f"Welcome to AppointmentTracker {user_name}!")
            print(" ")
            print("Please select from the following options:")
            print(" ")
            print("Press S to search the database.")
            print("Press C to create new data entries.")
            print("Press D to delete database entries.")
            print(" ")
            print("Press Q to quit.")
            print(" ")
            user_choice = input("What would you like to do next? ")
            if user_choice == "S" or user_choice == "s":
                Cli.search_database(self, user_choice)
            elif user_choice == "C" or user_choice == "c":
                Cli.create_entry(self, user_choice)
            elif user_choice == "D" or user_choice == "d":
                Cli.delete_record(self, user_choice)
            elif user_choice == "Q":
                break
            else:
                print("Invalid option entered. Please select from the list of options or press Q to exit.")
                
    def search_database(self,user_choice):
        while user_choice:
            print("You have selected the option to search the database.")
            print("Please choose from one of the search options below:")
            print(" ")
            print("a:Search for a doctor")
            print("b:Search for a patient")
            print("c:Search for an appointment")
            print(" ")
            print("Press Q to exit to main menu.")
            print(" ")
            search_option = input("Enter a search option: ")
            if search_option == "a":
                query_doctors(session, search_option)
            elif search_option == "b":
                query_patients(session, search_option)
            elif search_option == "c":
                query_appointments(session, search_option)
            elif search_option == "Q":
                break
            else:
                print("Invalid option, please select a, b, c, or press Q to quit.")
    
    def create_entry(session,user_choice):
        while user_choice:
            print(" ")
            print("CREATE NEW DATA ENTRIES:")
            print(" ")
            print("Select from the following options:")
            print(" ")
            print("a: Add new doctor to database.")
            print("b: Add new patient to database.")
            print(" ")
            print("Press Q to exit to main menu.")
            print(" ")
            search_option = input("Selection: ")
            if search_option == "a":
                new_doctor(session, search_option)
            elif search_option == "b":
                new_patient(session, search_option)
            elif search_option == "Q":
                break
            else:
                print("Invalid option, please select a, b, or press Q to quit.")

def delete_record(session,user_choice):
    while user_choice:
        print(" ")
        print("You have selected the option to delete a record.")
        print(" ")
        print("Select from the following options:")
        print(" ")
        print("a: Delete individual doctor from database.")
        print("b: Delete individual patient from database.")
        print(" ")
        print("Press Q to exit to main menu.")
        print(" ")
        search_option = input("Selection: ")
        if search_option == "a":
            delete_doctor(session, search_option)
        elif search_option == "b":
            delete_patient(session, search_option)
        elif search_option == "Q":
            break
        else:
            print("Invalid option, please select a, b or press Q to quit.")




if __name__ == "__main__":
    Cli()

'''def main():
    db_uri = 'sqlite:///appointments.db'
    engine = create_engine(db_uri)
    Session = sessionmaker(bind=engine)
    session = Session()

    user_type = input('Are you a doctor or a patient? (Enter "doctor" or "patient"): ')

    if user_type not in ('doctor', 'patient'):
        print('Invalid user type. Please enter "doctor" or "patient."')
        user_type = input('Are you a doctor or a patient? (Enter "doctor" or "patient"): ')
    
    
    if user_type == 'doctor':
        name = input('Name: ')
        age = int(input('Age: '))
        specialty = input('Specialty: ')
        phone_number = input('Phone Number: ')
        email = input('Email: ')
        hospital = input('Hospital: ')
        doctor = Doctors(name=name, age=age, specialty=specialty, phone_number=phone_number, email=email, hospital=hospital)
        session.add(doctor)
    else:
        name = input('Name: ')
        age = int(input('Age: '))
        gender = input('Gender: ')
        phone_number = input('Phone Number: ')
        email = input('Email: ')
        insurance_provider = input('Insurance provider: ')
        patient = Patients(name=name, age=age, gender=gender, phone_number=phone_number, email=email, insurance_provider=insurance_provider)
        session.add(patient)

    session.commit()
    print('Data added successfully.')

if __name__ == '__main__':
    main()'''
