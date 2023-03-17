from Category import category

categories = []

end = end2 = True

budget = category("budget")
budget_amount = input("Enter your budget:$ ")
budget.deposit(budget_amount)

def log():
    for x in categories:
        print(x)
def log_names():
    for x in categories:
        print(x.names)

while(end): #establish all classes 
    name = input("Enter category name: ")
    newCat = category(name)
    categories.append(newCat)
    ender = input("Make another category? yes(hit enter) no(n): ")
    if ender != "":
        end = False
while(end2):
        action = input("Would you like to: \n (a)transfer money to another category? \n (b)withdraw from a category? \n (c)Print out status \n input: " )
        
        if action == "a": #transfer
            amount = input("how much would you like to trasfer?")
        
        

        if action == 'b': #withdraw
            origin = input("where do you want to transfer from?")
            log_names()
            description = input("Description of why you are withdrawing")
            amount = input()            
            newCat.transfer(amount,budget)
            ender = input("Enter another transfer or withdraw? Enter(yes) no(n): ")
            if ender == "n":
                end2 = False
        

        if action == "c":
            log()
           







#prompt for name of catergory
#
#
#
#