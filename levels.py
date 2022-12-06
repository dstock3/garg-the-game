#Define level data
level_data = {
    "1": {
        "description": "A dark and damp dungeon",
        "enemies": ["Skeleton", "Zombie"],
        "items": ["Health Potion", "Sword"],
    },
    "2": {
        "description": "A deep and ancient cave",
        "enemies": ["Goblin", "Troll"],
        "items": ["Mana Potion", "Bow"],
    },
    "3": {
        "description": "The inner sanctum of the final boss",
        "enemies": ["Dragon"],
        "items": ["Elixir"],
    },
}

#Save level data to file
with open("levels.txt", "w") as f:
    f.write(str(level_data))

#This code creates a dictionary that contains the data for three levels. Each level is represented by a key in the dictionary, and the corresponding value is a dictionary that contains the level's description, enemies, and items.