from abc import ABCMeta, abstractmethod
import random

class State(metaclass=ABCMeta):
    @abstractmethod
    def insert_quarter(self):
        raise NotImplementedError

    @abstractmethod
    def eject_quarter(self):
        raise NotImplementedError

    @abstractmethod
    def trunk(self):
        raise NotImplementedError

    @abstractmethod
    def dispense(self):
        raise NotImplementedError

class GumballMachine:
    def __init__(self, count):
        self.ballcount = count
        self.soldoutstate = SoldOutState(self)
        self.noquarterstate = NoQuarterState(self)
        self.hasquarterstate = HasQuarterState(self)
        self.soldstate = SoldState(self)
        self.winnerstate = WinnerState(self)
        if count > 0:
            self.currentstate = self.noquarterstate
        else:
            self.currentstate = self.soldoutstate

    def insert_quarter(self):
        self.currentstate.insert_quarter()

    def eject_quarter(self):
        self.currentstate.eject_quarter()

    def trunk(self):
        self.currentstate.trunk()
        self.currentstate.dispense()

    def release_ball(self):
        print(f"gumball rolling out the ball #{self.ballcount}")
        if self.ballcount > 0:
            self.ballcount -= 1

    def set_state(self, state: State):
        self.currentstate = state

    def get_state(self):
        return self.currentstate

    def get_sold_out_state(self):
        return self.soldoutstate

    def get_has_quarter_state(self):
        return self.hasquarterstate

    def get_no_quarter_state(self):
        return self.noquarterstate

    def get_sold_state(self):
        return self.soldstate

    def get_count(self):
        return self.ballcount

    def get_winner_state(self):
        return self.winnerstate


class SoldState(State):
    def __init__(self, gmachine: GumballMachine):
        self.machine = gmachine

    def insert_quarter(self):
        print("please wait, we are already giving you a ball")

    def eject_quarter(self):
        print("sorry, you already trunked")

    def trunk(self):
        print("turning twice, doesn't get you another ball")

    def dispense(self):
        self.machine.release_ball()
        if self.machine.get_count() > 0:
            self.machine.set_state(self.machine.get_no_quarter_state())
        else:
            self.machine.set_state(self.machine.get_sold_out_state())

class SoldOutState(State):
    def __init__(self, gmachine: GumballMachine):
        self.machine = gmachine

    def insert_quarter(self):
        print("sorry, Machine is out of ball, can't insert")

    def eject_quarter(self):
        print("sorry, you can't play")

    def trunk(self):
        print("you can't trunk, machine is out of ball")

    def dispense(self):
        print("No gumball dispensed")

class HasQuarterState(State):
    def __init__(self, gmachine: GumballMachine):
        self.machine = gmachine

    def insert_quarter(self):
        print("you have a inserted already quarter, can't insert")

    def eject_quarter(self):
        print("quarter returned")
        self.machine.set_state(self.machine.get_no_quarter_state())

    def trunk(self):
        print("you trunked")
        a_list = [1, 2]
        distribution = [.9, .1]
        random_number = random.choices(a_list, distribution)
        if random_number == 1 and self.machine.get_count() > 0:
            self.machine.set_state(self.machine.get_winner_state())
        else:
            self.machine.set_state(self.machine.get_sold_state())

    def dispense(self):
        print("No gumball dispensed")

class NoQuarterState(State):
    def __init__(self, gmachine: GumballMachine):
        self.machine = gmachine

    def insert_quarter(self):
        print("you inserted a quarter")
        self.machine.set_state(self.machine.get_has_quarter_state())

    def eject_quarter(self):
        print("you have not inserted a quarter")

    def trunk(self):
        print("you trunked, but there is no quarter")

    def dispense(self):
        print("you need to pay first")

class WinnerState(State):
    def __init__(self, gmachine: GumballMachine):
        self.machine = gmachine

    def insert_quarter(self):
        print("please wait, we are already giving you a ball")

    def eject_quarter(self):
        print("sorry, you already trunked")

    def trunk(self):
        print("turning twice, doesn't get you another ball")

    def dispense(self):
        self.machine.release_ball()
        if self.machine.get_count() == 0:
            self.machine.set_state(self.machine.get_sold_out_state())
        else:
            print("you are winner, we are giving you another ball for free")
            self.machine.release_ball()
            if self.machine.get_count() > 0:
                self.machine.set_state(self.machine.get_no_quarter_state())
            else:
                self.machine.set_state(self.machine.get_sold_out_state())



if __name__ == "__main__":
    mac = GumballMachine(5)
    mac.insert_quarter()
    mac.trunk()
    mac.insert_quarter()
    mac.eject_quarter()
    mac.insert_quarter()
    mac.trunk()
    mac.insert_quarter()
    mac.trunk()
    mac.insert_quarter()
    mac.trunk()
    mac.insert_quarter()
    mac.trunk()
    mac.insert_quarter()
    mac.trunk()