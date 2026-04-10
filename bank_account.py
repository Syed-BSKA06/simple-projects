from datetime import datetime


class BankAccount:
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self.balance = initial_balance
        self.transactions = []
        if initial_balance > 0:
            self._record("Initial deposit", initial_balance)

    def _record(self, description, amount):
        self.transactions.append({
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "description": description,
            "amount": amount,
            "balance": self.balance,
        })

    def get_balance(self):
        print(f"\nAccount Owner : {self.owner}")
        print(f"Balance       : ${self.balance:.2f}")

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be greater than zero.")
            return
        self.balance += amount
        self._record("Deposit", amount)
        print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
            return
        if amount > self.balance:
            print(f"Insufficient funds. Available balance: ${self.balance:.2f}")
            return
        self.balance -= amount
        self._record("Withdrawal", -amount)
        print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")

    def show_history(self):
        if not self.transactions:
            print("No transactions yet.")
            return
        print(f"\n{'Date':<22} {'Description':<20} {'Amount':>10} {'Balance':>10}")
        print("-" * 65)
        for t in self.transactions:
            print(f"{t['date']:<22} {t['description']:<20} ${t['amount']:>9.2f} ${t['balance']:>9.2f}")


def main():
    print("=== Simple Bank Account ===")
    name = input("Enter account owner name: ").strip() or "User"
    try:
        opening = float(input("Enter opening balance (default 0): ") or 0)
    except ValueError:
        opening = 0
    account = BankAccount(name, opening)

    menu = """
1. Check Balance
2. Deposit
3. Withdraw
4. Transaction History
5. Exit
"""
    while True:
        print(menu)
        choice = input("Choose an option: ").strip()

        if choice == "1":
            account.get_balance()
        elif choice == "2":
            try:
                amount = float(input("Enter deposit amount: $"))
                account.deposit(amount)
            except ValueError:
                print("Invalid amount.")
        elif choice == "3":
            try:
                amount = float(input("Enter withdrawal amount: $"))
                account.withdraw(amount)
            except ValueError:
                print("Invalid amount.")
        elif choice == "4":
            account.show_history()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1-5.")


if __name__ == "__main__":
    main()
