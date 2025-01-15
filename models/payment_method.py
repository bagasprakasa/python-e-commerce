from .base import PaymentMethod

# Concrete Implementation for Credit Card

class CreditCardPayment(PaymentMethod):
    def process_payment(self, amount):
        return "Processed credit card payment of ${amount}"
    
    def refund(self, amount):
        return "Refunded credit card payment of ${amount}"

class PayPalPayment(PaymentMethod):
    def process_payment(self, amount):
        return "Processed PayPal payment of ${amount}"
    
    def refund(self, amount):
        return "Refunded PayPal payment of ${amount}"