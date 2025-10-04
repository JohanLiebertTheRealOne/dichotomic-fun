from random import randint

games_count = 0
ultimate_useful_var = False

def num_less_or_more(guess_num,random_num):
    if guess_num > random_num:
        print("[-] Less")
    if guess_num < random_num:
        print("[-] More")

def choose_range():
    while True:
        ask_range = int(input("[+] Enter the maximum number. \n"))
        if ask_range >= 0:
            break
    return ask_range

def play(arg_range):
    random_int = randint(0, arg_range)
    print(f"[-] A random number between 0 and {arg_range} has been chosen randomly")
    while True:
        user_guess = int(input("[+] Type your guess. \n"))
        if user_guess == random_int:
            print("[-] Correct ! GG !!!")
            break
        num_less_or_more(user_guess,random_int)

while ultimate_useful_var != True:
    while True:
        if games_count >= 1:
            ask_user_to_play = input("[+] Play again ? [y/n]")
        if games_count == 0:
            ask_user_to_play = input("[+] Play ? [y/n]")
        if ask_user_to_play=='y' or ask_user_to_play=='Y':
            ask_range = choose_range()
            play(ask_range)
            games_count += 1
        if ask_user_to_play=='n' or ask_user_to_play=='N':
            print("[-] See you later UwU")
            ultimate_useful_var = True
            break
        else:
            print("[+] Please, enter valid character 'y/n'")
            continue
