# Import the Simulation class from the car_simulation module
from car_simulation import Simulation

def main():
    # Loop to allow restarting the simulation after one full run
    while True:
        print("Welcome to Auto Driving Car Simulation!")

        # Prompt user for field dimensions
        while True:
            try:
                width, height = map(int, input("Please enter the width and height of the simulation field in x y format:\n").split())
                break
            except ValueError:
                print("Invalid input. Please enter two integers separated by a space.")
        sim = Simulation(width, height)
        print(f"You have created a field of {width} x {height}.")

        # Menu loop for adding cars or running simulation
        while True:
            print("Please choose from the following options:\n[1] Add a car to field\n[2] Run simulation")
            choice = input()

            if choice == '1':
                # Input car details
                name = input("Please enter the name of the car:\n").strip()
                x, y, direction = input(f"Please enter initial position of car {name} in x y Direction format:\n").split()

                # Validate direction input
                if direction not in ['N', 'S', 'E', 'W']:
                    print("Invalid direction. Use N, S, E, W only.")
                    continue

                # Get movement commands for the car
                while True:
                    commands = input(f"Please enter the commands for car {name}:\n").strip().upper()
                    if all(c in "FLR" for c in commands):  # Validate commands
                        break
                    print("Invalid commands. Use only F, L, R.")

                # Add the car to simulation
                sim.add_car(name, int(x), int(y), direction, commands)

                # Display all added cars
                print("Your current list of cars are:")
                for info in sim.get_car_info():
                    print(info)

            elif choice == '2':
                # Check if there are cars to simulate
                if not sim.cars:
                    print("No cars available to simulate. Please add cars first.")
                    continue

                # Display cars before running simulation
                print("Your current list of cars are:")
                for info in sim.get_car_info():
                    print(info)

                # Run the simulation
                collisions = sim.simulate()

                # Show final result after simulation
                print("After simulation, the result is:")
                for result in sim.get_results(collisions):
                    print(result)

                # Prompt user to start over or exit
                print("Please choose from the following options:\n[1] Start over\n[2] Exit")
                final_choice = input()

                if final_choice == '1':
                    break  # Restart outer while loop
                elif final_choice == '2':
                    print("Thank you for running the simulation. Goodbye!")
                    return  # Exit the program

# Entry point of the program
if __name__ == '__main__':
    main()
