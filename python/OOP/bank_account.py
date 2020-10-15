# class user:
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#     def display_user_balance(self):
#         print(self.name, self.balance)
#         return self
#     def make_deposit(self, amount):
#         self.balance += amount
#         return self
#     def make_withdrawal(self, amount):
#         self.balance -= amount
#         return self
#     def transfer_money(self, amount, other_user):
#         self.balance -= amount
#         other_user.balance += amount
#         return self

# greg = user("greg", 10)
# ashley = user("ashley", 100)
# pete = user("pete", -10000)

# greg.make_deposit(9000000000000).make_withdrawal(500).transfer_money(3,ashley).display_user_balance()
# ashley.display_user_balance()
# pete.make_withdrawal(-20000).display_user_balance()
class BankAccount:
    def __init__(self, int_rate, balance = 0):
        self.balance = balance
        self.int_rate = int_rate/100
    def make_deposit(self, amount):
        self.balance += amount
        return self
    def make_withdrawal(self, amount):
        self.balance -= amount
        return self
    def display_account_info(self):
        print("Balance =", self.balance)
        return self
    def yield_interest(self):
        self.balance += (self.int_rate)*self.balance
        return self

greg = BankAccount(int_rate=50)
ashley = BankAccount(50, 20)

greg.make_deposit(50).make_deposit(20).make_deposit(70).make_withdrawal(30).display_account_info()
greg.yield_interest().display_account_info()

ashley.make_deposit(50).make_deposit(10000).make_withdrawal(10).make_withdrawal(10).make_withdrawal(10).make_withdrawal(10).display_account_info()
ashley.yield_interest().display_account_info()
