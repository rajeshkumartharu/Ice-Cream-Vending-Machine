# Simple CLI Banking System (Pure File Handling)

ACCOUNTS_FILE = "accounts.txt"
TRANSACTIONS_FILE = "transactions.txt"

# ---------- File Helpers ----------
def read_accounts():
    accounts = {}
    try:
        with open(ACCOUNTS_FILE, "r") as f:
            for line in f:
                acc_no, name, pin, balance = line.strip().split(",")
                accounts[acc_no] = {"name": name, "pin": pin, "balance": int(balance)}
    except FileNotFoundError:
        pass
    return accounts

def write_accounts(accounts):
    with open(ACCOUNTS_FILE, "w") as f:
        for acc_no, data in accounts.items():
            f.write(f"{acc_no},{data['name']},{data['pin']},{data['balance']}\n")

def log_transaction(acc_no, details):
    with open(TRANSACTIONS_FILE, "a") as f:
        f.write(f"{acc_no},{details}\n")


# ---------- Banking Functions ----------
def create_account(accounts):
    acc_no = str(len(accounts) + 1001)   # simple auto id
    name = input("Enter Name: ")
    pin = input("Set 4-digit PIN: ")
    accounts[acc_no] = {"name": name, "pin": pin, "balance": 0}
    write_accounts(accounts)
    print(f"Account created! Your Account No: {acc_no}")

def login(accounts):
    acc_no = input("Enter Account No: ")
    pin = input("Enter PIN: ")
    if acc_no in accounts and accounts[acc_no]["pin"] == pin:
        print(f"Welcome {accounts[acc_no]['name']}!")
        return acc_no
    else:
        print("Invalid login!")
        return None

def deposit(accounts, acc_no):
    amt = int(input("Enter amount to deposit: "))
    accounts[acc_no]["balance"] += amt
    write_accounts(accounts)
    log_transaction(acc_no, f"Deposit {amt}")
    print("Deposit successful!")

def withdraw(accounts, acc_no):
    amt = int(input("Enter amount to withdraw: "))
    if amt > accounts[acc_no]["balance"]:
        print("Insufficient funds!")
    else:
        accounts[acc_no]["balance"] -= amt
        write_accounts(accounts)
        log_transaction(acc_no, f"Withdraw {amt}")
        print("Withdrawal successful!")

def transfer(accounts, acc_no):
    target = input("Enter target account no: ")
    if target not in accounts:
        print("Target account not found!")
        return
    amt = int(input("Enter amount to transfer: "))
    if amt > accounts[acc_no]["balance"]:
        print("Insufficient funds!")
    else:
        accounts[acc_no]["balance"] -= amt
        accounts[target]["balance"] += amt
        write_accounts(accounts)
        log_transaction(acc_no, f"Transfer {amt} → {target}")
        log_transaction(target, f"Received {amt} ← {acc_no}")
        print("Transfer successful!")

def transaction_history(acc_no):
    try:
        with open(TRANSACTIONS_FILE, "r") as f:
            print("\n--- Transactions ---")
            for line in f:
                acc, details = line.strip().split(",", 1)
                if acc == acc_no:
                    print(details)
    except FileNotFoundError:
        print("No transactions yet!")


# ---------- Main CLI ----------
def main():
    accounts = read_accounts()

    while True:
        print("\n=== Banking System ===")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose option: ")

        if choice == "1":
            create_account(accounts)

        elif choice == "2":
            acc_no = login(accounts)
            if acc_no:
                while True:
                    print("\n--- Account Menu ---")
                    print("1. Deposit")
                    print("2. Withdraw")
                    print("3. Transfer")
                    print("4. Transaction History")
                    print("5. Logout")
                    sub = input("Choose option: ")

                    if sub == "1":
                        deposit(accounts, acc_no)
                    elif sub == "2":
                        withdraw(accounts, acc_no)
                    elif sub == "3":
                        transfer(accounts, acc_no)
                    elif sub == "4":
                        transaction_history(acc_no)
                    elif sub == "5":
                        break

        elif choice == "3":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
