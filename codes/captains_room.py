from collections import Counter

def func():
    k = int(input())
    room_nos = list(map(int, input().split()))
    c = Counter(room_nos)
    for x in c.keys():
        if c[x] != k:
            print(x)

if __name__ == '__main__':
    func()

