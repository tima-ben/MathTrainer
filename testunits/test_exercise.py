#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'Eduard Balantsev'
__project__ = 'MathTrainer'

from unittest import TestCase
from unittest import main
from Exercise import Exercise


class TestExercise(TestCase):

    def setUp(self):
        self.s = Exercise()
        self.sub = Exercise(6, 1, 'sub')
        self.sub1 = Exercise(1, 6, 'sub')
        self.mul = Exercise(2, 6, 'mul')
        self.div = Exercise(2, 6, 'div')

    def test_exception_in_constructor(self):
        with self.assertRaises(Exception):
            Exercise(operation='test')

    def test_type_of_property(self):
        self.assertTrue(type(self.s.LIST_OPERATIONS) is tuple, 'obj.LIST_OPERATIONS ot type tuple')
        self.assertTrue(type(self.s.DEFAULT_OPERATION) is str, 'obj.DEFAULT_OPERATION ot type str')
        self.assertTrue(type(self.s.OUT_FORMAT_LIST) is tuple, 'obj.DEFAULT_OPERATION ot type tuple')
        self.assertTrue(type(self.s.singleOperation) is dict, 'obj.singleOperation ot type dict')
        self.assertTrue(type(self.s.create) is bool, 'obj.create ot type dict')
        self.assertTrue(type(self.s.operation) is str, 'obj.operation ot type str')
        self.assertTrue(type(self.s.a) is int, 'obj.a of type int')
        self.assertTrue(type(self.s.a_str) is str, 'obj.a_str of type str')
        self.assertTrue(type(self.s.b) is int, 'obj.b of type int')
        self.assertTrue(type(self.s.b_str) is str, 'obj.b_str of type str')
        self.assertTrue(type(self.s.result) is int, 'obj.result of type int')
        self.assertTrue(type(self.s.result_str) is str, 'obj.result_str of type str')

    def test_constructor(self):
        self.assertIsInstance(self.s, Exercise, 'Creation by default Exercise')
        self.assertEqual(self.s.a, 0, 'obj.a by default equal 0')
        self.assertEqual(self.s.b, 0, 'obj.b by default equal 0')
        self.assertEqual(self.s.result, 0, 'obj.result by default equal 0')
        self.assertEqual(self.s.a_str, ' 0 ', 'obj.a by default equal " 0 "')
        self.assertEqual(self.s.b_str, ' 0 ', 'obj.b by default equal " 0 "')
        self.assertEqual(self.s.result_str, ' 0 ', 'obj.result_str by default equal " 0 "')
        self.assertEqual(self.s.operation, 'sum', 'obj.operation_str by default equal "sum"')
        self.assertEqual(self.s.create, True, 'obj.create by default equal True')

    def test_operation_mul(self):
        self.assertIsInstance(self.mul, Exercise, 'Creation by default Exercise')
        self.assertEqual(self.mul.a, 2, 'obj.a by default equal 2')
        self.assertEqual(self.mul.b, 6, 'obj.b by default equal 6')
        self.assertEqual(self.mul.result, 12, 'obj.result by default equal 12')
        self.assertEqual(self.mul.a_str, ' 2 ', 'obj.a by default equal " 2 "')
        self.assertEqual(self.mul.b_str, ' 6 ', 'obj.b by default equal " 6 "')
        self.assertEqual(self.mul.result_str, '12 ', 'obj.result_str by default equal " 12"')
        self.assertEqual(self.mul.operation, 'mul', 'obj.operation_str by default equal "mul"')
        self.assertEqual(self.mul.create, True, 'obj.create by default equal True')

    def test_operation_div(self):
        self.assertIsInstance(self.div, Exercise, 'Creation by default Exercise')
        self.assertEqual(self.div.a, 12, 'obj.a by default equal 2')
        self.assertEqual(self.div.b, 6, 'obj.b by default equal 6')
        self.assertEqual(self.div.result, 2, 'obj.result by default equal 12')
        self.assertEqual(self.div.a_str, '12 ', 'obj.a by default equal "12 "')
        self.assertEqual(self.div.b_str, ' 6 ', 'obj.b by default equal " 6 "')
        self.assertEqual(self.div.result_str, ' 2 ', 'obj.result_str by default equal " 2 "')
        self.assertEqual(self.div.operation, 'div', 'obj.operation_str by default equal "div"')
        self.assertEqual(self.div.create, True, 'obj.create by default equal True')

    def test_operation_sub(self):
        self.assertIsInstance(self.sub, Exercise, 'Creation by default Exercise')
        self.assertEqual(self.sub.a, 6, 'obj.a by default equal 6')
        self.assertEqual(self.sub.b, 1, 'obj.b by default equal 1')
        self.assertEqual(self.sub.result, 5, 'obj.result by default equal 5')
        self.assertEqual(self.sub.a_str, ' 6 ', 'obj.a by default equal " 6 "')
        self.assertEqual(self.sub.b_str, ' 1 ', 'obj.b by default equal " 1 "')
        self.assertEqual(self.sub.result_str, ' 5 ', 'obj.result_str by default equal " 5 "')
        self.assertEqual(self.sub.operation, 'sub', 'obj.operation_str by default equal "sub"')
        self.assertEqual(self.sub.create, True, 'obj.create by default equal True')

    def test_operation_sub1(self):
        self.assertIsInstance(self.sub, Exercise, 'Creation by default Exercise')
        self.assertEqual(self.sub1.a, 6, 'obj.a by default equal 6')
        self.assertEqual(self.sub1.b, 6, 'obj.b by default equal 6')
        self.assertEqual(self.sub1.result, 0, 'obj.result by default equal 0')
        self.assertEqual(self.sub1.a_str, ' 6 ', 'obj.a by default equal " 6 "')
        self.assertEqual(self.sub1.b_str, ' 6 ', 'obj.b by default equal " 6 "')
        self.assertEqual(self.sub1.result_str, ' 0 ', 'obj.result_str by default equal " 0 "')
        self.assertEqual(self.sub1.operation, 'sub', 'obj.operation_str by default equal "sub"')
        self.assertEqual(self.sub1.create, True, 'obj.create by default equal True')

    def test_for_out(self):
        self.assertEqual(self.s.for_out(), '  0  +  0  =   ', 'obj.for_out() returned "'+self.s.for_out()+'"')
        self.assertEqual(self.s.for_out(0), '  0  +  0  = 0 ', 'obj.for_out(0) returned "'+self.s.for_out(0)+'"')
        self.assertEqual(self.s.for_out(2), '  0  +     = 0 ', 'obj.for_out(2) returned "'+self.s.for_out(2)+'"')
        self.assertEqual(self.s.for_out(3), '     +  0  = 0 ', 'obj.for_out(3) returned "'+self.s.for_out(3)+'"')
        self.assertEqual(self.s.for_out(4), '  0     0  = 0 ', 'obj.for_out(4) returned "'+self.s.for_out(4)+'"')
        self.assertEqual(self.sub.for_out(), '  6  -  1  =   ', 'obj.for_out() returned "'+self.sub.for_out()+'"')
        self.assertEqual(self.sub.for_out(0), '  6  -  1  = 5 ', 'obj.for_out(0) returned "'+self.sub.for_out(0)+'"')
        self.assertEqual(self.sub.for_out(2), '  6  -     = 5 ', 'obj.for_out(2) returned "'+self.sub.for_out(2)+'"')
        self.assertEqual(self.sub.for_out(3), '     -  1  = 5 ', 'obj.for_out(3) returned "'+self.sub.for_out(3)+'"')
        self.assertEqual(self.sub.for_out(4), '  6     1  = 5 ', 'obj.for_out(4) returned "'+self.sub.for_out(4)+'"')
        self.assertEqual(self.sub1.for_out(), '  6  -  6  =   ', 'obj.for_out() returned "'+self.sub1.for_out()+'"')
        self.assertEqual(self.sub1.for_out(0), '  6  -  6  = 0 ', 'obj.for_out(0) returned "'+self.sub1.for_out(0)+'"')
        self.assertEqual(self.sub1.for_out(2), '  6  -     = 0 ', 'obj.for_out(2) returned "'+self.sub1.for_out(2)+'"')
        self.assertEqual(self.sub1.for_out(3), '     -  6  = 0 ', 'obj.for_out(3) returned "'+self.sub1.for_out(3)+'"')
        self.assertEqual(self.sub1.for_out(4), '  6     6  = 0 ', 'obj.for_out(4) returned "'+self.sub1.for_out(4)+'"')
        self.assertEqual(self.mul.for_out(), '  2  ' + u'\xd7' + '  6  =   ', 'obj.for_out() returned "'
                         + self.mul.for_out()+'"')
        self.assertEqual(self.mul.for_out(0), '  2  ' + u'\xd7' + '  6  =12 ', 'obj.for_out(0) returned "'
                         + self.mul.for_out(0)+'"')
        self.assertEqual(self.mul.for_out(2), '  2  ' + u'\xd7' + '     =12 ', 'obj.for_out(2) returned "'
                         + self.mul.for_out(2)+'"')
        self.assertEqual(self.mul.for_out(3), '     ' + u'\xd7' + '  6  =12 ', 'obj.for_out(3) returned "'
                         + self.mul.for_out(3)+'"')
        self.assertEqual(self.mul.for_out(4), '  2     6  =12 ', 'obj.for_out(4) returned "'
                         + self.mul.for_out(4)+'"')
        self.assertEqual(self.div.for_out(), ' 12  ' + u'\xf7' + '  6  =   ', 'obj.for_out() returned "'
                         + self.div.for_out() + '"')
        self.assertEqual(self.div.for_out(0), ' 12  ' + u'\xf7' + '  6  = 2 ', 'obj.for_out(0) returned "'
                         + self.div.for_out(0) + '"')
        self.assertEqual(self.div.for_out(2), ' 12  ' + u'\xf7' + '     = 2 ', 'obj.for_out(2) returned "'
                         + self.div.for_out(2) + '"')
        self.assertEqual(self.div.for_out(3), '     ' + u'\xf7' + '  6  = 2 ', 'obj.for_out(3) returned "'
                         + self.div.for_out(3) + '"')
        self.assertEqual(self.div.for_out(4), ' 12     6  = 2 ', 'obj.for_out(4) returned "'
                         + self.div.for_out(4) + '"')


if __name__ == '__main__':
    print 'Hi, It is ' + __file__ + ' project ' + __project__ + ' by ' + __author__
    main()