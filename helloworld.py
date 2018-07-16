'''
Making a bunch of errors!

Adding

Weird

Unknown 

Stuff

and Text to an otherwise elegantly written program
'''

while True:
	print('I am an infinite loop!')


def infinite_recursion(func):
	func(infinite_recursion)

if __name__=='__main__':
	infinite_recursion(infinite_recursion)

print("hello-world")