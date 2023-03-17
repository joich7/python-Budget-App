from Category import category

categories = []

end = end2 = True

budget = category("budget")
budget_amount = input("Enter your budget:$ ")
budget.deposit(budget_amount)
categories.append({'budget': budget})

def finder(namestr):
    for i in categories:
        if namestr in i.keys():
            return i




def log():
    for x in categories:
        print(x)



while(end): #establish all classes 
    name = input("Enter category name: ")
    categories.append({name:category(name)})
    print(finder(name))
    ender = input("Make another category? yes(hit enter) no(n): ")

    if ender != "":
        end = False

while(end2):
        action = input("Would you like to: \n (a)transfer money to another category? \n (b)withdraw from a category? \n (c)Print out status \n input: " )
        
        if action == "a": #transfer
            log()
            origin = input("where do you want to transfer from: ")
            amount = int(input("How much do you want to transfer: "))
            target = input("Enter category to receive money: ")            
            categories[origin].transfer(amount, categories[target])

        

        if action == 'b': #withdraw
            log_names()
            origin = input("where do you want to transfer from: ")
            amount = input("How much do you want to transfer: ")
            target = input("Enter category to receive money: ")            
            categories[origin].transfer(amount, categories[target])

            ender = input("Enter another transfer or withdraw? Enter(yes) no(n): ")
            if ender == "n":
                end2 = False
        

        if action == "c":
            log()
           
        ender = input("Enter another transfer or withdraw? Enter(yes) no(n): ")
        if ender == "n":
            end2 = False






#prompt for name of catergory
#
#
#
#