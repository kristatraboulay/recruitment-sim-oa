import numpy as np
import math
import unittest

g = 9.81

def final_disk_speed(height: float, length: float, incline: float, mass: float, friction: float, radius: float) -> float:
    """
    Returns the speed of a uniform disk after it reaches the bottom of an inclined slope.

    :param height: the height of the incline (meters)
    :param length: the length of the slope (meters)
    :param incline: the angle of the slope (degrees)
    :param mass: the mass of the ball (kilograms)
    :param friction: kinetic friction coefficient of the slope's surface (0.0 - 1.0)
    :param radius: the radius of the disk (meters)
    :return: the speed of the disk (m/s)
    """

    initial_energy = mass * g * (height + radius)
    final_speed = math.sqrt(2 * initial_energy / mass)
    
    return final_speed


class TestFinalDiskSpeed(unittest.TestCase):
    """ Test class for function disk.final_disk_speed """

    def test_final_disk_speed_ex1(self):
        height1 = 5.0
        length1 = 10.0
        incline1 = 30.0
        mass1 = 10.0
        friction1 = 1.0
        radius1 = 1.0

        actual = final_disk_speed(height1, length1, incline1, mass1, friction1, radius1) 
        expected = 10.850
        self.assertEqual(round(actual, 3), expected) 

    def test_final_disk_speed_ex2(self):
        height2 = 20.0 * math.sin(math.pi / 12.0)
        length2 = 20.0
        incline2 = 15.0
        mass2 = 30.0
        friction2 = 0.0
        radius2 = 2.0

        actual = final_disk_speed(height2, length2, incline2, mass2, friction2, radius2) 
        expected = 11.866
        self.assertEqual(round(actual, 3), expected) 

if __name__ == '__main__':
    unittest.main(exit=False)