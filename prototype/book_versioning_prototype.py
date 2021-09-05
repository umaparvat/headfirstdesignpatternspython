"""
Scenario: Series of Book version needs to be published with pricing in website.
How to create objects for that.
Ans: Create a Book and Make a clone of it with varying attributes.

Why ordered dict -> to see the output similar for various print statement.

How prototype achieved : Using python deepcopy.

In this example: Prototype class can have various objects registered and can be cloned.
"""
from copy import deepcopy
from collections import OrderedDict


class Prototype:
    def __init__(self):
        self.objects = dict()

    def register_object(self, object, identifier):
        self.objects[identifier] = object

    def unregister_object(self, identifier):
        if identifier in self.objects:
            del self.objects[identifier]
        return

    def clone(self, identifier, **kwargs):
        found = self.objects.get(identifier)

        if not found:
            return ValueError(f"{identifier} object not registered")
        clone_obj = deepcopy(found)
        clone_obj.__dict__.update(kwargs)
        return clone_obj


class Book:
    def __init__(self, name, author, price, **rest):
        self.name = name
        self.author = author
        self.price = price
        self.__dict__.update(rest)

    def __str__(self):
        mylist = []
        ordereditems = OrderedDict(sorted(self.__dict__.items()))
        for key in ordereditems.keys():
            mylist.append(f"{key}:{ordereditems[key]}")
            if key == "price":
                mylist.append("$")
            mylist.append("\n")
        return "".join(mylist)

if __name__ == "__main__":
    book_v1 = Book("Harry Portter and sorcere's stone", "J k Rowling", "20", version="1")
    proto = Prototype()
    proto.register_object(object=book_v1, identifier="harryportter")
    book_v2 = proto.clone(identifier="harryportter", name="Harry Portter and champer of secrets", price="25", version="2")
    print(book_v1)
    print(book_v2)