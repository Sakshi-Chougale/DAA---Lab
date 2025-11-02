# Optimal Merge Pattern using Greedy Method
## File Compression Simulation in Python

### Overview
This program demonstrates the Optimal Merge Pattern using a Greedy Algorithm and a Min-Heap.
The goal is to minimize total merge cost when combining sorted files by always merging
the two smallest files first. A naive worst-case method is also implemented for comparison.

### Algorithm Logic
- Merge cost = sum of file sizes being merged
- Greedy method: always merge the two smallest files first (optimal)
- Naive method: merge largest files first (worst case)

### Applications
- File compression (Huffman compression principle)
- External sorting in DBMS and Big Data
- Search engine indexing
- Operating system log merging
- Compiler intermediate file merging

### Time & Space Complexity
| Method | Time Complexity | Space Complexity |
|--------|----------------|------------------|
| Greedy (Optimal) | O(n log n) | O(n) |
| Naive (Worst Case) | O(n^2 log n) | O(n) |

## How to run

# 1. Clone the repository

git clone https://github.com/Sakshi-Chougale/DAA---Lab.git

# Navigate to project folder
cd Experiment 04 - OptimalMerge

# Run the application
python app.py


### Sample Input
Files = [5, 10, 20, 30, 30]

### Sample Output
Step 1: Merge 5 + 10 = 15
Step 2: Merge 15 + 20 = 35
Step 3: Merge 30 + 30 = 60
Step 4: Merge 35 + 60 = 95

Optimal Total Cost: 205
Naive Total Cost:   275
Efficiency Gain:    25.45%

### **Requirements**
- Python 3.x or newer version

### Conclusion
The Greedy method yields the minimum total merge cost and significantly outperforms
the naive method, proving optimal efficiency.
