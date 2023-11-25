import threading

def find_valency(an):
    return (an - 1) % 9 + 1 if an > 0 else 0

def check_combination(results, i, equivalent_point, valency_of_first_component, valency_of_second_component):
    x = i * valency_of_first_component
    y = equivalent_point - x

    if y > 0 and y % valency_of_second_component == 0:
        results.append((i, y // valency_of_second_component))

def find_combinations_threaded(equivalent_point, valency_of_first_component, valency_of_second_component):
    results = []
    threads = []

    for i in range(equivalent_point, 0, -1):
        thread = threading.Thread(target=check_combination, args=(results, i, equivalent_point, valency_of_first_component, valency_of_second_component))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    return results

# Getting the input
non_balanced_component = input()
equivalent_point = int(input())
ascii_of_first_component = ord(non_balanced_component[0])
ascii_of_second_component = ord(non_balanced_component[1])
valency_of_first_component = find_valency(ascii_of_first_component)
valency_of_second_component = find_valency(ascii_of_second_component)

combinations = find_combinations_threaded(equivalent_point, valency_of_first_component, valency_of_second_component)

if not combinations:
    print("Not Possible")
else:
    for first, sec in combinations:
        print(f"{non_balanced_component[0]}{first} {non_balanced_component[1]}{sec}")
