#########################
# coding=utf-8
# 这里的泛型函数是指由一组为不同类型参数执行相似操作的函数组成的函数，具体调用哪一个函数的实现取决于分发算法和参数类型。
# Python单分发器是实现泛型函数的一种形式
# Python泛型函数与单分发器
##########################
from functools import singledispatch


@singledispatch
def fun(arg, verbose=False):
    if verbose:
        print('Let me just say', end='')
    print(arg)


@fun.register(int)
def _(arg, verbose=False):
    if verbose:
        print('Stength in numbers', end='')
    print(arg)


@fun.register(float)
def _(arg, verbose=False):
    if verbose:
        print('Half of your number is ', end='')
    print(arg / 2)


@fun.register(tuple)
def _(arg, verbose=False):
    if verbose:
        print('tuple')
    print(arg)


if __name__ == '__main__':
    fun(0.1)
