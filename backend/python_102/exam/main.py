from objects import Hero, Villain, Items
import random
import pathlib
import pathlib
from game_functions import *

path = pathlib.Path.cwd() / "backend" / "python_102" / "exam" / "item_descriptions.csv"

items_description = load_csv_file_to_dict(path)
print(items_description)

# create items
items = {}
for key, values in items_description.items():
    items[key] = Items(key, items_description[key]["strength"])

hero = Hero("Piter", 0)
villains = [Villain("Hans", 3), Villain("Khan", 5), Villain("Karl", 10)]

number_of_wins = 0
events_probabilities = get_events_probabilities(items_description)

def check_move():
    # funkcja reagująca na ruch gracza
    pass


while True:
    msg = """Your move.\n
    Press:
    1 to move,
    2 to help,
    3 to end the game. \n"""
    user_choice = user_move(msg, ['1', '2', '3'])
    
    if user_choice == "1":
        event, events_probabilities = draw_event(events_probabilities)

        if event != "villain":
            item = items[event]
            print(f"""You found {item.name})""")
            msg = """
    Press:
    1 - to take item,
    2 - to read about item,
    3 - to leave item./n
                    """
            response = user_move(msg, ['1', '2', '3'])
            hero.make_decision_what_to_do_with_item(response, item, msg)
            # hero.show_items()
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
    3 - to show items\n
                    """
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
    2 - poisonous elixir,
    3 - exit\n
                    """
                        )
                        if chose_item == '1':
                            try:
                                hero.elixirs['boosting elixir'].use(hero)
                                hero.delete_item('boosting elixir')
                                events_probabilities['boosting elixir'] = get_events_probabilities(items_description)['boosting elixir']
                            except KeyError:
                                print("You don't have this elixir.")
                        elif chose_item == '2':
                            try:
                                hero.elixirs['poisonous elixir'].use(opponent)
                                hero.delete_item('poisonous elixir')
                                events_probabilities['poisonous elixir']  = get_events_probabilities(items_description)['poisonous elixir']
#                                     return person.elixirs[self.name].pop()
# AttributeError: 'Villain' object has no attribute 'elixirs'
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
                    number_of_wins = fight_result
                    # dopisać scenariusze w zależności od wyniku walki
                    # jesli wygrał przywrócić siłę bohaterowiz początku walki

                    if fight_result != -1:
                        hero.strength = start_strength
                else:
                    print("Wrong choice.")

    elif user_choice == "2":
        print("Game description ...")
    else:
        print("Game was close")
        break
# Plan prac:
# 1) losowanie tucizn czy można mieć 2? 
# 2) 
# 3) 
# 4)
# 5) funkcja walki / unieczki prze walką
# 7) możliwość podejrzenia sprzętów przed wykonaiem ruch
# 8) możliwość sprawdzenia siły w trakcie walki
# 9) pętla do 3 wygranych
# 10) funkcja wczytująca z pliku.txt instrukcję

# Done
# 1) przygotować funkcję wczytującą plik z danymi o przedmiotach


# from objects import Hero, Villain, Items
# import random
# import pathlib
# import pathlib
# from game_functions import *

# path = pathlib.Path.cwd() / "backend" / "python_102" / "exam" / "item_descriptions.csv"

# items_description = load_csv_file_to_dict(path)
# print(items_description)

# for name in items_description:
#     events_propabilities[name] = items_description[name]['probability']

# def get_events_propabilities(items_description):

#     events_propabilities = {}
#     for name in items_description:
#         events_propabilities[name] = items_description[]