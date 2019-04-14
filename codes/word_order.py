from collections import OrderedDict
import sys

def func():
    n = int(input())
    dict_ = OrderedDict()

    for x in range(n):
        string = input()
        if string in dict_.keys():
            dict_[string] += 1
        else:
            dict_[string] = 1

    print(len(dict_.keys()))
    for x in dict_.keys():
        sys.stdout.write(str(dict_[x])+' ')
    print()
        

if __name__ == '__main__':
    func()

