import matplotlib.pyplot as plt
from environment import Environment
from agent import KnowledgeBase

env = Environment()
cells = {}

for x in range(1, env.size + 1):
    for y in range(1, env.size + 1):
        content = ""

        if (x, y) == env.agent:
            content += "A"
        if (x, y) == env.wumpus:
            content += "W"
        if (x, y) == env.gold:
            content += "G"
        if (x, y) in env.pits:
            content += "P"

        # Breeze
        if any(p in env.neighbors(x, y) for p in env.pits):
            content += "B"

        # Stench
        if env.wumpus in env.neighbors(x, y):
            content += "S"

        cells[(x, y)] = content if content else "."

fig, ax = plt.subplots(figsize=(6, 6))

for i in range(env.size + 1):
    ax.plot([0, env.size], [i, i], color="black")
    ax.plot([i, i], [0, env.size], color="black")

colors = ['black', 'black', 'black', 'black']
for i, c in enumerate(colors):
    ax.plot([0, env.size], [i+1, i+1], color=c)

for (x, y), text in cells.items():
    ax.text(x - 0.5, y - 0.5, text,
            ha='center', va='center',
            fontsize=14, fontweight='bold')

ax.set_xlim(0, env.size)
ax.set_ylim(0, env.size)
ax.set_title("Wumpus World")
ax.set_aspect('equal')

ax.axis('off')

plt.show()

kb = KnowledgeBase(env)
results = kb.evaluate()

print("\nInference Result:\n")
for k, v in results.items():
    print(f"{k} : {v}")