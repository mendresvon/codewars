from itertools import combinations
def choose_best_sum(t, k, ls):
    return max((sum(group) for group in combinations(ls, k) if sum(group) <= t), default=None)