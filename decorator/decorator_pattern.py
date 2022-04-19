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
        super().__init__("Espresso")

    def cost(self):
        return 0.6


class CondimentDecorator(Beverage):

    def __init__(self, beverage):
        self._beverage = beverage
        super().__init__(describe=None)

    @abstractmethod
    def getDescription(self):
        raise NotImplementedError

class Mocha(CondimentDecorator):
    def getDescription(self):
        return self._beverage.getDescription() + ", Mocha"

    def cost(self):
        return self._beverage.cost()+ 0.2


class soymilk(CondimentDecorator):
    def getDescription(self):
        return self._beverage.getDescription() + ", soy milk"

    def cost(self):
        return self._beverage.cost() + 0.2

class SteamedMilk(CondimentDecorator):
    def getDescription(self):
        return self._beverage.getDescription() + ", steamed milk"

    def cost(self):
        return self._beverage.cost() + 0.2

class Caramel(CondimentDecorator):
    def getDescription(self):
        return self._beverage.getDescription() + ", caramel"

    def cost(self):
        return self._beverage.cost() + 0.3


class Whippedcream(CondimentDecorator):
    def getDescription(self):
        return self._beverage.getDescription() + ", whipped cream"

    def cost(self):
        return self._beverage.cost() + 0.4



def main():
    while True:
        print("\n\n Welcome to starBuzz, place the order from the below menu:")
        print(f"\n1.Espresso\n2.EspressoWithSoyMilkAndCaramel\n3.HouseBlend\n4.HouseBlendWithSteamedMilkAndMocha\n5.Exit")
        try:
            inp = int(input("Enter number:").strip())
            if inp == 1:
                ins = Espresso()
            elif inp == 2:
                ins = Espresso()
                ins = soymilk(ins)
                ins = Caramel(ins)
            elif inp == 3:
                ins = HouseBlend()
            elif inp == 4:
                ins = Mocha(SteamedMilk(HouseBlend()))
            elif inp == 5:
                return
            else:
                print("\nPlease Enter number from the menu list")
                continue
            print(f"\n{ins.getDescription()} cost: {ins.cost()}")
            print(f"\n Thank you for placing the order\n ")
            stin = input("\nwould you like to contine? (y/n):").strip()
            if stin == "y":
                continue
            else:
                return
        except Exception as e:
            print(e)
            print("\nplease enter integer number from the menu")


if __name__ == "__main__":
    main()