#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from multiprocessing import Process, Queue
import math

EPS = .0000001


def inf_sum(x, out):
    summa = 1.0
    temp = 0
    n = 1
    while abs(summa - temp) > EPS:
        temp = summa
        summa += math.sin(n * x) / n
        n += 1

    out.put(summa)


def check(x, out):
    res = - math.log(2 * math.sin(0.5 * x))

    out.put(res)


if __name__ == '__main__':
    x = math.pi

    out1 = Queue()
    out2 = Queue()
    process_1 = Process(target=inf_sum, args=(x, out1))
    process_2 = Process(target=check, args=(x, out2))
    process_1.start()
    process_2.start()
    result1 = out1.get()
    result2 = out2.get()
    process_1.join()
    process_2.join()

    print(f"The sum is: {result1}")
    print(f"The check sum is: {result2}")