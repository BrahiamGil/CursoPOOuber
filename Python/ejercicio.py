def is_leap(year):
    leap = False

    # Write your logic here
    for i in year:
        number = i % 4 == 0
        print(number)
    return leap, number



year = int(input())
print(is_leap(year))


