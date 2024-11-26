import random
startPoint = 1
endPoint =100
guess = 0
answer = random.randint(startPoint,endPoint)
print("You have only 6 attempts to guess the number!")
while True:
    userGuess = input("Enter a guess number: ")
    if userGuess.isdigit():
        guess+=1
        print(f"Guess: {guess}")
        userGuess  = int(userGuess)
        if userGuess < startPoint or userGuess > endPoint:
            print(f"Please enter a number between {startPoint} - {endPoint}")
        elif userGuess == answer:
            print(f"Congragulations ! You guessed the number {answer}")
            break
        elif userGuess < answer:
            print("The guess is too low!")
        elif userGuess > answer:
            print("The guess is too high!") 
    else:
        print("Invalid input.")
    
    if guess == 6:
        print(f"Sorry , you did'nt guess the right number , the right number is {answer}!")
        break