#one.py
print('hello')
# __name__ = __main__ if python one.py

def func():
    print("Func in one.py")
print("Top level in one.py")

if __name__ == '__main__':
    print("one.py is working directly")
else:
    print("one.py is being imported")