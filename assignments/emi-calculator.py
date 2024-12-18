#function for oan EMI or Month installement

def loan_emi(amount, duration, rate, down_payment=0):
    """
    Calculate the monthly EMI for a loan.

    Parameters:
    - amount: Total loan amount.
    - duration: Loan duration in months.
    - rate: Annual interest rate as a decimal (e.g., 10% = 0.10).
    - down_payment: Down payment amount (default is 0).

    Returns:
    - Monthly EMI rounded to 2 decimal places.
    """
    loan_amount = amount - down_payment  # Subtract down payment
    monthly_rate = rate / 12  # Convert annual rate to monthly rate
    
    if monthly_rate == 0:  # Handle zero-interest loans
        emi = loan_amount / duration
    else:
        emi = loan_amount * monthly_rate * ((1 + monthly_rate) ** duration) / \
              (((1 + monthly_rate) ** duration) - 1)
    
    return round(emi, 2)
