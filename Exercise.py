#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__: str = 'Eduard Balantsev'
__project__: str = 'MathTrainer'


class Exercise(object):
    """
    Exemplar for test math tables
    """
    OPERATION_DIV: str = 'div'
    OPERATION_MUL: str = 'mul'
    OPERATION_SUB: str = 'sub'
    OPERATION_SUM: str = 'sum'
    DEFAULT_OPERATION: str = 'sum'
    LIST_OPERATIONS: tuple[str, str, str, str] = (OPERATION_SUM, OPERATION_SUB, OPERATION_DIV, OPERATION_MUL)
    ELEMENT_FORMAT: str = '{:^3}'
    OUT_FORMAT_LIST: tuple[str, str, str, str, str] = (' {0[0]:s} {0[1]:s} {0[2]:s} ={0[3]:s}',
                                                       ' {0[0]:s} {0[1]:s} {0[2]:s} =   ',
                                                       ' {0[0]:s} {0[1]:s}     ={0[3]:s}',
                                                       '     {0[1]:s} {0[2]:s} ={0[3]:s}',
                                                       ' {0[0]:s}   {0[2]:s} ={0[3]:s}')
    OUT_FORMAT_FULL: int = 0
    OUT_FORMAT_HIDE_RESULT: int = 1
    OUT_FORMAT_HIDE_B: int = 2
    OUT_FORMAT_HIDE_A: int = 3
    OUT_FORMAT_HIDE_OPERATION: int = 4
    create: bool = False
    singleOperation: dict[str, str] = {OPERATION_SUM: '+', OPERATION_SUB: '-', OPERATION_DIV: '\xf7',
                                       OPERATION_MUL: '\xd7'}

    def __init__(self, a: int = 0, b: int = 0, operation: str = DEFAULT_OPERATION):
        """
        constructor
        :type self: Exercise :type a: integer :type b integer :type operation basestring
        """
        if operation in self.LIST_OPERATIONS:
            self.operation = operation
        else:
            raise Exception('Parameter operation: \'%s\' not correct. it can be %s' % (operation,
                                                                                       self.LIST_OPERATIONS.__str__()))
        self.a: int = 0
        self.b: int = 0
        self.result: int = 0
        if operation == self.OPERATION_SUM or operation == self.OPERATION_MUL:
            self.a = a
            self.b = b
            if operation == self.OPERATION_SUM:
                self.result = self.a + self.b
            else:
                self.result = self.a * self.b
        elif operation == self.OPERATION_SUB:
            self.result = a
            self.a = self.result + b
            self.b = b
        else:
            self.a = a * b
            self.b = b
            self.result = int(self.a / self.b)
        self.a_str: str = self.ELEMENT_FORMAT.format(self.a, )
        self.b_str: str = self.ELEMENT_FORMAT.format(self.b, )
        self.result_str: str = self.ELEMENT_FORMAT.format(self.result, )
        self.create: bool = True
        self.list_for_out: tuple[str, str, str, str] = (self.a_str, self.singleOperation[self.operation], self.b_str,
                                                        self.result_str)

    def for_out(self, hide_index: int = OUT_FORMAT_HIDE_RESULT) -> str:
        """
        String exercise for output format
        :type self: Exercise :type hide_index: int
        :param hide_index: index in OUT_FORMAT_LIST which indicates output format
        :return:
        """
        return self.OUT_FORMAT_LIST[hide_index].format(self.list_for_out)


if __name__ == '__main__':
    print('Hi, It is', __file__, 'project', __project__, 'by', __author__)
