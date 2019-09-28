def add(n1,n2):
    print(n1+n2)
add(10,20)
number1=10
number2=input("Please provide a number: ")
#add(number1,number2)
#print("something happened")
try:
    result=10+10#'10'
except:
    print("Hey it looks like you arent addin correctly")
else:
    print("went well")
    print(result)


try:
    f = open('testfile','r')
    f.write('Write a test file')
except TypeError:
    print("There was a TypeError")
except OSError:
    print("Hey you have an OS error")
finally:
    print("I always run")


def ask_for_int():
    while True:
        try:
            result=int(input("Please provide an integer: "))
        except:
            print("This is not a number")
            continue
        else:
            print("Thank you")
            break
        finally:
            print("End")
ask_for_int()