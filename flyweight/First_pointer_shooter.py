from enum import Enum
import random

shooter = Enum('shooter', 'army, terrorist')

class Character:
    pool = {}

    def __new__(cls, shooter_type):
        obj = cls.pool.get(shooter_type, None)
        if not obj:
            obj = object.__new__(cls)
            obj.shooter = shooter_type
            cls.pool[shooter_type] = obj
        return obj

    def set_properties(self, health, weapons, location):
        print(f"{self.shooter} has {weapons} in location {location} and health is {health}")

    def duck(self, location):
        print(f"{self.shooter} ducks at {location}")

    def jump(self, location1, click=1):
        print(f"{self.shooter} move from {location1} to ({location1[0]+5}, {location1[1]+5})")


if __name__ == "__main__":
    rnd = random.Random()
    amry_count = 0
    terrorist_count = 0
    min_health, max_health = 0, 100
    min_weapon, max_weapon = 0, 3
    min_location, max_location = 0, 100
    terror_location_min, terror_location_max = 110, 310
    armies = []
    terrorists = []

    for _ in range(10):
        t1 = Character(shooter.army)
        t1.set_properties(health=rnd.randint(min_health, max_health),
                          weapons=rnd.randint(min_weapon, max_weapon),
                          location=(rnd.randint(min_location, max_location),
                                    rnd.randint(min_location, max_location))
                          )
        armies.append(t1)
        amry_count += 1

        t2 = Character(shooter.terrorist)
        t2.set_properties(health=rnd.randint(min_health, max_health),
                          weapons=rnd.randint(min_weapon, max_weapon),
                          location=(rnd.randint(terror_location_min, terror_location_max),
                                    rnd.randint(terror_location_min, terror_location_max))
                          )
        terrorist_count += 1
        terrorists.append(t2)

    print(f"total count {amry_count}+{terrorist_count}")
    print(f"actual object: {Character.pool}")
    army2 = armies[0]
    terrorist2 = terrorists[0]
    army2.jump(location1=(2, 30))
    terrorist2.duck(location=(200, 210))






