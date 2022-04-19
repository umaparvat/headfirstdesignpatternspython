from abc import ABC, abstractmethod
class Beverage(ABC):
    def __init__(self, describe):
        self._describe = describe

    def getDescription(self):
        return self._describe

    @abstractmethod
    def cost(self):
        raise NotImplementedError


class HouseBlend(Beverage):
    def __init__(self):
        super().__init__("Fantastic House Blend")

    def cost(self):
        return 0.4

class DarkRoast(Beverage):
    def __init__(self):
        super().__init__("Most excellent Dark Roast")

    def cost(self):
        return 0.5

class Decaf(Beverage):
    def __init__(self):
        super().__init__("The roasted coffee beans brewed in hot water")

    def cost(self):
        return 0.3

class Espresso(Beverage):
    def __init__(self):
        super().__init__("Black coffee")

    def cost(self):
        return 0.6


class HouseBlendWithSteamedMilkAndMocha(Beverage):
    def __init__(self):
        super().__init__("Fantastic House Blend wth steamed milk and mocha")

    def cost(self):
        return 0.7

class EspressoWithSoyMilkAndCaramel(Beverage):
    def __init__(self):
        super().__init__("Espresso with soy milk and caramel topping")

    def cost(self):
        return 0.8


def main():
    while True:
        print("\n\n Welcome to starBuzz, place the order from the below menu:")
        print(f"\n1.Espresso\n2.EspressoWithSoyMilkAndCaramel\n3.HouseBlend\n4.HouseBlendWithSteamedMilkAndMocha\n5.Exit")
        try:
            inp = int(input("Enter number:").strip())
            if inp == 1:
                ins = Espresso()
            elif inp == 2:
                ins = EspressoWithSoyMilkAndCaramel()
            elif inp == 3:
                ins = HouseBlend()
            elif inp == 4:
                ins = HouseBlendWithSteamedMilkAndMocha()
            elif inp == 5:
                return
            else:
                print("\nPlease Enter number from the menu list")
                continue
            print(f"\n{ins.getDescription()} cost: {ins.cost()}")
            print(f"\n Thank you for placing the order\n ")
        except Exception:
            print("\nplease enter integer number from the menu")




if __name__ == "__main__":
    main()
