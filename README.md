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
- Folder: `/Experiment01_BinarySearch`

---

### 2️⃣ Recursion – Factorial & Fibonacci
- Problem: Demonstrate recursive function behavior  
- Algorithm Type: Recursive  
- Key Concept: Stack frames, base & recursive cases  
- Complexity:  
  - Factorial: Time `O(n)` | Space `O(n)`  
  - Fibonacci (naive): Time `O(2^n)` | Space `O(n)`  
- Folder: `/Experiment02_Recursion`

---

### 3️⃣ Quick Sort & Merge Sort – Student Marks Sorter
- Problem: Sort student records by marks  
- Approach:  
  - **Quick Sort** (in-place, divide & conquer)  
  - **Merge Sort** (stable, divide & conquer)  
- Complexity:  
  - Quick Sort: Best/Avg `O(n log n)`, Worst `O(n²)`, Space `O(log n)`  
  - Merge Sort: Always `O(n log n)`, Space `O(n)`  
- Folder: `/Experiment03_Sorting`

---

### 4️⃣ Greedy Method – Project Resource Allocation (Knapsack)
- Problem: Maximize profit with limited project resources  
- Algorithm: Greedy Fractional-Knapsack approach  
- Decision Rule: Profit-to-Resource ratio  
- Complexity:  
  - Time: `O(n log n)`  
  - Space: `O(n)`  
- Folder: `/Experiment04_GreedyKnapsack`

---

### 5️⃣ Backtracking – N-Queens Solver
- Problem: Place N queens on a chessboard without attack  
- Algorithm Type: Backtracking  
- Key Concepts: Safe position check, row-by-row recursion  
- Complexity: Time `O(N!)`, Space `O(N)`  
- Folder: `/Experiment05_NQueens`

---

### 6️⃣ Dynamic Programming – 0/1 Knapsack
- Problem: Maximize profit with weight constraints  
- Difference vs Greedy: Considers optimal substructure, not ratio rule  
- Technique: DP Table  
- Complexity:  
  - Time: `O(nW)`  
  - Space: `O(nW)`  
- Folder: `/Experiment06_DPKnapsack`

---

## 📂 Repository Structure

DAA-Practicals/
│── Experiment01_BinarySearch/
│── Experiment02_Recursion/
│── Experiment03_Sorting/
│── Experiment04_GreedyKnapsack/
│── Experiment05_NQueens/
│── Experiment06_DPKnapsack/
└── README.md <-- (this file)

## 🧪 How to Run Programs

Requirements:
- Python 3.x  or newer version installed

Run any experiment by navigating inside its folder and executing:

```bash
python app.py

###🎯 Learning Outcomes

Mastered major algorithmic techniques:

- Divide & Conquer

- Recursion

- Greedy Method

- Backtracking

- Dynamic Programming

- Analyzed algorithm complexities

- Built real-world analogy based models (book search, student sorting, project allocation)



### 👤 Author

Name: Sakshi Shahaji Chougale
Roll No : 25143071   
Class : SYIT(Batch-I4)
Course: Information Technology
Subject: Design and Analysis of Algorithms


