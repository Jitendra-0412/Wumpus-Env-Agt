# Probabilistic Wumpus World 

A Python implementation of the Probabilistic Wumpus World using belief updates and normalized joint probabilities. This project demonstrates how an agent reasons under uncertainty using probability instead of pure logical inference.

The Wumpus World is a classic Artificial Intelligence problem used to demonstrate:
- Knowledge representation.
- Reasoning under uncertainty.
- Bayesian inference.
- Probabilistic belief updates
  
## In this implementation:
- Probabilistic belief updates
- The environment generates pits, breeze, stench, gold, and Wumpus.
- The agent maintains probabilistic beliefs about pits.
- The system computes:
- Prior probabilities, Updated belief state, Normalized joint probabilities.
- The world is visualized using matplotlib.

## Part 1: enviprob.py – Environment

This file is responsible for **creating and managing the Wumpus World environment**.

- Takes user input for world size.
- Accepts positions of the agent, Wumpus, gold, and pits.
- Stores pit locations explicitly (P11, P12, P21, etc.).
- Identifies neighboring cells.

This module represents the *actual world* from which the agent receives information.

## Part 2: agenprob.py – Probabilistic Agent

This file is responsible for:

- Assigning prior pit probabilities.
- Updating beliefs using percepts.
- Computing joint probabilities.
- Returning belief state.
- 
# The agent does not know pit locations directly. It reasons probabilistically using observed breezes.

## Part 3: Visualization & Execution (wumpus.py)

This is the **main execution file** of the project.
- Creates the environment.
- Builds a grid-based representation of the world.
- Displays entities such as Agent (A), Wumpus (W), Gold (G), Pit (P).
- Adds percepts like Breeze (B) and Stench (S).
- Visualizes the world using a Cartesian grid with Matplotlib.
- Executes the knowledge base and prints inference results.
# Responsible for:
- Initializing environment and agent.
- Updating beliefs.
- Printing:
- P(Pit(x,y))
- P(Pit(x,y) | Known, Unknown)
  
# Query
- Query=Pit(x,y) 
- Meaning:Is there a pit in cell (x,y)?

# Joint Probability
- P(Query,Known,Unknown)
- Where:
- Query → Pit(x,y)
- Known → Observed breezes
- Unknown → Other pit variables
