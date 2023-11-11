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


class User:

    def make_withdrawal(self, amount):
        self.account_balance -= amount
    
    def __init__(self , user_name , account , account_balance):
        self.user_name = user_name
        self.account = account
        self.account_balance = account_balance

    def Deposit(self,amount): 
        self.account_balance += amount
    
    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.Deposit(amount) 

    def disply_user_balance(self):
        print(self.account_balance)  
        


Newuser = User('habib','ahmad@axsos.com',50000)