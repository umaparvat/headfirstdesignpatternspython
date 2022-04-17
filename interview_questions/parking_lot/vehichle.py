
from enum import Enum

class VehichleTypes(Enum):
    car = 1
    truck = 2
    bike = 3


class Vehichle:
    def __init__(self, id, type):
        self._id = id
        self._type = type

    def get_type_num(self):
        return self._type

class Car(Vehichle):

    def __init__(self, num):
        super().__init__(num, VehichleTypes.car)
