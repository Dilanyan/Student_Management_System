import unittest
import helper

class TestFunctionFromHelper(unittest.TestCase):
    def test_user_age(self):
        self.assertFalse(helper.Helper.age_validation(-1))
        self.assertFalse(helper.Helper.age_validation(17.999))
        self.assertFalse(helper.Helper.age_validation(120.01))
        self.assertFalse(helper.Helper.age_validation(500))
        self.assertTrue(helper.Helper.age_validation(100))

