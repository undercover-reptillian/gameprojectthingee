# Rachel Jenkins

player = {'location': "Great Hall"}
rooms = {
        'Great Hall': {'South': 'Bedroom'},
        'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
        'Cellar': {'West': 'Bedroom'}
    }

def main():

    direction = ""
    valid_moves = ['North', 'South', 'East', 'West']
    while direction != 'Exit':
        print('You are in the ', player['location'])

        direction = input('Which way would you like to go? ').strip().title()
        if direction == "Exit":
            print("Game Over")
            break
        for move in valid_moves:
            if direction == move.title():
                roomlist = rooms[player['location']].keys()
                roomflag = True
                for room in roomlist:
                    if direction == room:
                        player['location'] = rooms[player['location']][room]
                        roomflag = False
                if roomflag:
                    print("Invalid direction")
                break

if __name__ == "__main__":
    main()