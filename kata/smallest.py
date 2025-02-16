def smallest(numbers):
    smallest_num = 0

    for number in numbers:
        if number < smallest_num:
            smallest_num = number
    smallest_num = sorted(numbers)[0]
    return smallest_num
