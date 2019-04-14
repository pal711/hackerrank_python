#!/usr/bin/python3
def func():
    input()
    eng = set(list(map(int, input().split())))
    input()
    frnch = set(list(map(int, input().split())))

    print(len(eng-frnch))


if __name__ == '__main__':
    func()

