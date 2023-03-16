class category:
    

    def __init__(self):
        self.ledger = []
 

    def deposit(self, amount, description):
        self.ledger.append({"amount":amount, "description":description})
        self.funds = amount

    def withdraw(self, amount, description):
       
        if amount <= self.check_funds():
            amount = - amount
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

    def message(self):
        outputStr = ""
        for i in self.ledger:
            if "withdraw" in i.keys():
                outputStr += (" "+ str(i["description"])+ str(i["withdraw"]) + " /n")
        print(outputStr)

    def __str__(self):
        outputStr = f""""""
        for i in self.ledger:
            if "withdraw" in i.keys():
                outputStr += (str(i["description"])+ str(i["withdraw"]))
        return(outputStr)

  