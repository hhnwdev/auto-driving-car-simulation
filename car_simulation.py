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

class Simulation:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cars = []

    def add_car(self, name, x, y, direction, commands):
        self.cars.append(Car(name, x, y, direction, commands))

    def simulate(self):
        car_count = len(self.cars)
        collisions = {}
        max_steps = max(len(car.commands) for car in self.cars)

        for step in range(max_steps):
            positions = {}
            for car in self.cars:
                if not car.active or step >= len(car.commands):
                    continue
                prev_position = car.get_position()
                car.execute_command(car.commands[step], self.width, self.height)
                car.step = step + 1
                pos = car.get_position()
                if pos in positions:
                    other = positions[pos]
                    collisions[car.name] = (pos, step + 1, other.name)
                    collisions[other.name] = (pos, step + 1, car.name)
                    car.active = False
                    other.active = False
                else:
                    positions[pos] = car
        return collisions

    def get_car_info(self):
        return [f"- {car.name}, ({car.x},{car.y}) {car.direction}, {''.join(car.commands)}" for car in self.cars]

    def get_results(self, collisions):
        results = []
        for car in self.cars:
            if car.name in collisions:
                pos, step, other = collisions[car.name]
                results.append(f"- {car.name}, collides with {other} at {pos} at step {step}")
            else:
                results.append(f"- {car.name}, ({car.x},{car.y}) {car.direction}")
        return results
