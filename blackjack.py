import random as rand
from os import name, system

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def hituser():
    global userscore
    global user_ace_count
    print("************************")
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    picked_card = rand.choice(cards)
    if picked_card == 11:
        user_ace_count += 1
    userscore += picked_card
    if userscore > 21 and user_ace_count > 0:
        userscore -= 10
        user_ace_count -= 1
        print(f"You picked {picked_card}!\n")
        print("Your point got above 21, your ace value is now 1!\n")
    else:
        print(f"You picked {picked_card}!\n")


def hitcom():
    global comscore
    global com_ace_count
    global com_picked_card
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    com_picked_card = rand.choice(cards)
    if com_picked_card == 11:
        com_ace_count += 1
    comscore += com_picked_card
    if comscore > 21 and com_ace_count > 0:
        comscore -= 10
        com_ace_count -= 1


def stand():
    global user_done
    print("You decided to stand.\n")
    user_done = True


actions = {
    "hit": hituser,
    "stand": stand,
}

###### new game starting sequence ######

new_game = "yes"

clear()

while new_game == "yes":
    clear()

    user_done = False
    user_ace_count = 0
    userscore = 0
    user_lost = False
    game_end = False

    com_ace_count = 0
    comscore = 0
    com_picked_card = 0

    hituser()
    hituser()  # user cards given
    print(f"You currently have {userscore} points!\n")

    if userscore == 21:
        print("BlackJack!\n")

    hitcom()
    print(f"Dealer's first card is {com_picked_card}!\n")

    hitcom()
    comcard2 = com_picked_card

    while not user_done and not user_lost:  # loop goes on until user either loses or stops
        if userscore == 21:
            user_done = True
        elif userscore > 21:
            user_lost = True
            print(f"Your point has passed 21!\n")
            print("You busted!\n")
            game_end == True

        if not user_done and not user_lost:
            user_action = (
                input("Please select your action:\nHit\nStand\n\n")).lower()
            action_taken = actions[user_action]
            action_taken()
            print(f"Your point is now {userscore}!\n")

    print(f"Dealer's second card was {comcard2}!\n")
    print(f"Dealer's total points are {comscore}!\n")

    while not user_lost and comscore < 22 and not game_end:  # loop goes on until computer loses

        while comscore < 16:
            hitcom()
            print(f"Dealer has picked a {com_picked_card}!\n")
            print(f"Dealer's total points are now {comscore}!\n")

        print("Dealer has stopped hitting.\n")
        print(f"Your final point is {userscore}\n")

        if comscore > 21:
            print("Dealer Bust!\n")
            print("You won!")
            game_end == True

        if userscore < 22 and comscore < 22:
            if userscore > comscore:
                print(f"You won!")
                game_end = True
            elif userscore == comscore:
                print("It's a draw!")
                game_end = True
            elif userscore < comscore:
                print("You lost!")
                game_end = True
            else:
                print("Unexpected error")

    new_game = input("Do you want to play a new game?(yes/no)\n")