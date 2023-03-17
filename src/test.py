while(end2):
        action = input("Would you like to transfer or withdraw?")
        if action == 'withdraw':
            description = input("Description of why you are withdrawing")
            amount = input()            
            newCat.transfer(amount,budget)
            ender = input("Enter another transfer or withdraw? Enter(yes) no(n): ")
            if ender == "n":
                end2 = False
        if action == "transfer":
            amount = input("how much would you like to trasfer?")
            if budget