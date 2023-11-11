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
    
    def __init__(self , user_name , email ):
        self.user_name = user_name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)

    def Deposit(self,amount): 
        self.account.deposit(amount)
    
    def transfer_money(self, other_user, amount):
        self.account.make_withdrawal(amount)
        other_user.account.Deposit(amount) 
       
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)

    def disply_user_balance(self):
        print(f"User: {self.user_name}, Balance: {self.account.display_account_info()}")     
    

    
       

habibUser = User('habib','ahmad@axsos.com')
habibUser.Deposit(56000)
habibUser.disply_user_balance()


