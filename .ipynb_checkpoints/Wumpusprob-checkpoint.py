import matplotlib.pyplot as plt
from Environmentprob import Environment
from Agentprob import ProbabilisticAgent

env = Environment()
agent = ProbabilisticAgent(env)

# Update beliefs using percepts
agent.update_beliefs()
beliefs = agent.get_beliefs()

print("\nPit Probabilities (Belief State):\n")
for cell, prob in sorted(beliefs.items()):
    print(f"Cell {cell} → P(Pit) = {prob:.2f}")

# Query = Pit(x, y)
joint_probs = {}

for cell in sorted(beliefs.keys()):
    joint_probs[cell] = agent.joint_probability(cell)

total = sum(joint_probs.values())

print("\nNormalized Joint Probabilities (Query | Known, Unknown):")
print("(Here, Query = Pit(x, y))\n")

if total > 0:
    for cell, jp in joint_probs.items():
        norm = jp / total
        print(f"P(Pit{cell} | Known, Unknown) = {norm:.4f}")
else:
    for cell in joint_probs:
        print(f"P(Pit{cell} | Known, Unknown) = 0.0000")

fig, ax = plt.subplots(figsize=(6, 6))

# Draw grid
for i in range(env.size + 1):
    ax.plot([0, env.size], [i, i], color="black")
    ax.plot([i, i], [0, env.size], color="black")

# Symbols ONLY (no probabilities)
for x in range(1, env.size + 1):
    for y in range(1, env.size + 1):
        text = ""

        if (x, y) == env.agent:
            text += "A "
        if (x, y) == env.wumpus:
            text += "W "
        if (x, y) == env.gold:
            text += "G "
        if (x, y) in env.pits:
            text += "P "
        if (x, y) in env.breezes:
            text += "B "
        if (x, y) in env.stenches:
            text += "S "

        if text:
            ax.text(
                x - 0.5,
                y - 0.5,
                text.strip(),
                ha="center",
                va="center",
                fontsize=12,
                fontweight="bold",
            )

ax.set_xlim(0, env.size)
ax.set_ylim(0, env.size)
ax.set_title("Probabilistic Wumpus World")
ax.set_aspect("equal")
ax.axis("off")

plt.show()