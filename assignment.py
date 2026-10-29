def replace_value(values, index, new_value):
    values[index] = new_value
    

def find_first(values, target):
    for i in range(len(values)):
        if values[i] == target:
            return i
    return -1


def summarize(values):
    return min(values), max(values), sum(values)
    
    
days = int(input("Enter the number of days: "))

original = []
for _ in range(days):
    visits = int(input("Enter the number of website visits: "))
    original.append(visits)

updated = original[:]

index = int(input("Enter the index to correct: "))
new_visits = int(input("Enter the new number of visits: "))
replace_value(updated, index, new_visits)

target = int(input("Enter the number of visits to search for: "))
first_index = find_first(updated, target)
count = updated.count(target)

minimum, maxmimum, total = summarize(updated)

sorted_list = sorted(updated)

print(f"Original: {original}")
print(f"Updated: {updated}")
print(f"Sorted: {sorted_list}")
print(f"Minimum number of visits: {minimum}")
print(f"Maximum number of visits: {maxmimum}")
print(f"Total number of visits: {total}")
if first_index == -1:
    print("Target not found")
else:
    print(f"First matching index: {first_index}")
print(f"Matching values: {count}")