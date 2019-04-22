#!bin/python3
import re

def func():
    t = int(input())
    pattern = '[+-]?[0-9]*\.[0-9]+'
    pattern = re.compile(pattern)
    while t:
        t -= 1
        string = input()
        match = re.match(pattern, string)
        if match and (match.end() - match.start() == len(string)):
            print("True")
        else:
            print("False")

    
if __name__ == '__main__':
    func()

