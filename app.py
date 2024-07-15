import random

def determine_winner(player, computer):
    if player == computer:
        return 'Barazim!'
    elif (player == "guri" and computer == "gershera") or \
         (player == "letra" and computer == "guri") or \
         (player == "gershera" and computer == "letra"):
        return 'player'
    else:
        return 'computer'

choices = ['guri', 'letra', 'gershera']
player_points = 0
computer_points = 0

while True:
    player = input("Zgjidh guri, letra, ose gershera: ").lower()

    # Ensure the player's choice is valid
    while player not in choices:
        print("Zgjedhje e pasakte! Te lutem, zgjidh guri, letra, ose gershera.")
        player = input("Zgjidh guri, letra, ose gershera: ").lower()

    computer = random.choice(choices)
    winner = determine_winner(player, computer)
    
    if winner == 'player':
        player_points += 1
        result = "Ti fitove!"
    elif winner == 'computer':
        computer_points += 1
        result = "Ti humbe!"
    else:
        result = "Barazim!"
    
    print(f"Lojtari zgjodhi {player}, Kompjuteri zgjodhi {computer}. Rezultati: {result}")

    # Ask if the player wants to play again
    play_again = input("Deshiron te luash perseri? (po/jo): ").lower()
    if play_again != "po":
        print(f"Ti bere {player_points} pike ndersa kompjuteri beri {computer_points} pike. Faleminderit qe luajte! :)")
        break