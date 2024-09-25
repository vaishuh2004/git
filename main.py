def greet():
    print("hii")
    print("hello")
greet()

def add():
    a=5
    b=7
     print(a+b)
add()

def add(a,b):
    print(a+b)
m=int(input("Enter a number:"))
n=int(input("Enter a number:"))
add(m,n)

def add(*b):
    print(sum(b))
add(1,2,3,4,5,6,7,8,9)

def sub():
    a=8
    b=5
    print(a-b)
sub()

def multi(*b):
    print(1*2*3*4)
multi(3*4*5)

def div():
    a=10
    b=5
    print(a/b)
div()