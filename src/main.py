from Category import category



food = category()

food.deposit(20, "Depositing this weeks payheck")
food.withdraw(10, "Groceries")
food.withdraw(5, "Mediterannian grill")
food.withdraw(100, "bacon")
print(food.ledger) 
print(food.check_funds())
#print(food.message())
print(food)

