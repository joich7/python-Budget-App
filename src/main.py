from Category import category



food = category("food")
food.deposit(2000, "Initial Deposit")
food.withdraw(10, "Groceries")
food.withdraw(5, "Mediterannian grill")
food.withdraw(100, "bacon")




clothes = category("clothes")
clothes.deposit(100, "Initial deposit")
clothes.withdraw(10, "bought new high heels")


#print(food.ledger) 
#print(food.check_funds())
#print(food.message())
print(food)
print(clothes)

food.transfer(40, clothes)
