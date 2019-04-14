from itertools import product

def func():
    k, m = list(map(int, input().split()))

    lists = []
    for x in range(k):
        temp = list(map(int, input().split()))
        lists.append(temp[1:])

    max_ = 0
    for x in product(*lists):
        temp = sum( map(lambda p : p ** 2, x) ) % m
        max_ = temp if temp > max_ else max_
    
    print(max_)



if __name__ == '__main__':
    func()

