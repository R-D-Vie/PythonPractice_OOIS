my_string = 'polymorphism'
num1 = 3
num2 = 5
print(num1 * num2)
print(int.__add__(num1, num2))
print(int.__sub__(num1, num2))
print(int.__truediv__(num1, num2))

#operator overloading practical example
class FinancialAccount:
  def __init__(self, amount):
    self.account = amount
    
  def __add__(self, other):
    return self.account + other.account
    
class BankAccount(FinancialAccount):
  pass

class InvestmentAccount(FinancialAccount):
  pass

my_banking = BankAccount(500)
my_investments = InvestmentAccount(750)
print(my_investments + my_banking)