def calculate_years(principal, interest, tax, desired):
    years = 0
    curr_balance = principal
    
    while curr_balance < desired:
        total_interest = curr_balance * interest * (1.0 - tax)
        curr_balance += total_interest
        years += 1
    
    return years