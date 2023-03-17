from Category import category



food = category("food")
food.deposit(100, "Initial Deposit")
food.withdraw(10, "Groceries")
food.withdraw(5, "Mediterannian grill")
food.withdraw(100, "bacon")




clothes = category("clothes")
food.transfer(30, clothes)


for i in ledger:
            if "food" in i.keys():
                
            elif "deposit" in i.keys():
                outputStr += f"{i['description']}: +{i['deposit']} \n"


print(food)

print(clothes)

#food.transfer(40, clothes)
