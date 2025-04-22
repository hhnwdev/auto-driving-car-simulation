import unittest
from car_simulation import Simulation

class TestSimulation(unittest.TestCase):
    def test_single_car_movement(self):
        sim = Simulation(10, 10)
        sim.add_car('A', 1, 2, 'N', 'FFRFFFFRRL')
        collisions = sim.simulate()
        results = sim.get_results(collisions)
        self.assertIn("- A, (5,4) S", results)

    def test_multiple_car_collision(self):
        sim = Simulation(10, 10)
        sim.add_car('A', 1, 2, 'N', 'FFRFFFFRRL')
        sim.add_car('B', 7, 8, 'W', 'FFLFFFFFFF')
        collisions = sim.simulate()
        results = sim.get_results(collisions)
        self.assertIn("- A, collides with B at (5, 4) at step 7", results[0])
        self.assertIn("- B, collides with A at (5, 4) at step 7", results[1])

if __name__ == '__main__':
    unittest.main()