import gamebundle.GuessingGame
import unittest



def test_new_num():
    assert GuessingGame.new_num() in range(1,100)

def replay():
    pass

def main():
    test_new_num()

if __name__ == "__main__":
    main()