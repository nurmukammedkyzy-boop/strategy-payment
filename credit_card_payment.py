from payment_strategy import PaymentStrategy

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        return f"Processing credit card payment of ${amount}"