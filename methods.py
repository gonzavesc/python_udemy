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
#*args and **kwargs in python arguments and key words arguments
def my_func(a,b,c=0,d=0):
	# returns 5% of the sum of a and b
	return sum((a,b,c,d))*0.05
print(my_func(40,60,d=10)) # can only put d= if it's set as a keyword!!
def myfunc(*args): #puts args in a tuple!!
	print(args)
	return sum(args)*0.05
print(myfunc(40,60,12,23,55325,65326,63,1))
def myfunc(*values): #the word after * can be anything, but always use args!!!!!
	print(values)
	return sum(args)*0.05

def myfunc(**kwargs):
	print(kwargs)
	if 'fruit' in kwargs: # kwargs is a dictionary!!
		print('My fruit of choice is {}'.format(kwargs['fruit']))
	else:
		print('I did not find any fruit here')
myfunc(fruit='apple', veggie='lettuce')

def myfunc(a,*args, **kwargs):
	print('I would like {} {} {}'.format(a, args[0], kwargs['food']))
myfunc(23,14,food='omelette')
def lesser_of_two_evens(a,b):
	if a%2==0 and b%2==0:
		return min(a,b)
	else:
		return max(a,b)
print(lesser_of_two_evens(2,4))
print(lesser_of_two_evens(2,5))

def animal_crackers(text):
	mylist = (text.split())
	return mylist[0][0].lower() == mylist[1][0].lower()
print(animal_crackers('turtle Tortoise'))
print(animal_crackers('hey ping'))

def old_macdonald(name):
	first_letter = name[0]
	inbetween = name[1:3]
	fourth_letter = name[3]
	rest = name[4:]
	first_half = name[:3]
	second_half = name[3:] # can use the capitalize!!!
	return first_letter.upper()+inbetween+fourth_letter.upper()+rest
print(old_macdonald('macdonald'))

def master_yode(text):
	wordlist = text.split()
	reversed_word = wordlist[::-1]
	return ' '.join(reversed_word)
print(master_yode('hello i am'))