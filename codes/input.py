#!/usr/bin/python3

def func():
    x, k = list(map(float, input().split()))
    poly = input()
    print(eval(poly)==k)

if __name__ =='__main__':
    func()
    
