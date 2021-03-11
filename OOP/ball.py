class Balls:

    def __init__(self, ball_type):
        """
        The self. is allowing to use the variable in the class, so now is a class
        atribute.
        . -- public
        ._ -- private

        """
        self._ball_type = ball_type
        self._is_Moving = False

    #these are methods
    def toss(self):
        self._is_Moving = True

    def catch(self):
        self._is_Moving = False

    """
    these are getters. You can acces the atributes of the class with them, but not modify them
    """
    def get_is_moving(self):
        return self._is_Moving
    
    def get_type_of_ball(self):
        return self._ball_type

    def __str__(self):
        if self._is_Moving:
            return f'{self._ball_type} is moving, better catch it'
        return f'{self._ball_type} is in your hand.'