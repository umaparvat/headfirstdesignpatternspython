import random

class Computer:

    def __init__(self, serial_no):
        self.serialNumber =serial_no
        self._memory = None
        self._hdd = None
        self._gpu = None

    @property
    def memory(self):
        return self._memory

    @memory.setter
    def memory(self, ram_size):
        self._memory = ram_size

    @property
    def hdd(self):
        return self._hdd

    @hdd.setter
    def hdd(self, value):
        self._hdd = value

    @property
    def gpu(self):
        return self._gpu

    @gpu.setter
    def gpu(self, value):
        self._gpu = value

    def __str__(self):
        return f"computer {self.serialNumber} has memory : {self.memory} " \
               f"and hdd: {self.hdd}, gpu: {self.gpu}"


class ComputerBuilder:

    def __init__(self, number):
        self.computer = Computer(number)

    def configure_gpu(self, value):
        self.computer.gpu = value

    def configure_memory(self, value):
        self.computer.memory = value

    def configure_hdd(self, value):
        self.computer.hdd = value


class Tablet:
    def __init__(self, number):
        self.number = number
        self.display = None
        self.ram = None
        self.battery = None
        self.storage = None

    def __str__(self):
        return f"tablet {self.number} has {self.display} inch display , " \
               f"{self.ram} GB RAM, Battery {self.battery} Ghz " \
               f"and {self.storage} Gb storage"


class TabletBuilder:
    def __init__(self, number):
        self.construct = Tablet(number)

    def configure(self, display, ram, battery, storage):
        self.construct.display = display
        self.construct.ram = ram
        self.construct.battery = battery
        self.construct.storage = storage


class Engineer:

    def __init__(self):
        self._builder = None

    def construct_computer(self, memory, hdd, gpu):
        self._builder = ComputerBuilder(random.randint(0, 10000))
        self._builder.configure_memory(memory)
        self._builder.configure_gpu(gpu)
        self._builder.configure_hdd(hdd)

    def construct_tablet(self, display, ram, battery, storage):
        self._builder = TabletBuilder(random.randint(20000, 400000))
        self._builder.configure(display, ram, battery, storage)

    @property
    def computer(self):
        return self._builder.computer

    @property
    def tablet(self):
        return self._builder.construct



if __name__ == "__main__":
    engineer = Engineer()
    engineer.construct_computer(100, 1024, 4)
    print(engineer.computer)
    engineer.construct_tablet(10, 4, 1024, 128)
    print(engineer.tablet)