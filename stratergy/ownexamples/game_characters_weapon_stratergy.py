from abc import ABC, abstractmethod
"""
In a game , the characters can change the weapon during their fight.
Each character can use one weapon at a time and can change weapon anytime.
"""

class WeaponBehavior(ABC):
    @abstractmethod
    def use_weapon(self):
        raise NotImplementedError

class KnifeBehavior(WeaponBehavior):
    def use_weapon(self):
        print("now using knife, it can cut")

class BowAndArrowBehavior(WeaponBehavior):
    def use_weapon(self):
        print("using bow and arrow, trigger a shot")

class SwordBehavior(WeaponBehavior):
    def use_weapon(self):
        print("using sword, swinging with sword")

class AxeBehavior(WeaponBehavior):
    def use_weapon(self):
        print("using axe, chopping with axe")


class Character(ABC):
    def __init__(self, weaponbehavior):
        self._weaponbehavior = weaponbehavior

    def set_weapon_behavior(self, wb):
        self._weaponbehavior = wb

    def fight(self):
        self._weaponbehavior.use_weapon()


class King(Character):
    def __init__(self):
        super().__init__(KnifeBehavior())

class Queen(Character):
    def __init__(self):
        super().__init__(BowAndArrowBehavior())

class Knight(Character):
    def __init__(self):
        super().__init__(SwordBehavior())

class Troll(Character):
    def __init__(self):
        super().__init__(AxeBehavior())

def main():
    king  = King()
    queen = Queen()
    knight = Knight()
    troll = Troll()
    print("king:", end=" ")
    king.fight()
    print("queen:", end=" ")
    queen.fight()
    print("troll:", end=" ")
    troll.fight()
    print("knight:", end=" ")
    knight.fight()
    print("queen is  chaning weapons")
    queen.set_weapon_behavior(AxeBehavior())
    print("queen:", end=" ")
    queen.fight()
if __name__ == "__main__":
    main()