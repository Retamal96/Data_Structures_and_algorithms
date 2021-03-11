import unittest
from ball import Balls


class TestBalls(unittest.TestCase):
    def test_tost(self):
        #Arrange, Act, Assert

        #Arrange - setup variables for testing
        ball = Balls(" ")
        expected_is_moving = True

        #Act - call the code we are testing and get an actual result
        ball.toss()
        actual_is_moving =ball.get_is_moving()

        #Assert - did we get what we expected
        self.assertEqual(expected_is_moving,actual_is_moving) 

    def test_catch(self):
        expected_is_moving = False
        ball = Balls(" ")
        ball.catch()
        x = ball.get_is_moving()
        self.assertEqual(x,expected_is_moving)


