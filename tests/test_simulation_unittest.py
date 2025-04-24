import unittest
import logging
import main
from unittest.mock import patch
from unittest import mock
from car_simulation import Simulation

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class TestSimulation(unittest.TestCase):
    
    # Existing unit tests
    def test_single_car_movement(self):
        logging.info("Starting test: test_single_car_movement")
        print("\nRunning test: test_single_car_movement")
        sim = Simulation(10, 10)
        sim.add_car('A', 1, 2, 'N', 'FFRFFFFRRL')
        logging.debug("Car A added with initial position (1, 2) facing North and commands 'FFRFFFFRRL'")
        collisions = sim.simulate()
        logging.debug(f"Simulation completed. Collisions: {collisions}")
        results = sim.get_results(collisions)
        logging.debug(f"Simulation results: {results}")
        print(f"Test: test_single_car_movement\nResults: {results}\n")
        with self.subTest("Check final position of car A"):
            self.assertIn("- A, (5,4) S", results)
        logging.info("Completed test: test_single_car_movement")
        print("Test test_single_car_movement passed.\n")

    def test_multiple_car_collision(self):
        logging.info("Starting test: test_multiple_car_collision")
        print("\nRunning test: test_multiple_car_collision")
        sim = Simulation(10, 10)
        sim.add_car('A', 1, 2, 'N', 'FFRFFFFRRL')
        logging.debug("Car A added with initial position (1, 2) facing North and commands 'FFRFFFFRRL'")
        sim.add_car('B', 7, 8, 'W', 'FFLFFFFFFF')
        logging.debug("Car B added with initial position (7, 8) facing West and commands 'FFLFFFFFFF'")
        collisions = sim.simulate()
        logging.debug(f"Simulation completed. Collisions: {collisions}")
        results = sim.get_results(collisions)
        logging.debug(f"Simulation results: {results}")
        print(f"Test: test_multiple_car_collision\nResults: {results}\n")
        with self.subTest("Check collision details for car A"):
            self.assertIn("- A, collides with B at (5, 4) at step 7", results[0])
        with self.subTest("Check collision details for car B"):
            self.assertIn("- B, collides with A at (5, 4) at step 7", results[1])
        logging.info("Completed test: test_multiple_car_collision")
        print("Test test_multiple_car_collision passed.\n")

    def test_car_str(self):
        sim = Simulation(10, 10)
        sim.add_car('A', 1, 2, 'N', 'FFRFFFFRRL')
        car = sim.cars[0]  # Access the car object
        expected_str = "A, (1,2) N"  # Adjust the expected output if necessary
        self.assertEqual(str(car), expected_str)

    def test_get_car_info(self):
        sim = Simulation(10, 10)
        sim.add_car('A', 1, 2, 'N', 'FFRFFFFRRL')
        car_info = sim.get_car_info()
        expected_info = ["- A, (1,2) N, FFRFFFFRRL"]  # Adjust if necessary
        self.assertEqual(car_info, expected_info)

    # New unit tests for main.py scenarios

    def test_scenario_single_car_simulation(self):
        # Simulate user inputs for a single car simulation
        mock_inputs = [
            "10 10",              # Field size
            "1",                  # Add car
            "A",                  # Car name
            "1 2 N",              # Car position
            "FFRFFFFRRL",         # Car commands
            "2",                  # Run simulation
            "2"                   # Exit
        ]

        # Mock user input and print statements
        with mock.patch("builtins.input", side_effect=mock_inputs):
            with mock.patch("builtins.print") as mocked_print:
                main.main()  # Run the main function

                # Check if the correct simulation result is printed
                mocked_print.assert_any_call("After simulation, the result is:")
                mocked_print.assert_any_call("- A, (5,4) S")
                mocked_print.assert_any_call("Thank you for running the simulation. Goodbye!")

    def test_scenario_multiple_car_collision(self):
        # Simulate user inputs for a multiple cars collision simulation
        mock_inputs = [
            "10 10",              # Field size
            "1",                  # Add car A
            "A",                  # Car name
            "1 2 N",              # Car position
            "FFRFFFFRRL",         # Car commands
            "1",                  # Add car B
            "B",                  # Car name
            "7 8 W",              # Car position
            "FFLFFFFFFF",         # Car commands
            "2",                  # Run simulation
            "2"                   # Exit
        ]

        # Mock user input and print statements
        with mock.patch("builtins.input", side_effect=mock_inputs):
            with mock.patch("builtins.print") as mocked_print:
                main.main()  # Run the main function

                # Check if the correct simulation result is printed for collisions
                mocked_print.assert_any_call("After simulation, the result is:")
                mocked_print.assert_any_call("- A, collides with B at (5, 4) at step 7")
                mocked_print.assert_any_call("- B, collides with A at (5, 4) at step 7")
                mocked_print.assert_any_call("Thank you for running the simulation. Goodbye!")

if __name__ == '__main__':
    unittest.main()