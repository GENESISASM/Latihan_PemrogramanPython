import random
number = random.randint(1,10)
for i in range(0,3):
    user = int(input("Guess the Number: "))
    if user == number:
        print('Horeee !!!')
        print(f"you guessed, the number right its {number}")
        break
if user != number:
    print(f"your guess is incorrect, the number is {number}")