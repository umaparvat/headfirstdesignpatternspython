from abc import ABC, abstractmethod

"""
the subclasses are for real ducks.
the common methods(behaviors) are in abstract class.
"""

class Duck(ABC):
    def quack(self):
        print("quack")
    def swim(self):
        print("i'm swimming")

    @abstractmethod
    def display(self):
        raise NotImplementedError

class MallardDuck(Duck):
    def display(self):
        print("i'm mallard")

class RedHead(Duck):
    def display(self):
        print("i'm readhead")


def main():
    mallard = MallardDuck()
    redhead = RedHead()
    mallard.quack()
    mallard.swim()
    mallard.display()
    redhead.quack()
    redhead.swim()
    redhead.display()

if __name__ == "__main__":
    main()


