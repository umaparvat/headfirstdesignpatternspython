
"""
Manager manges 2 kind of reportees.
1. developers
2. Ux designers
"""
class Manager:
    def __init__(self):
        self.developers = []
        self.designers = []

    def add_devs(self, developer):
        self.developers.append(developer)

    def add_design(self, designers):
        self.designers.append(designers)


class Dev:
    def __init__(self):
        print("developer added")
    def work(self):
        print("i code")

class Desinger:
    def __init__(self):
        print("designer added")

    def work(self):
        print("design the UI")

def main():
    a = Manager()
    a.add_devs(Dev())
    a.add_design(Desinger())


if __name__ == "__main__":
    main()
