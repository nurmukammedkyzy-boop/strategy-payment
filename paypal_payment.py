from payment_strategy import PaymentStrategy

class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        return f"Processing PayPal payment of ${amount}"