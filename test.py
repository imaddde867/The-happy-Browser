import numpy as np
import matplotlib.pyplot as plt
import time

# Generate matrices of increasing sizes for time complexity analysis
sizes = [10, 100, 500, 1000, 2000, 5000]
times_task1 = []
times_task2 = []
times_task3 = []

for size in sizes:
    # Generate a random matrix of the given size
    matrix = np.random.randint(0, 100, (size, size))

    # Task 1: Print the element at (0,0)
    start = time.time()
    element = matrix[0][0]
    times_task1.append(time.time() - start)

    # Task 2: Double the first row
    start = time.time()
    matrix[0, :] *= 2
    times_task2.append(time.time() - start)

    # Task 3: Double the entire matrix
    start = time.time()
    matrix *= 2
    times_task3.append(time.time() - start)

# Plotting the results
plt.plot(sizes, times_task1, label="Task 1: Print element at (0,0)")
plt.plot(sizes, times_task2, label="Task 2: Double first row")
plt.plot(sizes, times_task3, label="Task 3: Double entire matrix")

plt.xlabel("Matrix size (n x n)")
plt.ylabel("Time (seconds)")
plt.title("Empirical Time Complexity of Matrix Operations")
plt.legend()
plt.show()
