from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardStrategy(PaymentStrategy):
    def __init__(self, card_number):
        self.card_number = card_number

    def pay(self, amount):
        print(f"Paid {amount} using Credit Card: {self.card_number}")

class PayPalStrategy(PaymentStrategy):
    def __init__(self, email):
        self.email = email

    def pay(self, amount):
        print(f"Paid {amount} using PayPal: {self.email}")

class ShoppingCart:
    def __init__(self):
        self.strategy = None

    def set_payment_strategy(self, strategy):
        self.strategy = strategy

    def checkout(self, amount):
        if self.strategy:
            self.strategy.pay(amount)
        else:
            print("No payment strategy set.")

if __name__ == "__main__":
    cart = ShoppingCart()

    credit_card = CreditCardStrategy("1234-5678-9876-5432")
    paypal = PayPalStrategy("user@example.com")

    cart.set_payment_strategy(credit_card)
    cart.checkout(100) # Outputs: Paid 100 using Credit Card: 1234-5678-9876-5432

    cart.set_payment_strategy(paypal)
    cart.checkout(200) # Outputs: Paid 200 using PayPal: user@example.com