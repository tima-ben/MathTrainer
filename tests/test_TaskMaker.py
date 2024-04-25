#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
import io
from datetime import datetime
from unittest import TestCase, main, mock
from os import linesep as eol, path
from src.TaskMaker import TaskMaker
from src.Exercise import Exercise
import inspect

__author__: str = 'Eduard Balantsev'
__project__: str = 'MathTrainer'


def whoami():
    return inspect.stack()[1][3]


class TestTaskMaker(TestCase):
    """
    Unit Test for :py:class:`TaskMaker` class.
    """
    FILE_NAME: str = 'test_task_to_print.txt'

    def setUp(self):
        # print(whoami())
        self.task: TaskMaker = TaskMaker()

    def tearDown(self):
        # print(whoami())
        self.task = None
        del self.task

    def test_exception_in_constructor(self):
        """Test exception constructor."""
        # print(whoami())
        with self.assertRaises(Exception):
            TaskMaker(type_of_test='test')

    def test_type_of_property(self):
        """Test values all property after initialization."""
        # print(whoami())
        self.assertEqual(type(self.task), TaskMaker, 'Type of task should be TaskMaker')
        self.assertIsInstance(self.task, TaskMaker, 'task should be a subclass of TaskMaker')
        self.assertTrue(self.task.defaultSet, 'property task.defaultSet should be True after initialization')
        self.assertEqual(self.task.learner, self.task.DEFAULT_LEARNER_NAME,
                         'property task.learner should be equal DEFAULT_LEARNER_NAME')
        self.assertEqual(type(self.task.rows), list, 'property task.rows should be a list')
        # print(self.task.rows)
        self.assertCountEqual(self.task.rows, [], 'property task.rows should be empty after initialization')
        self.assertEqual(self.task.quality, TaskMaker.QUALITY_OF_TEST_SIMPLE,
                         'property task.quality should be equal to QUALITY_OF_TEST_SIMPLE after initialization')
        self.assertEqual(type(self.task.first), range, 'property task.first should be a range after initialization')
        self.assertEqual(self.task.first, range(1, 13),
                         'property task.first should be a range(1-13) after initialization')
        self.assertEqual(type(self.task.second), range, 'property task.second should be a range after initialization')
        self.assertEqual(self.task.second, range(1, 13),
                         'property task.second should be a range(1-13) after initialization')
        self.assertEqual(self.task.operations, Exercise.LIST_OPERATIONS,
                         'property task.operations should be a Exercise.LIST_OPERATIONS after initialization')

    # @mock.patch('sys.stdout', new_callable=io.StringIO)
    # def test_output_note(self, mock_stdout):
    #     """Test output_note() method."""
    #     self.task.output_note()
    #     self.assertEqual(mock_stdout.getvalue().strip(),
    #                      'Note:' + eol + ' The value in (<val>) will be the default value.')

    def test_output_note(self):
        """Test output_note() method."""
        # print(whoami())
        with mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            self.task.output_note()
            self.assertEqual(mock_stdout.getvalue().strip(),
                             'Note:' + eol + ' The value in (<val>) will be the default value.')
            self.assertTrue('Note:' in mock_stdout.getvalue(), 'output should contain a "Note:".')

    def test_input_learner(self):
        """Test input_learner() method."""
        # print(whoami())
        # Test task.learner after initialization
        self.assertEqual(self.task.learner, self.task.DEFAULT_LEARNER_NAME,
                         'property task.learner should be equal DEFAULT_LEARNER_NAME')
        # Test empty input
        with mock.patch('builtins.input', side_effect=['']):
            self.assertEqual(self.task.input_learner(), self.task.DEFAULT_LEARNER_NAME,
                             'For empty input learner should be equal to DEFAULT_LEARNER_NAME')
        # Test input '1'
        with mock.patch('builtins.input', side_effect=['1']):
            self.assertEqual(self.task.input_learner(), 'Timur Balantsev',
                             'For empty input learner should be equal to Timur Balantsev')
        # Test input '2'
        with mock.patch('builtins.input', side_effect=['2']):
            self.assertEqual(self.task.input_learner(), 'Arina Balantseva',
                             'For empty input learner should be equal to Arina Balantseva')
        # Test input 'Other Variant'
        with mock.patch('builtins.input', side_effect=['Other Variant']):
            self.assertEqual(self.task.input_learner(), 'Other Variant',
                             'For empty input learner should be equal to Other Variant')

    def test_input_quality(self):
        """
        Test for
        :py:meth:`TaskMaker.input_quality()`: method.
        """
        # print(whoami())
        # Test task.quality after initialization
        self.assertEqual(self.task.quality, TaskMaker.QUALITY_OF_TEST_SIMPLE,
                         'quality should be equal to QUALITY_OF_TEST_SIMPLE')
        # Test empty input
        with mock.patch('builtins.input', side_effect=['']):
            self.assertEqual(self.task.input_quality(), self.task.QUALITY_OF_TEST_SIMPLE,
                             'For empty input quality should be equal to QUALITY_OF_TEST_SIMPLE')
        # Test input '1'
        with mock.patch('builtins.input', side_effect=['1']):
            self.assertEqual(self.task.input_quality(), self.task.QUALITY_OF_TEST_SIMPLE,
                             'For 1 input quality should be equal to QUALITY_OF_TEST_SIMPLE')
        # Test input '2'
        with mock.patch('builtins.input', side_effect=['2']):
            self.assertEqual(self.task.input_quality(), self.task.QUALITY_OF_TEST_COMPLEX,
                             'For 2 input quality should be equal to QUALITY_OF_TEST_COMPLEX')

    def test_input_elements(self):
        """Test input_elements() method."""
        # print(whoami())
        # Test task.first and task.second after initialization
        self.assertEqual(self.task.quality, TaskMaker.QUALITY_OF_TEST_SIMPLE,
                         'quality should be equal to QUALITY_OF_TEST_SIMPLE')
        self.assertEqual(type(self.task.first), range,
                         'property task.first should be a range after initialization')
        self.assertEqual(self.task.first, range(1, 13),
                         'property task.first should be a range(1-13) after initialization')
        self.assertEqual(type(self.task.second), range, 'property task.second should be a range after initialization')
        self.assertEqual(self.task.second, range(1, 13),
                         'property task.second should be a range(1-13) after initialization')
        # Test input '' for first
        with mock.patch('builtins.input', side_effect=['']):
            self.assertEqual(self.task.input_elements(), range(1, 13),
                             'For empty input elements should be equal range(1-13)')
        with mock.patch('builtins.input', side_effect=['']):
            self.assertEqual(self.task.input_elements('first'), range(1, 13),
                             'For empty input elements should be equal range(1-13)')
        with mock.patch('builtins.input', side_effect=['']):
            self.assertEqual(self.task.input_elements('second'), range(1, 13),
                             'For empty input elements should be equal range(1-13)')
        # Test input not empty list for elements
        with mock.patch('builtins.input', side_effect=['2,3,4,5,6']):
            self.assertEqual(self.task.input_elements(), (2, 3, 4, 5, 6),
                             'For empty input elements should be equal (2, 3, 4, 5, 6)')
        with mock.patch('builtins.input', side_effect=['5,6,7,8,9,10,11']):
            self.assertEqual(self.task.input_elements('first'), (5, 6, 7, 8, 9, 10, 11),
                             'For empty input elements should be equal (5, 6, 7, 8, 9, 10, 11)')
        with mock.patch('builtins.input', side_effect=['3,4,7,8,12']):
            self.assertEqual(self.task.input_elements('second'), (3, 4, 7, 8, 12),
                             'For empty input elements should be equal (3, 4, 7, 8, 12)')

    def test_input_operations(self):
        """Test input_operations() method."""
        # print(whoami())
        # Test task.operations after initialization
        self.assertEqual(self.task.operations, Exercise.LIST_OPERATIONS,
                         'task.operations should be equal to Exercise.LIST_OPERATIONS')
        # Test empty input '' for list operation
        with mock.patch('builtins.input', side_effect=['']):
            self.assertEqual(self.task.input_operations(), ('sum', 'sub', 'div', 'mul'),
                             'For empty input task.operation should be equal (sum, sub, div, mul)')
        # Test not empty input for list operations
        with mock.patch('builtins.input', side_effect=['sub']):
            self.assertEqual(self.task.input_operations(), ('sub', 'sub', 'sub', 'sub'),
                             'For empty input task.operation should be equal (sub, sub, sub, sub)')
        with mock.patch('builtins.input', side_effect=['sub, div']):
            self.assertEqual(self.task.input_operations(), ('sub', 'div', 'sub', 'div'),
                             'For empty input task.operation should be equal (sub, div, sub, div)')
        with mock.patch('builtins.input', side_effect=['sub, div,mul']):
            self.assertEqual(self.task.input_operations(), ('sub', 'div', 'mul', 'sum'),
                             'For empty input task.operation should be equal (sub, div, mul, sum)')
        with mock.patch('builtins.input', side_effect=['sub, div,mul,div']):
            self.assertEqual(self.task.input_operations(), ('sub', 'div', 'mul', 'div'),
                             'For empty input task.operation should be equal (sub, div, mul, div)')
        with mock.patch('builtins.input', side_effect=['sub, div,mul,div, sum']):
            self.assertEqual(self.task.input_operations(), ('sub', 'div', 'mul', 'div'),
                             'For empty input task.operation should be equal (sub, div, mul, div)')
        with mock.patch('builtins.input', side_effect=['sub, dav,mul,div, sum']):
            self.assertEqual(self.task.input_operations(), ('sub', 'sum', 'mul', 'div'),
                             'For empty input task.operation should be equal (sub, div, mul, div)')

    def test_set_info(self):
        """Test for TaskMaker.set_info() method."""
        # print(whoami())
        # Test object after initialization
        self.assertEqual(self.task.type_of_test, TaskMaker.TYPE_OF_TEST_CONSOLIDATION,
                         'task.type_of_test should be OF_TEST_CONSOLIDATION')
        # Test all by default
        with mock.patch('builtins.input', side_effect=['', '', '', '', '', '']):
            self.assertEqual(self.task.set_info(), None,
                             'Method set_info() returned None')
        # TODO more tests for different enter

    def test_get_first(self):
        """
        Test for :py:class:`TaskMaker.TaskMaker.get_first()`
        :return:
        :rtype None:
        """
        # print(whoami())
        # Test object after initialization
        self.assertEqual(self.task.type_of_test, TaskMaker.TYPE_OF_TEST_CONSOLIDATION,
                         'task.type_of_test should be OF_TEST_CONSOLIDATION')
        self.assertTrue(self.task.get_first(0) in self.task.first,
                        'result task.get_second() should be from to task.second')
        # Test for type of test EDUCATION
        self.task.type_of_test = TaskMaker.TYPE_OF_TEST_EDUCATION
        self.assertEqual(self.task.get_first(0), 1, 'result task.get_first(0) should be 1')
        self.assertEqual(self.task.get_first(7), 8, 'result task.get_first(0) should be 8')
        # Test for type of test Other
        self.task.type_of_test = TaskMaker.TYPE_OF_TEST_CHECKING
        element = self.task.get_first(3)
        # print(element)
        self.assertTrue(element in range(2, 13),
                        'result task.get_first() should be from to 2-13')

    def test_get_second(self):
        """
        Test for :py:class:`TaskMaker.TaskMaker.get_second()`
        :return:
        :rtype None:
        """
        # print(whoami())
        # Test object after initialization
        self.assertEqual(self.task.type_of_test, TaskMaker.TYPE_OF_TEST_CONSOLIDATION,
                         'task.type_of_test should be OF_TEST_CONSOLIDATION')
        self.assertTrue(self.task.get_second() in self.task.second,
                        'result task.get_second() should be from to task.second')
        # Test for type of test EDUCATION
        self.task.type_of_test = TaskMaker.TYPE_OF_TEST_EDUCATION
        self.assertTrue(self.task.get_second() in self.task.second,
                        'result task.get_second() should be from to task.second')
        # Test for type of test Other
        self.task.type_of_test = TaskMaker.TYPE_OF_TEST_CHECKING
        self.assertTrue(self.task.get_second() in range(2, 13),
                        'result task.get_second() should be from to 2-13')

    def test_get_operation(self):
        """Test get_operation() method"""
        # print(whoami())
        # Test operations after initialization
        self.assertEqual(self.task.type_of_test, TaskMaker.TYPE_OF_TEST_CONSOLIDATION,
                         'task.type_of_test should be OF_TEST_CONSOLIDATION')
        for index in (0, 1, 2, 3):
            self.assertEqual(self.task.get_operation(index), self.task.operations[index],
                             f'name of operation with index: {index:d} should be equal {self.task.operations[index]}')
        self.task.type_of_test = TaskMaker.TYPE_OF_TEST_EDUCATION
        for index in (0, 1, 2, 3):
            self.assertEqual(self.task.get_operation(index), self.task.operations[index],
                             f'name of operation with index: {index:d} should be equal {self.task.operations[index]}')
        self.task.type_of_test = TaskMaker.TYPE_OF_TEST_CHECKING
        for index in (0, 1, 2, 3):
            self.assertTrue(self.task.get_operation(index) in self.task.operations,
                            f'name of operation with index: {index:d} should be in {str(self.task.operations)}')

    def test_get_template_id(self):
        """Test get_template_id"""
        # print(whoami())
        self.assertEqual(self.task.type_of_test, TaskMaker.TYPE_OF_TEST_CONSOLIDATION,
                         'by default task.type_of_test is TYPE_OF_TEST_CONSOLIDATION')
        self.assertEqual(self.task.get_template_id(), Exercise.OUT_FORMAT_HIDE_RESULT,
                         'template id should be equal Exercise.OUT_FORMAT_HIDE_RESULT by default')
        self.task.type_of_test = TaskMaker.TYPE_OF_TEST_EDUCATION
        self.assertEqual(self.task.get_template_id(), Exercise.OUT_FORMAT_HIDE_RESULT,
                         'template id should be equal Exercise.OUT_FORMAT_HIDE_RESULT')
        self.task.type_of_test = TaskMaker.TYPE_OF_TEST_VERIFICATION
        self.assertEqual(self.task.get_template_id(), Exercise.OUT_FORMAT_FULL,
                         'template id should be equal Exercise.OUT_FORMAT_FULL')
        self.task.type_of_test = TaskMaker.TYPE_OF_TEST_CHECKING
        self.assertTrue(self.task.get_template_id() in (1, 2, 3),
                        'template id should be equal 1, 2 or 3 for TaskMaker.TYPE_OF_TEST_CHECKING')

    def test_generate(self):
        """Test generate() method"""
        # print(whoami())
        # Test after initialization
        self.assertEqual(len(self.task.rows), 0, 'task should have empty rows')
        self.task.generate()
        self.assertEqual(len(self.task.rows), 12, 'task should have 12 rows')

    def test_get_title_for_print(self):
        """Test get_title_for_print() method."""
        # print(whoami())
        title_for_print = (self.task.strLeftMargin[:-1] + self.task.title + 'date ' +
                           datetime.now().strftime('%Y-%m-%d ') + self.task.learner +
                           ' (' + self.task.quality + ')')
        self.assertEqual(self.task.get_title_for_print(), title_for_print, 'Title for print')

    def test_set_title(self):
        """Test set_title() method."""
        # print(whoami())
        self.assertEqual(self.task.title, 'Test for ', 'task.title should be Test for after initialization')
        # Test task.set_title() by default (without arguments)
        self.assertEqual(self.task.set_title(), None, 'task.set_title should be return None')
        self.assertEqual(self.task.title, 'Trace d\'etude ',
                         "task.title should be <Trace d'etude> after set_title() without arguments")
        # Test task.set_title() with argument
        self.task.set_title('New title for test ')
        self.assertEqual(self.task.title, 'New title for test ', 'task.title should be <New title for test >')

    def test_to_screen(self):
        """Test to_screen() method"""
        # print(whoami())
        with mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            # self.task.generate()
            self.task.to_screen()
            output_mock = mock_stdout.getvalue()
            lines = output_mock.splitlines()
            self.assertEqual(len(lines), 26, 'Output should have 12 lines.')
            self.assertTrue('Test for date ' + datetime.now().strftime('%Y-%m-%d ') in output_mock,
                            'output should contain a "Test for:" in output".')

    def test_to_file(self):
        """Test to_file() method"""
        # print(whoami())
        full_file_name = '/'.join([TaskMaker.DATA_PATH, self.FILE_NAME])
        self.assertFalse(path.isfile(full_file_name), 'file should not exist.')
        self.task.to_file(self.FILE_NAME)
        self.assertTrue(path.isfile(full_file_name), 'file should be exist after to_file().')
        file_size = path.getsize(full_file_name)
        print(file_size)
        self.assertTrue(file_size > 2000, 'file size should be greater than 2000 bytes.')
        if path.isfile(full_file_name):
            os.remove(full_file_name)


if __name__ == '__main__':
    print('Hello', eol, 'It is file:', path.basename(__file__), eol, 'Project:', __project__, eol, 'Created by:',
          __author__, eol, '=' * 20, eol, 'Unit Test for class TaskMaker', eol, '=' * 20)
    main()
