#!/usr/bin/python3

def func():
    t = int(input())
    while t:
        t -= 1
        input()
        a = set(list(map(int, input().split())))
        input()
        b = set(list(map(int, input().split())))
        
        print("False") if a-b else print("True")

    
if __name__ == '__main__':
    func()

