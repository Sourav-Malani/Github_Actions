#Create wallet class with the following methods: getBalance, addBalance, removeBalance
class wallet:
    balance = 0
    def __init__(self, balance):
        self.balance = balance
    def getBalance(self):
        return self.balance
    def addBalance(self, amount):
        self.balance += amount
    def removeBalance(self, amount):
        self.balance -= amount

def add(a, b):
    return a + b

if __name__ == "__main__":
    result = add(2, 3)
    print(f"The result is: {result}")    
#add funtion to take power of a number

