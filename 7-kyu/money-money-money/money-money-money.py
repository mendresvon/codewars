def calculate_years(principal, interest, tax, desired):
    balance = principal
    years = 0
    
    while balance < desired:
        yearly_interest = balance * (interest * (1-tax))
        balance += yearly_interest
        years += 1
    
    return years