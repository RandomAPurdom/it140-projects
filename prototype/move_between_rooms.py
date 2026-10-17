# A dictionary for the simplified dragon text game.
# The dictionary links a room to other rooms.
rooms = {
    "Narthex Entrance": {"south": "Gargoyle Gallery", "east": "Crossing"},
    "Gargoyle Gallery": {"north": "Narthex Entrance"},
    "Crossing": {"west": "Narthex Entrance"},
    "Exit": {}
    }

# Start the player in the Narthex Entrance
current_room = 'Narthex Entrance'

# Show the Game Instructions to Player
print('Welcome to A Night in Notre Dame!')
print('Commands: go South, go North, go East, go West, Exit')
print('-' * 40)

# Create the gameplay loop required by the milestone.
# Within the loop, complete the required behavior in small steps:
#   1. Display the current room.
#   2. Prompt for a movement command or "exit".
#   3. Branch for a valid move, exit, or invalid input.
#   4. Update the room only after a valid movement command.
#   5. Continue until the required exit condition is reached.
while True:
    # Check if the Player's Current Room is set to 'Exit'
    if current_room == 'Exit':
        print('Thanks for playing!')
        break
    elif current_room != 'Exit':
        print(f"You are in the {current_room}")
        print(f"Available directions: {', '.join(rooms[current_room])}")
        command = input("Enter command: ").strip().lower()
        if command == "exit":
            current_room = "Exit"
        elif command.startswith("go "):
            direction = command.split()[1]
            if direction in rooms[current_room]:
                current_room = rooms[current_room][direction]
            else:
                print("The cathedral walls block your path!")
        else:
            print("That direction echoes strangely... but leads nowhere. Invalid command!")

        # Separate each area for legibility
        print('-' * 40)

# TODO: Run and debug all milestone cases in prototype/README.md.
