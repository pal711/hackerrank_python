#!/usr/bin/python3

def func():
    t = int(input())
    while t > 0:
        input()
        t -= 1
        ple_flag = True
        sides = list(map(int, input().split()))
        top = sides.pop(0) if sides[0] >= sides[-1] else sides.pop(-1)
        
        while sides:
            index = 0 if sides[0] >= sides[-1] else -1
            if top >= sides[index]:
                top = sides.pop(index)
            else:
                ple_flag = False
                break
            
        print("Yes") if ple_flag else print("No")


if __name__ == '__main__':
    func()

