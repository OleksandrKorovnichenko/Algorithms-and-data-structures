import time
import random
from practical_work_3.structureexamples import StructureExample, ArrayParts, ArrayWithoutListMethods


def object_generator(n: int):
    for _ in range(n):
        yield random.randint(1, 100)


# Creating instances of data structures with the object generator
start_time = time.time()
example_structex = StructureExample(object_generator(10000))
print(f"StructureExample creation time: {time.time() - start_time} seconds")

start_time = time.time()
example_struct = ArrayParts(object_generator(10000))
print(f"ArrayParts creation time: {time.time() - start_time} seconds")

start_time = time.time()
example_struct = ArrayWithoutListMethods(object_generator(10000))
print(f"ArrayWithoutListMethods creation time: {time.time() - start_time} seconds")

# Clear or recreate the structure and measure the speed of appending at the end
start_time = time.time()
example_structex.clear()  # Assuming clear() method is available in your structure class
example_struct = StructureExample(object_generator(10000))
print(f"Cleared and recreated the structure in: {time.time() - start_time} seconds")

# Measure appending speed for the recreated structure
start_time = time.time()
for _ in range(10000):
    example_struct.append(random.randint(1, 100))  # Assuming append() method is available in your structure class
print(f"Appending time for the recreated structure: {time.time() - start_time} seconds")

# Reset the object at index 5000
index_to_change = 5000
new_value = next(object_generator(1))  # Get the first value from the generator

start_time = time.time()
example_struct[index_to_change] = new_value
print(f"Changed object at index {index_to_change} in: {time.time() - start_time} seconds")

# Change all elements sequentially
start_time = time.time()
for i in range(len(example_struct)):
    example_struct[i] = next(object_generator(1))  # Change each element to the next value from the generator
print(f"Changed all elements sequentially in: {time.time() - start_time} seconds")

# Search for the first object
start_time = time.time()
first_object = example_struct[0]
print(f"Found first object in: {time.time() - start_time} seconds")

# Search for the last object
start_time = time.time()
last_object = example_struct[-1]
print(f"Found last object in: {time.time() - start_time} seconds")

# Calculate the index for the middle object
middle_index = len(example_struct) // 2
middle_object = example_struct[middle_index]

# Search for the middle object
start_time = time.time()
print(f"Found middle object in: {time.time() - start_time} seconds")

# Access object at specified index
index_to_access = 5000  # Change this to the index you want to access

start_time = time.time()
object_at_index = example_struct[index_to_access]
print(f"Accessed object at index {index_to_access} in: {time.time() - start_time} seconds")

# Remove element from the beginning
start_time = time.time()
removed_from_beginning = example_struct.pop(0)
print(f"Removed element from the beginning in: {time.time() - start_time} seconds")

# Remove element from the end
start_time = time.time()
removed_from_end = example_struct.pop()
print(f"Removed element from the end in: {time.time() - start_time} seconds")
