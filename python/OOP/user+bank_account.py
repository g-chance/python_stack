class user:
    def __init__(self, name):
        self.name = name
        self.account1 = BankAccount(int_rate=50)
        self.account2 = BankAccount(int_rate=20)
    def display_user_balance(self):
        print(self.name, "Account 1", self.account1.balance, "Account 2", self.account2.balance)
        return self
    def make_deposit(self, account, amount):
        if(account == "account1"):
            self.account1.balance += amount
        elif(account == "account2"):
            self.account2.balance += amount
        return self
    def make_withdrawal(self, account, amount):
        if(account == "account1"):
            self.account1.balance -= amount
        elif(account == "account2"):
            self.account2.balance -= amount
        return self
    def transfer_money(self, account, amount, other_user, other_user_account):
        if(account == "account1"):
            self.account1.balance -= amount
            if(other_user_account == "account1"):
                other_user.account1.balance += amount
            elif(other_user_account == "account2"):
                other_user.account2.balance += amount
        elif(account == "account2"):
            self.account2.balance -= amount
            if(other_user_account == "account1"):
                other_user.account1.balance += amount
            elif(other_user_account == "account2"):
                other_user.account2.balance += amount
        return self




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

# greg = BankAccount(int_rate=50)
# ashley = BankAccount(50, 20)

# greg.make_deposit(50).make_deposit(20).make_deposit(70).make_withdrawal(30).display_account_info()
# greg.yield_interest().display_account_info()

# ashley.make_deposit(50).make_deposit(10000).make_withdrawal(10).make_withdrawal(10).make_withdrawal(10).make_withdrawal(10).display_account_info()
# ashley.yield_interest().display_account_info()

greg = user("greg")
ashley = user("ashley")
pete = user("pete")

greg.display_user_balance()
greg.make_deposit(account="account1", amount = 50)
greg.display_user_balance()
ashley.display_user_balance()
greg.make_deposit(amount=9000000000000, account="account1").make_withdrawal(amount=500, account="account2").display_user_balance()
greg.transfer_money(amount=3, account="account1", other_user=ashley, other_user_account="account1").display_user_balance()
ashley.display_user_balance()
# ashley.make_deposit(50).display_user_balance()
# pete.make_withdrawal(-20000).display_user_balance()