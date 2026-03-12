def average_age(csv_string):
    lines = csv_string.strip().split("\n")
    ages = []
    for line in lines[1:]:
        parts = line.split(",")
        ages.append(int(parts[1]))
    if len(ages) == 0:
        return 0.0
    else:
        return sum(ages)/len(ages)

# Sample CSV string
csv_data = "name,age\nAlice,30\nBob,25\nCharlie,35"

result = average_age(csv_data)
print(result)
