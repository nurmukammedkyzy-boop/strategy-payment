class PaymentProcessor:
    def __init__(self):
        self.strategy = None

    def set_strategy(self, strategy):
        self.strategy = strategy

    def process_payment(self, amount):
        if not self.strategy:
            raise Exception("Payment strategy not set!")
        return self.strategy.pay(amount)