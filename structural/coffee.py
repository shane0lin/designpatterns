from abc import ABC, abstractmethod


# Define the base Coffee class inheriting from ABC with abstract methods get_description and cost
class Coffee(ABC):
    @abstractmethod
    def get_description(self):
        pass
    
    @abstractmethod
    def cost(self):
        pass


# Define the SimpleCoffee class inheriting from Coffee
class SimpleCoffee(Coffee):
    def get_description(self):
        return "Simple Coffee"
    
    def cost(self):
        return 1


# Define the CoffeeDecorator class inheriting from Coffee with an init method that takes a Coffee object
class CoffeeDecorator(Coffee):
    def __init__(self, coffee):
        self.coffee = coffee
    
    def get_description(self):
        return self.coffee.get_description()
    
    def cost(self):
        return self.coffee.cost()


# Define the VanillaDecorator class inheriting from CoffeeDecorator and overriding get_description and cost methods
class VanillaDecorator(CoffeeDecorator):
    def get_description(self):
        return f"{self.coffee.get_description()}, +Vanilla"
    
    def cost(self):
        return self.coffee.cost() + 3


# Define the MilkDecorator class inheriting from CoffeeDecorator and overriding get_description and cost methods
class MilkDecorator(CoffeeDecorator):
    def get_description(self):
        return f"{self.coffee.get_description()}, +Milk"
    
    def cost(self):
        return self.coffee.cost() + 10


# Define the CoffeeSet class inheriting from Coffee
# - This class should contain a list to store Coffee objects
# - It should implement methods to add a Coffee object, and to calculate the total cost and description of the set
class CoffeeSet(Coffee):
    def __init__(self):
        self.coffees = []
    
    def add(self, coffee):
        self.coffees.append(coffee)
    
    def cost(self):
        sum_ = 0
        for coffee in self.coffees:
            sum_ += coffee.cost()
        
        return sum_
    
    def get_description(self):
        rst = ""
        for coffee in self.coffees:
            rst += f"({coffee.get_description()}, Cost: {coffee.cost()})"
        return rst


if __name__ == "__main__":
    # Create instances of SimpleCoffee, VanillaDecorator, and MilkDecorator
    simple = SimpleCoffee()
    vanilla = VanillaDecorator(simple)
    simple2 = SimpleCoffee()
    milk = MilkDecorator(simple2)
    
    # Create an instance of CoffeeSet and add the created coffee items
    coffeeset = CoffeeSet()
    coffeeset.add(vanilla)
    coffeeset.add(milk)
    # Print the description and total cost of the CoffeeSet
    print(coffeeset.get_description())
    print(f"Total cost: {coffeeset.cost()}")