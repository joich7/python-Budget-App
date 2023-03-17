class category:
    

    def __init__(self, category):
        self.ledger = []
        self.category = category

    def deposit(self, amount, description=""):
        self.ledger.append({"deposit":amount, "description":description})
        self.funds = amount

    def withdraw(self, amount, description):
       
        if self.check_funds(amount):
            amount = -amount
            self.ledger.append({"withdraw": amount, "description": description})
        else:
            print(f"insufficient funds! could not withdraw ${amount} for {description}")
            
    def check_funds(self, amount):
        return amount <= self.get_balance()
    
    def withdraws_sum(self):
        withdraws = 0
        for i in self.ledger:
            if "withdraw" in i.keys():
                withdraws += i["withdraw"]
        return withdraws
    
    def deposits_sum(self):
        deposits = 0
        for i in self.ledger:
            if "deposit" in i.keys():
                deposits += i["deposit"]
        return deposits
    
    def percentage_spent(self):
        if self.withdraws_sum() == 0:
            return 0
        else:
            sum = float(-self.withdraws_sum() / self.deposits_sum())*100
            return sum

    def get_balance(self):
        
        sum = self.withdraws_sum() + self.deposits_sum()
        #print(self.funds)
        #print(f"Withdraws: {withdraw}")
        #print(f"deposits: {deposits}")
        return(sum)#adding because sum is a negative number

    #transfer function/ will need target input and amount. use check funds
    def transfer(self, amount, destination):
        if self.check_funds(amount):
            self.ledger.append({"withdraw": -amount, "description": f"transer to {destination.category}"})
            destination.ledger.append({"deposit": amount, "description": f"transfer from {self.category}"})

        else:
            print(f"insufficient funds! could not transfer ${amount} to {destination}")


        
    def __str__(self):
        ledger = self.ledger 
        outputStr = "Category: " + str(self.category)+"\n"

        for i in ledger:
            if "withdraw" in i.keys():
                outputStr += f"{i['description']}: {i['withdraw']} \n"
            elif "deposit" in i.keys():
                outputStr += f"{i['description']}: +{i['deposit']} \n"
        outputStr += "Total: " + str(self.get_balance()) + "\n"
        outputStr += f"Budget Spent: {self.percentage_spent()} % \n"
        
        
        return(outputStr)

  