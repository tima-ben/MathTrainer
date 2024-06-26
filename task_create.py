#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__: str = 'Eduard Balantsev'
__project__: str = 'MathTrainer'
import datetime
from src.TaskMaker import TaskMaker

if __name__ == '__main__':
    time_start = datetime.datetime.now()
    print('Hi!', __author__)
    test = TaskMaker(set_info=True)
    test.generate()
    change_title = input('Do change title? (y/N):')
    if change_title == 'y' or change_title == 'Y':
        test.set_title()
    test.to_screen()
    test.to_file()
    test.type_of_test = test.TYPE_OF_TEST_VERIFICATION
    test.to_screen()
    time_end = datetime.datetime.now()
    print(time_start.microsecond)
    print('start script:', time_start)
    print('end script:', time_end, 'work time', (time_end - time_start))
