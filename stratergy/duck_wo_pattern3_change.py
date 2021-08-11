from abc import ABC, abstractmethod
"""
The below design introduces different behavior of fly and quack .
but code duplication in real duck concrete(sub) classes.
whenever the fly behavior has to be changed , all classes will be modified.
"""

class FlyBehavior(ABC):
    @abstractmethod
    def fly(self):
       raise NotImplementedError

class QuackableBehavior(ABC):
    @abstractmethod
    def quack(self):
       raise NotImplementedError


class Duck:

    def swim(self):
        print("i can swim")

    @abstractmethod
    def display(self):
        raise  NotImplementedError

class Rubber(Duck, FlyBehavior, QuackableBehavior):
    def fly(self):
        print("i can fly")

    def quack(self):
        print("squeak")

    def display(self):
        print("i'm rubber")

class Wooden(Duck, FlyBehavior, QuackableBehavior):
    def fly(self):
        print("I can't fly")

    def quack(self):
        print("I can't quack")

    def display(self):
        print("I'm wooden duck")

class Mallard(Duck, FlyBehavior, QuackableBehavior):
    def fly(self):
        print("I can fly")

    def quack(self):
        print("quack")

    def display(self):
        print("I'm mallard real duck")

class RedHead(Duck, FlyBehavior, QuackableBehavior):
    """
    all real duck classes will have code duplication for fly and quack
    """
    def fly(self):
        print("I can fly")

    def quack(self):
        print("quack")

    def display(self):
        print("i'm red head real duck")

def main():
    mallard = Mallard()
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