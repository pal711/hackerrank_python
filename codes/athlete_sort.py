#!/bin/python3
import sys

def func(arr, k):
    arr.sort(key = lambda x : x[k])

    for list_ in arr:
        for item in list_:
            sys.stdout.write(str(item)+ " ")
        print()


if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())

    func(arr, k)

