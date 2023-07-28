import random, time, sys
from colorama import init, Fore, Style
global win
win = False
init(autoreset=True)

TTT = {'top-l': ' ', 'top-m': ' ', 'top-r': ' ',
       'mid-l': ' ', 'mid-m': ' ', 'mid-r': ' ',
       'btm-l': ' ', 'btm-m': ' ', 'btm-r': ' '
}
def checkwin():
    global win
    win_conditions = [
        ['top-l', 'top-m', 'top-r'],  # Top row
        ['mid-l', 'mid-m', 'mid-r'],  # Middle row
        ['btm-l', 'btm-m', 'btm-r'],  # Bottom row
        ['top-l', 'mid-l', 'btm-l'],  # Left column
        ['top-m', 'mid-m', 'btm-m'],  # Middle column
        ['top-r', 'mid-r', 'btm-r'],  # Right column
        ['top-l', 'mid-m', 'btm-r'],  # Diagonal from top-left to bottom-right
        ['top-r', 'mid-m', 'btm-l']  # Diagonal from top-right to bottom-left
    ]

    for condition in win_conditions:
        if TTT[condition[0]] == TTT[condition[1]] == TTT[condition[2]] != ' ':
            global winning_team
            winning_team = TTT[condition[0]]
            win = True
            return
        else:
            win = False

def theboard():
    print(f"\033[1;36m{TTT['top-l']}  \033[1;37m| \033[1;36m {TTT['top-m']} \033[1;37m| \033[1;36m {TTT['top-r']}\033[0m")
    print('\033[1;34m   +    +   \033[0m')
    print('\033[1;34m------------\033[0m')
    print(f"\033[1;36m{TTT['mid-l']}  \033[1;37m| \033[1;36m {TTT['mid-m']} \033[1;37m|\033[1;36m {TTT['mid-r']}\033[0m")
    print('\033[1;34m   +    +   \033[0m')
    print('\033[1;34m------------\033[0m')
    print(f"\033[1;36m{TTT['btm-l']}  \033[1;37m| \033[1;36m {TTT['btm-m']} \033[1;37m|\033[1;36m {TTT['btm-r']}\033[0m")
    print('\033[1;34m   +    +   \033[0m')


legend = str(input("Do you want to see the legend before proceeding? Y/N:  ")).lower()

if legend == 'y':
    print(f"{Fore.YELLOW}{Style.BRIGHT}{'-' * 25} LEGEND {'-' * 25}{Style.RESET_ALL}")
    print(f"{Fore.LIGHTRED_EX}{Style.BRIGHT}Top Left of Grid    = \033[1;3m\033[1;1mtop-l\033[0m")
    print(f"{Fore.LIGHTRED_EX}{Style.BRIGHT}Top Middle of Grid  = \033[1;3m\033[1;1mtop-m\033[0m")
    print(f"{Fore.LIGHTRED_EX}{Style.BRIGHT}Top Right of Grid   = \033[1;3m\033[1;1mtop-r\033[0m")
    print(f"{Fore.LIGHTGREEN_EX}{Style.BRIGHT}Middle Left of Grid = \033[1;3m\033[1;1mmid-l\033[0m")
    print(f"{Fore.LIGHTGREEN_EX}{Style.BRIGHT}Middle of Grid      = \033[1;3m\033[1;1mmid-m\033[0m")
    print(f"{Fore.LIGHTGREEN_EX}{Style.BRIGHT}Middle Right of Grid  \033[1;3m\033[1;1mmid-r\033[0m")
    print(f"{Fore.LIGHTBLUE_EX}{Style.BRIGHT}Bottom Left of Grid = \033[1;3m\033[1;1mbtm-l\033[0m")
    print(f"{Fore.LIGHTBLUE_EX}{Style.BRIGHT}Bottom Middle of Grid = \033[1;3m\033[1;1mbtm-m\033[0m")
    print(f"{Fore.LIGHTBLUE_EX}{Style.BRIGHT}Bottom Right of Grid = \033[1;3m\033[1;1mbtm-r\033[0m{Style.RESET_ALL}")


else:
    pass


coin = ['\033[1;1mHeads\033[0m', '\033[1;1mTails\033[0m']
print("\033[1;33mWelcome to TTT!\033[0m")
print('\033[1;33mFlipping a coin to decide who goes first....\033[0m')
time.sleep(3)
flip = random.choice(coin)
print(f'{flip}!')
chance = str(input("\033[1;32mEnter either \033[1;1mX\033[0m\033[1;32m or \033[1;1mO\033[0m\033[1;32m: \033[0m")).upper()

for i in range(9):
    theboard()
    checkwin()
    if win == True and winning_team == 'X':
        f = open('X.txt')
        ascii = f.read()
        print(ascii)
        f.close()
        sys.exit()
    elif win == True and winning_team == 'O':
        f = open('O.txt')
        aascii = f.read()
        print(aascii)
        f.close()
        sys.exit()

    else:
        if i == 8 and win == False:
            f = open('DRAW.txt')
            aaascii = f.read()
            print(aaascii)
            f.close()

            sys.exit()

    print(f"\033[1;32mIt's \033[1;1m{chance}\033[0m\033[1;32m's turn to play, where do you choose to move?\033[0m")
    move = str(input("")).lower()

    while move not in TTT:
        print("Please refer to the legend for the accepted moves & try again.")
        move = str(input("")).lower()


    while TTT[move] != ' ':
        print("\033[1;31mPosition already taken. Choose another position.\033[0m")
        move = str(input("")).lower()

    TTT[move] = chance
    if chance == 'X':
        chance = 'O'
    else:
        chance = 'X'


    print("\033[1;33mProcessing....\033[0m")
    time.sleep(4.6)
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    print(' ')    
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    print(' ')    
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    print(' ')
