import sys
from itertools import groupby

def func():
    s = input()

    for key, group in groupby(s):
        output_str = '('+str(len(list(group))) + ', ' + str(key)+') '
        sys.stdout.write(output_str)
    print()

if __name__ =='__main__':
    func()

