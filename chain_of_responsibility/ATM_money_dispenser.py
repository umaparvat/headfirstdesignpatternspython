"""
Distribute Money in Indian ATM, where the amounts are 1000, 500, 100 denominations.
if the amount is 1000, it should distribute as 500 *1  and 100*5
if amount is greater than 1000, it should distribute the amount in 1000's.
if amount is 500, distribute it as 5* 100.
if amount is greater than 500, it should distribute the amount in 500's and the
       last one 500 should be in hundreds.
if amount is lesser than 100, it should throw error to enter valid amount.
"""

from constants import Config, Moneys
from abc import ABC, abstractmethod


class Handler(ABC):

    @abstractmethod
    def set_next(self, handler):
        raise NotImplementedError

    @abstractmethod
    def distribute(self, amount):
        raise NotImplementedError


class ActualHandler(Handler):
    _next_handler = None

    def set_next(self, handler):
        self._next_handler = handler

    def distribute(self, amount):
        if self._next_handler:
            return self._next_handler.distribute(amount)
        return None

class ThousandsHandler(ActualHandler):

    def distribute(self, amount):
        total = amount // Moneys.THOUSAND.value
        if Config.THOUSAND and 1 < total <= Config.THOUSAND:
            if amount % Moneys.THOUSAND.value == 0:
                total -= 1
            Config.THOUSAND -= total
            print(f"{Moneys.THOUSAND.value}: {total}")
            amount -= (total * Moneys.THOUSAND.value)
        return super().distribute(amount)

class FiveHundredHandler(ActualHandler):
    def distribute(self, amount):
        total = amount // Moneys.FHUNDRED.value
        if amount > Moneys.FHUNDRED.value and Config.FHUNDRED and total <= Config.FHUNDRED:
            if amount % Moneys.FHUNDRED.value == 0:
                total -= 1
            Config.FHUNDRED -= total
            print(f"{Moneys.FHUNDRED.value}: {total}")
            amount -= (total * Moneys.FHUNDRED.value)
        return super().distribute(amount)

class HundredHandler(ActualHandler):
    def distribute(self, amount):
        #print(f"now: {amount}")
        total = amount // Moneys.HUNDRED.value
        if Config.HUNDRED and 0 < total <= Config.HUNDRED:
            Config.FHUNDRED -= total
            print(f"{Moneys.HUNDRED.value}: {total}")
            amount -= (total * Moneys.HUNDRED.value)
        return super().distribute(amount)

class ATM:
    def __init__(self, handler):
        self.handler = handler

    def _valid_denominations(self, amount):
        last_denomination = list(Moneys)[-1]
        if amount % last_denomination.value > 0:
            raise Exception("Not a valid denomination")
        return True

    def dispense(self, amount):
        self._valid_denominations(amount)
        return self.handler.distribute(amount)


if __name__ == "__main__":
    achander = ActualHandler()
    thandler = ThousandsHandler()
    fhandler = FiveHundredHandler()
    hhandler = HundredHandler()
    thandler.set_next(fhandler)
    fhandler.set_next(hhandler)
    atm = ATM(handler=thandler)
    while True:
        print(f"\nAvaliable Denominations\n")
        for data in Moneys:
            if Config().__getattribute__(data.name):
                print(f"{data.value}", end=" ")
        amount = int(input("\nEnter Amount:").strip())
        collect = atm.dispense(amount)
        cont = input(f"\n Do you want to withdraw again? (y/n):").strip()
        if cont.lower() != 'y':
            break
        continue



