#!/usr/bin/python3
def func():
    a = set(list(map(int, input().split())))
    res = True
    for x in range(int(input())):
        if res:
            temp = set(list(map(int, input().split())))
            if not (a.issuperset(temp) and len(a) > len(temp)):
                res = False
                continue
        else:
            input()
        
    print(res)

if __name__ == '__main__':
    func()

