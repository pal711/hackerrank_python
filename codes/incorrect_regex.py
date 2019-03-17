import re

def func():
	t = int(input())
	while t > 0:
		t -= 1
		pattrn = input()
		valid = True
		try:
			re.compile(pattrn)
		except:
			valid = False

		print(valid)

if __name__ == "__main__":
	func()

