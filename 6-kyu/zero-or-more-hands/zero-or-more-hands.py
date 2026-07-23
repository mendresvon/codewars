from collections.abc import Iterable;
from preloaded import Hand;
(NONE,LEFT,RIGHT,BOTH) = Hand;
​
def which_hand(word: Iterable[str]) -> Hand:
    left_chars = set("qwertasdfgzxcvb")
    right_chars = set("yuiophjklnm")
    
    left_used = False
    right_used = False
    
    for char in word:
        if char in left_chars:
            left_used = True
        elif char in right_chars:
            right_used = True
        
        if left_used and right_used:
            return BOTH
    
    return LEFT if left_used else RIGHT if right_used else NONE