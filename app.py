import random

high_score = 0


def start_game():
    global high_score
    print("Hello and welcome to the Number Guessing Game! I'm thinking of a number between 1 - 10")
    number = random.randint(1, 10)
    correctness = False
    try_count = 0
    if high_score != 0:
                print("The score to beat is {}.".format(high_score))
    while correctness == False:
        try:
            guess = int(input("Go ahead, take a guess at what the number is.   "))
            if guess > 10 or guess < 1:
                raise ValueError
            try_count += 1
            if guess == number:
                print("Congrats! You guessed the right number!")
                if high_score == 0 or try_count < high_score:
                    print("NEW HIGH SCORE!!!")
                    high_score = try_count
                correctness = True
                break
            elif guess > number:
                print("WRONG! It's lower.")
                continue
            elif guess < number:
                print("WRONG! It's higher.")
                continue
        except ValueError:
            print("Oops! That's not a valid guess! Please pick a number greater than 0 but less than or equal to 10.")
            continue
    print("You took {} guesses before getting it right! Thank you for playing!".format(try_count))
    def play_again():
        play_again_answer = input("Would you like to play again? (Y/N)   ")
        if play_again_answer.lower() == "y":
            print("New game started!")
            start_game()
        elif play_again_answer.lower() == "n":
            print("Have a great day!")
        else:
            print("Please answer using 'Y' or 'N' for yes or no.")
            play_again()
    play_again()

    # Kick off the program by calling the start_game function.
start_game()