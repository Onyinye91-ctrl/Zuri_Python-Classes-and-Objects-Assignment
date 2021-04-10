

#Solution 1. Create a Budget class that can instantiate objects based on different budget categories like food, clothing, and entertainment.
class Budget:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

#Solution 2. Depositing funds to each of the categories
    def deposit(self, amount):
        self.balance = amount 

        return f"The new balance in your account is ${self.balance} for {self.name} budget."

#Solution 3.  Withdrawing funds from each category
    def Withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient Fund")
        else:
            old_balance = self.balance
            self.balance = self.balance - amount
            return f"Your balance is ${old_balance} for {self.name} budget,you Withdrew ${amount} from {self.name} burget and your current balance is {self.balance} for {self.name} budget."

#Solution 4. Computing category balances
    def cat_balances (self):
        response = f"Your balance is ${self.balance} for {self.name} budget"  

        return response  

#Solution 5. Transferring balance amounts between categories
    def transfer(self, amount, cat_transfer):
        if self.balance < amount:
            return 'You don\'t have Sufficient Balance'
        else:
            self.balance = self.balance - amount
            cat_transfer.balance  = cat_transfer.balance + amount

            response = f'You transfered ${amount} to {cat_transfer.name} budget\n'
            response += f'from {self.name} budget.Your remaining Balance is {self.balance} for {self.name} budget'

            return response




food = Budget("food", 1000)
clothing = Budget("clothing", 2000)
entertainment = Budget("entertainment", 1000)

print("*" *50)
print(f"These are my Burgets, {food.name}, {clothing.name} and {entertainment.name}.\n")

print("*" * 50)
print(clothing.deposit(3000))
print(food.deposit(5000))
print(entertainment.deposit(5000))

print("*" * 50)
print(clothing.Withdraw(1000))
print(food.Withdraw(2000))
print(entertainment.Withdraw(3000))

print("*" * 50)
print(food.cat_balances())

print("*" * 50)
print(food.transfer(1000, entertainment))
