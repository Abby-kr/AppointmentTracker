#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Doctors,Patients,Appointments



if __name__ == '__main__':
    
    engine = create_engine('sqlite:///appointments.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    doctor1 = Doctors(name='Dr. Smith', age=40, specialty='Cardiology', phone_number='123-456-7890', email='dr.smith@example.com', hospital='Hospital A')
    doctor2 = Doctors(name='Dr. Johnson', age=35, specialty='Dermatology', phone_number='987-654-3210', email='dr.johnson@example.com', hospital='Hospital B')

    patient1 = Patients(name='Alice', age=25, gender='Female',phone_number='555-555-5555', email='alice@example.com', insurance_provider='Insurance A')
    patient2 = Patients(name='Bob', age=30, gender='Male',phone_number='444-444-4444', email='bob@example.com', insurance_provider='Insurance B')

    
    appointment1 = Appointments(doctor=doctor1, patient=patient1, date='2023-11-15', time='10:00:00')
    appointment2 = Appointments(doctor=doctor2, patient=patient2, date='2023-11-16', time='14:30:00')

    session.add_all([doctor1, doctor2, patient1, patient2, appointment1, appointment2])

    # Commit the changes to the database
    session.commit()