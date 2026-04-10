from collections import defaultdict
def calculate(price_dict, transaction):
    history = defaultdict(list)
    i = 0
    n = len(transaction)
    total = 0
    
    while i < n:
        if transaction[i].isalpha(): #cancel case
            # check if curr_letter is in history and remove if so
            if history[transaction[i]]:
                to_remove = history[transaction[i]].pop()
                total -= to_remove
        else: #add case
            # check for negative sign
            sign = 1
            if transaction[i] == '-':
                sign = -1
                i += 1
                
            # check for multiple-digit num
            j = i
            while transaction[i].isdigit():
                i += 1
            
            # check if trailing number
            if i >= n:
                break
            
            # add price to history and total
            qty = int(transaction[j:i])
            curr_char = transaction[i]
            curr_total = qty * price_dict[curr_char] * sign
            history[curr_char].append(curr_total)
            total += curr_total
        i += 1
    
    return total