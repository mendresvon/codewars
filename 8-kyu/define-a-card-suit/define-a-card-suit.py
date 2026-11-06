from preloaded import DECK
​
def define_suit(card):
    match card[-1]:
        case 'C':
            return "clubs"
        case 'D':
            return "diamonds"
        case 'H':
            return "hearts"
        case 'S':
            return "spades"