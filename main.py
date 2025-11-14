class product:
    item: str
    price: float
    quantity: int
    description: str

    def __init__(self, item: str, price: float, quantity: int, description: str):
        self.item = item
        self.price = price
        self.quantity = quantity
        self.description = description

    def display_info(self):
        return f"Item: {self.item}, Price: ${self.price:.2f}, Quantity: {self.quantity}, Description: {self.description}"
    
    def __str__(self):
        return f"{self.item} - ${self.price:.2f} (Qty: {self.quantity})"
    

