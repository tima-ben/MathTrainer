#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__: str = 'Eduard Balantsev'
__project__: str = 'MathTrainer'
import datetime
from src.TaskMaker import TaskMaker
time_start = datetime.datetime.now()

if __name__ == '__main__':
    print('Hi', __author__, sep=',')
    test = TaskMaker(set_info=True)
    test.generate()
    test.to_screen()
    test.to_file()
    test.type_of_test = test.TYPE_OF_TEST_VERIFICATION
    test.to_screen()
    time_end = datetime.datetime.now()
    print(time_start.microsecond)
    print('start script:', time_start)
    print('end script:', time_end, 'wort time', (time_end - time_start))
