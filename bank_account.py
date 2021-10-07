# class IPhone(Phone):
#   def __init__(self, phone_number):
#     super().__init__(phone_number):
#     self.fingerprint = None

#   def set_fingerprint(self, fingerprint):
#     self.fingerprint = fingerprint

#   def unlock(self, fingerprint=None):
#     if (fingerprint == self.fingerprint):
#       print("Phone unlocked because no fingerprint has not been set.")

# class BankAccount():
#   def __init__(self, kind):
#     self.kind = kind
#     self.balance = 0
#     self.overdraft_fees = 0

#   def deposit(self, amount):
#     self.balance += amount

#   def withdraw(self, amount):
#     self.amount -= amount
#     if (self.amount < 0):
#       self.overdraft_fees += 20
#     return amount

class Bank_Account():
    def __init__(self, interest=1.02):
        self.balance = 0
        self.interest = interest
    
    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if (self.balance >= amount):
            self.balance -= amount
            return self.balance
        else:
            return False
    
    def accumulate_interest(self):
        self.balance = self.balance*self.interest
        return self.balance

class Childrens_Account(Bank_Account):
    def __init__(self):
        super().__init__()

        self.interest = 1
        self.balance = 0
    
    def accumulate_interest(self):
        self.balance += 10
        return self.balance

class Overdraft_Account(Bank_Account):
    def __init__(self, overdraft_penalty=40):
        super().__init__()
        self.overdraft_penalty = overdraft_penalty

        def withdraw(self, amount):
            if (self.balance >= amount):
                self.balance -= amount
                return self.balance
            else:
                self.balance -= self.overdraft_penalty


basic_account = Bank_Account()
basic_account.deposit(600)
print("Basic account has ${}".format(basic_account.balance))
basic_account.withdraw(17)
print("Basic account has ${}".format(basic_account.balance))
basic_account.accumulate_interest()
print("Basic account has ${}".format(basic_account.balance))
print()

childs_account = Childrens_Account()
childs_account.deposit(34)
print("Child's account has ${}".format(childs_account.balance))
childs_account.withdraw(17)
print("Child's account has ${}".format(childs_account.balance))
childs_account.accumulate_interest()
print("Child's account has ${}".format(childs_account.balance))
print()

overdraft_account = Overdraft_Account()
overdraft_account.deposit(12)
print("Overdraft account has ${}".format(overdraft_account.balance))
overdraft_account.withdraw(17)
print("Overdraft account has ${}".format(overdraft_account.balance))
overdraft_account.accumulate_interest()
print("Overdraft account has ${}".format(overdraft_account.balance))