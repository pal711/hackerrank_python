#/bin/python3

def func():
    input()
    str_ = input().split()
    print(all(['-' not in x for x in str_]) and any( [ x == x[-1::-1] for x in str_]))

if __name__ == '__main__':
    func()

