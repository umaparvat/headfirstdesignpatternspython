"""
create 18 tree objects
and check how it is reused
object creation optimized by flyweight
"""
from enum import Enum
import random

TreeType = Enum('TreeType', "apple_tree cherry_tree mango_tree")

class Tree:
    pool = dict()

    def __new__(cls, tree_type):
        obj = cls.pool.get(tree_type, None)
        if not obj:
            obj = object.__new__(cls)
            obj.tree_type = tree_type
            cls.pool[tree_type] = obj
        return obj

    def render(self, age, x, y):
        """
        set the mutable values for the object.
        This will be passed explicitly by client code
        :param age:
        :param x:
        :param y:
        :return:
        """
        print(f"render of a {self.tree_type} and age {age} at ({x}, {y})")


if __name__ == "__main__":
    rnd = random.Random()
    min_age, max_age = 0, 30
    min_point, max_point = 0, 100
    tree_counter = 0

    for _ in range(10):
        t1 = Tree(TreeType.apple_tree)
        t1.render(age=rnd.randint(min_age, max_age),
                  x=rnd.randint(min_point, max_point),
                  y=rnd.randint(min_point, max_point))
        tree_counter += 1

    for _ in range(3):
        t2 = Tree(TreeType.cherry_tree)
        t2.render(age=rnd.randint(min_age, max_age),
                  x=rnd.randint(min_point, max_point),
                  y=rnd.randint(min_point, max_point))
        tree_counter += 1

    for _ in range(5):
        t3 = Tree(TreeType.mango_tree)
        t3.render(age=rnd.randint(min_age, max_age),
                  x=rnd.randint(min_point, max_point),
                  y=rnd.randint(min_point, max_point))
        tree_counter += 1

    print(f"Trees rendered: {tree_counter}")
    print(f"Trees actually created: {Tree.pool}")

    t4 = Tree(TreeType.cherry_tree)
    t5 = Tree(TreeType.cherry_tree)
    t6 = Tree(TreeType.apple_tree)
    print(f" id(t4) == id(t5) ? = ({(id(t4))}== {id(t5)})")
    print(f" id(t5) == id(t6) ? = ({(id(t5))}== {id(t6)})")
