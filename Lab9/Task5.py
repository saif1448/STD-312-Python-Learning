

class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def cost(self):
        return self.price * self.quantity

class Cart:
    def __init__(self):
        self.items = []

    def addItem(self, item):
        self.items.append(item)

    def total(self):
        total = 0
        for item in self.items:
            total += item.cost()
        return total

    def summary(self):
        for item in self.items:
            print(f'{item.name}: {item.price} x {item.quantity} = ${item.cost()}')
        print(f'Total = ${self.total()}')


cart = Cart()

milk_item = Item(name='Milk', price=70, quantity=5)
bread_item = Item(name='Bread', price=40, quantity=7)
eggs_item = Item(name='Eggs', price=30, quantity=10)

cart.addItem(milk_item)
cart.addItem(bread_item)
cart.addItem(eggs_item)

cart.summary()

