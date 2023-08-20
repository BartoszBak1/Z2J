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

    def fight(self, opponent, number_of_wins):
        if self.strength > opponent.strength:
            number_of_wins += 1
            print("Congratulation you win.")
            return number_of_wins

        elif self.strength == opponent.strength:
            print(
                "You are too weak to defeat your opponent, but luckily, you managed to escape.\nKeep playing."
            )
            return number_of_wins

        else:
            print("You loose. :(\nTHE END!")
            return -1

    def run_away(self):
        print("You ran away. Keep explore map.")
        return 1

    def show_items(self):
        print(
            f"Your weapons: {list(self.weapons.keys())}, Your elixirs: {list(self.elixirs.keys())}"
        )

    def take_item(self, item):
        if item.name.find("elixir") != -1:
            self.elixirs[item.name] = item
        else:
            self.weapons[item.name] = item
            self.strength = self.strength + item.strength_boost

    def leave_item(self, item):
        print(f"You leave {item.name}")

    def make_decision_what_to_do_with_item(self, response: str, item, msg: str):
        while response == "2":
            item.describe()
            response = gf.user_move(msg, ["1", "2", "3"])
        if response == "1":
            self.take_item(item)
            print(f"You have taken {item.name}.")

        if response == "3":
            self.leave_item(item)

    def delete_item(self, item):
        del self.elixirs[item]

    def use_elixir(
        self, recipient, opponent, elixir_name, events_probabilities, items_description
    ):
        try:
            self.elixirs[elixir_name].use(recipient)
            self.delete_item(elixir_name)
            events_probabilities[elixir_name] = gf.get_events_probabilities(
                items_description
            )[elixir_name]
            print(
                f"You used {elixir_name}. Your strength is {self.strength}. Strength of your opponent is {opponent.strength}"
            )
        except KeyError:
            print("You don't have this elixir.")

        return events_probabilities

    def choose_elixir(
        self, opponent, msg_elixir, events_probabilities, items_description
    ):
        # if hero.elixirs != {}:
        self.show_items()
        chose_item = gf.user_move(msg_elixir, ["1", "2", "3"])
        if chose_item == "1":
            events_probabilities = self.use_elixir(
                self,
                opponent,
                "boosting elixir",
                events_probabilities,
                items_description,
            )
        elif chose_item == "2":
            events_probabilities = self.use_elixir(
                opponent,
                opponent,
                "poisonous elixir",
                events_probabilities,
                items_description,
            )
        elif chose_item == "3":
            pass

    def manage_fight(
        self,
        opponent,
        response,
        msg_fight,
        msg_elixir,
        events_probabilities,
        items_description,
        number_of_wins,
        start_strength,
        start_opp_strength,
    ):
        while response not in ["1", "2"]:
            response = gf.user_move(msg_fight, ["1", "2", "3"])
            if response == "3":
                self.choose_elixir(
                    opponent, msg_elixir, events_probabilities, items_description
                )
            elif response == "2":
                self.run_away()
            elif response == "1":
                number_of_wins = self.fight(opponent, number_of_wins)

        self.strength = start_strength
        opponent.strength = start_opp_strength
        return number_of_wins


class Villain(Person):
    def speak(self, sound="I destroy you!"):
        return super().speak(sound)


class Items:
    def __init__(self, name, strength_boost, description):
        self.name = name
        self.strength_boost = strength_boost
        self.description = description

    def use(self, person):
        person.strength = person.strength + self.strength_boost

    def describe(self):
        print(self.description)


class Elixirs(Items):
    pass


# Czym będzie się różnić kalsa broń od zwykłego przedmiotu?
# klasa eliksir będzię się różnić od broni funkcją use()
