#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__: str = 'Eduard Balantsev'
__project__: str = 'MathTrainer'

import io
import random
import datetime
from decouple import config
from os import linesep as eol
from typing import Any

from src.Exercise import Exercise


class TaskMaker(object):
    """

    """
    DATA_PATH = '/'.join([config('PROJECT_PATH'), config('DATA_PATH')])
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

    def __init__(self, learner: str = DEFAULT_LEARNER_NAME, type_of_test: str = TYPE_OF_TEST_CONSOLIDATION,
                 first: range = range(1, 13), second: range = range(1, 13),
                 operations: tuple[str, str, str, str] = Exercise.LIST_OPERATIONS, set_info: bool = False):
        """

        :param learner:
        :param type_of_test:
        :param first:
        :param second:
        :param operations:
        :param set_info:
        """
        self.rows: list[Any] = []
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

    def set_info(self) -> None:
        """
        Get information about leaner and task from command line and set it for task
        """
        changed: bool = False
        TaskMaker.output_note()
        self.learner = self.input_learner()
        self.quality = self.input_quality()
        if self.quality == self.QUALITY_OF_TEST_SIMPLE:
            self.first = self.simple_set
            self.second = self.simple_set
        else:
            self.first = self.complex_set
            self.second = self.complex_set
        before = self.first
        self.first = self.input_elements('first')
        if self.first == before:
            self.second = self.input_elements('second')
        self.operations = self.input_operations()

    @staticmethod
    def output_note() -> None:
        """
        Output note on the screen
        :return:
        """
        print('Note:' + eol, 'The value in (<val>) will be the default value.')

    def input_learner(self) -> str:
        """
        Get learner name from command line input
        :return:
        """
        name: str = input('Enter learner name: 1-Timur or 2-Arina or (Guest) or name? ') or self.learner
        if len(name) == 1:
            if type(self.name_learner[name]) is not None:
                return self.name_learner[name]
            return self.DEFAULT_LEARNER_NAME
        elif len(name) > 1:
            return name

    def input_quality(self) -> str:
        """
        Get quality from command line input and set it for task 1 for simple, 2 for complex.
        :return:
        """
        quality: str = input('Choose quality of test (1-simple) or 2-complex? ') or '1'
        if int(quality) == 2:
            return self.QUALITY_OF_TEST_COMPLEX
        else:
            return self.QUALITY_OF_TEST_SIMPLE

    def input_elements(self, order: str = 'first') -> tuple[int, ...] | range:
        """
        Get elements from command line input
        :param str order:
        :return:
        """
        elements: str = input('Enter variants for ' + order + ' element (1-12)? ')
        if len(elements.strip()) > 0:
            tmp: list[int] = []
            for digital in tuple(elements.strip().split(',')):
                tmp.append(int(digital))
            return tuple(tmp)
        else:
            if order == 'first':
                return self.first
            else:
                return self.second

    def input_operations(self) -> tuple[str, str, str, str]:
        """

        :return:
        """
        operations: str = input('Enter list operations (sum, sub, div, mul)? ').strip()
        if len(operations.strip()) > 0:
            tmp: list[str] = []
            symbol: str
            for symbol in tuple(operations.strip().split(',')):
                symbol = symbol.strip()
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
            elif len(tmp) > 4:
                tmp = tmp[slice(4)]
            return tuple(tmp)
        else:
            return self.operations

    def get_first(self, row: int):
        """
        :param int row: index of row
        :return: element for :py:class:`Exercise.a`
        :rtype int:
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

    def get_operation(self, column) -> str:
        """
        Return code name operation
        :return: str
        """
        if self.type_of_test in (self.TYPE_OF_TEST_CONSOLIDATION, self.TYPE_OF_TEST_EDUCATION):
            name_operation = self.operations[column]
        else:
            name_operation = self.operations[random.randint(0, 3)]
        return name_operation

    def get_template_id(self) -> int:
        """
        index line from Exercise.OUT_FORMAT_LIST
        :return: int
        """
        if self.type_of_test in (self.TYPE_OF_TEST_CONSOLIDATION, self.TYPE_OF_TEST_EDUCATION):
            template_id = Exercise.OUT_FORMAT_HIDE_RESULT
        elif self.type_of_test == self.TYPE_OF_TEST_VERIFICATION:
            template_id = Exercise.OUT_FORMAT_FULL
        else:
            template_id = random.randint(1, 3)
        return template_id

    def check_repeat(self, exercise: Exercise, column_index: int) -> bool:
        """
        Method verify if exercise is repeated or not in the column.

        :param exercise: Exercise
        :param column_index: int
        :return:
        """
        is_repeat = False
        for row in self.rows:
            if row[column_index].list_for_out == exercise.list_for_out:
                is_repeat = True
                break
        return is_repeat

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

    def row_to_sting(self, row) -> str:
        """
        Return one line on rom for print or for save in file
        :param row: list[
        :return: str
        """
        line = self.strLeftMargin
        for first in row:
            line += first.for_out(self.get_template_id()) + ' |'
        return line

    def get_title_for_print(self):
        """

        :return: string
        """
        return self.strLeftMargin[:-1] + self.title + 'date ' + datetime.datetime.now().strftime(
            '%Y-%m-%d ') + self.learner + ' (' + self.quality + ')'

    def set_title(self, title=u'Trace d\'etude '):
        self.title = title

    def to_screen(self) -> None:
        """
        Output to screen the table with exercises
        :return: None
        """
        if len(self.rows) == 0:
            self.generate()
        print(self.get_title_for_print())
        for row in self.rows:
            print(self.blankLine)
            print(self.row_to_sting(row))
        print(self.blankLine)

    def to_file(self, name_of_file: str = 'last_task_to_print.txt') -> None:
        """

        :param name_of_file: str
        :return: None
        """
        if len(self.rows) == 0:
            self.generate()
        name_of_file = '/'.join([self.DATA_PATH, name_of_file])
        print(name_of_file)
        f = io.open(name_of_file, 'wt', encoding='utf-8')
        f.write(self.get_title_for_print() + '\n')
        for row in self.rows:
            f.write(self.blankLine + '\n')
            f.write(self.row_to_sting(row) + '\n')
        f.write(self.blankLine + '\n')
        f.close()


if __name__ == '__main__':
    print('Hi, It is', __file__, 'project', __project__, 'by', __author__)
