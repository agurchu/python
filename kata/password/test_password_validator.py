import unittest
from password_validator import is_password_secure


class TestPasswordValidator(unittest.TestCase):
    def test_password(self):
        self.assertEqual(is_password_secure("123Wtc@cjc"), True)


if __name__ == "__main__":
    unittest.main()
