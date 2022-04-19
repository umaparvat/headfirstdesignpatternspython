"""
Builder exists as innerclass
disadvantage: Whenever new builder is added , the class will change

"""

class Pizza:
    def __init__(self, builder):
        self.garlic = builder.garlic
        self.extra_cheese = builder.extra_cheese
    def __str__(self):
        garlic = "yes" if self.garlic else "no"
        cheese = "yes" if self.extra_cheese else "no"
        info = {"garlic": garlic, "cheese": cheese}
        return str(info)

    class Pizzabuilder:
        def __init__(self):
            self.extra_cheese = False
            self.garlic = False

        def add_garlic(self):
            self.garlic = True
            return self

        def add_cheese(self):
            self.extra_cheese = True
            return self

        def build(self):
            return Pizza(self)

if __name__ == "__main__":
    pizza = Pizza.Pizzabuilder().add_garlic().add_cheese().build()
    print(pizza)


