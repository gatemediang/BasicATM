# register
# -firstname, lastname, password, email
# -generate user account

# login
# -account number and password

# bank operations

# Initialize the system

import random

database = {}


# database = {}


# dict.update(newkey1 ='portal')


def init():
    print('Welcome To BankPP')

    have_account = int(
        input('Do you have account with us? 1(Yes) 2(No) \n'))

    if have_account == 1:
        login()

    elif have_account == 2:
        print(register())

    else:
        print('You hve selected an invalid option, try again')
        init()


def login():
    print('Please Login into your account login')

    account_number_from_user = int(
        input("what is your account number? \n"))
    password = input("what is your password \n")

    for account_number, user_details in database.items():
        if account_number == account_number_from_user:
            if user_details[3] == password:
                bank_operations(user_details)
            else:
                print('invalid account or password')
                login()
        else:
            print('invalid account or password')
            login()


def register():
    print('***********REGISTER HERE***********')
    email = input('What is your email address? \n')
    firstname = input('What is your first name? \n')
    lastname = input('What is your last name? \n')
    password = input('Create a password \n')

    account_number = generate_account_number()
    database[account_number] = [email, firstname, lastname, password, 0]

    print('Congratulations! Your Account Has Been Created')
    print("=== ==== ===== ===== ==== ===")
    print("Your account number is: %d" % account_number)
    print('Make sure you keep it safe')
    print("=== ==== ===== ===== ==== ===")

    login()


def bank_operations(user):
    print('Welcome %s %s' % (user[0], user[1]))
    for account_number, user_details in database.items():
        selected_option = int(input(
            'What would you like to do? (1) Deposit, (2) Withdraw, (3) Check Account Balance, (4) Logout, (5) Exit \n'))

        if selected_option == 1:
            deposit_operation()

        elif selected_option == 2:
            withdrawal_operation()

        elif selected_option == 3:
            current_balance = user_details[4]
            print('Account Balance: NGN %d' % current_balance)
            print('Thank You For Banking With Us \n Care to do any other transaction?')
            bank_operations(user_details)

        elif selected_option == 4:
            logout()

        elif selected_option == 5:
            exit()
        else:
            print('invalid option selected, try again')
            bank_operations(user)


def deposit_operation():
    print('*** Make Payment Deposit Here ***')
    for account_number, user_details in database.items():

        # get current balance

        # get amount to deposit
        user_deposit = int(input('How much are you depositing? \n'))
        # add deposited amount to current balance
        current_balance = user_details[4] + user_deposit
        # display current balance
        print('Deposit Payment Successful! Your new balance is: NGN. %d' % current_balance)
        transaction = int(input('Are you still doing any other transaction (1) Yes, (2) No \n'))
        if transaction == 1:
            bank_operations(user_details)

        elif transaction == 2:
            print('Thank you for banking with us')
            exit()

        else:
            print('Invalid input try again')
            int(input('Are you still doing any other transaction (1) Yes, (2) No \n'))
        return current_balance


def withdrawal_operation():
    print('****** Make Withdraws Here ******')
    for account_number, user_details in database.items():
        # get current balance
        current_balance = user_details[4]
        # get amount to withdraw
        debit_amount = int(input('Amount To Withdraw? \n'))
        # check if current balance >= withdraw balance
        if current_balance >= debit_amount:
            current_balance = current_balance - debit_amount
            print('Transaction Successful! \n Take your cash %d' % debit_amount)
            print('Account Balance: NGN %d' % current_balance)
            print('Thank you for Banking with us')
        else:
            print('Insufficient Funds!, Check account balance and try again')
            bank_operations(user_details)
        # deduct withdrawn amount form current balance
        # display current balance


def generate_account_number():
    return random.randrange(1111111111, 9999999999)


def set_current_balance(user_details, balance):
    user_details[4] = balance


def get_current_balance(user_details):
    return user_details[4]


def logout():
    login()


init()
