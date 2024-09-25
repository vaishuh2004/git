#stack using lists
backstack=[]
forwardstack=[]
runningstack=[]
def search():
    i=input("Enter a word for search:")
    if len(runningstack)>=1:
        backstack.append(runningstack.pop())
    runningstack.append(i)
def back():
    c=backstack.pop()
    print(c)
    forwardstack.append(c)
def forward():
    c=forwardstack.pop()
    backstack.append(c)
    print(c)
oper="search"
while True:
    oper=input("What you need to do?")
    if oper=="serach":
        search()
    elif oper=="exit":
        break
    elif oper=="forward":
        forward()
    elif oper=="back":
        back()


def fact(n):
    print(n)
    if n<=1:
        return 1
    c=n*fact(n-1)
    return c
print(fact(5))

#stack using collection
from collections import deque
stack=deque([1,"2",3,4])
print(stack)
stack.appendleft(5)
print(stack)
stack.popleft()
print(stack)