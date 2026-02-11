class ProbabilisticAgent:
    def __init__(self, env, pit_prior=0.2):
        self.env = env
        self.belief = {}

        # Initialize belief state
        for x in range(1, env.size + 1):
            for y in range(1, env.size + 1):
                self.belief[(x, y)] = pit_prior

        # Agent's starting cell is safe
        self.belief[env.agent] = 0.0

    def update_beliefs(self):
        # Increase probability near breezes
        for (x, y) in self.env.breezes:
            for n in self.env.neighbors(x, y):
                self.belief[n] = min(1.0, self.belief[n] + 0.25)

        # Decrease probability where there is no breeze
        for x in range(1, self.env.size + 1):
            for y in range(1, self.env.size + 1):
                if (x, y) not in self.env.breezes:
                    for n in self.env.neighbors(x, y):
                        self.belief[n] = max(0.0, self.belief[n] - 0.15)

    def get_beliefs(self):
        return self.belief

    def joint_probability(self, query_cell):
        joint_prob = 1.0
        # P(Query + Unknown)
        for cell, prob in self.belief.items():
            if cell == query_cell:
                joint_prob *= prob
            else:
                joint_prob *= (1 - prob)

        # P(Known | Unknown) using breeze evidence
        for breeze_cell in self.env.breezes:
            neighbors = self.env.neighbors(*breeze_cell)
            if neighbors:
                avg_prob = sum(self.belief[n] for n in neighbors) / len(neighbors)
                joint_prob *= avg_prob

        return joint_prob