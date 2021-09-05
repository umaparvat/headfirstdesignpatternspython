"""
Real Time Stratergy Game has Barracks which can generate various unit types(archer, knights) with different level.

Scenario: The unit type strength and weakness various as per the game level the unit is in.
How to generate object based on teh level of the game the character is in.

Solution: Create a Base character and clone for all the levels the character. the clone can have values changed.
"""
from abc import ABC, abstractmethod
from copy import deepcopy

class Prototype(ABC):

    @abstractmethod
    def clone(self):
        raise NotImplementedError

class Knight(Prototype):
    def __init__(self, level):
        self.unit_type = "Knight"
        self.level = level
        filename = f"knight_{level}.dat"
        with open(filename, "r") as fs:
            line = fs.read().split("\n")
            self.life = line[0]
            self.speed = line[1]
            self.attack_power = line[2]
            self.attack_range = line[3]
            self.weapon = line[4]

    def clone(self):
        return deepcopy(self)

    def __str__(self):
        return f"Type:{self.unit_type}\nLevel:{self.level}\nLife:{self.life} \n Speed:{self.speed}\n Attack Power:{self.attack_power}\n Attach Range:{self.attack_range}\nWeapon:{self.weapon}"


class Archer(Prototype):
    def __init__(self, level):
        self.unit_type = "Archer"
        self.level = level
        filename = f"archer_{level}.dat"
        with open(filename, "r") as fs:
            line = fs.read().split("\n")
            self.life = line[0]
            self.speed = line[1]
            self.attack_power = line[2]
            self.attack_range = line[3]
            self.weapon = line[4]

    def clone(self):
        return deepcopy(self)

    def __str__(self):
        return f"Type:{self.unit_type}\nLevel:{self.level}\nLife:{self.life} \n Speed:{self.speed}\n Attack Power:{self.attack_power}\n Attach Range:{self.attack_range}\nWeapon:{self.weapon}"


class Barracks(object):
    def __init__(self):
        self.units = {
            "knight": {1: Knight(1), 2: Knight(2)},
            "archer": {1: Archer(1), 2: Archer(2)}
        }

    def build_unit(self, unit_type, level):
        return self.units[unit_type][level].clone()


if __name__ == "__main__":
    barracks = Barracks()
    knight1 = barracks.build_unit("knight", 1)
    print(f"[knight1]{knight1}")
    archer2 = barracks.build_unit("archer", 2)
    print(f"[archer2]{archer2}")