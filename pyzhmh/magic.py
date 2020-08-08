import os
from sys import _getframe as __frame__


def __dirname__():
    """
    :return: 文件所在目录
    """
    return os.path.abspath(os.path.dirname(__frame__().f_back.f_code.co_filename))


def __line__():
    """
    :return: 所在位置行号
    """
    return __frame__().f_back.f_lineno


def __fun__():
    """
    :return: 所在位置函数名
    """
    return __frame__().f_back.f_code.co_name


def __assert__(condition, error_text='', exit_code=1):
    where_call = __frame__().f_back
    try:
        assert condition
    except AssertionError:
        print('\033[31m', end='')
        print('AssertionError')
        print(' * Filename: %s:' % where_call.f_code.co_filename)
        print(' * Module: %s' % where_call.f_code.co_name)
        print(' * Line: %s' % where_call.f_lineno)
        print(' * Description: %s' % error_text)
        print('\033[0m', end='')
        exit(exit_code)
