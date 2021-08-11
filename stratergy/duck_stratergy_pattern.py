from abc import ABC, abstractmethod

"""
the changing behvior is introducted as different class
the behavior can be changed at runtime.
No code duplication. 
Change can be adapted easily.
"""

class FlyBehavior(ABC):
    @abstractmethod
    def fly(self):
        raise NotImplementedError

class FlyWithWings(FlyBehavior):
    def fly(self):
        print("i can fly")

class FlyNoWay(FlyBehavior):
    def fly(self):
        print("i can't fly")

class FlyWithRocketPowered(FlyBehavior):
    def fly(self):
        print("i can fly with rocket power")

class QuackableBehavior(ABC):
    @abstractmethod
    def quack(self):
        raise NotImplementedError

class Quack(QuackableBehavior):
    def quack(self):
        print("quack")

class Squeak(QuackableBehavior):
    def quack(self):
        print("squeak")

class MuteQuack(QuackableBehavior):
    def quack(self):
        print("i'm muted")

class DeviceQuack(QuackableBehavior):
    def quack(self):
        print("i quack from device")

class Duck(ABC):
    def __init__(self, flybehavior, quackbehavior):
        self.flybehavior = flybehavior
        self.quackbehavior = quackbehavior

    def set_fly_behavior(self, fb):
        self.flybehavior = fb

    def set_quack_behavior(self, qb):
        self.quackbehavior = qb

    def performFly(self):
        self.flybehavior.fly()

    def performquack(self):
        self.quackbehavior.quack()

    def swim(self):
        print("i can swim")

    @abstractmethod
    def display(self):
        raise NotImplementedError

class Mallard(Duck):
    """
    I can fly and quack
    """
    def __init__(self):
        super().__init__(FlyWithWings(), Quack())

    def display(self):
        print("i'm mallard")

class RedHead(Duck):
    """
    I can fly and quack
    """
    def __init__(self):
        super().__init__(FlyWithWings(), Quack())

    def display(self):
        print("i'm read head real duck")

class Rubber(Duck):
    """
    I can fly and make sound as squeak
    """
    def __init__(self):
        super().__init__(FlyWithWings(), Squeak())

    def display(self):
        print("i'm rubber duck")

class Wooden(Duck):
    """
    I can neither fly nor make sound
    """
    def __init__(self):
        super().__init__(FlyNoWay(), MuteQuack())

    def display(self):
        print("i'm wooden duck")

class ModelDuck(Duck):
    """
    I can fly normally and also rocketpower and makes sound using device
    """
    def __init__(self):
        super().__init__(FlyWithWings(), DeviceQuack())

    def display(self):
        print("i'm a device machine")


def main():
    mallard = Mallard()
    redhead = RedHead()
    mallard.display()
    mallard.performquack()
    mallard.swim()
    mallard.performFly()
    redhead.display()
    redhead.performquack()
    redhead.swim()
    redhead.performFly()

    rubber = Rubber()
    rubber.display()
    rubber.performquack()
    rubber.performFly()

    wooden = Wooden()
    wooden.display()
    wooden.performquack()
    wooden.performFly()
    wooden.swim()
    print("##########")
    device = ModelDuck()
    device.display()
    device.performFly()
    device.performquack()
    device.swim()
    device.set_fly_behavior(FlyWithRocketPowered())
    print("changed the device behavior to rocket power")
    device.performFly()

if __name__ == "__main__":
    main()