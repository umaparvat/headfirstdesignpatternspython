from enum import Enum
import time
PizzaProgress = Enum("PizzaProgress", "queued preparation baking ready")
PizzaDough = Enum("PizzaDough", "thick thin")
PizzaTopping = Enum("PizzaTopping", "mozerella double_mozerella, backon ham mushroom red_onion oregano")
PizzaSauce = Enum("PizzaSauce", "tomato cream_fraiche")
STEP_DELAY = 3

class Pizza:

    def __init__(self, name):
        self.dough = None
        self.topping = []
        self.sauce = None
        self.name = name

    def __str__(self):
        return self.name

    def prepare_dough(self, dough):
        print(f"preparing dough {dough} for your {self}")
        self.dough = dough
        print(f"dough preparation is done for {self.dough.name}")

class MagaritaPizzaBuilder:

    def __init__(self):
        self.pizza = Pizza("magaritta")
        self.progress = PizzaProgress.queued
        self.baking_time = 5

    def prepare_dough(self):
        self.progress = PizzaProgress.preparation
        self.pizza.prepare_dough(PizzaDough.thin)

    def add_sauce(self):
        print("adding tomato sauce to your magarita")
        self.pizza.sauce  = PizzaSauce.tomato
        time.sleep(STEP_DELAY)
        print("done with the tomato sauce")

    def add_topping(self):
        print("adding the topping double mozerella and oregano to your magaritta...")
        self.pizza.topping.append([i for i in (PizzaTopping.double_mozerella, PizzaTopping.oregano)])
        time.sleep(STEP_DELAY)
        print(f"done with the topping addition...")

    def baking(self):
        print(f"baking your {self.pizza.name}")
        self.progress = PizzaProgress.baking
        time.sleep(self.baking_time)
        print(f"your magarita pizza is ready")
        self.progress = PizzaProgress.ready


class BackonHamBuilder:

    def __init__(self):
        self.pizza = Pizza("BackonHam")
        self.progress = PizzaProgress.queued
        self.baking_time = 7

    def prepare_dough(self):
        self.progress = PizzaProgress.preparation
        self.pizza.prepare_dough(PizzaDough.thick)

    def add_sauce(self):
        print(f"adding cream fraiche sauce to your {self.pizza.name}")
        self.pizza.sauce = PizzaSauce.cream_fraiche
        time.sleep(STEP_DELAY)
        print(f"done with the cream fraiche sauce")

    def add_topping(self):
        print("adding the topping backon, ham,  mozerella and oregano, red_onion to your pizza...")
        self.pizza.topping.append([i for i in (PizzaTopping.mozerella, PizzaTopping.oregano, PizzaTopping.backon,
                                               PizzaTopping.red_onion, PizzaTopping.ham)])
        time.sleep(STEP_DELAY)
        print(f"done with the topping addition...")

    def baking(self):
        print(f"baking your {self.pizza.name}")
        self.progress = PizzaProgress.baking
        time.sleep(self.baking_time)
        print(f"your {self.pizza.name} pizza is ready")
        self.progress = PizzaProgress.ready

class HawaianPizzaBuilder(BackonHamBuilder):
    def __init__(self):
        super().__init__()
        self.pizza.name = "HawianPizza"
        self.baking_time = 6



class Waiter:
    def __init__(self):
        self.builder = None

    def construct_pizza(self, builder):
        self.builder = builder
        [step() for step in (self.builder.prepare_dough,
                             self.builder.add_sauce,
                             self.builder.add_topping, self.builder.baking)]

    @property
    def pizza(self):
        return self.builder.pizza


def validate_style(builders):
    try:
        pizza_style = input("What Pizza would you like, key(m) for magaritta and key(c) for creamy backon, key(h) for hawaian:\n")
        builder = builders[pizza_style]()
        valid_input= True
    except KeyError as er:
        print("Sorry, only available options are m or c for magaritta/creamy backon")
        return False, None
    return True, builder



def main():
    builders = dict(m=MagaritaPizzaBuilder, c=BackonHamBuilder, h=HawaianPizzaBuilder)
    valid_input = False
    while not valid_input:
        valid_input, builder = validate_style(builders)
    w = Waiter()
    w.construct_pizza(builder)
    print("Enjoy your pizza...")
    print(w.pizza)

if __name__ == "__main__":
    main()



