class BankAccount:
           
    def __init__(self,int_rate,balance):
         self.int_rate = int_rate
         self.balance = balance
         
    def withdraw(self, amount):
        self.balance -= amount
        return self

    def deposit(self,amount):
        self.balance += amount
        return self

    def yield_interest(self): 
        self.balance += self.balance * self.int_rate
        return self
        
    def display_account_info(self):
        print( 'Balance: ' , self.balance)
    
    

bankAccount_1 = BankAccount(0.05,5050)
bankAccount_2 = BankAccount(0.05,25000)

bankAccount_1.deposit(900).deposit(50000).deposit(2500).withdraw(15000).yield_interest().display_account_info()

bankAccount_2.deposit(15000).deposit(2500).withdraw(500).withdraw(3000).withdraw(450).withdraw(660).yield_interest().display_account_info()





