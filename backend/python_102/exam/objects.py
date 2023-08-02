import game_functions as gf

class Person:
    def __init__(self, name, strength):
        self.name = name
        self.strength = strength

    def speak(self, sound=""):
        print(f"My name is {self.name}, and my strength is {self.strength}.{sound}")


class Hero(Person):
    def __init__(self, name, strength):
        self.weapons = {}
        self.elixirs = {}
        super().__init__(name, strength)

    def attack(self, opponent_strength):
        if self.strength > opponent_strength:
            print("You win.")
            return 1
        else:
            print("Your opponent was stronger. You lose.")
            return 0

    def move(self):
        print("You move.")
        return 1

    def run_away(self):
        print("You ran away. Keep explore map.")
        return 1

    def show_items(self):
        # zw;racać nazwę i siłę przedmiotów, a nie drukować.
        print(f"Your weapons: {list(self.weapons.keys())}, Your elixirs: {list(self.elixirs.keys())}")
         
    def take_item(self, item):
        # Jak rozróznić elksiry od broni
        # zmienić weapons i eliksiry na słowniki
        if item.name.find("elixir") != -1:
            self.elixirs[item.name] = item
        else :   
            self.weapons[item.name] = item
            self.strength = self.strength + item.strength_boost

    def leave_item(self, item):
        print(f"You leave {item.name}")
    
    def make_decision_what_to_do_with_item(self, response:str, item,  msg:str):

        while response == '2':
            item.describe()
            response = gf.user_move(msg, ['1', '2', '3'])
        if response == "1":
            self.take_item(item)
            print(f"You have taken {item.name}.")

        if response == "3":
            self.leave_item(item)

    def delete_item(self, item):
        del self.elixirs[item]

class Villain(Person):
    def speak(self, sound="I destroy you!"):
        return super().speak(sound)


class Items:
    def __init__(self, name, strength_boost):
        self.name = name
        self.strength_boost = strength_boost

    def use(self, person):
        person.strength = person.strength + self.strength_boost
        
        

    def describe(self):
        print("I'm describing item.")

class Elixirs(Items):
    pass
# Czym będzie się różnić kalsa broń od zwykłego przedmiotu?
# klasa eliksir będzię się różnić od broni funkcją use()
