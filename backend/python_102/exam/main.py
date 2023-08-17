from objects import Hero, Villain, Items
import random
import pathlib
import pathlib
from game_functions import *

path = pathlib.Path.cwd() / "backend" / "python_102" / "exam" / "item_descriptions.csv"
game_des_path = (
    pathlib.Path.cwd() / "backend" / "python_102" / "exam" / "game_description.txt"
)

items_description = load_csv_file_to_dict(path)
# print(items_description)
game_description = load_csv_file(game_des_path)

# create items
items = {}
for key, values in items_description.items():
    items[key] = Items(
        key, items_description[key]["strength"], items_description[key]["description"]
    )

hero = Hero("Piter", 0)
villains = [Villain("Hans", 3), Villain("Khan", 5), Villain("Karl", 10)]

number_of_wins = 0
events_probabilities = get_events_probabilities(items_description)

msg_elixir = f"""
Select elixir:
1 - boosting elixir,
2 - poisonous elixir,
3 - exit\n
"""
msg_item = """
    Press:
    1 - to take item,
    2 - to read about item,
    3 - to leave item./n
                    """
msg_fight = """
    Press:
    1 - to fight,
    2 - to run away,
    3 - to show items\n
                    """
msg_start = """Your move.\n
    Press:
    1 to move,
    2 to help,
    3 to end the game. \n"""

while True:
    user_choice = user_move(msg_start, ["1", "2", "3"])

    if user_choice == "1":
        event, events_probabilities = draw_event(events_probabilities)

        if event != "villain":
            item = items[event]
            print(f"""You found {item.name}""")
            # what to do with item?
            response = user_move(msg_item, ["1", "2", "3"])
            hero.make_decision_what_to_do_with_item(response, item, msg_item)
        else:
            opponent = return_villain_to_fight(number_of_wins, villains)
            start_strength = hero.strength
            print(
                f"""You meet villain with strength of:  {opponent.strength}. Your strength is {hero.strength}"""
            )
            opponent.speak()
            response = ""
            # użyć funakcji user_move()
            # sprobować to zamknąc w funkcji odtąd - patrz funkcja make_decision_what_to_do_with_item
            while response not in ["1", "2"]:
                response = user_move(msg_fight, ["1", "2", "3"])
                # czy walczyć?
                if response == "3":
                    hero_items = hero.show_items()
                    if hero.elixirs != {}:
                        chose_item = user_move(msg_elixir, ["1", "2", "3"])
                        if chose_item == "1":
                            events_probabilities = chose_elixir(
                                hero,
                                hero,
                                opponent,
                                "boosting elixir",
                                events_probabilities,
                                items_description,
                            )
                        elif chose_item == "2":
                            events_probabilities = chose_elixir(
                                hero,
                                opponent,
                                opponent,
                                "poisonous elixir",
                                events_probabilities,
                                items_description,
                            )
                        elif chose_item == "3":
                            pass
                elif response == "2":
                    hero.run_away()
                elif response == "1":
                    fight_result = fight(hero, opponent, number_of_wins)
                    number_of_wins = fight_result
                    if fight_result != -1:
                        hero.strength = start_strength
            # dotąd
    elif user_choice == "2":
        print(game_description)
    else:
        print("Bye. Game was closed")
        break
    if number_of_wins == 3:
        print("Congratulations. You win with all enemies.\nTHE END")
        break
    elif number_of_wins == -1:
        break

# Plan prac:
# 1)
# 2) poprawienie formatowania komunikatów do urzytkownika:
# 3) linia 72 użyć funkcji user_move() przy wyborze czy walczyć czy uciekać
# 4)
# 5)
# 7)
# 8)
# 9)
# 10)
