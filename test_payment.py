import unittest
from payment_processor import PaymentProcessor
from credit_card_payment import CreditCardPayment
from paypal_payment import PayPalPayment
from crypto_payment import CryptoPayment


class TestPaymentStrategies(unittest.TestCase):

    def setUp(self):
        self.processor = PaymentProcessor()

    def test_credit_card_payment(self):
        self.processor.set_strategy(CreditCardPayment())
        result = self.processor.process_payment(100)
        self.assertEqual(result, "Processing credit card payment of $100")

    def test_paypal_payment(self):
        self.processor.set_strategy(PayPalPayment())
        result = self.processor.process_payment(150)
        self.assertEqual(result, "Processing PayPal payment of $150")

    def test_crypto_payment(self):
        self.processor.set_strategy(CryptoPayment())
        result = self.processor.process_payment(200)
        self.assertEqual(result, "Processing crypto payment of $200")

    def test_switching_strategies(self):
        self.processor.set_strategy(CreditCardPayment())
        result1 = self.processor.process_payment(100)

        self.processor.set_strategy(PayPalPayment())
        result2 = self.processor.process_payment(100)

        self.assertNotEqual(result1, result2)


if __name__ == "__main__":
    unittest.main()