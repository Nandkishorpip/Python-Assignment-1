class BankAccount:
    def __init__(self,initial_deposite=0):
        self.balance = initial_deposite
        print(f"Account created with initial deposite:{self.balance}")

    def deposite(self,amount):
        if amount > 0:
            self.balance += amount
            print("Deposite:{amount}")
        else:
            print(f"Invalid Deposite ! please give a positive amount")

    def withdrawl(self,amount):
        if amount > self.balance:
            print("Insufficient fund ! withdrawl denied")
        elif amount < 0:
            print("Invalid withdral amount please give a positive amount")
        else:
            self.balance -= amount
            print(f"withdraw:{amount}")

    def check_balance(self):
        print(f"available balance:{self.balance}")

def main():
    print("welcome to the bank account system")
    initial_deposite = float(input("Enter initial deposite to create your account:"))
    account = BankAccount(initial_deposite)
    while True:
        print("\nMenu")
        print("1.deposite")
        print("2.withdraw")
        print("3.check_balance")
        print("4.Exit")

        choice = input("Chose an option (1-4):")
        if choice == '1':
            amount = float(input("Enter amount to deposite:"))
            account.deposite(amount)
        elif choice == '2':
            amount = float(input("Enter amount to withdraw:"))
            account.withdrawl(amount)
        elif choice == '3':
            account.check_balance()
        elif choice == '4':
            print("Thank you for using the bank account system.GoodBye")
            break
        else:
            print("Invalid choice.please input a valid choice.")


if __name__ == "__main__":
    main()


