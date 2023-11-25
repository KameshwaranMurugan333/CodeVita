def find_valency(an):
    return (an - 1) % 9 + 1 if an > 0 else 0

def find_combinations(non_balanced_component, equivalent_point):
    first_component = non_balanced_component[0]
    second_component = non_balanced_component[1]

    ascii_of_first_component = ord(first_component)
    ascii_of_second_component = ord(second_component)

    valency_of_first_component = find_valency(ascii_of_first_component)
    valency_of_second_component = find_valency(ascii_of_second_component)

    results = []

    for i in range(equivalent_point, 0, -1):
        x = i * valency_of_first_component
        y = equivalent_point - x

        if y > 0 and y % valency_of_second_component == 0:
            results.append((i, y // valency_of_second_component))

    return results

# Getting the input
non_balanced_component = input()
equivalent_point = int(input())

combinations = find_combinations(non_balanced_component, equivalent_point)

if not combinations:
    print("Not Possible")
else:
    for i, (first, sec) in enumerate(combinations):
        print(f"{non_balanced_component[0]}{first} {non_balanced_component[1]}{sec}")
