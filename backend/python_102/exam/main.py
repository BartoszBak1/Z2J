from objects import Hero, Villain, Items
import random
import pathlib
import pathlib
from game_functions import *

path = pathlib.Path.cwd() / "backend" / "python_102" / "exam" / "item_descriptions.csv"

items_description = load_csv_file_to_dict(path)
# create items
items = {}
for key, values in items_description.items():
    items[key] = Items(key, items_description[key]["strength"])

hero = Hero("Piter", 0)
villains = [Villain("Hans", 3), Villain("Khan", 5), Villain("Karl", 10)]

number_of_wins = 0
events = ["sword", "shield", "boosting_elixir", "poisonous_elixir", "villain"]
probabilities = [0.1, 0.2, 0.3, 0.2, 0.2]


def draw_event(events, probabilities):
    return random.choices(events, probabilities, k=1)[0]


def user_move(msg):
    return input(msg)


def check_move():
    # funkcja reagująca na ruch gracza
    pass


msg = "Your move.  "
user_choice = user_move(msg)

if user_choice == "1":
    event = draw_event(events, probabilities)
    # jeśli wylosował przedmiot, który już ma losuj dalej.
    if event != "villain":
        item = items[event]
        print(f"""You found {items[event].name})""")
        response = ""
        while response not in ["1", "2", "3"]:
            response = input(
                """
                Press:
                1 - to take item,
                2 - to read about item,
                3 - to leave item."""
            )
            if response == "1":
                hero.take_item(item)
            elif response == "2":
                items[event].describe()
            elif response == "3":
                hero.leave_item(item)
            else:
                print("Wrong choice.")
    else:
        opponent = return_villain_to_fight(number_of_wins, villains)
        start_strength = hero.strength
        print(
            f"""You meet villain with strength of:  {opponent.strength}. Your strength is {hero.strength}"""
        )
        opponent.speak()
        response = ""
        while response not in ["1", "2"]:
            response = input(
                """
                Press:
                1 - to fight,
                2 - to run away,
                3 - to show items"""
            )
            if response == "3":
                hero_items = hero.show_items()
                if hero.elixirs != {}:
                    chose_item = ""
                    while chose_item not in ['1','2','3']:
                        chose_item = input(
                        f"""
                Select item:
                1 - boosting elixir,
                2 - poison elixir,
                3 - exit"""
                    )
                    if chose_item == '1':
                        try:
                            hero.elixirs['boosting_elixir'].use(hero)
                        except KeyError:
                            print("You don't have this elixir.")
                    elif chose_item == '2':
                        try:
                            hero.elixirs['poison_elixir'].use(opponent)
                        except KeyError:
                            print("You don't have this elixir.")
                    elif chose_item == '3':
                        pass
                    else:
                        print('Select number from 1 to 3.')
            elif response == "2":
                hero.run_away()
            elif response == "1":
                fight_result = fight(hero, opponent, number_of_wins)
                # dopisać scenariusze w zależności od wyniku walki
                # jesli wygrał przywrócić siłę bohaterowiz początku walki


# Plan prac:
# 1) 
# # 2)
# 3) losowanie przedimiotów których gracz aktualnie nie posiada
# 4)
# 5) funkcja walki / unieczki prze walką
# 7) możliwość podejrzenia sprzętów przed wykonaiem ruch
# 8) możliwość sprawdzenia siły w trakcie walki
# 9) pętla do 3 wygranych
# 10) funkcja wczytująca z pliku.txt instrukcję

# Done
# 1) przygotować funkcję wczytującą plik z danymi o przedmiotach
