list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
list_numbers.index(max(list_numbers)) #9
list_numbers.index(min(list_numbers)) #12
list_numbers[9], list_numbers[12] = list_numbers[12], list_numbers[9]
# TODO Оформить решение

print(list_numbers)
