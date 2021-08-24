class Robot:
    """Simulates robot moving on the table top."""

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
            update_x = guide[self.state["F"]][0]
            update_y = guide[self.state["F"]][1]
            if self.on_table(self.state["X"] + update_x, self.state["Y"] + update_y):
                self.state["X"] += update_x
                self.state["Y"] += update_y

    def report(self):
        guide = {"N": "NORTH", "S": "SOUTH", "E": "EAST", "W": "WEST"}

        if self.state:
            return f'{self.state["X"]}, {self.state["Y"]}, {guide[self.state["F"]]}'
