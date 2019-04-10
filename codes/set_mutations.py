#!/bin/python3

def func():
    input()
    a = set(list(map(int, input().split())))
    for x in range(int(input())):
        operation = input().split()[0]
        b = set(list(map(int, input().split())))
        command = 'a.'+operation+'(b)'
        eval(command)
        
    print(sum(a))

if __name__ == "__main__":
    func()

