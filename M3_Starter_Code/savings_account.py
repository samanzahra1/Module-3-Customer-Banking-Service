"""Import the Account class from the Account.py file."""
from Account import Account

# Define a function for the Savings Account
class Account: 
    def create_savings_account(self,balance, interest_rate, months, updated_balance):
        self.balance = balance
        self.interest_rate = interest_rate
        self.months = months
        self.updated_balance = updated_balance

    """Creates a savings account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.

    Returns:
        float: The updated savings account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0. (???) 
    def __init__ (self, balance, interest_rate, months):
        self.balance = float(balance)
        self.interest_rate = (float)(interest_rate)
        self.months = months


    # Calculate interest earned
    interest_earned = months * interest_rate

    # Update the savings account balance by adding the interest earned
    # ADD YOUR CODE HERE
    updated_balance = balance + interest_earned

    # Pass the updated_balance to the set balance method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE
    create_savings_account(updated_balance)


    # Pass the interest_earned to the set interest method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE
    class Account: 
       def create_savings_account(self, balance, interest_rate, months, updated_balance):
           self.balance = balance
           self.interest_rate = interest_rate
           self.months = months
           self.updated_balance = updated_balance

    # Return the updated balance and interest earned.
    return updated_balance, interest_earned