#!/usr/bin/env python3
from sqlalchemy import (create_engine,CheckConstraint, UniqueConstraint,
    Index, Column, Date, Integer, String, Time,ForeignKey)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///appointments.db')

Base = declarative_base()

class Doctors(Base):
    __tablename__ = 'doctors'

    Index('index_name', 'name')

    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String())
    age = Column(Integer)
    specialty = Column(String)
    phone_number = Column(String)
    email = Column(String(20))
    hospital = Column(String)

    appointments = relationship('Appointments',backref=backref('doctor'))

    def __repr__(self):
        return f"Doctor: {self.name}: " \
            + f"Specialty: {self.specialty}, "

class Patients(Base):
    __tablename__ = 'patients'

    Index('index_name', 'name')

    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String)
    age = Column(Integer)
    gender = Column(String)
    phone_number = Column(String)
    email = Column(String(20))
    insurance_provider = Column(String)

    appointments = relationship('Appointments',backref=backref('patient'))

    def __repr__(self):
        return f"Patient: {self.name}: " \
            + f"Age: {self.age}, " \
            + f"Gender: {self.gender}"
    
class Appointments(Base):
    __tablename__ = 'appointments'
    __table_args__ = (UniqueConstraint('doctor_id', 'patient_id', 'date', 'time'),)

    Index('index_name', 'name')

    id = Column(Integer,primary_key=True,autoincrement=True)
    patient_id = Column(Integer, ForeignKey('patients.id'))
    doctor_id = Column(Integer, ForeignKey('doctors.id'))
    date = Column(Date)
    time = Column(Time)

    doctor = relationship('Doctors', back_populates='appointments')
    patient = relationship('Patients', back_populates='appointments')

    def __repr__(self):
        return f"Doctor: {self.doctor.name} " \
            + f"Patient: {self.patient.name}, " \
            + f"Date: {self.date}"\
            + f"Time: {self.time}"
