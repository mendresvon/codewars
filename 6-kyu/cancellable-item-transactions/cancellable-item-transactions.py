from collections import defaultdict
def calculate(price_dict, transaction):
    history = defaultdict(list)
    total = 0
    i = 0
    n = len(transaction)
    
    while i < n:
        char = transaction[i]
        
        if char.isalpha(): # cancel last transaction
            if char in history and history[char]:
                to_remove = history[char].pop()
                total -= to_remove
​
        else: # add transaction
            sign = 1
            if char == '-':
                sign = -1
                i += 1
            
            j = i
            while i < n and transaction[i].isdigit():
                i += 1
            if i >= n:
                break
            
            qty = int(transaction[j:i])
            curr_total = qty * sign * price_dict[transaction[i]]
            total += curr_total
            
            history[transaction[i]].append(curr_total)
        
        i += 1
        
    return total