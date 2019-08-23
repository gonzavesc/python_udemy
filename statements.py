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