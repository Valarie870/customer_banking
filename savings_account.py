"""Import the Account class from the Accounts.py file."""
# import Account.py 
from Accounts import Account

#Create instance of Account
my_account = Account(balance=1000, interest=0.05)
print(f"Initial balance: ${my_account.balance}")
print(f"Interest rate: {my_account.interest * 100}%")

#Update the balance and interest
my_account.set_balance(1500)
my_account.set_interest(0.07)
print(f"Updated balance: ${my_account.balance}")
print(f"Updated interest rate: {my_account.interest * 100}%")

# Define a function for the Savings Account
def create_savings_account(balance, interest_rate, months):
    """Creates a savings account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.

    Returns:
        float: The updated savings account balance after adding the interest earned.
        And returns the interest earned.
    """
    #create an instance of SavingsAccount
    savings_account = Account(balance, 0)

    #Calcuate the interest earned
    interest_earned = balance * (interest_rate / 100) * (months / 12)

    #Update the account balance with the interest earned
    updated_balance = balance + interest_earned

    #Pass updated balance to the set_balance method using the instance of the Account class
    savings_account.set_balance(updated_balance)

    #Pass interest earned to the set_interest method using the instance of the Account class
    savings_account.set_interest(interest_earned)
    
    #Return the updated balance and interest earned
    return updated_balance, interest_earned

    #Using
    initial_balance = 1000.0
    annual_interest_rate = 5.0
    savings_period = 6

    updated_balance, interest = create_savings_account(initial_balance, annual_interest_rate, savings_period)
    print(f"Updated Balance: ${updated_balance:.2f}")
    print(f"Interest Earned: ${interest:.2f}")



    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    # ADD YOUR CODE HERE

    # Calculate interest earned
     # ADD YOUR CODE HERE

    # Update the savings account balance by adding the interest earned
    # ADD YOUR CODE HERE

    # Pass the updated_balance to the set balance method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE

    # Pass the interest_earned to the set interest method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE

    # Return the updated balance and interest earned.
    return  # ADD YOUR CODE HERE
