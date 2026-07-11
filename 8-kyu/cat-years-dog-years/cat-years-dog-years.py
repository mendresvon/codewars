def human_years_cat_years_dog_years(human_years):
    # Your code here
    dog_years = 0
    cat_years = 0
    for i in range(human_years):
        if i == 0:
            dog_years += 15
            cat_years += 15
        elif i == 1:
            dog_years += 9
            cat_years += 9
        else:
            dog_years += 5
            cat_years += 4
    return [human_years, cat_years, dog_years]