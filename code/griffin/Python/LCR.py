import random as r

def diceroll(player_list, pot=0):
    die = ("l","c","r","1","1","1")
    result = r.choice(die)
    print(f'roll: {result}')
    for i, player in enumerate(player_list):
        if result == 'c':
            player['coins'] -= 1
            pot += 1
        elif result == 'l':
            player['coins'] -= 1
            if player_list[i] == 0:
                player_list[len(player_list)-1]['coins'] += 1
            else:
                player_list[i-1]['coins'] += 1
        elif result == 'r':
            player['coins'] -= 1
            if player_list[i] == len(player_list)-1:
                player_list[0]['coins'] += 1
            else:
                player_list[i+1]['coins'] += 1
    print(player_list)
    print(f'pot: {pot}')
    #return player_list

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


'''def main():
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
            result = diceroll()
            if result == 'c':
                player['coins'] -= 1
                pot += 1
            elif result == 'l':
                player['coins'] -= 1
                if player_list[i] == 0:
                    player_list[len(player_list)-1]['coins'] += 1
                else:
                    player_list[i-1]['coins'] += 1
            elif result == 'r':
                player['coins'] -= 1
                if player_list[i] == len(player_list)-1:
                    player_list[0]['coins'] += 1
                else:
                    player_list[i+1]['coins'] += 1
            check = game_end_check(player_list)
            if check == True:
                game = False
                break
    for player in player_list:
        if player['coins'] > 0:
            print(f'{player} is the winner')
'''

'''if __name__ == "__main__":
    main()'''



test_player_list = [{'name':'Grof','coins':3},{'name':'Blof','coins':3},{'name':'Nof','coins':3},{'name':'Nof','coins':3},]
diceroll(test_player_list,0)
