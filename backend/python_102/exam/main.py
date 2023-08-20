from objects import Hero, Villain, Items
import random
import pathlib
import pathlib
from game_functions import *

path = pathlib.Path.cwd() / "backend" / "python_102" / "exam" / "item_descriptions.csv"
game_des_path = (
    pathlib.Path.cwd() / "backend" / "python_102" / "exam" / "game_description.txt"
)
# load data from files
items_description = load_csv_file_to_dict(path)
game_description = load_csv_file(game_des_path)

# create items and characters
items = {}
for key, values in items_description.items():
    items[key] = Items(
        key, items_description[key]["strength"], items_description[key]["description"]
    )
hero_name = input("Hi, Enter your character's name: ")
hero = Hero(hero_name, 0)
villains = [Villain("Hans", 3), Villain("Khan", 5), Villain("Karl", 10)]
# define game variables
number_of_wins = 0
events_probabilities = get_events_probabilities(items_description)

msg_elixir = f"""
Select elixir:
1 - boosting elixir,
2 - poisonous elixir,
3 - exit\n
Your choice: """
msg_item = """
Press:
1 - to take item,
2 - to read about item,
3 - to leave item.\n
Your choice: """
msg_fight = """
Press:
1 - to fight,
2 - to run away,
3 - to show items\n
Your choice: """
msg_start = """
Your move.\n
Press:
1 - to move,
2 - to help,
3 - to end the game.\n
Your choice: """

# main code
while True:
    user_choice = user_move(msg_start, ["1", "2", "3"])
    if user_choice == "1": #if user decided to move:
        event, events_probabilities = draw_event(events_probabilities)
        # check what the user drew
        if event != "villain": #if drew some item:
            item = items[event]
            print(f"""\nYou found {item.name}""")
            response = user_move(msg_item, ["1", "2", "3"])
            hero.make_decision_what_to_do_with_item(response, item, msg_item)
        else: #if drew opponent to fight
            opponent = return_villain_to_fight(number_of_wins, villains)
            start_strength = hero.strength
            start_opp_strength = opponent.strength
            print(
                f"""\nYou meet villain with strength of:  {opponent.strength}. Your strength is {hero.strength}"""
            )
            opponent.speak()
            response = ""
            # fight
            number_of_wins = hero.manage_fight(
                opponent,
                response,
                msg_fight,
                msg_elixir,
                events_probabilities,
                items_description,
                number_of_wins,
                start_strength,
                start_opp_strength
            )
    elif user_choice == "2": #if user need to help:
        print(game_description)
    else: #if user want to end game:
        print("\nBye. Game was closed")
        break
    # check result of the game
    if number_of_wins == 3: 
        print("\nCongratulations. You win with all enemies.\nTHE END")
        break
    elif number_of_wins == -1:
        break

# Plan prac:
# 1) zaktualizować opis gry
# 2) dodać komentarze do funkcji
# 3) 
# 4)
# 5)
# 7)
# 8)
# 9)
# 10)
