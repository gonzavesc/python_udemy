hungry = 2
if hungry > 3:
	print('Hey')
else:
	print('not')

loc = 'dsada'
if loc == 'Bank':
	print('Bank')
elif loc == 'a':
	print('a')
else:
	print('else')

mylist = [1,2,3,4,5,6,7,8,9,10]
for num in mylist:
	if num % 2 == 0:
		print('The number {n:1.2f} is even'.format(n=num))
list_sum = 0
for num in mylist:
	list_sum += num
print(list_sum)
mystring = 'Hello World'
for letter in mystring:
	print(letter)
mylist =[(1,2), (3,4), (5,6)]
for item in mylist:
	print(item)
for (a,b) in mylist: #tuple unpacking!!
	print(a)
	print(b)
d = {'k1':1, 'k2':2, 'k3':3}
for item in d:
	print(item) #only oututs keys
for item in d.items():
	print(item)
for item in d.values():
	print(item)

i = 0
while(i <10):
	i+=1
	print(i)

x = [1,2,3]
for item in x:
	pass # pass does nothing at all
	if item == 1:
		continue # jumps to next iteration
	else:
		print(item)
		break #exits iteration
for num in range(10):
	print(num)
for num in range(0,10):
	print(num)
for num in range(0,10,2):
	print(num)
a = list(range(0,100,10))
print(a)
word = 'abcde'
for item in enumerate(word): #primts index and value!!!
	print(item)
for index, letter in enumerate(word):
	print('The index is {} and letter is {}'.format(index,letter))
my_list1 = [1, 2, 3]
my_list2 = ['a', 'b', 'c']
for item in zip(my_list1, my_list2):
	print(item)
my_list1 = [1, 2, 3]
my_list2 = ['a', 'b', 'c']
my_list3 = [100, 200, 300, 400]
for item in zip(my_list1, my_list2, my_list3):
	print(item)

a = list(zip(my_list1, my_list2, my_list3))
print(a)
b = 'x' in [1,2,3]
print(b)
print('mykey' in {'mykey':100})
d = {'mykey':100}
print(100 in d.values())
print(min(my_list1))
print(max(my_list1))

from random import shuffle
my_list = [1,2,3,4,5,6,7,8,9]
shuffle(my_list)
print(my_list)
from random import randint
print(randint(0,101))

result = input('Enter a number here: ') # always are strings!!!
result = float(result)