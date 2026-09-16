def stairs_in_20(stairs):
    year = sum(sum(stair) for stair in stairs)
    return year * 20