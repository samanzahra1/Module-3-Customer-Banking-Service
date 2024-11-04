# Import the create_cd_account and create_savings_account functions
from cd_account import create_cd_account


from savings_account import create_savings_account


# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    savings_account_balance = input("what is your current savings account balance?")
    savings_account_interest_rate = input("what is the interest rate on your account")
    savings_account_months =input("whats the time in months")

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_account_balance, savings_account_interest_rate, savings_account_months)
    updated_savings_balance.set_balance()
    interest_earned.set_interest()
    

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    #print() with f string - need # value that is returned from function here.
    print(f"total interest earned on the savings account is ${interest_earned:.2f}. ")  
    print(f"total savings ammount is ${updated_savings_balance:.2f}. ")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    cd_account_balance = input("what is your current savings cd balance?")
    cd_account_interest = input("what is the interest rate on your cd")
    cd_account_months =input("whats the time in months")

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_account_balance, cd_account_interest, cd_account_months)
    updated_cd_balance.set_balance()
    interest_earned.set_interest() 

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    #print() with f string - need # value that is returned from function here.
    print(f"total interest earned for CD is ${cd_account_interest:2f}.")  
    print(f"total balance for CD is ${updated_cd_balance:2f}.")

if __name__ == "__main__":
    main()