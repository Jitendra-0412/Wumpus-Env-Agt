class KnowledgeBase:
    def __init__(self, env=None):
        self.env = env

    def evaluate(self):
        B11 = False
        B21 = True

        P11 = False
        P12 = False
        P21 = False
        P22 = False
        P31 = True

        R1 = not P11                         # R1 is True if P11 has no pit
        R2 = B11 == (P12 or P21)             # B11 is True if P12 or P21 has a pit
        R3 = B21 == (P11 or P22 or P31)      # B21 is True if P11, P22, or P31 has a pit
        R4 = not B11                         # R4 is True if P21 has no pit
        R5 = B21                             # R5 is True if B11 is True

        # Combine all rules
        KB = R1 and R2 and R3 and R4 and R5

        return {
            "R1": R1,
            "R2": R2,
            "R3": R3,
            "R4": R4,
            "R5": R5,
            "KB": KB
        }