#python program that uses loops to construct a number diamond
n = int(input("Enter the height of the diamond: "))
for i in range (0,n):
    for j in range (0,n - i - 1):
        print(end = " ")
    for j in range (0,i+1):
        print(i+1, end = " ")
    print()
for i in range(n-1,0,-1):
    for j in range (0,n-i):
        print(end = " ")
    for j in range (0,i):
        print (i, end = " ")
    print()
