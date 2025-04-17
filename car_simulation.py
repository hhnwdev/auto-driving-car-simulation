DIRECTIONS = ['N', 'E', 'S', 'W']
MOVE_MAP = {
    'N': (0, 1),
    'E': (1, 0),
    'S': (0, -1),
    'W': (-1, 0)
}

class Car:
    def __init__(self, name, x, y, direction, commands):
        self.name = name
        self.x = x
        self.y = y
        self.direction = direction
        self.commands = list(commands)
        self.step = 0
        self.active = True

    def rotate_left(self):
        idx = DIRECTIONS.index(self.direction)
        self.direction = DIRECTIONS[(idx - 1) % 4]

    def rotate_right(self):
        idx = DIRECTIONS.index(self.direction)
        self.direction = DIRECTIONS[(idx + 1) % 4]

    def move_forward(self, width, height):
        dx, dy = MOVE_MAP[self.direction]
        new_x = self.x + dx
        new_y = self.y + dy
        if 0 <= new_x < width and 0 <= new_y < height:
            self.x = new_x
            self.y = new_y

    def execute_command(self, command, width, height):
        if command == 'L':
            self.rotate_left()
        elif command == 'R':
            self.rotate_right()
        elif command == 'F':
            self.move_forward(width, height)

    def get_position(self):
        return (self.x, self.y)

    def __str__(self):
        return f"{self.name}, ({self.x},{self.y}) {self.direction}"
