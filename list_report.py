items = ["bread", "avocado", "milk", "sweet potatoes", "tea"]

# Print each item with a number
number = 1
for item in items:
    print(f"{number}. {item}")
    number += 1

# Count items with more than 4 letters
count = 0
for item in items:
    if len(item) > 4:
        count += 1

print(f"\nItems with more than 4 letters: {count}")

# Find the longest item
longest = items[0]

for item in items:
    if len(item) > len(longest):
        longest = item

print(f"Longest item: {longest}")