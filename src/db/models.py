#from ast import For
from email.policy import default
from enum import unique
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, LargeBinary, ForeignKey, true
from sqlalchemy.dialects.mysql import YEAR, JSON
from sqlalchemy.orm import relationship
from datetime import datetime, timedelta
#import json

Base = declarative_base() 

class Access_Points(Base):
    __tablename__ = 'access_points'
    id = Column(Integer, primary_key=True)
    authority_id = Column(Integer, ForeignKey('authority.id'))
    item_id = Column(Integer, ForeignKey('item.id'))
    relation = Column(String(length=100))

    authority = relationship("Authority", back_populates="access_points")
    item = relationship("Item", back_populates="access_points")

    def __repr__(self):
        return self.relation



""" class Authorship(Base):
    __tablename__ = 'authorship'
    id = Column(Integer, primary_key=True)
    authority_id = Column(Integer, ForeignKey('authority.id'))
    item_id = Column(Integer, ForeignKey('item.id'))
    relation = Column(String(length=100))
    publicationyear = Column(YEAR)
    #relationship
    authority = relationship("Authority", back_populates="authorship")
    item = relationship("Item", back_populates="authorship")

    def __repr__(self):
        return self.relation """
    
""" class Item_Subject(Base):
    __tablename__ = 'item_subject'
    id = Column(Integer, primary_key=True)
    authority_id = Column(Integer, ForeignKey('authority.id'))
    subject_id = Column(Integer, ForeignKey('subject.id'))
    item_id = Column(Integer, ForeignKey('item.id'))
    relation = Column(String(length=100))
    #relationship
    subject = relationship("Subject", back_populates="item_subject")
    authority = relationship("Authority", back_populates="item_subject")
    item = relationship("Item", back_populates="item_subject")

    def __repr__(self):
        return self.relation
 """
class Item(Base):
    __tablename__ = 'item'
    id = Column(Integer, primary_key=True)
    title = Column(String(length=255))
    marc = Column(JSON)
    logs = Column(JSON)
    created_at = Column(Date, default=datetime.now())
    

    #relationship
    #authorship = relationship("Authorship", back_populates="item")
    #item_subject = relationship("Item_Subject", back_populates="item")
    access_points = relationship("Access_Points", back_populates="item")
    exemplares = relationship("Exemplar", back_populates="item")

    def __repr__(self):
        return self.title

class Authority(Base):
    __tablename__ = 'authority'
    id = Column(Integer, primary_key=True)
    name = Column(String(length=255))
    #format = Column(String(length=100), default='marcxml')
    #schema = Column(String(length=100), default='marc21')
    #marc_record = Column(LargeBinary)
    marc = Column(JSON)
    type = Column(String(length=255))
    log = Column(JSON)
    created_at = Column(Date, default=datetime.now())

    #authorship = relationship("Authorship", back_populates="authority")
    #item_subject = relationship("Item_Subject", back_populates="authority")
    access_points = relationship("Access_Points", back_populates="authority")

    def __repr__(self):
        return self.name

""" class Subject(Base):
    __tablename__ = 'subject'
    id = Column(Integer, primary_key=True)
    name = Column(String(length=255))
    tag = Column(String(length=5))
    format = Column(String(length=100), default='marcxml')
    schema = Column(String(length=100), default='marc21')
    marc_record = Column(LargeBinary)
    created_at = Column(Date, default=datetime.now())

    item_subject = relationship("Item_Subject", back_populates="subject")

    def __repr__(self):
        return self.name
 """
class Exemplar(Base):
    __tablename__ = 'exemplar'
    id = Column(Integer, primary_key=True)
    item_id = Column(Integer, ForeignKey('item.id'))
    
    library = Column(String(30))
    shelf = Column(String(30))
    callnumber = Column(String(30))
    collection = Column(String(30))
    number = Column(String(10))
    volume = Column(String(10))
    ex = Column(String(10))
    status = Column(String(30))
    created_at = Column(Date, default=datetime.now())
    #user

    item = relationship("Item", back_populates="exemplares")
    loan = relationship("Loan", back_populates="exemplar")

    def __repr__(self):
        return self.number

#Users
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    email = Column(String(100), unique=True)
    addressCep = Column(String(100))
    addressCity = Column(String(100))
    addressDistrict = Column(String(100))
    addressNumber = Column(String(100))
    addressStreet = Column(String(100))
    birth = Column(String(100))
    cellphone = Column(String(100))
    sex = Column(String(100))
    surname = Column(String(100))
    vinculo = Column(String(100))
    img = Column(String(100))
    hash_password = Column(String(255))
    created_at = Column(Date, default=datetime.now())

    #relationship
    loan = relationship("Loan", back_populates="user")

    def json(self):
        return {'id': self.id, 'name': self.name, "email": self.email}

    def __repr__(self):
        
        return f"id:{self.id!r}, name:{self.name!r}, email:{self.email!r}"


class Loan(Base):
    __tablename__ = 'loan'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    exemplar_id = Column(Integer, ForeignKey('exemplar.id'))
    created_at = Column(Date, default=datetime.now())
    due = Column(Date, default=datetime.now()+timedelta(days = 7))
    status = Column(String(100), default="Emprestado")
    log = Column(JSON)


    user = relationship("User", back_populates="loan")
    exemplar = relationship("Exemplar", back_populates="loan")
