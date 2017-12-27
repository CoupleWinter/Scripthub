# coding=utf-8

from functools import wraps
from inspect import getgeneratorstate


def coroutine(func):
    # 装饰器：向前执行到第一个yield 表达式，预激func
    @wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen

    return primer


@coroutine
def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total / count


if __name__ == '__main__':
    a = averager()
    print(getgeneratorstate(a))
    print(a.send(10))
