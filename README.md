# Design and Analysis of Algorithms – Practical Work

This repository contains all six laboratory experiments completed as part of the **Design and Analysis of Algorithms (DAA)** course.  
Each experiment includes problem definition, algorithm explanation, Python implementation, sample outputs, and time/space complexity analysis.

---

## ✅ Completed Experiments

### 1️⃣ Binary Search – Library Book Finder
- Problem: Search for a book in a sorted list efficiently  
- Algorithm Type: Divide and Conquer  
- Approach: Iterative Binary Search  
- Key Concept: Mid-element comparison, reducing search space  
- Complexity:  
  - Time: `O(log n)`  
  - Space: `O(1)`  
- Folder: `/Experiment 01-Binary Search`

---

### 2️⃣ Quick Sort & Merge Sort – Student Marks Sorter
- Problem: Sort student records by marks  
- Approach:  
  - **Quick Sort** (in-place, divide & conquer)  
  - **Merge Sort** (stable, divide & conquer)  
- Complexity:  
  - Quick Sort: Best/Avg `O(n log n)`, Worst `O(n²)`, Space `O(log n)`  
  - Merge Sort: Always `O(n log n)`, Space `O(n)`  
- Folder: `/Experiment 02 - Sorting`

---

### 3️⃣ Greedy Method – Project Resource Allocation (Knapsack)
- Problem: Maximize profit with limited project resources  
- Algorithm: Greedy Fractional-Knapsack approach  
- Decision Rule: Profit-to-Resource ratio  
- Complexity:  
  - Time: `O(n log n)`  
  - Space: `O(n)`    
- Folder: `/Experiment 03 - Knapsack`

---

### 4️⃣ Optimal Merge Pattern - File Compression system
- Problem : Minimize total cost when merging multiple files into a single file during compression.
- Algorithm : Greedy — Optimal Merge Pattern using a Min-Heap.
- Decision Rule : Always merge the two smallest files first (lowest sizes → minimum incremental merge cost).
- Complexity:
- Time: O(n log n) due to heap operations for repeated extract-min and insert
- Space: O(n) for heap storage
- Folder: `/Experiment 04 - OptimalMerge`

---

### 5️⃣ MST – Campus Network Design System
- Problem : Connect all campus buildings with network cables at the minimum total cost while ensuring every building is reachable.
- Algorithm : Minimum Cost Spanning Tree using Prim's and Kruskal's algorithms.
- Decision Rule:
- Prim's : Always expand the network by choosing the lowest-weight edge from visited to unvisited nodes.
- Kruskal's: Always add the smallest-weight edge that does not create a cycle (using union-find to check).
- Complexity:
  - Time:
     - Prim’s (array implementation): O(V^2)
     - Kruskal’s: O(E log E) for sorting edges
  - Space: O(V + E) for adjacency / edge list and union-find structures 
- Folder: `/Experiment 05 - MST`

---

### 6️⃣ Dijkstra Algorithm - City Navigation System
- Problem : Find the most efficient routes between city locations based on either minimum distance or minimum travel time.
- Algorithm : Dijkstra’s Single-Source Shortest Path algorithm using a min-priority queue (min-heap).
- Decision Rule:
At each step, always expand the unvisited location with the current smallest cumulative cost (distance or time), updating neighbors only if a shorter route is found.
- Complexity:
   - Time: O((V + E) log V) using a heap
   - Space: O(V + E) for adjacency list, distance array, and priority queue
- Folder: `/Experiment 06 - Dijkstra`

---

## 📂 Repository Structure

DAA-Practicals/
│── Experiment 01-BinarySearch/
│── Experiment 02 - Sorting/
│── Experiment 03 - Knapsack/
│── Experiment 04 - OptimalMerge/
│── Experiment 05 - MST/
│── Experiment 06 - Dijkstra/
└── README.md <-- (this file)

## 🧪 How to Run Programs
## Requirements:
- Python 3.x or newer version installed

### Steps to Run:
1. Navigate to the specific experiment folder :
   cd Experiment 01 - BinarySearch
2. Run the Python program :
   python app.py

## 🎯 Learning Outcomes

Mastered major algorithmic techniques:

- Divide & Conquer

- Recursion

- Greedy Method

- Backtracking

- Dynamic Programming

- Analyzed algorithm complexities

- Built real-world analogy based models (book search, student sorting, project allocation)



## 👤 Author

- Name: Sakshi Shahaji Chougale
- Roll No : 25143071   
- Class : SYIT(Batch-I4)
- Course: Information Technology
- Subject: Design and Analysis of Algorithms


