def sumPdivisors(n):
    sum = 0
    for i in range(1,n):
        if n%i == 0:
            sum = sum+i
    print("The sum of the proper divisors = ", sum)
    
n = int(input("Enter the number: "))
a = sumPdivisors(n)