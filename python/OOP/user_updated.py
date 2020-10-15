class user:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def display_user_balance(self):
        print(self.name, self.balance)
        return self
    def make_deposit(self, amount):
        self.balance += amount
        return self
    def make_withdrawal(self, amount):
        self.balance -= amount
        return self
    def transfer_money(self, amount, other_user):
        self.balance -= amount
        other_user.balance += amount
        return self

greg = user("greg", 10)
ashley = user("ashley", 100)
pete = user("pete", -10000)

greg.make_deposit(9000000000000).make_withdrawal(500).transfer_money(3,ashley).display_user_balance()

ashley.display_user_balance()

pete.make_withdrawal(-20000).display_user_balance()