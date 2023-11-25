def get_ascii_values(input_string):
    ascii_values = [ord(char) for char in input_string]
    return ascii_values

value = "(@HR*i{kcQl"
anotherValue = "6*K4AQf]gpi"

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
numbers_array = get_ascii_values(anotherValue)
print(numbers_array)
target_number = 78

nearest_numbers = find_nearest_numbers(target_number, numbers_array)
nearest_numbers = find_nearest_numbers(54, numbers_array)

print(f"The nearest numbers to {target_number} in the array are: {nearest_numbers}")

numbers = [1, 2, 2, 3, 4, 4, 5]

unique_numbers = list(set(numbers))

print("Original List:", numbers)
print("List with Duplicates Removed:", unique_numbers)
