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
    
class customer:
    id: int
    name: str
    email: str
    phone: str
    address: str

    def __init__(self,id: int, name: str, email: str, phone: str, address: str):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address

    def customer_info(self):
        return f"Name: {self.name}, Email: {self.email}, Phone: {self.phone}, Address: {self.address}"
    
    def __str__(self):
        return f"{self.name} - {self.email}"


class order:
    def __init__(self,c_id: int, pid: str, quantity: int, order_date: str, status: str):
        self.cust_id = c_id
        self.prod_id = pid
        self.quantity = quantity
        self.order_date = order_date
        self.status = status