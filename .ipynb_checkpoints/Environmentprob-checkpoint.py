class Environment:
    def __init__(self):
        self.size = int(input("Enter Wumpus World size: "))

        print("Enter Agent position (x y):")
        self.agent = tuple(map(int, input().split()))

        print("Enter Wumpus position (x y):")
        self.wumpus = tuple(map(int, input().split()))

        print("Enter Gold position (x y):")
        self.gold = tuple(map(int, input().split()))

        self.pits = []
        n = int(input("Enter number of pits: "))
        for i in range(n):
            print(f"Enter Pit {i+1} position (x y):")
            self.pits.append(tuple(map(int, input().split())))

        self.breezes = set()
        self.stenches = set()

        self._generate_breezes()
        self._generate_stenches()

    def neighbors(self, x, y):
        adj = []
        if x > 1: adj.append((x - 1, y))
        if x < self.size: adj.append((x + 1, y))
        if y > 1: adj.append((x, y - 1))
        if y < self.size: adj.append((x, y + 1))
        return adj

    def _generate_breezes(self):
        for pit in self.pits:
            for n in self.neighbors(*pit):
                self.breezes.add(n)

    def _generate_stenches(self):
        for n in self.neighbors(*self.wumpus):
            self.stenches.add(n)