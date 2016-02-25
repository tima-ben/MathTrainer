#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'Eduard Balantsev'
__project__ = 'MathTrainer'

import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()


class MLearner(Base):
    """
    @type: self MLearner
    """
    # Here we define columns for the table learner
    # Notice that each column is also a normal Python instance attribute.

    __tablename__ = 'learner'
    id_learner = Column(Integer, primary_key=True, autoincrement=True)
    login = Column(String(32), nullable=False)
    name = Column(String(32), nullable=False)
    last_name = Column(String(32), nullable=False)
    date_ne = Column(Date)


class MExercise(Base):
    """
    @type: self MExercise
    """
    # Here we define columns for the table exercise
    # Notice that each column is also a normal Python instance attribute.

    __tablename__ = 'exercise'
    id_exercise = Column(Integer, primary_key=True)
    a = Column(Integer, nullable=False)
    b = Column(Integer, nullable=False)
    result = Column(Integer, nullable=False)
    operation = Column(String(3))

# Create an engine that stores data in the local directory's
# math_trainer.db file.
engine = create_engine('sqlite:///db_sqlite3/math_trainer.db')

if __name__ == '__main__':
    print 'Hi, It is ' + __file__ + ' project ' + __project__ + ' by ' + __author__
    # Create all tables in the engine. This is equivalent to "Create Table"
    # statements in raw SQL.
    Base.metadata.create_all(engine)
