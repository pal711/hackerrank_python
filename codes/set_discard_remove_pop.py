def func():
    int(input())
    s = set(map(int, input().split()))
    N = int(input())

    for x in range(N):
        op = input().split()
        if len(op) == 1:
            s.pop()
        elif 'remove' in op:
            s.remove(int(op[1]))
        else:
            s.discard(int(op[1]))
    
    print(sum(s))

if __name__ == '__main__':
    func()

