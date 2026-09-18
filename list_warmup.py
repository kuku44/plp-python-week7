# fruits list containing four fruits 
fruits = ['apple', 'banana', 'cherry', 'date']

# Print the first and the last item using indexes
print("first fruit:", fruits[0])
print("last fruit:", fruits[-1])

# .append() a fifth fruit, then print the whole list

fruits.append('watermelon')
print('after adding a fifth fruit:', fruits)

# .remove() one fruit, then print the list again

fruits.remove('cherry')
print('after removing one fruit:', fruits)

# Print how many fruits remain

print('how many fruits remain:', len(fruits))




