#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'Eduard Balantsev'
__project__ = 'MathTrainer'

from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class Learner(Base):
    """
    @type: self Learner
    """
    # Here we define columns for the table learner
    # Notice that each column is also a normal Python instance attribute.

    __tablename__ = 'learner'
    id_learner = Column(Integer, primary_key=True, autoincrement=True)
    login = Column(String(32), nullable=False)
    name = Column(String(32), nullable=False)
    last_name = Column(String(32), nullable=False)
    date_ne = Column(Date)

    def __init__(self, login , name, last_name, date_ne):
        self.login = login
        self.name = name
        self.last_name = last_name
        self.date_ne = date_ne

    def __repr__(self):
        return "<Learner('%s','%s', '%s', '%s' )>" % (self.login, self.name, self.last_name, self.date_ne)

if __name__ == '__main__':
    print 'Hi, It is ' + __file__ + ' project ' + __project__ + ' by ' + __author__
