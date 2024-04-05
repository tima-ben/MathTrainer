#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__: str = 'Eduard Balantsev'
__project__: str = 'MathTrainer'


from sqlalchemy_declarative import *
from sqlalchemy.orm import sessionmaker
import datetime


if __name__ == '__main__':
    print('Hi, It is', __file__, 'project', __project__, 'by', __author__)
    Session = sessionmaker(engine)
    session = Session()
    learner = MLearner()
#    learner.id_learner = 2
    learner.login = 'arina'
    learner.name = 'Arina'
    learner.last_name = 'Balantseva'
    learner.date_ne = datetime.date(2004, 9, 2)
    session.add(learner)
    session.commit()
    print(learner.id_learner)
