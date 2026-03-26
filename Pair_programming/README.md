### Collaborative Pair Programming: Game of Life

This project is the result of a **Fast-Paced Pair Programming** exercise. The goal was to implement Conway's Game of Life under strict time constraints, rotating roles to maintain momentum and fresh perspectives.

### The Challenge
The task was to build a terminal-based version of **Conway's Game of Life** using Python and NumPy. Key requirements included:
* **Customizable Grid**: Users define the board size (rows and columns).
* **Dynamic Visualization**: Configurable markers for "Alive" and "Dead" cells.
* **Evolution Logic**: Implementation of the standard rules:
    * Any live cell with 2 or 3 neighbors survives.
    * Any dead cell with exactly 3 neighbors becomes alive.
* **Execution Speed**: User-defined intervals between "ticks" of the simulation.

### Project Structure
* **Implementation (`game_of_life.py`):** The core script containing the `LifeBoard` class and the main execution loop.
* **Key Dependencies:** * `NumPy`: Used for efficient matrix manipulation and neighbor slicing.
    * `os` & `time`: Used for screen clearing and simulation pacing.

### Contributors
* **Szymon Flis (@flis0)**
* **Iwo Chwiszczuk (@iwonieevo)**

### The Process
1. **Pair Programming**: The team worked in alternating roles of **Driver** and **Navigator**.
2. **Time-Boxed Sprints**: The entire solution was developed in **four 10-minute bursts**.
3. **Role Rotation**: Participants swapped control of the keyboard at the end of every burst to ensure collaborative ownership of the code.

### How to Run
Ensure you have `numpy` installed, then run:
```bash
python game_of_life.py