class Robot:
    """Simulates robot moving on the table top."""

    def __init__(self):
        self.state = None

    def on_table(self, x, y):
        range = [0, 1, 2, 3, 4, 5]
        return x in range and y in range

    def place(self, x, y, f):
        if self.on_table(x, y):
            self.state = {"X": x, "Y": y, "F": f}
