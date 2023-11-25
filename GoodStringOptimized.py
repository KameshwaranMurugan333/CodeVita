def calculate_distance(good_string, name):
    total_distance = 0
    previous_good_letter = good_string[0]

    for char in name:
        if char in good_string:
            # If the character is already in the good string, calculate distance accordingly
            total_distance += abs(ord(char) - ord(previous_good_letter))
        else:
            min_distance = float('inf')
            selected_good_letter = None

            for good_char in good_string:
                distance = abs(ord(char) - ord(good_char))

                if distance < min_distance or (distance == min_distance and ord(good_char) < ord(previous_good_letter)):
                    min_distance = distance
                    selected_good_letter = good_char

            total_distance += min_distance
            previous_good_letter = selected_good_letter

    return total_distance

# Input
good_string = "6*K4AQf]gpi"
name = "Nainika"

# Output
result = calculate_distance(good_string, name)
print(result)
