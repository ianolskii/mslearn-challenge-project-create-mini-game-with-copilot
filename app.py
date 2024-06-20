from random import randint
import sys


ACTIONS = ["rock", "scissors", "paper"]


def check_win(p1, p2) -> int:
    if p1 == p2:
        return -1
    elif (p1 == "rock") and (p2 == "paper"):
        return 1
    elif (p1 == "rock") and (p2 == "scissors"):
        return 0
    elif (p1 == "paper") and (p2 == "rock"):
        return 0
    elif (p1 == "paper") and (p2 == "scissors"):
        return 1
    elif (p1 == "scissors") and (p2 == "paper"):
        return 0
    elif (p1 == "scissors") and (p2 == "rock"):
        return 1
    

def new_round():
    p1 = "undefined"
    p2 = "undefined"
    while True:
        try:
            p1 = input(f"input your action from these options: {ACTIONS}: ")
            p1 = p1.lower()
            if p1 not in ACTIONS:
                raise ValueError
            break
        except Exception:
            print(f"{p1} is invalid command. Try again.")
    
    p2 = ACTIONS[randint(0, 2)]

    return p1, p2, check_win(p1, p2)


def main():
    while True:
        try_again = "undefined"
        p1, p2, game = new_round()
        print(f"You choose: '{p1}', AGI choose: '{p2}'")
        if game == 0:
            print("You won!")
        elif game == 1:
            print("Computer won!")
        else:
            print("Tie!")
        try:
            try_again = input("Try again? [yes/no]: ")
            try_again = try_again.lower()
            if try_again == "no":
                print("Bye!")
                sys.exit(0)
            elif try_again == "yes":
                continue
            else:
                raise ValueError()
        except Exception:
            print(f"Wrong command {try_again}. Exiting now")
            sys.exit(1)
        

if __name__ == "__main__":
    main()  # start the game loop