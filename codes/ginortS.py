import re

def func():
    string = input()
    lower = re.compile('[a-z]')
    upper = '[A-Z]'
    odd = '[13579]'
    even = '[02468]'

    lower_str = sorted(re.findall(lower, string))
    upper_str = sorted(re.findall(upper, string))
    odd_str = sorted(re.findall(odd, string))
    even_str = sorted(re.findall(even, string))

    sorted_str = "".join(lower_str) + "".join(upper_str) + \
    "".join(odd_str) + "".join(even_str)

    print(sorted_str)

if __name__ == '__main__':
    func()

