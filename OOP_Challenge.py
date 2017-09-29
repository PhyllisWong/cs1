"""Animal and Zookeeper class challenge."""


class Animal(object):
    """Animal class class that increments of all animal instances."""
    # Variable to count population
    population = 0

    @classmethod
    def populationCount(cls):
        """"""
        return Animal.population

    def __init__(self, name, favFood):
        """"""
        self.name = name
        self.favFood = favFood
        Animal.population += 1

    def eat(self, food):
        if food == self.favFood:
            print(self.name + " eats " + food)
            print("YUM! " + self.name + " wants more " + food)
        else:
            print(self.name + " eats " + food)

    def sleep(self):
        print(self.name + " sleeps for 8 hours")


class Tiger(Animal):
    """"""
    def __init__(self, name):
        super().__init__(name, "meat")


class Bear(Animal):
    """"""
    def __init__(self, name):
        super().__init__(name, "fish")

    def sleep(self):
        print(self.name + " hibernates for 4 months")


class Unicorn(Animal):
    """"""
    def __init__(self, name):
        super().__init__(name, "marshmallows")

    def sleep(self):
        print(self.name + " sleeps in a cloud")


class Giraffe(Animal):
    """"""
    def __init__(self, name):
        super().__init__(name, "leaves")

    def eat(self, food):
        if food == self.favFood:
            # use the superclass eat method
            Animal.eat(self, food)
        else:
            # modify the superclass method for this condition
            print(self.name + " eats " + food)
            print("YUCK! " + self.name + " spits out " + food)


class Bee(Animal):
    """"""
    def __init__(self, name):
        super().__init__(name, "pollen")

    def eat(self, food):
        # Use the giraffe class eat method
        Giraffe.eat(self, food)

    def sleep(self):
        print(self.name + " never sleeps")


class Zookeeper(object):
    """"""
    def __init__(self, name):
        """"""
        self.name = name

    def feedAnimals(self, animals, food):
        """"""
        animals_num = str(len(animals))
        population = str(Animal.populationCount())
        print(self.name + " is feeding " + food + " to " + animals_num + " of " + population + " total animals")

        for i in animals:
            i.eat(food)
            i.sleep()
