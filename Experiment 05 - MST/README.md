# Campus Network Design Using Minimum Cost Spanning Tree  
Using **Prim’s Algorithm** and **Kruskal’s Algorithm**

## 🎯 Objective
Design a campus network connecting all buildings with the **minimum cable cost**, without loops.  
This simulates **real network planning** used in universities, IT parks, and enterprise setups.

## 📘 Description
Each building is treated as a **node**, and each cable cost is treated as **weighted edge**.  
The program constructs a **Minimum Spanning Tree (MST)** using:

- **Kruskal's Algorithm** – Sorts edges by cost, connects smallest first using Union-Find  
- **Prim's Algorithm** – Grows MST by always choosing the cheapest next connection

Both ensure **minimum total cabling cost**.

## ✅ Features
- Realistic campus network simulation  
- Compares **Prim vs Kruskal** on same dataset  
- Demonstrates how ISPs & IT teams reduce infrastructure cost  

## 📎 Example Graph
Buildings = 6 (0-5)

| Connection | Cost |
|-----------|------|
| 0–1 | 4 |
| 0–2 | 3 |
| 1–2 | 1 |
| 1–3 | 2 |
| 2–3 | 4 |
| 3–4 | 2 |
| 4–5 | 6 |
| 3–5 | 3 |

## ▶️ How to Run
# 1. Clone the repository

git clone https://github.com/Sakshi-Chougale/DAA---Lab.git

# Navigate to project folder
cd Experiment 05 - MST

# Run the application
python app.py


### **Requirements**
- Python 3.x or newer version