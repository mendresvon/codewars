from collections.abc import Iterable;
from preloaded import Hand;
(NONE,LEFT,RIGHT,BOTH) = Hand;
​
def which_hand(word: Iterable[str]) -> Hand:
    left_char = set("qwertasdfgzxcvb")
    right_char = set("yuiophjklnm")
    seen_left = False
    seen_right = False
    
    for char in word:
        # check which hand
        if char in left_char:
            seen_left = True
        if char in right_char:
            seen_right = True
        
        # check if both hands have been seen
        if seen_left and seen_right:
            return BOTH
        
    if seen_left:
        return LEFT
    elif seen_right:
        return RIGHT
    else:
        return NONE