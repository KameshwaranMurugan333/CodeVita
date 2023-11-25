def get_ascii_values(input_string):
    ascii_values = [ord(char) for char in input_string]
    return ascii_values

def find_nearest_numbers(target, number_array):
    closest_numbers = []
    min_difference = float('inf')

    for number in number_array:
        difference = abs(target - number)
        
        if difference < min_difference:
            # Found a new minimum difference, update the list
            min_difference = difference
            closest_numbers = [number]
        elif difference == min_difference:
            # Found another number with the same minimum difference
            closest_numbers.append(number)

    return closest_numbers


# Getting the input
good_string = input()
student_name = input()

ascci_good_string = get_ascii_values(good_string)
ascci_student_name = get_ascii_values(student_name)

distanceArr = []

for index, ascii_value in enumerate(ascci_student_name):
    current_good_letter = find_nearest_numbers(ascii_value,ascci_good_string)
    if len(current_good_letter) == 1:
        distanceArr.append(abs(ascii_value - current_good_letter.pop()))

print(sum(distanceArr))