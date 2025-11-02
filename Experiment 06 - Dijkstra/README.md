# 🚦 City Navigation System Using Dijkstra's Algorithm

This project implements a **City Navigation System** that finds the shortest path between locations using **Dijkstra's Algorithm**.  
The system optimizes routes based on **minimum distance** and **minimum travel time**, similar to how Google Maps and other navigation apps work.

---

## 📌 Features

- Navigation based on two metrics:
  - ✅ Shortest Distance (km)
  - ✅ Shortest Time (minutes)
- Displays full route (Home → School → Hospital…)
- Uses **Priority Queue (Min-Heap)** for efficiency
- Prints total distance & travel time for each destination
- Includes detailed **time & space complexity breakdown**

---

## 🗺️ Locations in the City

| ID | Location |
|---|--------|
| 0 | Home |
| 1 | School |
| 2 | Mall |
| 3 | Hospital |
| 4 | Park |
| 5 | Station |
| 6 | Airport |

---

## 🧠 Algorithm Used

### **Dijkstra’s Algorithm**

Used to compute shortest paths from a source to all nodes in a weighted graph (no negative weights).

Real-world uses:
- GPS Route planning  
- Intelligent transportation systems  
- Network routing protocols  
- Emergency service routing  

---

## 🧮 Time & Space Complexity

| Type | Complexity |
|------|-----------|
Time Complexity | **O((V + E) log V)**  
Space Complexity | **O(V + E)**  

Where:
- **V** = number of locations
- **E** = number of routes

Why?
- Heap operations = `log V`
- Every vertex & edge processed once → `(V + E)`



## ▶️ How to Run

# 1. Clone the repository

git clone https://github.com/Sakshi-Chougale/DAA---Lab.git

# Navigate to project folder
cd Experiment 06 - Dijkstra

# Run the application
python app.py


### **Requirements**
- Python 3.x or newer version




