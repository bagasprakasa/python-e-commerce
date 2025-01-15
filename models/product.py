from .base import BaseProduct

class PhysicalProduct(BaseProduct):
    def calculate_shipping(self):
        return f"Shipping cost for {self.name} is ${self.price * 0.1}"
    
class DigitalProduct(BaseProduct):
    def calculate_shipping(self):
        return f"{self.name} is a digital product. No shipping required."
