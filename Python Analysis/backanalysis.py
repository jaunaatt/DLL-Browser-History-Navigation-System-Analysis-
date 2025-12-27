import sys
import time
import matplotlib.pyplot as plt
import numpy as np

# Increase recursion limit for deep recursion tests
sys.setrecursionlimit(10000)

# --- YOUR DLL CLASSES ---
class NodeDLL:
    def __init__(self, id_val):
        self.id = id_val
        self.next = None
        self.prev = None

class HistoryDLL:
    def __init__(self):
        self.head = None
        self.current = None

    def add_page(self, id_val):
        new_node = NodeDLL(id_val)
        
        if not self.head:
            self.head = new_node
            self.current = new_node
        else:
            # Connect current node to new node
            self.current.next = new_node
            new_node.prev = self.current
            # Move current pointer to the new node
            self.current = new_node

    # --- DLL: Iterative Back ---
    def back_iterative(self, steps):
        while steps > 0 and self.current.prev is not None:
            self.current = self.current.prev
            steps -= 1

    # --- DLL: Recursive Back ---
    def back_recursive(self, steps):
        # Base case: no steps left or reached the beginning
        if steps == 0 or self.current.prev is None:
            return
        
        self.current = self.current.prev
        self.back_recursive(steps - 1)

    # Helper to reset pointer to end so we can re-test
    def reset_to_end(self):
        while self.current.next is not None:
            self.current = self.current.next

# --- BENCHMARKING SETUP ---

# 1. Prepare the Data Structure
# We need a DLL large enough to support the maximum steps we want to test.
# If we test up to 2000 steps, we need at least 2000 nodes.
max_steps = 2500
dll = HistoryDLL()
print(f"Populating DLL with {max_steps} nodes...")
for i in range(max_steps):
    dll.add_page(i)

# 2. Define Input Sizes (Number of steps to go back)
# We test going back 10 steps, then 60, ..., up to 2000.
step_values = range(10, 2000, 50)
time_iterative = []
time_recursive = []

print("Starting benchmark...")

for n in step_values:
    # --- Measure Iterative ---
    # Important: Reset pointer to the end before the test
    dll.reset_to_end() 
    
    start = time.perf_counter()
    dll.back_iterative(n)
    end = time.perf_counter()
    time_iterative.append(end - start)

    # --- Measure Recursive ---
    # Important: Reset pointer to the end before the test
    dll.reset_to_end()
    
    start = time.perf_counter()
    try:
        dll.back_recursive(n)
    except RecursionError:
        print(f"Recursion limit hit at n={n}")
        break 
    end = time.perf_counter()
    time_recursive.append(end - start)

# --- PLOTTING ---
plt.figure(figsize=(10, 6))

# Plot Recursive
plt.plot(step_values, time_recursive, label='Recursive Back (Actual Time)', color='red', alpha=0.7)
# Plot Iterative
plt.plot(step_values, time_iterative, label='Iterative Back (Actual Time)', color='blue', alpha=0.7)

plt.title('Time Complexity: DLL Back Operation (Iterative vs Recursive)')
plt.xlabel('Number of Steps Back (n)')
plt.ylabel('Execution Time (seconds)')
plt.legend()
plt.grid(True)
plt.tight_layout()

# Save the plot
plt.savefig('dll_benchmark_comparison.png')
print("Benchmark complete. Image saved as 'dll_benchmark_comparison.png'.")
plt.show()