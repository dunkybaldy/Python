from enum import Enum

class Pizza():
    breadType = None
    baseSauce = None
    toppings = []

    def __init__(self, breadType, baseSauce):
        self.breadType = breadType
        self.baseSauce = baseSauce

    def AddTopping(self, topping):
        self.toppings.append(topping)

    def RemoveTopping(self, topping):
        if topping not in self.toppings:
            print("You don't have this topping.\r\n")
            return
        else:
            self.toppings.pop(topping)            

class BreadType(Enum):
    THICK_CRUST: 0
    THIN_CRUST: 1
    STUFFED_CRUST: 2