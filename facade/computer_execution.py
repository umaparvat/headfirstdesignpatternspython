"""
structural pattern
"""

class Memory:
    def load(self, bootaddress, sector):
        return f"{bootaddress} is loaded from the harddive {sector}"


class HardDrive:
    def read(self, address):
        return f"x{address}"

class Cpu:
    def jump(self, mem_address):
        print(f"cpu switched to {mem_address}")

    def execute(self, boot_address):
        print(f"cpu executed {boot_address}")


class Computer:
    def __init__(self):
        self.cpu = Cpu()
        self.hdd = HardDrive()
        self.mem = Memory()

    def start(self):
        boot_address = self.mem.load("123", sector=self.hdd.read("45678"))
        self.cpu.jump(mem_address=boot_address)
        self.cpu.execute(boot_address)


if __name__ == "__main__":
    Computer().start()


