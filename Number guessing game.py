import random
random_number = random.randint(1,100)
user_guess = int(input("Guess the number: "))
while user_guess in range (1,100):
    if user_guess>random_number:
        print("Too high")
        user_guess = int(input())
    elif user_guess<random_number:
        print("Too low")
        user_guess = int(input())
    elif user_guess == random_number:
        print("Correct!")
        break
    