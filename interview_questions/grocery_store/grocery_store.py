import random

class Customer:
    def __init__(self, store):
        self.store = store
        self.basket = []
        self.amount = 10000

    def shop(self):
        self.select_groceries()
        self.checkout()

    def select_groceries(self):
        mybasket = self.basket
        for i in range(self.store.KIND_OF_ITEMS):
            for j in range(3):
                if random.randint(0,2) == 1:
                    mybasket.append(self.store.ITEMS[i])
                    self.store.ITEM_COUNT[i] -= 1
        #print(self.basket)


    def checkout(self):
        cashier = self.store.get_cashier()
        #print(self.basket)
        total = cashier.bill(self.basket)
        self.amount -= total
        print(total)
        cashier.pay(total)




class Cashier:
    def __init__(self):
        self.store = None

    def set_store(self, store):
        self.store = store

    def bill(self, basket):
        total = 0
        for i in range(len(basket)):
            #print(basket[i], basket[i].price)
            total+= basket[i].price
        return  total

    def pay(self, amount):
        self.store.amount += amount
        #print(self.store.amount)


class GroceryItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} and price:{self.price}"

class GroceryStore:
    KIND_OF_ITEMS = 4
    ITEM_COUNT = [20]*4
    ITEMS = [None]*4
    amount = 0

    def __init__(self):
        self.cashier = None
        self.items_inventory()

    def hire(self, cashier):
        self.cashier = cashier
        self.cashier.set_store(self)

    def items_inventory(self):
        GroceryStore.ITEMS[0] = GroceryItem("milk", 2.12)
        GroceryStore.ITEMS[1] = GroceryItem("butter", 2.50)
        GroceryStore.ITEMS[2] = GroceryItem("eggs", 0.89)
        GroceryStore.ITEMS[3] = GroceryItem('bread', 1.59)
        for i in range(GroceryStore.KIND_OF_ITEMS):
            GroceryStore.ITEM_COUNT[i] = 50



    def get_cashier(self):
        return self.cashier


if __name__ == "__main__":
    g = GroceryStore()
    cashier = Cashier()
    g.hire(cashier)
    cus = Customer(g)
    cus.shop()
