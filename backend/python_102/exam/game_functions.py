# funkcje pomocnicze wykorzystywane do obsłużenia logiki gry
import csv
import pathlib


def process_row(row):
    row["strength"] = float(row["strength"])
    row["probability"] = float(row["probability"])
    return row


def load_csv_file_to_dict(path):
    # items = []
    items_dict = {}
    with path.open(mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row = process_row(row)
            items_dict[row["name"]] = row
            del items_dict[row["name"]]["name"]

    return items_dict

def return_villain_to_fight(number_of_wins, villains):
        return villains[number_of_wins]

def fight(hero, opponent, number_of_wins):
    if hero.strength > opponent.strength:
        number_of_wins += 1
        print("Congratulation you win.")
        return number_of_wins
    
    elif hero.strength == opponent.strength:
        print("You are too weak to defeat your opponent, but luckily, you managed to escape.\nKeep playing.")
        return number_of_wins
    
    else:
         print("You loose. :(\nTHE END!")
         return -1