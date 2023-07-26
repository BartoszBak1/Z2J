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
        print(f"Your weapons: {self.weapons}, Your elixirs: {self.elixirs}")
         
    def take_item(self, item):
        # Jak rozróznić elksiry od broni
        # zmienić weapons i eliksiry na słowniki
        if item.name.find("elixir") != -1:
            self.elixirs[item.name] = item.strength_boost
        else :   
            self.weapons[item.name] = item.strength_boost
            self.strength = self.strength + item.strength_boost

    def leave_item(self, item):
        print(f"You leave {item.name}")


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
