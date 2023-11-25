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

# Example usage:
numbers_array = [80, 78, 12, 123, 212]
target_number = 77

nearest_numbers = find_nearest_numbers(target_number, numbers_array)

print(f"The nearest numbers to {target_number} in the array are: {nearest_numbers}")
