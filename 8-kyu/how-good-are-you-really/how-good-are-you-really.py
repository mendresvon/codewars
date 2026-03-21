def better_than_average(class_points, your_points):
    # Your code here
    student_count = len(class_points)
    total = 0
    for num in class_points:
        total += num
    avg = total / student_count
    return True if your_points > avg else False