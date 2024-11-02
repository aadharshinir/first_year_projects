#to print a number pyramid pattern using loops
n = int(input("Enter the height of the pyramid: "))
for i in range (1, n+1):
    #for space
   
    for j in range (1, n-i+1):
        print(" ", end = " ")
    #for increasing order: 1,2...
    for j in range (1,i+1):
        print(j, end = " ")
    #for decreasing order: 3,2,1...
    for j in range (i-1,0,-1):
        print(j, end = " ")
    print()
