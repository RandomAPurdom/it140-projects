#Random Purdom

# A Night in Notre Dame Text Adventure

# Notre Dame room connections
rooms = {
    "Narthex Entrance": {
        "north": "Bell Tower Stairwell",
        "east": "Crossing",
        "south": "Gargoyle Gallery"
    },
    "Gargoyle Gallery": {
        "north": "Narthex Entrance"
    },
    "Bell Tower Stairwell": {
        "south": "Narthex Entrance"
    },
    "Crossing": {
        "north": "North Transept",
        "east": "Choir Loft",
        "south": "South Transept",
        "west": "Narthex Entrance"
    },
    "South Transept": {
        "north": "Crossing"
    },
    "North Transept": {
        "south": "Crossing"
    },
    "Choir Loft": {
        "east": "Crypt of the Saints",
        "west": "Crossing"
    },
    "Crypt of the Saints": {
        "south": "Chamber of the Undead",
        "west": "Choir Loft"
    },
    "Chamber of the Undead": {
        "north": "Crypt of the Saints"}
    }

# Sacred items in the rooms of Notre Dame
items = {
    "Bell Tower Stairwell": "Bell of Dawn",
    "Gargoyle Gallery": "Gargoyle Fang",
    "North Transept": "Silver Chalice",
    "Crossing": "Cursed Rosary",
    "South Transept": "Holy Manuscript",
    "Choir Loft": "Sanctified Candle",
    "Crypt of the Saints": "Holy Water Vial"
}

# Villain Room
villain_room = "Chamber of the Undead"

# Start the player in the Narthex Entrance
current_room = "Narthex Entrance"

# Player Inventory
inventory = []

# Total number of items needed to win
required_items = len(items)

# Game Map
game_map = """
Bell Tower Stairwell    North Transept
        |                   |
        |                   |
Narthex Entrance ------- Crossing ----- Choir Loft ----- Crypt of the Saints
        |                   |                                     |
        |                   |                                     |
Gargoyle Gallery        South Transept                  Chamber of the Undead
"""

# Help Menu
help_menu = """
========== HELP MENU ==========

OBJECTIVE:
Collect all six sacred relics and the Holy Water Vial before
entering the Chamber of the Undead and facing Dracula.

COMMANDS:
go north - Move north
go east  - Move east
go south - Move south
go west  - Move west

grab relic - Pick up the item in the current room
map        - Display the map of Notre Dame Cathedral
help       - Display this help menu
quit       - Exit the game

TRACKING:
Relics collected: 0 - 6
Holy Water Vial is tracked separately. 

===============================
"""

# Show the Game Instructions to Player
def show_instructions():
    print("=" * 35)
    print(" Welcome to A Night in Notre Dame!")
    print("=" * 35)

    print("\nOBJECTIVE:")
    print("Collect all six sacred relics and the holy water vial to douse them before confronting Dracula "
          "to banish him once more!.")

    print("\nDirectional Commands: go South, go North, go East, go West")
    print("Other Commands: grab relic, map, help, instructions, quit")
    print("-" * 40)

# Confirm Action Function
def confirm_action(message):
    """Ask the player to confirm an action."""
    while True:
        response = input(f"{message} (y/n): ").strip().lower()
        if response in ["y", "yes"]:
            return True
        elif response in ["n", "no"]:
            return False
        else:
            print("Please enter yes or no.")

# Show Status Function
def show_status(current_room, inventory, items):
    print(f"You are in the {current_room}")

    if inventory:
        print("Inventory:", ", ".join(inventory))
    else:
        print("Inventory: Empty")

    relic_score = len(inventory)

    if "Holy Water Vial" in inventory:
        relic_score -= 1
        has_water = "Yes"
    else:
        has_water = "No"

    print(f"Collected Relics: {relic_score}/6")
    print(f"Holy Water Vial Collected: {has_water}")

    if current_room in items:
        print(f"You see the {items[current_room]}")

    return relic_score, has_water

show_instructions()

# Main Game Loop
while True:

    # Show current status
    relic_score, has_water = show_status(current_room, inventory, items)

    # Check for villainous encounter with Dracula
    if current_room == villain_room:
        if len(inventory) == required_items:
            print("\nYou confront Dracula with all six relics and the Holy Water Vial.")
            print("You use the sacred relics, blessed with holy water")
            print("""
            ===================================
                         YOU WIN!!!
            ===================================
            Dracula has been banished from
             the realm once more!
            ===================================
             """)
        else:
            print("\nDracula emerges from the shadows!")
            print("You are too late! Without all six relics and the Holy Water Vial, you are powerless.")
            print("""
            ===================================
                        GAME OVER
            ===================================
                Dracula's darkness consumes 
                Notre Dame Cathedral and 
                ALL of Paris!
            ===================================
            """)
        break

    # Show possible directions
    print(f"Available directions: {', '.join(rooms[current_room])}")

    # Attain next command
    command = input("\nEnter command: ").strip().lower()

    # Exit Game
    if command == "quit":
        if confirm_action("Are you sure you want to leave Notre Dame?"):
            print("""
            ===================================
                Hope you enjoyed playing!
            ===================================
            """)
            break

    # Directional Command
    elif command.startswith("go "):
        direction = command.split()[1]
        if direction in rooms[current_room]:
            if confirm_action(f"A dark corridor leads {direction}. Proceed?"):
                current_room = rooms[current_room][direction]
                print(f"You cautiously move {direction}.")
            else:
                print("You remain where you are.")
        else:
            print("The cathedral walls block your path!")

    # Game Map Command
    elif command == "map":
        print("\n===== NOTRE DAME MAP =====")
        print(game_map)

    # Retrieve Item Command
    elif command == "grab relic":
        if current_room in items:
            if confirm_action(f"Retrieve the {items[current_room]}?"):
                item = items[current_room]
                inventory.append(item)
                print(f"You have retrieved the {item}!")
                del items[current_room]
            else:
                print("You leave the relic behind.")
        else:
            print("There is no relic in this room.")

    # Help Menu
    elif command == "help":
        print(help_menu)

    # Game Instructions
    elif command == "instructions":
        show_instructions()

    # Invalid Commands
    else:
        print("You hear strange echoes that lead nowhere. INVALID COMMAND!")

        # Separate each area for legibility
    print("-" * 40)
