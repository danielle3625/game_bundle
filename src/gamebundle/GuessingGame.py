import random


def intro():
    print("Welcome to Guessing Game! "
          "\nI'm thinking of a number between 1 and 100 "
          "\nIf your guess is within 10 of my number, I will tell you: Warm!")
    print('If your guess is more than 10 away from my number, I will tell you: Cold!')
    print('If your guess is closer than your previous guess, I will tell you: Warmer!')
    print('If you guess is farther than your previous guess, I will tell you: Colder!')
    print("Let's Play!!")


def new_num():
    secret_num = random.randint(1, 100)
    return secret_num


def replay():
    global my_num, guess_list
    choice = input("Do you want to play again? Yes or No: ").upper()
    if choice[0] == 'Y':
        my_num = new_num()
        guess_list = [0]
        return True
    else:
        return False


def guess():
    x = 0

    while x not in range(1, 101):
        try:
            x = int(input("Enter your guess: "))
        except ValueError:
            print('Please enter an integer between 0 and 100')
            continue

    return x


game_play = True


def gameplay():

    while True:

        global game_play, my_num, guess_list

        intro()
        my_num = new_num()
        guess_list = []

        while game_play:

            user_guess = guess()

            guess_list.append(user_guess)

            if user_guess == my_num:
                print(f"You win! You used {len(guess_list)} tries!")
                break

            elif len(guess_list) > 1:
                if abs(my_num - user_guess) <= abs(my_num - guess_list[-2]):
                    print("Warmer!")
                else:
                    print("Colder!")

            else:
                if abs(my_num - user_guess) <= 10:
                    print("Warm!")
                else:
                    print("Cold!")

        if not replay():
            break
