#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__: str = 'Eduard Balantsev'
__project__: str = 'MathTrainer'

import io
import os
import random
import datetime
from os import linesep as eol
from typing import Tuple, Dict, List, Any

from Exercise import Exercise


class TaskMaker(object):
    """

    """
    COUNT_ROW: int = 12
    COUNT_COLUMN: int = 4
    DEFAULT_LEARNER_NAME: str = 'Guest'
    LEFT_MARGIN: int = 8
    TYPE_OF_TEST_CONSOLIDATION: str = 'consolidation'
    TYPE_OF_TEST_EDUCATION: str = 'education'
    TYPE_OF_TEST_VERIFICATION: str = 'verification'
    TYPE_OF_TEST_CHECKING: str = 'checking'
    TYPE_OF_TESTS: tuple[str, str, str, str] = (TYPE_OF_TEST_CONSOLIDATION,
                                                TYPE_OF_TEST_EDUCATION,
                                                TYPE_OF_TEST_VERIFICATION,
                                                TYPE_OF_TEST_CHECKING)
    QUALITY_OF_TEST_SIMPLE: str = 'simple'
    QUALITY_OF_TEST_COMPLEX: str = 'complex'
    strLeftMargin: str = ' ' * LEFT_MARGIN + '|'
    blankLine: str = ' ' * LEFT_MARGIN + '+' + '----------------+' * COUNT_COLUMN
    title: str = 'Test for '
    name_learner: dict[str, str] = {'1': 'Timur Balantsev', '2': 'Arina Balantseva'}
    defaultSet: bool = True
    simple_set: tuple[int, int, int, int, int, int, int, int, int, int, int] = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
    complex_set: tuple[int, int, int, int, int, int, int, int] = (2, 3, 4, 6, 7, 8, 9, 12)
    quality = QUALITY_OF_TEST_SIMPLE
    rows: list[Any] = []

    def __init__(self, learner: str = DEFAULT_LEARNER_NAME, type_of_test: str = TYPE_OF_TEST_CONSOLIDATION,
                 first: range = range(1, 12), second: range = range(1, 12),
                 operations: tuple[str, str, str, str] = Exercise.LIST_OPERATIONS, set_info: bool = False):
        """

        :param learner:
        :param type_of_test:
        :param first:
        :param second:
        :param operations:
        :param set_info:
        """
        self.learner: str = learner
        if type_of_test in self.TYPE_OF_TESTS:
            self.type_of_test: str = type_of_test
        else:
            raise Exception(
                'Type of test: \'%s\' not correct. it can be %s' % (type_of_test, self.TYPE_OF_TESTS.__str__()))
        self.first: range = first
        self.second: range = second
        self.operations: tuple[str, str, str, str] = operations
        if set_info:
            self.set_info()

    def set_info(self):
        """
        Get information about leaner and task from command line and set it for task
        """
        changed: bool = False
        self.first = self.simple_set
        self.second = self.simple_set
        print('Note:' + eol, 'The value in (<val>) will be the default value.')
        name: str = input('Enter learner name: 1-Timur or 2-Arina or (Guest) or name? ') or self.learner
        if len(name) == 1:
            if type(self.name_learner[name]) is not None:
                self.learner = self.name_learner[name]
                changed = True
        elif len(name) > 1:
            self.learner = name
            changed = True
        quality: str = input('Choose quality of test (1-simple) or 2-complex? ') or '1'
        if int(quality) == 2:
            self.quality = self.QUALITY_OF_TEST_COMPLEX
            changed = True
        first: str = input('Enter variants for first element (1-12)? ')
        skip_second: bool = False
        if len(first.strip()) > 0:
            tmp: list[int] = []
            for digital in tuple(first.strip().split(',')):
                tmp.append(int(digital))
            self.first = tuple(tmp)
            changed = True
            skip_second = True
        if not skip_second:
            second: str = input('Enter variants for second element (1-12)? ')
            if len(second.strip()) > 0:
                tmp: list[int] = []
                for digital in tuple(second.strip().split(',')):
                    tmp.append(int(digital))
                self.second = tuple(tmp)
            elif self.quality == self.QUALITY_OF_TEST_COMPLEX:
                self.second = self.complex_set
            changed = True
        operations: str = input('Enter list operation (sum, sub, div, mul)? ')
        if len(operations.strip()) > 0:
            tmp: list[str] = []
            symbol: str
            for symbol in tuple(operations.strip().split(',')):
                if symbol in Exercise.LIST_OPERATIONS:
                    tmp.append(symbol)
                else:
                    print('Operation {:s} changed by sum'.format(symbol))
                    tmp.append('sum')
            if len(tmp) == 1:
                tmp *= 4
            elif len(tmp) == 2:
                tmp *= 2
            elif len(tmp) == 3:
                tmp.append(Exercise.DEFAULT_OPERATION)
            self.operations = tuple(tmp)
            changed = True

        self.defaultSet: bool = not changed

    def get_first(self, row):
        """

        :return: integer
        """
        if self.type_of_test == self.TYPE_OF_TEST_CONSOLIDATION:
            for_ret = random.choice(self.first)
        elif self.type_of_test == self.TYPE_OF_TEST_EDUCATION:
            for_ret = row + 1
        else:
            for_ret = random.randint(2, 12)
        return for_ret

    def get_second(self):
        """

        :return: integer
        """
        if self.type_of_test == self.TYPE_OF_TEST_CONSOLIDATION:
            for_ret = random.choice(self.second)
        elif self.type_of_test == self.TYPE_OF_TEST_EDUCATION:
            if len(self.second) > 1:
                self.second = (random.choice(self.second),)
            for_ret = self.second[0]
        else:
            for_ret = random.randint(2, 12)
        return for_ret

    def get_operation(self, column):
        """

        :return: string
        """
        if self.type_of_test in (self.TYPE_OF_TEST_CONSOLIDATION, self.TYPE_OF_TEST_EDUCATION):
            for_ret = self.operations[column]
        else:
            for_ret = self.operations[random.randint(0, 3)]
        return for_ret

    def get_template_id(self):
        """
        index line from Exercise.OUT_FORMAT_LIST
        :return: int
        """
        if self.type_of_test in (self.TYPE_OF_TEST_CONSOLIDATION, self.TYPE_OF_TEST_EDUCATION):
            for_ret = Exercise.OUT_FORMAT_HIDE_RESULT
        elif self.type_of_test == self.TYPE_OF_TEST_VERIFICATION:
            for_ret = Exercise.OUT_FORMAT_FULL
        else:
            for_ret = random.randint(1, 3)
        return for_ret

    def check_repeat(self, exercise, column_index):
        """
        :param exercise: Exercise
        :param column_index: int
        :return:
        """
        repeat = False
        for row in self.rows:
            if row[column_index].list_for_out == exercise.list_for_out:
                repeat = True
                break
        return repeat

    def generate(self):
        """
        Generation task
        :return:
        """
        for row_index in range(0, self.COUNT_ROW):
            columns = []
            for column_index in range(0, self.COUNT_COLUMN):
                tmp_exercise = Exercise(self.get_first(row_index), self.get_second(), self.get_operation(column_index))
                while self.check_repeat(tmp_exercise, column_index):
                    tmp_exercise = Exercise(self.get_first(row_index), self.get_second(),
                                            self.get_operation(column_index))
                columns.append(tmp_exercise)
            self.rows.append(columns)

    def row_to_sting(self, row):
        """

        :return: string
        """
        line = self.strLeftMargin
        for first in row:
            line += first.for_out(self.get_template_id()) + ' |'
        return line

    def get_title(self):
        """

        :return: string
        """
        return self.strLeftMargin[:-1] + self.title + 'date ' + datetime.datetime.now().strftime(
            '%Y-%m-%d ') + self.learner + ' (' + self.quality + ')'

    def set_title(self, title=u'Trace d\'etude '):
        self.title = title

    def to_screen(self):
        """
        :return:
        """
        if len(self.rows) == 0:
            self.generate()
        print(self.get_title())
        for row in self.rows:
            print(self.blankLine)
            print(self.row_to_sting(row))
        print(self.blankLine)

    def to_file(self, name_of_file: str = 'task_to_print') -> None:
        """

        :param name_of_file: str
        :return: None
        """
        f = io.open(name_of_file, 'w', encoding='utf-8')
        f.write(self.get_title() + eol)
        for row in self.rows:
            f.write(self.blankLine + eol)
            f.write(self.row_to_sting(row) + eol)
        f.write(self.blankLine + eol)
        f.close()


if __name__ == '__main__':
    print('Hi, It is', __file__, 'project', __project__, 'by', __author__)
