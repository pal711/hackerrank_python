import sys
from collections import deque

def func():
    d = deque()
    for x in range(int(input())):
        command = input().split()
        if len(command) == 2:
            cmd_str = "d." + command[0] + "(" + command[1] +")"
        else:
            cmd_str = "d." + command[0] + "()"
        
        eval(cmd_str)

    for x in d:
        sys.stdout.write(str(x)+ ' ')


if __name__ == '__main__':
    func()

