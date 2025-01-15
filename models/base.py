from abc import ABC, abstractmethod

# Abstract Base Class for Users
class BaseUser(ABC):
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @abstractmethod
    def get_role(self):
        pass

    def login(self):
        return f"{self.username} logged in."

# Payment Interface
class PaymentMethod(ABC):   
    @abstractmethod
    def process_payment(self, amount):
        pass

    @abstractmethod
    def refund(self, amount):
        pass

# Abstract Base Class for Products
class BaseProduct(ABC):
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock
    
    @abstractmethod
    def calculate_shipping(self):
        pass