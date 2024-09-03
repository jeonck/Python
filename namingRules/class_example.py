class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item_name: str, quantity: int, price: float):
        item = {
            "name": item_name,
            "quantity": quantity,
            "price": price
        }
        self.items.append(item)

    def remove_item(self, item_name: str):
        self.items = [item for item in self.items if item["name"] != item_name]

    def calculate_total(self) -> float:
        total = sum(item["quantity"] * item["price"] for item in self.items)
        return total

    def get_receipt(self) -> str:
        receipt = "\n".join(f"{item['quantity']} x {item['name']} = ${item['quantity'] * item['price']}" for item in self.items)
        return receipt
