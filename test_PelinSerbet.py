import unittest
from AgeCheck import young_driver_age, older_driver_age, elderly_driver_age, \
    young_driver_premium_multiplier, older_driver_premium_multiplier, elderly_driver_premium_multiplier, \
    young_driver_experience_multiplier, no_multiplier, young_driver_experience, older_driver_experience

from AgeCheck import agecheck

class TestAgeCheck(unittest.TestCase):
    
    def test_1(self):
        # Test a young driver with low experience
        age = 20
        experience = 1
        expected_result = young_driver_premium_multiplier * young_driver_experience_multiplier
        self.assertEqual(agecheck(age, experience), expected_result)

    def test_2(self):
        # Test a young driver
        age = 24
        experience = 3
        expected_result = young_driver_premium_multiplier
        self.assertEqual(agecheck(age, experience), expected_result)

    def test_3(self): 
        # Test a middle-aged driver with low experience
        age = 76
        experience = 3
        expected_result = older_driver_premium_multiplier
        self.assertEqual(agecheck(age, experience), expected_result)

    def test_4(self):
        # Test an elderly driver
        age = 88
        experience = 6
        expected_result = elderly_driver_premium_multiplier
        self.assertEqual(agecheck(age, experience), expected_result)

    def test_boundary(self):
        # Test for boundaries of age and experience
        age = 25
        experience = 2
        expected_result = young_driver_premium_multiplier * young_driver_experience_multiplier
        self.assertEqual(agecheck(age, experience), expected_result)

if __name__ == '__main__':
    tests = unittest.TestLoader().loadTestsFromTestCase(TestAgeCheck)
    testRunner = unittest.TextTestRunner(verbosity=2)
    result = testRunner.run(tests)

    # Check the test results
    if result.wasSuccessful():
        print("All tests passed!")
    else:
        print("Some tests failed.") 