class Robot:
    """Simulates a robot moving on a square 5 by 5 table top."""

    def __init__(self):
        self.state = None

    def on_table(self, x, y):
        return x in range(6) and y in range(6)

    def place(self, x, y, f):
        self.state = {"X": x, "Y": y, "F": f} if self.on_table(x, y) else self.state

    def left(self):
        guide = {"N": "W", "S": "E", "E": "N", "W": "S"}

        if self.state:
            self.state["F"] = guide[self.state["F"]]

    def right(self):
        guide = {"N": "E", "S": "W", "E": "S", "W": "N"}

        if self.state:
            self.state["F"] = guide[self.state["F"]]

    def move(self):
        guide = {"N": (0, 1), "S": (0, -1), "E": (1, 0), "W": (-1, 0)}

        if self.state:
            new_x = self.state["X"] + guide[self.state["F"]][0]
            new_y = self.state["Y"] + guide[self.state["F"]][1]
            if self.on_table(new_x, new_y):
                self.state["X"] = new_x
                self.state["Y"] = new_y

    def report(self):
        guide = {"N": "NORTH", "S": "SOUTH", "E": "EAST", "W": "WEST"}

        if self.state:
            return f'{self.state["X"]}, {self.state["Y"]}, {guide[self.state["F"]]}'
