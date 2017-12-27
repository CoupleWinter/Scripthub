# coding=utf-8

from functools import wraps
from inspect import getgeneratorstate
from collections import namedtuple

Result = namedtuple('Result', 'count average')


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
        try:
            term = yield average
            if term is None:
                break
            total += term
            count += 1
            average = total / count
        except Exception as e:
            print(e.message)
        else:
            print('Coroutine received')
    return Result(count, average)


if __name__ == '__main__':
    a = averager()
    print(getgeneratorstate(a))
    a.send(10)
    try:
        a.send(None)
    except StopIteration as exc:
        result = exc.value
        print(result)
    a.close()
