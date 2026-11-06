from preloaded import DECK
​
def define_suit(card):
    d = {
        'C': 'clubs',
        'D': 'diamonds',
        'H': 'hearts',
        'S': 'spades',
    }
    return d[card[-1]]