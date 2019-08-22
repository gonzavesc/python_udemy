a = 5.
a = 10.
a = a + a
print(a)
print(type(a))

my_income = 100
tax_rate= 0.1
my_taxes = my_income * tax_rate
print(my_taxes)

new_word = "hello"
print(new_word)
print(len(new_word))
my_string = "Hello World"
print(my_string[-2])
print(my_string[2:])
print(my_string[:3])
print(my_string[3:6])
print(my_string[::2]) #The start stop step size!
print(my_string[::-1])

x = 'Hello World'
a = x + ' it is beautiful outside'
print(a)
b = a.upper()
print(b)
c = x.split('o')
print(c)

print("this is a string {}".format('INSERTED'))
print("The {} {} {}".format('fox', 'brown', 'quick'))
print("The {2} {1} {0}".format('fox', 'brown', 'quick'))
print("The {q} {b} {f}".format(f='fox', b='brown', q='quick'))

result = 100/777
print(result)
print("The result was {r:.3f}".format(r=result)) #value:with.precision f

name = "Jose"
print(f'Hello, his name is {name}') #formatted string literals

my_list = [1, 2, 3]
print(len(my_list))
my_list[0] = 24
print(my_list)
my_list.append(200)
print(my_list)
my_list.pop()
print(my_list)
my_list.pop(1)
print(my_list)
alfabet_list = ['a','i','b', 'h']
alfabet_list.sort()
print(alfabet_list)
alfabet_list.reverse()
print(alfabet_list)