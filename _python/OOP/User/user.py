class User:

    def make_withdrawal(self, amount):
        self.balance -= amount
    
    def __init__(self , user_name , account,balance):
        self.user_name = user_name
        self.account = account
        self.balance = balance 

    def Deposit(self,amount):
        self.balance += amount
    
    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.Deposit(amount) 

    def disply_user_balance(self):
        print(self.balance)  

user_one = User('yazan','yazan@axos.com',15000)
user_two = User('ahmad','ahmad@axsos.com',500)
user_three = User('sarah','sarah@axsos.com',4000)

user_one.Deposit(4000)
user_one.Deposit(5000)
user_one.Deposit(3500)

user_one.make_withdrawal(15000)

user_one.disply_user_balance()

user_two.Deposit(7000)
user_two.Deposit(1000)

user_two.make_withdrawal(500)
user_two.make_withdrawal(2570)

user_two.disply_user_balance()


user_three.Deposit(20000)

user_three.make_withdrawal(500)
user_three.make_withdrawal(6540)
user_three.make_withdrawal(4200)

user_three.disply_user_balance()

user_one.transfer_money(user_three,2500)

user_one.disply_user_balance()
user_three.disply_user_balance()










