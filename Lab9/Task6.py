
class TicketMachine:
    def __init__(self, price):
        if price < 0:
            raise ValueError('Ticket Price Cannot be Negative!')
        self.price = price
        self.balance = 0
        self.total = 0

    def insertMoney(self, amount):
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        self.balance = self.balance + amount

    def getPrice(self):
        return self.price

    def getBalance(self):
        return self.balance

    def printTicket(self):
        if self.balance < self.price:
            print("Not enough money to print the ticket!")
        else:
            print("Ticket is being printed!")
            self.total += self.price
            self.balance = 0

    def getTotatlCollected(self ):
        return self.total


ticketMachine = TicketMachine(10)
ticketMachine.insertMoney(100)

print(f'Ticket Price: {ticketMachine.getPrice()}')
print(f'Balance: {ticketMachine.getBalance()}')

ticketMachine.printTicket()

print(f'Total collected by the machine: {ticketMachine.getTotatlCollected()}')


print(f'Ticket Price: {ticketMachine.getPrice()}')
print(f'Balance: {ticketMachine.getBalance()}')

ticketMachine.printTicket() # for this time, error will occur, as the balance is not sufficient

ticketMachine.insertMoney(40)
ticketMachine.printTicket()


print(f'Total collected by the machine: {ticketMachine.getTotatlCollected()}')
print(f'Balance: {ticketMachine.getBalance()}')