class category:
    

    def __init__(self, category):
        self.ledger = []
        self.deposits = 0
        self.withdraws = 0

        self.category = category

    def deposit(self, amount, description=""):
        self.ledger.append({"deposit":amount, "description":description})
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
        withdraw = 0
        deposits = 0
        for i in self.ledger:
            if "withdraw" in i.keys():
                withdraw += i["withdraw"]
        for i in self.ledger:
            if "deposit" in i.keys():
                deposits += i["deposit"]
        #print(self.funds)
        #print(f"Withdraws: {withdraw}")
        #print(f"deposits: {deposits}")
        return(deposits + withdraw)#adding because sum is a negative number

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
        for i in ledger:
            if "withdraw" in i.keys() or "transfer" in i.keys():
                outputStr += (str(i["description"]) + str(i["withdraw"]))+"\n"
        outputStr += "Total: " + str(self.check_funds()) + "\n"
        
        return(outputStr)

  