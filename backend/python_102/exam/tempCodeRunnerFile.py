from objects import Hero, Villain, Items
import random
import pathlib
import pathlib
from game_functions import *

path = pathlib.Path.cwd() / "backend" / "python_102" / "exam" / "item_descriptions.csv"

items_description = load_csv_file_to_dict(path)
print(items_description)