# funkcje pomocnicze wykorzystywane do obsłużenia logiki gry
import csv
import random

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

def process_row(row):
    row["strength"] = float(row["strength"])
    row["probability"] = float(row["probability"])
    return row

def load_csv_file(path):
  
    with path.open(mode="r", encoding="utf-8") as file:
        text = file.read()
    return text

def return_villain_to_fight(number_of_wins, villains):
    return villains[number_of_wins]

def get_events_probabilities(items_description: dict):
    """Funkcja zwracająca słownik z eventem i prawdopodobieństwem.

    Args:
        items_description (dict): wynik funkcji load_csv_file_to_dict

    Returns:
        dict: {'event name': probability, ...}
    """
    events_probabilities = {}
    for name in items_description:
        events_probabilities[name] = items_description[name]["probability"]
    events_probabilities["villain"] = 0.2

    return events_probabilities

def draw_event(events_probabilities: dict):
    """Funkcja losująca event. Zwraca nazwę wylosowanego eventu i słownik z eventami bez wylosowanego eventu.

    Args:
        events_probabilities (dict): wynik funkcji get_events_probabilities()

    Returns:
        str: nazwa eventu
        dict: słownik bez wylosowaego eventu
    """
    events = list(events_probabilities.keys())
    probabilities = list(events_probabilities.values())

    event = random.choices(events, probabilities, k=1)[0]
    if event != "villain":
        del events_probabilities[event]
    return event, events_probabilities


def user_move(msg: str, values: list):
    move = input(msg)
    while move not in values:
        print("Wrong choice")
        move = input(msg)
    return move