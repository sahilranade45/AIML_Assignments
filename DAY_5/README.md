# Bank Account Management

This is a simple Python program that demonstrates the basic concepts of Object-Oriented Programming (OOP) using a Bank Account example.

## Concepts Used

- Class
- Object
- Constructor (`__init__`)
- `self`
- Attributes
- Methods
- Conditional statements

## Program Description

The `BankAccount` class represents a bank account.

It contains two attributes:

- `owner` - stores the account owner's name
- `balance` - stores the current account balance

The class contains three methods:

### 1. deposit()

Adds money to the account balance.

### 2. withdraw()

Withdraws money from the account if sufficient balance is available.

If the withdrawal amount is greater than the available balance, the program displays:

    Insufficient balance

### 3. show_balance()

Displays the account owner's name and current balance.

## Program Code

    class BankAccount:
        def __init__(self, owner, balance):
            self.owner = owner
            self.balance = balance

        def deposit(self, amount):
            self.balance += amount

        def withdraw(self, amount):
            if amount <= self.balance:
                self.balance -= amount
            else:
                print("Insufficient balance")

        def show_balance(self):
            print(f"Balance for {self.owner} is {self.balance}")


    account = BankAccount("Sahil", 1000)

    account.deposit(500)
    account.withdraw(200)
    account.show_balance()

## Output

    Balance for Sahil is 1300

## Execution Flow

    BankAccount class
           ↓
    Create account
           ↓
    __init__("Sahil", 1000)
           ↓
    Balance = 1000
           ↓
    deposit(500)
           ↓
    Balance = 1500
           ↓
    withdraw(200)
           ↓
    Balance = 1300
           ↓
    show_balance()
           ↓
    Balance for Sahil is 1300

## Step-by-Step Execution

### Step 1: Create Object

    account = BankAccount("Sahil", 1000)

The `__init__()` constructor is automatically called.

    owner = Sahil
    balance = 1000

### Step 2: Deposit

    account.deposit(500)

The balance becomes:

    1000 + 500 = 1500

### Step 3: Withdraw

    account.withdraw(200)

The program checks whether sufficient balance is available:

    200 <= 1500

The condition is true, so:

    1500 - 200 = 1300

### Step 4: Show Balance

    account.show_balance()

The program displays:

    Balance for Sahil is 1300

## Technologies Used

- Python

## Author

**Sahil Ranade**

AIML Batch