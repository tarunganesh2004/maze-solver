
# 🌀 Infinite Maze Generator & Solver

## 📌 Project Overview
This Python-based **Infinite Maze Generator & Solver** dynamically generates random mazes and solves them using **Depth-First Search (DFS) & Breadth-First Search (BFS)**. The project features **real-time visualization using Pygame**, allowing users to watch the solving process live. 

## 🚀 Features
- ✅ **Random Maze Generation** (Backtracking / Prim’s Algorithm)
- ✅ **DFS vs BFS Solving Algorithms** (Shortest Path Calculation)
- ✅ **Real-Time Visualization** (Using Pygame)
- ✅ **Customizable Maze Size** (User Input)
- ✅ **Save & Load Mazes** (Persistence Feature)
- ✅ **Step-by-Step Solving Animation** (Live Pathfinding)
- ✅ **Auto-Resizing Pygame Window** (Supports Larger Mazes)

## 🏗️ Project Structure
```plaintext
maze_solver/
│── maze_generator.py    # Generates the maze  
│── solver.py            # Implements DFS/BFS for solving  
│── visualizer.py        # Handles visualization using Pygame  
│── main.py              # Runs the program  
│── maze_utils.py        # Utility functions (saving/loading mazes)  
│── README.md            # Documentation  
```

## ⚙️ Installation
Ensure you have Python installed (>= 3.7). Then install the dependencies:
```bash
pip install pygame numpy
```

## ▶️ Usage
Run the program:
```bash
python main.py
```

### Interactive Steps:
1. Choose whether to **load a saved maze or generate a new one**  
2. Enter **maze width & height** (odd numbers like `21x21`, `51x51`, etc.)  
3. Choose **maze generation algorithm** (`backtracking` or `prim`)  
4. Select **solver algorithm** (`dfs` or `bfs`)  
5. Watch the **maze generate & solve live in Pygame!** 🎮  

## 📝 How It Works
### 🏗️ **Maze Generation**
- **Backtracking Algorithm**: Uses depth-first search to carve paths recursively.
- **Prim’s Algorithm**: Selects walls randomly to create a natural-looking maze.

### 🔍 **Maze Solving Algorithms**
- **Depth-First Search (DFS)**: Explores one path fully before backtracking.
- **Breadth-First Search (BFS)**: Explores all shortest paths first (optimal for finding the shortest path).



## 🔄 Future Enhancements
- 🚀 **Multiplayer Mode** – Race to solve the maze first 🏃‍♂️🏃‍♀️  
- 🚀 **3D Maze Mode** – Visualize mazes in a first-person view 🎮  
- 🚀 **Obstacles & Portals** – Add teleportation points & dynamic obstacles 🔄  
- 🚀 **Maze Editor** – Let users manually modify walls 🖊️  

## 🤝 Contributing
Feel free to fork the repository, submit issues, and create pull requests!

## 📜 License
This project is licensed under the **MIT License**.

## 📬 Contact
For any queries or suggestions, reach out via **[enstarunganesh@gmail.com](mailto:enstarunganesh@gmail.com)**.
