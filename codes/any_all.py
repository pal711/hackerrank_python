#/bin/python3

def chk_palindrome(string):
    strt = 0
    end = len(string) - 1
    palindrm = True
    while strt <= end:
        if string[strt] != string[end]:
            palindrm = False
            break
        strt += 1
        end -= 1
    
    return palindrm

def func():
    input()
    numbers = input().split()
    pos = all(['-' not in x for x in numbers])
    palindrm = any([chk_palindrome(x) for x in numbers])
    print(pos and palindrm)

if __name__ == '__main__':
    func()

