num = int(input("Enter the number: "))
sum = 0
while num>0:
    remainder = num%10 #gives remainder
    sum = sum + remainder
    num = num//10  #gives quotient
print(sum)
    