def load_data(file_path):
    with open(file_path, 'r') as f:
        data = [line.strip().split() for line in f.readlines()]
    return data
def calculate_attribute_values(data):
    num_attributes = len(data[0]) - 1  # Zakładamy, że ostatnia kolumna to atrybut decyzyjny
    attribute_values = {i: set() for i in range(num_attributes)}  # Zbiór unikalnych wartości dla każdego atrybutu

    for record in data:
        for i in range(num_attributes):
            attribute_values[i].add(record[i])

    return attribute_values


def count_attribute_occurrences(data):
    num_attributes = len(data[0]) - 1
    occurrences = {i: {} for i in
                   range(num_attributes)}  # Słownik dla każdego atrybutu, który przechowuje liczby wystąpień

    for record in data:
        for i in range(num_attributes):
            value = record[i]
            if value in occurrences[i]:
                occurrences[i][value] += 1
            else:
                occurrences[i][value] = 1

    return occurrences

file_path = 'data.txt'
data = load_data(file_path)

attribute_values = calculate_attribute_values(data)
occurrences = count_attribute_occurrences(data)

print("Attribute Values:", attribute_values)
print("Occurrences:", occurrences)
