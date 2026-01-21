# Wumpus-Env-Agt
This project is a Python implementation of the Wumpus World problem from the Artificial Intelligence, where a dynamic environment is created using user-defined inputs. The project is divided into three parts: environment creation, knowledge-based logical reasoning, and grid-based visualization, demonstrating percepts like breeze and stench with inference results.

# Wumpus World

## Part 1: Environment (environment.py)

This file is responsible for **creating and managing the Wumpus World environment**.

- Takes user input for world size.
- Accepts positions of the agent, Wumpus, gold, and pits.
- Stores pit locations explicitly (P11, P12, P21, etc.).
- Identifies neighboring cells.
- Generates the **breeze percept** when a pit is present in an adjacent cell.
- Generates the **stench percept** when a wumpus is present in an adjacent cell.

This module represents the *actual world* from which the agent receives information.

## Part 2: Agent / Knowledge Base (agent.py)

This file implements a **knowledge-based agent** using propositional logic.

- Defines logical symbols for pits and breezes.
- Evaluates each rule individually.
- Combines all rules to determine whether the knowledge base is consistent.

The values are used to clearly demonstrate **logical inference**, similar to textbook and Lecture-4.

## Part 3: Visualization & Execution (wumpus.py)

This is the **main execution file** of the project.
- Creates the environment.
- Builds a grid-based representation of the world.
- Displays entities such as Agent (A), Wumpus (W), Gold (G), Pit (P).
- Adds percepts like Breeze (B) and Stench (S).
- Visualizes the world using a Cartesian grid with Matplotlib.
- Executes the knowledge base and prints inference results.
