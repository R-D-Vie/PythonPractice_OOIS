
#correct answer
class BankAccount():
  def __init__(self):
    self._checking = 0
    self._savings = 0
    
  def get_checking(self):
    return self._checking
  
  def set_checking(self, new_value):
    self._checking = new_value
    
  def get_savings(self):
    return self._savings
  
  def set_savings(self, new_value):
    self._savings = new_value

my_account = BankAccount()
print(my_account.set_checking(523.48))
print(my_account.get_checking())
print(my_account.set_savings(386.15))
print(my_account.get_savings())

#my answer
class BankAccount:
    def __init__(self, checking, savings):
        self._checking = checking
        self._savings = savings

    def get_checking(self):
        return self._checking

    def set_checking(self, new_checking):
        self._checking = new_checking

    def get_savings(self):
        return self._savings

    def set_savings(self, new_savings):
        self._savings = new_savings

my_account = BankAccount(523.48, 386.15)
print(my_account.set_checking(523.48))
print(my_account.get_checking())
print(my_account.set_savings(386.15))
print(my_account.get_savings())


