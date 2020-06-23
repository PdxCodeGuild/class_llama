import random as r

def diceroll():
    die = ("l","c","r","1","1","1")
    result = r.choice(die)
    return result

def create_player(name):
    player = {'name':name,'coins':3}
    return player



def game_end_check(a_list):
    death_count = 0
    for player in a_list:
        if player['coins'] == 0:
            death_count += 1
    if death_count == len(a_list) - 1:
        return True


def main():
    pot = 0
    player_list = []
    while True:
        player_name = input("enter a player name or type done to start the game: ")
        if player_name == 'done': 
            break
        else:
            new_player = create_player(player_name)
            player_list.append(new_player)
    
    game = True

    while game == True:
        for i, player in enumerate(player_list):
            #need to implement a function here to change number of dice thrown based on number of coins possessed
            for i in range(1,3):
                result = diceroll()
                if result == 'c':
                    player['coins'] -= 1
                    pot += 1
                elif result == 'l':
                    player['coins'] -= 1
                    player_list[i-1]['coins'] += 1
                elif result == 'r':
                    player['coins'] -= 1
                    player_list[i+1]['coins'] += 1
            check = game_end_check(player_list)
            if check == True:
                game = False
                break
    for player in player_list:
        if player['coins'] > 0:
            print(f'{player} is the winner')


if __name__ == "__main__":
    main()