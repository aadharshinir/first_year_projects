num = input("Enter the number: ")
reverse = num[::-1]
if num == reverse:
    print("The given number is a palindrome")
else:
    print("The given number is not a palindrome")