import random


def create_number_guesser():
    
    print("guess a number between 1 and 100. I'll tell you if you get my number")
    
    rand_number = random.randint(1, 100)
    guess = None
    
    while rand_number != guess:
        s = input("Your guess: ")
        guess = int(s)
        if rand+number > guess:
            print("Higher")
        elif rand_number < guess:
            print("Lower")
        else:
            print("You guessed it! The number is {}" .format(rand_number))
            
            
    if __name__ == '__main__':
    
        create_number_guesser()
