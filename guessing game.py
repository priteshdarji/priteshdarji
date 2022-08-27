answer = 5 

print("Please guess the number between 1 to 10: ")
guess = int(input())

if guess < answer:
    print("please guess higher")
elif guess > answer:
    print("please guess lower")
else:
    print("You got it first time")

