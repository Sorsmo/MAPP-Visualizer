class Cell:
    def __init__(self, row, col) -> None:
        self.color = (255, 255, 255)
        self.row = row
        self.col = col
        self.start = False
        self.end = False
        self.wall = False

    def pos(self):
        return self.row, self.col

    def make_normal(self):
        self.wall = False
        self.end = False
        self.start = False
        self.color = (255, 255, 255)

    def make_wall(self, color):
        self.color = color
        self.wall = True

    def make_start(self, color):
        self.color = color
        self.start = True

    def make_end(self, color):
        self.color = color
        self.end = True
    
    def is_wall(self):
        return self.wall

    def is_start(self):
        return self.start
    
    def is_end(self):
        return self.end