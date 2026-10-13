def twice_as_old(dad_years_old, son_years_old):
    years = 0
    if son_years_old * 2 > dad_years_old:
        while son_years_old * 2 > dad_years_old:
            son_years_old -= 1
            dad_years_old -= 1
            years += 1
    elif son_years_old * 2 < dad_years_old:
        while son_years_old * 2 < dad_years_old:
            son_years_old += 1
            dad_years_old += 1
            years += 1
    return years