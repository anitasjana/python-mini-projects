import random

def get_random_number():
    random_number=random.randint(1,100)
    return random_number


def get_user_guess():
    while True:
        try:
            guess=int(input("Guess a number between 1 and 100: "))
            return guess
        except ValueError:
            print("Invalid input. Please enter a number.")


def check_guess(random_number, guess):
    
    if guess>random_number:
        print("Too high.")
        
    elif guess<random_number:
        print("Too low.")


def play_game():
    random_number=get_random_number()
    c=0
    while True:
        guess=get_user_guess()
        c+=1
        if guess==random_number:
            print(f"Congratulations! You guessed it in {c}  attempts.")
            break
        else:
            check_guess(random_number,guess)
        
        
if __name__=="__main__":
    play_game()