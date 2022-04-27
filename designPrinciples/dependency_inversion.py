"""
Manager manges 2 kind of reportees.
1. developers
2. Ux designers
"""


class Manager:
    def __init__(self):
        self.reportees = []

    def add_reportees(self, employee):
        self.reportees.append(employee)

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


# class QA:
#     def __init__(self):
#         print("tester added")
#
#     def work(self):
#         print("test the code")


def main():
    a = Manager()
    a.add_reportees(Dev())
    a.add_reportees(Desinger())
    # a.add_reportees(QA())


if __name__ == "__main__":
    main()
