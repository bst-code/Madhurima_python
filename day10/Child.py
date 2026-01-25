from day10.GrandParent import GrandParent
from day10.Parent import Parent


class Child(Parent, GrandParent):

    def child_property(self):
        print("Child property -- Toy car")

obj = Child()
obj.child_property()
obj.parent_property()
obj.grand_property()
