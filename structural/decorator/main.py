from abc import ABC, abstractmethod

class Burger(ABC):
    def get_description(self):
        return "Burger"
    
    @abstractmethod
    def cost(self):
        pass


class SimpleBurger(Burger):
    def cost(self):
        return 5.0


class BurgerDecorator(Burger):
    def __init__(self, decorated_burger):
        self.decorated_burger = decorated_burger

    def get_description(self):
        return self.decorated_burger.get_description()

    def cost(self):
        return self.decorated_burger.cost()


class CheeseDecorator(BurgerDecorator):
    def get_description(self):
        return f"{self.decorated_burger.get_description()}, Cheese"
    
    def cost(self):
        return self.decorated_burger.cost() + 1.0


class BaconDecorator(BurgerDecorator):
    def get_description(self):
        return f"{self.decorated_burger.get_description()}, Bacon"
    
    def cost(self):
        return self.decorated_burger.cost() + 1.5


# Example usage
my_burger = SimpleBurger()
print(f"Description: {my_burger.get_description()}, Cost: {my_burger.cost()}")
print("---------------")


cheese_burger = CheeseDecorator(my_burger)
print(f"Description: {cheese_burger.get_description()}, Cost: {cheese_burger.cost()}")

bacon_burger = BaconDecorator(cheese_burger)
print(f"Description: {bacon_burger.get_description()}, Cost: {bacon_burger.cost()}")

# TODO: Swap the order of cheese and bacon
print("---------------")

bacon_burger = BaconDecorator(my_burger)
print(f"Description: {bacon_burger.get_description()}, Cost: {bacon_burger.cost()}")

cheese_burger = CheeseDecorator(bacon_burger)
print(f"Description: {cheese_burger.get_description()}, Cost: {cheese_burger.cost()}")

