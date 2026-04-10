class BankAccount:
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self.balance = initial_balance

    def get_balance(self):
        print(f"\nAccount Owner : {self.owner}")
        print(f"Balance       : ${self.balance:.2f}")

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be greater than zero.")
            return
        self.balance += amount
        print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
            return
        if amount > self.balance:
            print(f"Insufficient funds. Available balance: ${self.balance:.2f}")
            return
        self.balance -= amount
        print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")


if __name__ == "__main__":
    account = BankAccount("Aman", 500)
    account.get_balance()
    account.deposit(200)
    account.withdraw(100)
    account.withdraw(700)
