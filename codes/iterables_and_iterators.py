#!/usr/bin/python3
from itertools import combinations

def func():
    input()
    str_ = input().split()
    k = int(input())
    str_without_a = list(filter(lambda x : x != 'a', str_))
    com_all = len(list(combinations(str_, k)))
    com_without_a = len(list(combinations(str_without_a, k)))
    res = round( (com_all - com_without_a) / com_all, 4 )
    print(res)

if __name__ == '__main__':
    func()

