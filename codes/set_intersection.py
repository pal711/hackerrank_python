#!/usr/bin/python3

def func():
    input()
    eng = map(int, input().split())
    input()
    frnch = map(int, input().split())
    print(len(set(eng).intersection(set(frnch))))
    

if __name__ == '__main__':
    func()

