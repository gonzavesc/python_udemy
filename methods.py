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
	return ' '.join(reversed_word) #joins using the character between ' '
print(master_yode('hello i am'))

def has_33(nums):
	for i in range(0, len(nums)-1):
		if nums[i] ==3 and nums[i+1] == 3: # if nums[i:i+2] == [3,3]
			return True
	return False
def paper_doll(text):
	result = ''
	for char in text:
		result += char * 3
	return result
print(paper_doll('hey'))
def summer_69(arr):
	sum = 0
	add = True
	for num in arr:
		while add:
			if num != 6:
				sum += num
				break
			else:
				add = False
		while not add:
			if num != 9:
				break
			else:
				add = True
				break
	return sum
print(summer_69([1,2,3,4,5,6,7,8,9,10]))

def spy_game(nums):
	code = [0,0,7,'x']
	for num in nums:
		if num == code[0]:
			code.pop(0)
	return len(code)==1
print(spy_game([0,0,7,12]))

def count_primes(num):
	if num < 2:
		return 0
	primes = [2]
	x = 3
	while x <= num:
		for y in range(3,x,2):
			if x%y == 0:
				x += 2
				break
		else: # solo entra si no usa el break
			primes.append(x)
			x += 2
	print(primes)
	return len(primes)
print(count_primes(2000))
#check out the eulerproject!!!!
def square(num):
	return num**2
my_nums = [1,2,3,4,5]
for item in map(square, my_nums):
	print(item)