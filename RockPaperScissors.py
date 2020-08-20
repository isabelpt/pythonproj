import random
print("Welcome to Rock Paper Scissors!")
print("-------------------------------")
print("This game is case sensitive.")
print("Do not capitalize any letters in your input.")
print("Input \"exit\" at any time to exit")

def playing():
    print("Rock, paper, or scissors?")
    print("Your choice:")
    rpc = input()
    random_number = random.randint(1, 3)
    if rpc == "rock" or rpc == "paper" or rpc == "scissors":
        print("Computer choice:")
        if random_number == 1:
            random_number = "rock"
            print(random_number)
        elif random_number == 2:
            random_number = "paper"
            print(random_number)
        elif random_number == 3:
            random_number = "scissors"
            print(random_number)
        else:
            print("Error: Internal Problem")
    elif rpc != "rock" and rpc != "paper" and rpc != "scissors":
        print("Error: Wrong Input")
    elif rpc == "exit":
        print("Thanks for playing!")
        exit()
    else:
        print("Error: Internal Problem")
    if rpc == random_number:
        print("Tie")
    elif rpc == "rock" and random_number == "scissors":
        print("You win.")
    elif rpc == "scissors" and random_number == "paper":
        print("You win.")
    elif rpc == "paper" and random_number == "rock":
        print("You win.")
    else:
        print("The computer wins.")

def still_playing():
    game = False
    while not game:
        play_again = input("Play again? [yes/no]\n")
        if play_again == "yes" or "Yes":
            playing()
        elif play_again == "no" or "No":
            print("Thanks for playing!")
            print("Final score:")
            print(str(user_score) + " : " + str(comp_score))
            game = True
            exit()
        elif play_again == "exit":
            print("Thanks for playing!")
        elif play_again != "yes" and play_again != "no":
            print("Error: Misspelling")
        else:
            print("Error: Internal Issue")

start_playing = False
while not start_playing:
    bp = input("Would you like to begin playing? [yes/no]\n")
    if bp == "yes" or bp == "Yes":
        playing()
        still_playing()
        start_playing = True
    elif bp == "no" or bp == "No":
        print("Have a nice day!")
        start_playing = True
        exit()
    elif bp == "exit":
        exit()
    else:
        print("Error: Mispelling")

still_playing()
