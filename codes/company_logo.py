#!/bin/python3

from collections import Counter

def cmp_(a):
    return a[1]* 100 + (ord('z') - ord(a[0]))

def func():
    s = input()
    top = list(Counter(s).items())
    top = sorted(top, key = cmp_ , reverse = True)[:3]
    for x in top:
        print(x[0], x[1])


if __name__ == '__main__':
    func()

