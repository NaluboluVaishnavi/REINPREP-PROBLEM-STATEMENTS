#nested loop->a loop inside a loop
'''n=int(input())
start=1
for i in range(n):
    for j in range(n):
        if j>=i:
            print("*",end=" ")
            start=start+1
        else:
            print(" ",end=" ")
    print()'''
n=int(input())
start="A"
for i in range(n):
    for j in range(n):
        if j<=i:
            print(start,end="")
            start=char(ord(start)+1)#ascii value
        else:
            print("",end="")
            print()    
