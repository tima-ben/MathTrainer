#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'Eduard Balantsev'
__project__ = 'MathTrainer'
import datetime
from TaskMaker import TaskMaker
time_start = datetime.datetime.now()

if __name__ == '__main__':
    print 'Hi Привет '+__author__
    test = TaskMaker(set_info=True)
    test.generate()
    test.to_screen()
    test.to_file()
    test.type_of_test=test.TYPE_OF_TEST_VERIFICATION
    test.to_screen()
    time_end=datetime.datetime.now()
    print (time_start.microsecond)
    print 'start script:', time_start
    print 'end script:', time_end, ' wort time', (time_end - time_start)
