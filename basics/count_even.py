def count_even(numbers):
    count = 0

    for number in numbers:
        if number % 2 == 0:
            count += 1

    return count


print(count_even([3, 8, 2, 5, 6]))