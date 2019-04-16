#!/usr/bin/python3

def func():
    n,x = list(map(int, input().split()))
    marks = []
    for y in range(x):
        marks.append(list(map(float, input().split())))
    
    for scores in zip(*marks):
        print(round(sum(scores)/x,1))

if __name__ == '__main__':
    func()
   
