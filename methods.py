mylist = []
help(mylist.insert)
#functions in python
def name_function():
	'''
	DOCSTRING: Information about the function
	INPUT
	OUTPUT
	'''
	print('hello')
name_function()
help(name_function)

def say_hello(name):
	print('hello '+name)
say_hello('jose')
def say_hello_def(name='NAME'):
	print('hello '+name)
say_hello_def()
say_hello_def(name='hey')
say_hello_def('heeey')
def say_hello_ret(name='NAME'):
	return 'hello '+name
result = say_hello_ret('test')
print(result)

def add(n1,n2):
	return n1+n2
print(add(20,30))
def dog_check(mystring):
	if 'dog' in mystring.lower():
		return True
	else:
		return False

print(dog_check('my dog is huge'))

def dog_check_2(mystring):
	return 'dog' in mystring.lower()
print(dog_check('my Dog is huge'))
#pig latin
# is starts with vowel ad ay to end if not put first letter at the end an add
# ay
def pig_latin(word):
	first_letter = word[0]
	if first_letter in 'aeiou':
		pig_word = word + 'ay'
	else:
		pig_word = word[1:] + first_letter + 'ay'
	return pig_word
print(pig_latin('hello'))