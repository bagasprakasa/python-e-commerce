class Cart:
    def __init__(self):
        self.items = []

    def add_to_cart(self, product, quantity):
        if product.stock >= quantity:
            self.items.append({"product": product, "quantity": quantity})
            product.update_stock(-quantity)
            print(f"Added {quantity} of {product.name} to cart.")
        else:
            print(f"Insufficient stock for {product.name}.")

    def remove_from_cart(self, product):
        for item in self.items:
            if item["product"] == product:
                product.update_stock(item["quantity"])
                self.items.remove(item)
                print(f"Removed {product.name} from cart.")
                return
        print(f"{product.name} not found in cart.")

    def view_cart(self):
        if not self.items:
            print("Your cart is empty.")
        for item in self.items:
            product = item["product"]
            quantity = item["quantity"]
            print(f"{product.name} - ${product.price:.2f} x {quantity}")

    def calculate_total(self):
        return sum(item["product"].price * item["quantity"] for item in self.items)
    # def calculate_total(self):
    #     return sum(item["product"].price * item["quantity"] for item in self.items)
