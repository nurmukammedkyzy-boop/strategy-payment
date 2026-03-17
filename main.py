from payment_processor import PaymentProcessor
from credit_card_payment import CreditCardPayment
from paypal_payment import PayPalPayment
from crypto_payment import CryptoPayment

processor = PaymentProcessor()

# Credit Card
processor.set_strategy(CreditCardPayment())
print(processor.process_payment(100))

# PayPal
processor.set_strategy(PayPalPayment())
print(processor.process_payment(200))

# Crypto
processor.set_strategy(CryptoPayment())
print(processor.process_payment(300))