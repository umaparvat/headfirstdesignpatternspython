import enum
from abc import ABCMeta, abstractmethod

class Power(enum.Enum):
    ON = 1
    OFF = 2
    HIBERNATE = 3
    SLEEP = 4
    RESTART = 5

class Option:

    @abstractmethod
    def action(self):
        raise NotImplementedError
class ON(Option):
    def __init__(self, computer):
        self.computer = computer
        self.state = Power.ON
        self.allowed = [Power.OFF, Power.SLEEP, Power.HIBERNATE, Power.RESTART]

    def action(self):
        print("powering on")
        self.computer.set_power_option(self.computer.get_off_mode())

class OFF(Option):
    def __init__(self, computer):
        self.computer = computer
        self.state = Power.OFF
        self.allowed = [Power.ON]

    def action(self):
        print("powering off")
        self.computer.set_power_option(self.computer.get_on_mode())

class Computer:
    def __init__(self):
        self.off = OFF(self)
        self.current = self.off
        self.on = ON(self)

    def set_power_option(self, option):
        self.current = option

    def get_power_option(self):
        return self.current

    def execute(self):
        self.current.action()

    def get_on_mode(self):
        return self.on

    def get_off_mode(self):
        return self.off


if __name__ == "__main__":
    mylaptop = Computer()
    mylaptop.execute()
    mylaptop.execute()