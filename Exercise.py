#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'Eduard Balantsev'
__project__ = 'MathTrainer'


class Exercise(object):
    """ Exemplar for test math tables
    """
    LIST_OPERATIONS = ('sum', 'sub', 'div', 'mul')
    DEFAULT_OPERATION = 'sum'
    OUT_FORMAT_LIST = (u' {0[0]:s} {0[1]:s} {0[2]:s} ={0[3]:s}',
                       u' {0[0]:s} {0[1]:s} {0[2]:s} =   ',
                       u' {0[0]:s} {0[1]:s}     ={0[3]:s}',
                       u'     {0[1]:s} {0[2]:s} ={0[3]:s}',
                       u' {0[0]:s}   {0[2]:s} ={0[3]:s}')
    OUT_FORMAT_FULL = 0
    OUT_FORMAT_HIDE_RESULT = 1
    OUT_FORMAT_HIDE_B = 2
    OUT_FORMAT_HIDE_A = 3
    OUT_FORMAT_HIDE_OPERATION = 4
    create = False
    singleOperation = {'sum': u'+', 'sub': u'-', 'div': u'\xf7', 'mul': u'\xd7'}

    def __init__(self, a=0, b=0, operation='sum'):
        """ constructor for Exercise
        :type self: Exercise :type a: integer :type b integer :type operation basestring
        """
        if operation in self.LIST_OPERATIONS:
            self.operation = operation
        else:
            raise Exception('Parameter operation: \'%s\' not correct. it can be %s' % (operation,
                                                                                       self.LIST_OPERATIONS.__str__()))
        if operation == 'sum' or operation == 'mul':
            self.a = a
            self.b = b
            if operation == 'sum':
                self.result = self.a+self.b
            else:
                self.result = self.a*self.b
        elif operation == 'sub':
            self.result = a-1
            self.a = self.result + b
            self.b = b
        else:
            self.a = a*b
            self.b = b
            self.result = self.a/self.b
        self.a_str = '{:^3}'.format(self.a,)
        self.b_str = '{:^3}'.format(self.b,)
        self.result_str = '{:^3}'.format(self.result,)
        self.create = True
        self.list_for_out = (self.a_str, self.singleOperation[self.operation], self.b_str, self.result_str)

    def for_out(self, hide=OUT_FORMAT_HIDE_RESULT):
        return self.OUT_FORMAT_LIST[hide].format(self.list_for_out)

if __name__ == '__main__':
    print 'Hi, It is '+__file__+' project '+__project__+' by '+__author__
