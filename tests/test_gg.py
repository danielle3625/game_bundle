from gamebundle import GuessingGame
import unittest

# Remember to install package using command  python -m pip install -e

class TestBattle(unittest.TestCase):
    def test_new_num(self):
        assert GuessingGame.new_num() in range(1,100)

def replay():
    pass
   # expected = True
   # expect = False
   # if [choice[0].lower() == 'y']:
   #     assert GuessingGame.replay() == True
   # else
   #     assert GuessingGame.replay() == False  


if __name__ == "__main__":
    unittest.main()
