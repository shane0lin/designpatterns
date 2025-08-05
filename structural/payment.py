from abc import ABC, abstractmethod


# Define a PaymentGateway interface class with a process_payment method
class PaymentGateway(ABC):
    @abstractmethod
    def process_payment(self):
        pass


# Implement PayPal, Stripe, and Square classes with different payment processing methods
class Paypal(PaymentGateway):
    def process_payment(self):
        print("Pay with Paypal")


class Stripe(PaymentGateway):
    def process_payment(self):
        print("Pay with Stripe")
        
    
class Square(PaymentGateway):
    def process_payment(self):
        print("Pay with Square")
        
        
# Create PayPalAdapter, StripeAdapter, and SquareAdapter classes
# inheriting from PaymentGateway, using Adapter pattern


class PayPalAdapter(PaymentGateway):
    def __init__(self, paypal):
        self.paypal = paypal
    
    def process_payment(self):
        self.paypal.process_payment()
        
        
class StripeAdapter(PaymentGateway):
    def __init__(self, stripe):
        self.stripe = stripe
    
    def process_payment(self):
        self.stripe.process_payment()
        
        
class SquareAdapter(PaymentGateway):
    def __init__(self, square):
        self.square = square
    
    def process_payment(self):
        self.square.process_payment()
        
        
# TDefine a ProductComponent interface class with a show_details method
class ProductComponent(ABC):
    @abstractmethod
    def show_details(self):
        pass


# Implement Product class inheriting from ProductComponent with name and price attributes
class Product(ProductComponent):
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def show_details(self):
        print(f"{self.name}, {self.price}")
        

# Implement ProductBundle class inheriting from ProductComponent with a list of ProductComponent
class ProductBundle(ProductComponent):
    def __init__(self):
        self.components = []
    
    def show_details(self):
        for component in self.components:
            component.show_details()

# Implement add, remove methods, and show_details method in ProductBundle class
    def add(self, com):
        self.components.append(com)
    
    def remove(self, com):
        self.components.remove(com)


# Implement a ProductFeature class inheriting from ProductComponent, using Decorator pattern
class ProductFeature(ProductComponent):
    def __init__(self, product):
        self.component = product
        
    def show_details(self):
        self.component.show_details()


# Implement DiscountFeature and GiftWrapFeature classes inheriting from ProductFeature, adding specific behaviors
class DiscountFeature(ProductFeature):

    def show_details(self):
        self.component.show_details()
        print("with discount")
        

class GiftWrapFeature(ProductFeature):
    def show_details(self):
        self.component.show_details()
        print("with GiftWrap")


def main():
    paypal = Paypal()
    paypal.process_payment()
    stripe = Stripe()
    stripe.process_payment()
    square = Square()
    square.process_payment()
    print("-----")
    adapter = PayPalAdapter(paypal)
    adapter.process_payment()
    adapter = StripeAdapter(stripe)
    adapter.process_payment()
    adapter = SquareAdapter(square)
    adapter.process_payment()
    
    print()
    p1 = Product("name1", 1)
    p1.show_details()
    p2 = Product("p2", 200)
    p2.show_details()
    print("-----")
    pb = ProductBundle()
    pb.add(p1)
    pb.add(p2)
    pb.show_details()

    print("-----")
    dis = DiscountFeature(p2)
    dis.show_details()
    print("-----")
    gift = GiftWrapFeature(dis)
    gift.show_details()
    
    
if __name__ == "__main__":
    main()