"""
Create a custom computer with different memory, gpu, hdd
"""

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
        return f"computer {self.serialNumber} has memory : {self.memory} Gb" \
               f" and hdd: {self.hdd} Gb, gpu: {self.gpu} Gb"


def main():
    # 50 gb hard disk and 16 gb ram and 2 GB GPU card
    c1 = Computer(random.randint(0,1000))
    c1.hdd = 50
    c1.gpu = 2
    c1.memory = 16
    print(c1)

    # 1 Tb hard disk and 32 GB ram and 16 GB GPU
    c2 = Computer(random.randint(0, 1000))
    c2.hdd = 1024
    c2.gpu = 16
    c2.memory = 32
    print(c2)

if __name__ == "__main__":
    main()