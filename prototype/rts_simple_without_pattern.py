class Knight(object):
    def __init__(self, life, speed, attack_power, attack_range, weapon):
        self.life = life
        self.speed = speed
        self.attack_power = attack_power
        self.attack_range = attack_range
        self.weapon = weapon

    def __str__(self):
        return f"Life:{self.life} \n Speed:{self.speed}\n Attack Power:{self.attack_power}\n Attach Range:{self.attack_range}\nWeapon:{self.weapon}"


class Archer(object):
    def __init__(self, life, speed, attack_power, attack_range, weapon):
        self.life = life
        self.speed = speed
        self.attack_power = attack_power
        self.attack_range = attack_range
        self.weapon = weapon

    def __str__(self):
        return f"Life:{self.life} \n Speed:{self.speed}\n Attack Power:{self.attack_power}\n Attach Range:{self.attack_range}\nWeapon:{self.weapon}"


class Barracks(object):
    def generate_knight(self):
        return Knight(400, 5, 3,1, "short sword")

    def generate_archer(self):
        return Archer(200, 7, 1, 5, "short bow")


if __name__ == "__main__":
    barracks = Barracks()
    knight1 = barracks.generate_knight()
    print(f"[knight1]{knight1}")
    archer1 = barracks.generate_archer()
    print(f"[archer1]{archer1}")