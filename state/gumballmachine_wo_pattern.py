
class GumballMachine:
    SOLD_OUT = 0
    NO_QUARTER = 1
    HAS_QUARTER = 2
    SOLD = 3
    def __init__(self, count):
        self.ballcount = count
        if count > 0:
            self.current = GumballMachine.NO_QUARTER

    def insert_quarter(self):
        if self.current == GumballMachine.HAS_QUARTER:
            print("Already machine has quarter, can't insert one more")
        elif self.current == GumballMachine.NO_QUARTER:
            self.current = GumballMachine.HAS_QUARTER
            print("quarter is inserted")
        elif self.current == GumballMachine.SOLD:
            print("ball is on the way, wait for inserting the coin")
        else:
            print("Machine is out of balls, can't play")

    def eject_quarter(self):
        if self.current == GumballMachine.HAS_QUARTER:
            self.current = GumballMachine.NO_QUARTER
            print("quarter is returned")
        elif self.current == GumballMachine.NO_QUARTER:
            print("no quarter is inserted, can't return anything")
        elif self.current == GumballMachine.SOLD:
            print("ball is on the way, please wait")
        else:
            print("Machine is out of balls, can't play")

    def trunk(self):
        if self.current == GumballMachine.HAS_QUARTER:
            self.current = GumballMachine.SOLD
            self.dispense()
        elif self.current == GumballMachine.NO_QUARTER:
            print("no quarter is inserted, can't return anything")
        elif self.current == GumballMachine.SOLD:
            print("ball is on the way, please wait")
        else:
            print("Machine is out of balls, can't play")

    def dispense(self):
        if self.current == GumballMachine.SOLD:
            print(f"ball number {self.ballcount} released")
            self.ballcount -= 1
            if self.ballcount > 0:
                self.current = GumballMachine.NO_QUARTER
            else:
                print("No more balls left in the machine to play")
                self.current = GumballMachine.SOLD_OUT
        elif self.current == GumballMachine.HAS_QUARTER:
            print("you have to trunk first")
        elif self.current == GumballMachine.NO_QUARTER:
            print("pay first please")
        elif self.current == GumballMachine.SOLD_OUT:
            print("no gumball dispensed")


if __name__ == "__main__":
    machine = GumballMachine(5)
    machine.insert_quarter()
    machine.eject_quarter()
    machine.insert_quarter()
    machine.trunk()
    machine.insert_quarter()
    machine.trunk()
    machine.insert_quarter()
    machine.trunk()
    machine.insert_quarter()
    machine.trunk()
    machine.insert_quarter()
    machine.trunk()
    machine.insert_quarter()
    machine.trunk()
