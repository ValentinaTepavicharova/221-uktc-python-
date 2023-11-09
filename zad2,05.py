from collections import deque

stack=deque()

n=int(input("Enter 1 to put the number at the back of the stack;Enter 2 to delete the number that is on top of the stack;Enter 3 to print the biggest number in the stack;Enter 4 to print the smallest number in the stack;Enter 5 to print the lenght of the stack;: "))
for i in range (n):
    command=input().split(" ")
    command[0]=int(command[0])
    if command[0]==1:
        stack.append(int(command[1]))
    elif command[0]==2:
        stack.popleft()
    elif command[0]==3:
        print(max(stack))
    elif command[0]==4:
        print(min(stack))
    elif command[0]==5:
        print(len(stack))
while  not len(stack)==0:
    print(stack.pop(),end=', ')
        


