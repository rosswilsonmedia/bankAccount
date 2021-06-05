class BankAccount:
    __all_accounts=[]
    def __init__(self, int_rate, balance=0):
        self.int_rate=int_rate
        self.balance=balance
        BankAccount.__all_accounts.append(self)
    def deposit(self, amount):
        self.balance+=amount
        return self
    def withdraw(self, amount):
        if amount>self.balance:
            print('insufficient funds: Charging a $5 fee')
            self.balance-=5
        else:
            self.balance-=amount
        return self
    def display_account_info(self):
        print('Balance:', self.balance)
        return self
    def yield_interest(self):
        if self.balance>0:
            self.balance=self.balance*(1+self.int_rate)
        return self

    @classmethod
    def all_info(cls):
        for account in cls.__all_accounts:
            print("Balance:",account.balance,"Rate:",account.int_rate)

account1=BankAccount(int_rate=.01)
account2=BankAccount(int_rate=.02,balance=50)

account1.deposit(50).deposit(20).deposit(45).withdraw(30).yield_interest().display_account_info()
account2.deposit(25).deposit(25).withdraw(10).withdraw(10).withdraw(10).withdraw(10).yield_interest().display_account_info()

BankAccount.all_info()