import random

def player_num(choice):
    p_choice = choice 
    if p_choice == "P" or p_choice == "p" or p_choice == "Paper":
        p_no = 1
    if p_choice == "R" or p_choice == "r" or p_choice == "Rock":
        p_no = 2
    if p_choice == "S" or p_choice == "s" or p_choice == "Scissors":
        p_no = 3
    return p_no

def player_sym(p_no):
    if p_no == 1:
        p_sym = "Paper \U0001F4C4"
    if p_no == 2:
        p_sym = "Rock \U0001FAA8"
    if p_no == 3:
        p_sym = "Scissors \u2702"
    return p_sym

def bot_num():
    b_no = random.randint(0,3)
    return b_no

def bot_choice(b_no):
    if b_no == 1:
        b_choice = "Paper \U0001F4C4"
    if b_no == 2:
        b_choice = "Rock \U0001FAA8"
    if b_no == 3:
        b_choice=  "Scissors \u2702"
    return b_choice


def play_rps(bot_num):
    print("WELCOME to ROCK, PAPER, SCISSORS!")
    print(" ")
    status = True 
    points = 0

    while status:
        rounds = int(input("How many times would you like to play? (1-10)"))
        if rounds < 1 or rounds > 10:
            print("Please enter a number between 1 and 10.")
            continue
        else: 
            print("Now loading...")
            print(" ")
            for i in range(0, rounds):
                print("Round", i + 1, "of", rounds)
                player = input("Rock, Paper, Scissors: ")
                plr_num = player_num(player)
                plr_sym = player_sym(plr_num)
                bt_num = bot_num()

                bt_choice = bot_choice(bt_num)

                result = plr_num - bt_num
                if result == -2 or result == 1:
                    f_result = "You Lose!"
                elif result == -1 or result == 2:
                    f_result = "You Win!"
                    points += 1
                elif result == 0.0:
                    f_result = "It's a Draw!"
                
                print("You chose:", plr_sym)
                print("The bot chose:", bt_choice)
                print(" ")
                print(f_result)
                print("Current points:", points)
                print(" ")

            choice_cont = input("Would you like to continue [Y/N]: ")
            if choice_cont == "Y":
                continue 
            elif choice_cont == "N":
                break
    print("""
        EEEEE   N     N   DDD
        E       N N   N   D   D
        EEEEE   N  N  N   D    D
        E       N   N N   D   D
        EEEEE   N     N   DDDD
        """)


if __name__ == "__main__":
    bot_number = bot_num()
    play_rps(bot_number)