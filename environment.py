class Environment:
    def __init__(self):
        self.size = int(input("Enter Wumpus World size: "))

        print("\nEnter Agent position (x y):")
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

        self.P11 = (1,1) in self.pits
        self.P12 = (1,2) in self.pits
        self.P21 = (2,1) in self.pits
        self.P22 = (2,2) in self.pits
        self.P31 = (3,1) in self.pits

        self.B11 = self._breeze(1,1)
        self.B21 = self._breeze(2,1)

    def neighbors(self, x, y):
        adj = []
        if x > 1: adj.append((x-1, y))
        if x < self.size: adj.append((x+1, y))
        if y > 1: adj.append((x, y-1))
        if y < self.size: adj.append((x, y+1))
        return adj

    def _breeze(self, x, y):
        return any(p in self.neighbors(x, y) for p in self.pits)