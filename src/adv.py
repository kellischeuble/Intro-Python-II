import textwrap
from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
                    passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
                    into the darkness. Ahead to the north, a light flickers in
                    the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
                    to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
                    chamber! Sadly, it has already been completely emptied by
                    earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


player = Player("Kelli", "outside")

play = True

while play == True:

    player_current_room = room[player.current_room]

    print(f"\nYou are currently in the {player_current_room.name}")
    print(f"{player_current_room.description}\n")
    
    direction = input("Enter movement 'n' 'e' 's' or 'w' or press 'q' to quit:\n")
    
    if direction == 'q':
        play = False

    elif direction == 'n':
        if player_current_room.s_to:
            player.current_room = player_current_room.s_to
        print("You lost? There's nothing out there. Try a different direction \n")

    elif direction == 'e':
        if player_current_room.w_to:
            player.current_room = player_current_room.w_to
        print("You lost? There's nothing out there. Try a different direction \n")

    elif direction == 's':
        if player_current_room.n_to:
            player.current_room = player_current_room.n_to
        print("You lost? There's nothing out there. Try a different direction \n")

    elif direction == 'w':
        if player_current_room.e_to:
            player.current_room = player_current_room.e_to
        print("You lost? There's nothing out there. Try a different direction \n")
    
    else:
        print("Follow the damn directions")

    