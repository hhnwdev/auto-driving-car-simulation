# Define cardinal directions in clockwise order for easy rotation
DIRECTIONS = ['N', 'E', 'S', 'W']

# Define movement deltas for each direction
MOVE_MAP = {
    'N': (0, 1),   # North: move up
    'E': (1, 0),   # East: move right
    'S': (0, -1),  # South: move down
    'W': (-1, 0)   # West: move left
}

class Car:
    def __init__(self, name, x, y, direction, commands):
        self.name = name                          # Unique car identifier
        self.x = x                                # Current x-coordinate
        self.y = y                                # Current y-coordinate
        self.direction = direction                # Current facing direction (N, E, S, W)
        self.commands = list(commands)            # List of commands (F, L, R)
        self.step = 0                             # Step counter for simulation
        self.active = True                        # Flag to check if car is still active (not collided)

    def rotate_left(self):
        # Rotate car 90 degrees to the left
        idx = DIRECTIONS.index(self.direction)
        self.direction = DIRECTIONS[(idx - 1) % 4]

    def rotate_right(self):
        # Rotate car 90 degrees to the right
        idx = DIRECTIONS.index(self.direction)
        self.direction = DIRECTIONS[(idx + 1) % 4]

    def move_forward(self, width, height):
        # Move car forward by 1 unit based on its current direction
        dx, dy = MOVE_MAP[self.direction]
        new_x = self.x + dx
        new_y = self.y + dy
        # Ensure car stays within bounds of the field
        if 0 <= new_x < width and 0 <= new_y < height:
            self.x = new_x
            self.y = new_y

    def execute_command(self, command, width, height):
        # Execute one command: L (left), R (right), F (forward)
        if command == 'L':
            self.rotate_left()
        elif command == 'R':
            self.rotate_right()
        elif command == 'F':
            self.move_forward(width, height)

    def get_position(self):
        # Return current position as a tuple
        return (self.x, self.y)

    def __str__(self):
        # Return car state as a string
        return f"{self.name}, ({self.x},{self.y}) {self.direction}"

class Simulation:
    def __init__(self, width, height):
        self.width = width              # Width of the field
        self.height = height            # Height of the field
        self.cars = []                  # List of all cars in the simulation

    def add_car(self, name, x, y, direction, commands):
        # Add a new car to the simulation
        self.cars.append(Car(name, x, y, direction, commands))

    def simulate(self):
        if not self.cars:
            return {}  # No cars to simulate, return empty collisions
        max_steps = max(len(car.commands) for car in self.cars)  # Max command length

        car_count = len(self.cars)
        collisions = {}                                # Track any collisions

        # Run simulation step by step
        for step in range(max_steps):
            positions = {}  # Map of current positions to car objects
            for car in self.cars:
                if not car.active or step >= len(car.commands):
                    continue  # Skip car if it's inactive or out of commands

                prev_position = car.get_position()  # Track position before move
                car.execute_command(car.commands[step], self.width, self.height)  # Perform command
                car.step = step + 1
                pos = car.get_position()  # Position after command

                # Detect collision
                if pos in positions:
                    other = positions[pos]
                    # Register collision for both cars
                    collisions[car.name] = (pos, step + 1, other.name)
                    collisions[other.name] = (pos, step + 1, car.name)
                    car.active = False
                    other.active = False
                else:
                    positions[pos] = car

        return collisions

    def get_car_info(self):
        # Return initial info of all cars
        return [f"- {car.name}, ({car.x},{car.y}) {car.direction}, {''.join(car.commands)}" for car in self.cars]

    def get_results(self, collisions):
        # Return results after simulation, either final position or collision message
        results = []
        for car in self.cars:
            if car.name in collisions:
                pos, step, other = collisions[car.name]
                results.append(f"- {car.name}, collides with {other} at {pos} at step {step}")
            else:
                results.append(f"- {car.name}, ({car.x},{car.y}) {car.direction}")
        return results
