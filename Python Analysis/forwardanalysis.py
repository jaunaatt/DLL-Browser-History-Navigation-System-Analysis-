import sys
import time
import matplotlib.pyplot as plt

# Increase recursion limit to handle the deep recursion in the "Worst Case" test
sys.setrecursionlimit(10000)

class NodeDLL:
    def __init__(self, id_val):
        self.id = id_val
        self.next = None
        self.prev = None

class HistoryDLL:
    def __init__(self):
        self.head = None
        self.current = None

    # Helper to build the list
    def add_page(self, id_val):
        new_node = NodeDLL(id_val)
        if not self.head:
            self.head = new_node
            self.current = new_node
        else:
            # Add to the end
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node
            new_node.prev = curr
            # We don't move self.current here so we can control it manually later

    # --- MATCHING YOUR C++ LOGIC: ITERATIVE ---
    # void goForwardIterative(int steps) { ... }
    def go_forward_iterative(self, steps):
        while steps > 0 and self.current.next is not None:
            self.current = self.current.next
            steps -= 1

    # --- MATCHING YOUR C++ LOGIC: RECURSIVE ---
    # void goForwardRecursive(int steps) { ... }
    def go_forward_recursive(self, steps):
        # Base case: steps is 0 or we are at the end
        if steps == 0 or self.current.next is None:
            return
        
        self.current = self.current.next
        self.go_forward_recursive(steps - 1)

    # --- HELPER FOR BENCHMARKING ---
    # To test "Forward", we must start at the HEAD (Beginning)
    def reset_to_head(self):
        self.current = self.head

# --- BENCHMARKING SETUP ---

# 1. Prepare Data
# We need a list larger than the maximum steps we plan to test.
max_steps = 2500
dll = HistoryDLL()
print(f"Populating DLL with {max_steps} nodes...")
for i in range(max_steps):
    dll.add_page(i)

# 2. Define Input Sizes (Number of steps to go forward)
step_values = range(10, 2000, 50)
time_iterative = []
time_recursive = []

print("Starting benchmark...")

for n in step_values:
    # --- Measure Iterative ---
    dll.reset_to_head() # Reset to start so we can move forward
    
    start = time.perf_counter()
    dll.go_forward_iterative(n)
    end = time.perf_counter()
    time_iterative.append(end - start)

    # --- Measure Recursive ---
    dll.reset_to_head() # Reset to start so we can move forward
    
    start = time.perf_counter()
    try:
        dll.go_forward_recursive(n)
    except RecursionError:
        print(f"Recursion limit hit at n={n}")
        break 
    end = time.perf_counter()
    time_recursive.append(end - start)

# --- PLOTTING ---
plt.figure(figsize=(10, 6))

# Plot Recursive
plt.plot(step_values, time_recursive, label='Recursive Forward (O(N) Stack)', color='red', linestyle='-', marker='o', markersize=3)
# Plot Iterative
plt.plot(step_values, time_iterative, label='Iterative Forward (O(1) Stack)', color='blue', linestyle='-', marker='x', markersize=3)

plt.title('Performance Comparison: DLL Forward Traversal')
plt.xlabel('Number of Steps (n)')
plt.ylabel('Execution Time (seconds)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()

# Save and Show
plt.savefig('dll_forward_benchmark.png')
print("Benchmark complete. Image saved as 'dll_forward_benchmark.png'.")
plt.show()