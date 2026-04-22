def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    square_root = sq ** (1/2)
    if square_root % 1 != 0:
        return -1
    else:
        return (square_root + 1) ** 2