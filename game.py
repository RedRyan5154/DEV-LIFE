import os
from colorama import Fore
import random
import time

os.system('cls' if os.name == 'nt' else 'clear')

print("""
██████╗ ███████╗██╗   ██╗              ██╗     ██╗███████╗███████╗
██╔══██╗██╔════╝██║   ██║              ██║     ██║██╔════╝██╔════╝
██║  ██║█████╗  ██║   ██║    █████╗    ██║     ██║█████╗  █████╗
██║  ██║██╔══╝  ╚██╗ ██╔╝    ╚════╝    ██║     ██║██╔══╝  ██╔══╝
██████╔╝███████╗ ╚████╔╝               ███████╗██║██║     ███████╗
╚═════╝ ╚══════╝  ╚═══╝                ╚══════╝╚═╝╚═╝     ╚══════╝


V0.1
""")
print("\n\nLoading . . .\n\n |", end="")
time.sleep(1)
for x in range(92):
    print("█", end="")
print("|")
input("\n\n\nPress enter to continue . . .")

def black_screen(time_=1.5):
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(float(time_))

def gl(room, text, input_="Press enter to continue . . ."):
    os.system('cls' if os.name == 'nt' else 'clear')

    words = text.split("\n")
    size = max(len(word) for word in words)
    print(f"""

    --------------------------------
    🧠 {intelect} | 🫂 {friends} | {money}$ | {xp}xp     |
    --------------------------------
    {room}

""")
    print("    " + '*' * (size + 4))
    for word in words:
        print("    " + '* {:<{}} *'.format(word, size))
    print("    " + '*' * (size + 4))
    return input("\n" + input_)


intelect = 50
friends = 0
money = 100
xp = 10
name = ""

############### rooms
def reload_rooms():
    global bedroom
    global bedroom_h
    global sign_up_for_hackathon1
    global sign_up_for_hackathon2
    bedroom = r"""

                                                                    ________________________
                                                                   |                        |
                                                                   |   Elon Brusk           |
                                                                   |          ______        |
                                                                   |         /      |       |
                                                                   |        /        \      |
                                                                   |       { (*) (*)  }     |
                                                                   |       |    (     |     |
                                                                   |        \_\___/__/      |
                                                                   |        __|   |__       |
                 \                                                 |       /         \      |
                  \                                      _         |______/___________\_____|
                   \                                    | |
                    \                                   | |
                     \_____________                     | |
       _______________|____________|_                   | |                                                     ___________
      |______________________________|                  | |                ____________________________________|           |
                    | |                 ________________| |             __|____________________________________|___________|
                    | |                |__________________|             |                                                   |
                    | |                   ||          ||                |                                                   |
                    | |                   ||          ||                |                                                   |
                    | |                   ||          ||                |___________________________________________________|
           _________|_|________           ||          ||                      |  |                               |  |
          |____________________|          ||          ||                      |__|                               |__|
    """

    bedroom_h = r"""

                                                                    ________________________
                                                                   |                        |
                                                                   |   Elon Brusk           |
                                                                   |          ______        |
                                                                   |         /      |       |
                                                                   |        /        \      |
                                                                   |       { (*) (*)  }     |
                                                                   |       |    (     |     |
                                                                   |        \_\___/__/      |
                                                                   |        __|   |__       |
                 \                                                 |       /         \      |
                  \                                      _         |______/___________\_____|
                   \      ◄ ---Laptop [1]               | |                                       Bed [2]
                    \                                   | |                                          |
                     \_____________                     | |                                          ▼
       _______________|____________|_                   | |                                                     ___________
      |______________________________|                  | |                ____________________________________|           |
                    | |                 ________________| |             __|____________________________________|___________|
                    | |                |__________________|             |                                                   |
                    | |                   ||          ||                |                                                   |
                    | |                   ||          ||                |                                                   |
                    | |                   ||          ||                |___________________________________________________|
           _________|_|________           ||          ||                      |  |                               |  |
          |____________________|          ||          ||                      |__|                               |__|
    """

    sign_up_for_hackathon1 = r"""
         _________________________________________________________________________________
         |                                      (o)                                      |
         |      _______________ ___                                        _________     |
         |     / Hackathon.com \_+_\______________________________________/(-)(□)(X)\    |
         |    |                                                                      |   |
         |    |      WELCOME TO HACK-A-THON                                          |   |
         |    |                                                                      |   |
         |    |      To participate you first need to register:                      |   |
         |    |                                                                      |   |
         |    |             Name: ______                                             |   |
         |    |                                                                      |   |
         |    |             fmail: ______@hackathon.com                              |   |
         |    |                                                                      |   |
         |    |                                                                      |   |
         |    |                                                                      |   |
         |    |                                                                      |   |
         |    |                                                                      |   |
         |    |                                                                      |   |
         |    |                                                                      |   |
         |    |______________________________________________________________________|   |
         |_______________________________________________________________________________|
        /                                                                                 \
       /                                                                                   \
      /                                                                                     \
     /_______________________________________________________________________________________\
    |                                                                                         |
    |_________________________________________________________________________________________|
    """

    sign_up_for_hackathon2 = fr"""
         _________________________________________________________________________________
         |                                      (o)                                      |
         |      _______________ ___                                        _________     |
         |     / Hackathon.com \_+_\______________________________________/(-)(□)(X)\    |
         |    |                                                                      |   |
         |    |      WELCOME TO HACK-A-THON                                          |   |
         |    |                                                                      |   |
         |    |      To participate you first need to register:                      |   |
         |    |                                                                      |   |
         |    |             Name: {name}{" "*(20-len(name))}                               |   |
         |    |                                                                      |   |
         |    |             fmail: {name.lower()}@hackathon.com{" "*(20-len(name))}                |   |
         |    |                                                                      |   |
         |    |                                                                      |   |
         |    |                                                                      |   |
         |    |                                                                      |   |
         |    |                                                                      |   |
         |    |                                                                      |   |
         |    |                                                                      |   |
         |    |______________________________________________________________________|   |
         |_______________________________________________________________________________|
        /                                                                                 \
       /                                                                                   \
      /                                                                                     \
     /_______________________________________________________________________________________\
    |                                                                                         |
    |_________________________________________________________________________________________|
    """
############### start game
reload_rooms()
name = gl(sign_up_for_hackathon1, "Welcome to the programming world, you have been invited to participate on a hack-a-thon. Enter your name to participate", "Enter your name: ")
reload_rooms()
gl(sign_up_for_hackathon2, "Great, you have registred on hackathon, it would help you get a job if you win")
gl(sign_up_for_hackathon2, "Let's go check out your new room")
black_screen()
gl(bedroom, "Wow! Nice room, I really like that poster\nYou should start practising for the hackathon, ill leave you to it")
reload_rooms()
gl(bedroom_h, "Go to your laptop", "What do you want to do: ")
