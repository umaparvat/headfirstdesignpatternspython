from abc import ABC, abstractmethod

"""
the below design introduces, method overwritten in all sub classes wherever the behavior changes.
"""


class Duck(ABC):
    """
    A new method is introducted, fly
    """
    def quack(self):
        print("quack")
    def swim(self):
        print("i'm swimming")

    def fly(self):
        print("i can fly")

    @abstractmethod
    def display(self):
        raise NotImplementedError

class MallardDuck(Duck):
    def display(self):
        print("i'm mallard")

class RedHead(Duck):
    def display(self):
        print("i'm readhead")

class Wooden(Duck):
    def display(self):
        print("i'm wooden duck")
    def quack(self):
        print("i can't quack")
    def fly(self):
        print("i can't fly")


class Rubber(Duck):
    def display(self):
        print("i'm rubber duck")

    def quack(self):
        print("squeak")

    def fly(self):
        print("i can't fly")
    def swim(self):
        print("i can't swim")

def main():
    mallard = MallardDuck()
    redhead = RedHead()
    mallard.display()
    mallard.quack()
    mallard.swim()
    redhead.display()
    redhead.quack()
    redhead.swim()

    rubber = Rubber()
    rubber.display()
    rubber.quack()
    rubber.fly()
    wooden = Wooden()
    wooden.display()
    wooden.fly()
    wooden.quack()
    wooden.swim()

if __name__ == "__main__":
    main()


