import unittest
import logging
from car_simulation import Simulation

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class TestSimulation(unittest.TestCase):
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

if __name__ == '__main__':
    unittest.main()