from .base import BaseUser

class Customer(BaseUser):
    def get_role(self):
        return "Customer"

class Admin(BaseUser):
    def get_role(self):
        return "Admin"