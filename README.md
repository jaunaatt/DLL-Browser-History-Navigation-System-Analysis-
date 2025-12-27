# DLL-Browser-History-Navigation-System-Analysis-
# Browser History Navigation System: Algorithmic Analysis

This project focuses on finding the most efficient approach for implementing a Browser History Navigation System. It involves a comparative analysis of **Singly Linked Lists (SLL)** vs. **Doubly Linked Lists (DLL)** and **Iterative** vs. **Recursive** implementation techniques.

The primary goal is to quantify performance differences to determine the optimal configuration for a responsive user experience.

## 📖 Table of Contents
- [Abstract](#abstract)
- [Methodology](#methodology)
- [Algorithmic Analysis](#algorithmic-analysis)
  - [Time Complexity Derivation](#time-complexity-derivation)
  - [Space Complexity](#space-complexity)
- [Performance Visualization](#performance-visualization)
- [Conclusion](#conclusion)

---

## Abstract
Modern web browsers require frequent operations such as loading new pages, deleting entries, and navigating bidirectionally (Back/Forward). This project analyzes the efficiency of these implementations by determining their theoretical Time Complexity classes (Big-O) and measuring empirical running times across various input sizes.

## Methodology
The algorithms are implemented in **C++** to ensure direct control over memory management and accurate performance measurement. The simulation focuses on two key procedures:
1.  **GoBack(steps):** Moves the current pointer to previous nodes.
2.  **GoForward(steps):** Moves the current pointer to next nodes.

---

## Algorithmic Analysis

### Time Complexity Derivation
We analyzed the theoretical running time $T(n)$ for moving $n$ steps in both directions.

#### Iterative Approach (Back & Forward)
For the iterative approach, we perform constant work inside a loop that runs $n$ times.
* **Recurrence Relation:** $T(n) = T(n-1) + c$ for $n > 0$
* **Base Case:** $T(0) = c_0$

Expanding the relation:
$$T(n) = T(n-1) + c$$
$$T(n) = (T(n-2) + c) + c = T(n-2) + 2c$$
$$...$$
$$T(n) = T(0) + n \cdot c$$

Since $c_0$ and $c$ are constants:
$$T(n) \approx c \cdot n \Rightarrow O(n)$$

#### Recursive Approach (Back & Forward)
The recursive function calls itself $n$ times until the base case (steps = 0) is reached.
* **Recurrence Relation:** $T(n) = T(n-1) + c$
* **Base Case:** $T(0) = c_{base}$

This yields the same linear time complexity:
$$T(n) \in O(n)$$

### Space Complexity
The critical distinction lies here:
* **Iterative:** Operates with **$O(1)$ constant space**. It requires a fixed amount of memory for a single pointer and a counter variable.
* **Recursive:** Operates with **$O(n)$ linear space**. It relies on the system call stack, creating a new stack frame for every step taken.

---

## Performance Visualization

We measured the actual execution time (in seconds) against the number of steps ($n$) using python.

### 1. GoBack Operation
The graph below compares the iterative and recursive implementations for the backward navigation. As predicted, the recursive approach incurs higher overhead due to stack frame allocation.

![DLL Backward Complexity Graph](DLL%20backward%20graph.png)

### 2. GoForward Operation
Similarly, the forward navigation demonstrates that while both are linear ($O(n)$), the iterative approach consistently outperforms the recursive one in raw speed.

![DLL Forward Complexity Graph](DLL%20forward%20graph.png)

---

## Conclusion
Based on the comparative analysis:
1.  **Time Complexity:** Both approaches differ negligibly in theoretical Big-O ($O(n)$), but empirically, the **Iterative** approach is faster due to the lack of function call overhead.
2.  **Space Complexity:** The **Iterative** approach is superior ($O(1)$ vs $O(n)$). The Recursive approach risks a **Stack Overflow** error if a user navigates back thousands of pages in a single session.

**Recommendation:** The **Iterative Doubly Linked List** is the optimal choice for a Browser History Navigation System.

---
