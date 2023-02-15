from gamebundle import GuessingGame
import unittest

# Remember to install package using command  python -m pip install -e .

class TestBattle(unittest.TestCase):
    def test_new_num(self):
        # Note that new_num() uses random.randint which is INCLUSIVE and range is exclusive of last num
        self.assertIn(GuessingGame.new_num(), range(1,101))
    
    # I'm not sure if this test is actually kosher because it requires user input
    def test_guess_appropriate_range(self):
        self.assertIn(GuessingGame.guess(), range(1,101))

def replay():
    pass
    # Don't test this because should test it within that while True loop - separate test

if __name__ == "__main__":
    unittest.main()
