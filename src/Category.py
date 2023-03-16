class category:
    

    def __init__(self, category):
        self.ledger = []
        self.deposits = 0
        self.withdraws = 0

        self.category = category

    def deposit(self, amount, description=""):
        self.ledger.append({"amount":amount, "description":description})
        self.funds = amount

    def withdraw(self, amount, description):
       
        if amount <= self.check_funds():
            amount = -amount
            self.ledger.append({"withdraw": amount, "description": description})
        else:
            print(f"insufficient funds! could not withdraw ${amount} for {description}")
            
    def get_balance(self):

        balance = self.funds
        return balance

    def check_funds(self):
        sum = 0
        for i in self.ledger:
            if "withdraw" in i.keys():
                sum += i["withdraw"]
        #print(self.funds)
        return(self.funds + sum)#adding because sum is a negative number

    #transfer function/ will need target input and amount. use check funds
    def transfer(self, amount, destination):
        if amount <= self.check_funds():
            self.ledger.append({"withdraw": -amount, "description": f"transer to {destination}"})
            destination.ledger.append({"deposit": amount, "description": f"transfer from {self.category} "})

        else:
            print(f"insufficient funds! could not transfer ${amount} to {destination}")


        
    def __str__(self):
        ledger = self.ledger 
        outputStr = "Category: " + str(self.category)+"\n"
        outputStr += f"Initial Deposit:{ledger[0]['amount']}" +"\n"
        for i in ledger:
            if "withdraw" in i.keys() or "transfer" in i.keys():
                outputStr += (str(i["description"]) + str(i["withdraw"]))+"\n"
        outputStr += "Total: " + str(self.check_funds()) + "\n"
        
        return(outputStr)

  