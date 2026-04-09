from collections import defaultdict
def calculate(price_dict, transaction):
    history = defaultdict(list)
    total = 0
    i = 0
    
    while i < len(transaction):
        char = transaction[i]
        
        # cancel case
        if char.isalpha():
            if char in history and history[char]:
                to_remove = history[char].pop()
                total -= to_remove
            i += 1
            continue
                
        else: # not cancel case
            sign = 1
            # if char is '-' sign, set sign to negative and move i forward
            if char == '-':
                sign = -1
                i += 1
            
            # keep moving until we arrive at a letter
            j = i
            while i < len(transaction) and transaction[i].isdigit():
                i += 1
            
            if i >= len(transaction):
                break
            
            curr_char = transaction[i]
            qty = int(transaction[j:i])
            curr_total = qty * sign * price_dict[curr_char]
            history[curr_char].append(curr_total)
            total += curr_total
            i += 1
        
    return total