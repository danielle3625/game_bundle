import gamebundle.GuessingGame
import unittest



def test_new_num():
    assert GuessingGame.new_num() in range(1,100)

def replay():
    pass
   # expected = True
   # expect = False
   # if [choice[0].lower() == 'y']:
   #     assert GuessingGame.replay() == True
   # else
   #     assert GuessingGame.replay() == False  

def main():
    test_new_num()

if __name__ == "__main__":
    main()
