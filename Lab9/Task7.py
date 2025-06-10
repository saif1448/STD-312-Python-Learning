
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
            self.total += self.balance
            self.balance = 0

    def getTotatlCollected(self ):
        return self.total



class TicketMachineSystem:
    def __init__(self):
        self.ticketMachines = {}
        # 1 ---> ticketmachine1
        # 2 ---> ticketmachine2

    def addTicketMachine(self, id, newTicketMachine):
        self.ticketMachines[id] = newTicketMachine
        print(f'Ticket Machine {id} has been added!')

    def removeTicketMachine(self, id):
        del self.ticketMachines[id]
        print(f'Ticket Machine  #{id} has been removed!')

    def showTotalIndividual(self, id):
        total = self.ticketMachines[id].getTotatlCollected()
        print(f'Ticket Machine  #{id} Total: {total}')

    def getTotalSale(self):
        total_sale = 0
        for id , ticketMachine in self.ticketMachines.items():
            total_sale += ticketMachine.getTotatlCollected()

        print(f'Total Sale: {total_sale}')


try:
    t1 = TicketMachine(10)
    t2 = TicketMachine(15)
    t3 = TicketMachine(20)
    t4 = TicketMachine(20)
    t5 = TicketMachine(10)

    ticketMachineSystem = TicketMachineSystem()

    ticketMachineSystem.addTicketMachine(1, t1)
    ticketMachineSystem.addTicketMachine(2, t2)
    ticketMachineSystem.addTicketMachine(3, t3)
    ticketMachineSystem.addTicketMachine(4, t4)
    ticketMachineSystem.addTicketMachine(5, t5)

    ticketMachineSystem.getTotalSale()

    t1.insertMoney(30)
    t1.printTicket()
    t2.insertMoney(30)
    t2.printTicket()
    t4.insertMoney(30)
    t4.printTicket()
    t5.insertMoney(30)
    t5.printTicket()

    ticketMachineSystem.getTotalSale()

    ticketMachineSystem.showTotalIndividual(3)

    ticketMachineSystem.removeTicketMachine(1)
    ticketMachineSystem.getTotalSale()
except Exception as e:
    print(e)