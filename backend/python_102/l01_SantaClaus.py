# Script with class structure of St. Cause village.


class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def speak(self, sound="Hello"):
        print(f"{sound} my name is {self.name}.")


class StClaus(Person):
    position = "in the office"

    def speak(self):
        return super().speak(sound="Ho ho, Merry Christmas ")

    def give_presents(self):
        self.position = "on the road"
        return "I'm going to children give them presents."

    def back_to_village(self):
        self.position = "in the office"
        return "I go back to my office."


class Elf(Person):
    energy = 5

    def __init__(self, name, age, occupation):
        self.occupation = occupation
        super().__init__(name, age)

    def work(self):
        if self.energy < 1:
            return "I can't work I need rest."
        else:
            self.energy = self.energy - 1
            return "I am going to work."

    def rest(self):
        if self.energy < 5:
            self.energy = self.energy + 1
            return "I'm resting."
        else:
            return "I am fresh and ready to work"

    def get_energy(self):
        return self.energy


class Factory:

    def __init__(self, n_prod_line, kind_prod):
        self.n_prod_line = n_prod_line
        self.kind_prod = kind_prod
        self.max_workers = n_prod_line * 5
        self.workers = []

    def add_worker(self, worker):
        if len(self.workers) < self.max_workers:
            self.workers.append(worker)
            return True
        else:
            print(
                "You have got to much workers. First you have to add new production line."
            )
            return False

    def add_prod_line(self):
        self.max_workers = self.max_workers + 5
        return self.max_workers

    def get_number_of_workers(self):
        return len(self.workers)

    def get_avg_energy_of_workers(self):
        value = 0
        for worker in self.workers:
            value = value + worker.get_energy()

        return value / self.get_number_of_workers()

# test
elf1 = Elf("Tim", 225, "mechanics")
elf2 = Elf("Bob", 130, "production worker")
elf3 = Elf("Tom", 221, "production worker")
elf4 = Elf("Clark", 325, "production worker")
elf5 = Elf("Michael", 842, "production worker")
elf6 = Elf("Bart", 450, "production worker")

st_claus = StClaus("Santa Claus", 1740)

toys_factory = Factory(1, "doll")


toys_factory.add_worker(elf1)
print(
    f"Number of workers: {toys_factory.get_number_of_workers()}. Average energy of workers: {toys_factory.get_avg_energy_of_workers()}"
)
elf1.work()
toys_factory.add_worker(elf2)
print(
    f"Number of workers: {toys_factory.get_number_of_workers()}. Average energy of workers: {toys_factory.get_avg_energy_of_workers()}"
)

print(elf2.rest())

st_claus.speak()
print(st_claus.give_presents())
