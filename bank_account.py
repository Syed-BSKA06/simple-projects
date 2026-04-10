class BankAccount:
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self.balance = initial_balance

    def get_balance(self):
        print(f"\nAccount Owner : {self.owner}")
        print(f"Balance       : ${self.balance:.2f}")


if __name__ == "__main__":
    account = BankAccount("Aman", 500)
    account.get_balance()
