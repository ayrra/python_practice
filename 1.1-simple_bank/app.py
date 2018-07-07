from random import randint

#Still needs typechecking for inputs, but shows the logic of the program working with the classes.
#Breaking down prompts into methods would also improve usability with invalid inputs. 

class Bank:
    list_of_accounts = []

    def addAccount(self, account):
        self.list_of_accounts.append(account)

    def login(self, id, name):
        for acc in self.list_of_accounts:
            if int(id) == acc.returnId() and name == acc.name:
                return acc
            else:
                pass
        return None

class Account:
    def __init__(self, name, deposit):
        self.name = name
        self.balance = deposit
        self.__id = None
    
    def setId(self, id):
        self.__id = id

    def returnId(self):
        return self.__id

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Deposit Successful!")
        print("New Balance is: " + str(self.balance))

    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient Funds!")
        else:
            self.balance = self.balance - amount
            print("Withdraw Successful!\nNew Balance is: " + str(self.balance))

    def print_account_info(self):
        print("Saving Account Number is: " + str(self.__id))
        print("Account name: " + self.name)
        print("Current Balance: " + str(self.balance)+"\n")
       


def initial_prompt():
    prompt = input("Welcome to the banking app!\nPress 1 to create a new savings account.\nPress 2 to access an existing savings account.\nPress 3 to exit.\n")
    if prompt is "1":
        print("Creating new savings account!")
        in_name = input("Please enter your full name: ")
        in_amount = input("Please enter how much you would like to deposit: ")
        new_acc = Account(in_name, int(in_amount))
        new_acc.setId(randint(10000,99999))
        bank.addAccount(new_acc)
        print("Account added!")
        new_acc.print_account_info()
        initial_prompt()
    elif prompt is "2":
        auth_id = input("Please enter savings account number: ")
        auth_name = input("Please enter the name for the account: ")
        loaded_account = bank.login(auth_id, auth_name)
        if loaded_account != None:
            loaded_account.print_account_info()
            prompt_loaded_account = input("Press 1 to deposit\nPress 2 to withdraw: ")
            if prompt_loaded_account is "1":
                deposit_amount = input("Please enter how much you would like to deposit: ")
                loaded_account.deposit(int(deposit_amount))
                initial_prompt()
            elif prompt_loaded_account is "2":
                withdraw_amount = input("Please enter how much you would like to withdraw: ")
                loaded_account.withdraw(int(withdraw_amount))
                initial_prompt()
            else:
                print("Invalid Response")
                initial_prompt()
        else:
            print("Account does not exist or incorrect credentials!\n")
            initial_prompt()
    elif prompt is "3":
        print("Exiting App!\nThanks for using the banking app!")
        exit()
    else:
        print("invalid input")
        initial_prompt()

bank = Bank()
initial_prompt()