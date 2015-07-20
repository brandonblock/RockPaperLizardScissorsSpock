import random


def name_to_number(name):
    if name == "rock":
        x = 0
    elif name == "paper":
        x = 1
    elif name == "lizard":
        x = 2
    elif name == "scissors":
        x = 3
    elif name == "Spock":
        x = 4
    else:
        print "Please input something acceptable!"
    return x


def number_to_name(number):
    if number == 0:
        y = "rock"
    elif number == 1:
        y = "paper"
    elif number == 2:
        y = "lizard"
    elif number == 3:
        y = "scissors"
    elif number == 4:
        y = "Spock"
    else:
        print "Please input something acceptable!"
    return y


def rpsls(player_choice):
    player_number = name_to_number(player_choice)
    computer_choice = random.randrange(0, 5)

    print
    print "Player chooses " + player_choice + "!"
    print "Computer chooses " + number_to_name(computer_choice) + "!"

    if (computer_choice - player_number) % 5 == 1 or (computer_choice - player_number) % 5 == 2:
        print"Computer wins!"
    elif computer_choice - player_number == 0:
        print"It's a tie!"
    else:
        print"Player wins!"


rpsls("rock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
rpsls("Spock")
