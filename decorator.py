def func():
    return 1

def hello():
    return "hello!"

greet = hello
print(greet())
del hello
print(greet())
def hello(name ='Jose'):
    print("The hello() function has been executed!")

    def greet():
        return "\t This is the greet() func inside hello"
    print(greet())
    def welcome():
        return "\t This is the welcome inside hello"
    print(welcome())
    print("I am going to retun a function")
    if name == 'Jose':
        return greet
    else:
        return welcome

hello()
my_newfunc=hello('Jose')
print(my_newfunc())

def cool():
    def super_cool():
        return 'I am very cool'
    return super_cool
some_func = cool()
print(some_func())
def hello():
    return 'Hi Jose'
def other(some_def_func):
    print('some other code runs here')
    print(some_def_func())
other(hello)
def new_decorator(original_function):
    def wrap_func():
        print('some extra code, before the original funtion')
        original_function()
        print('adding code after')
    return wrap_func
def func_needs_decorator():
    print('I want to be decorated')
decorated_func = new_decorator(func_needs_decorator)
decorated_func()
@new_decorator
def func_needs_decorator():
    print('I want to be decorated')
func_needs_decorator()