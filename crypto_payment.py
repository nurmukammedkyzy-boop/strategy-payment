from payment_strategy import PaymentStrategy

class CryptoPayment(PaymentStrategy):
    def pay(self, amount):
        return f"Processing crypto payment of ${amount}"