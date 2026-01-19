import random
secret_number = random.randint(1,10)
bln = False

while bln == False:
    guess = int(input("Guess a number from 1 to 10 "))
    if guess > secret_number:
        print("Too big")
    elif guess < secret_number:
        print("Too small")
    else:
        print("Right Number")
        bln = True