class Player:
    """A person taking part in a game. The responsibility of Player is to keep track of their identity and last input(a guess).
    
    Stereotype: 
        Information Holder

    Attributes:
        _name (string): The player's name.
        _code (Selection): The player's last input (trying to guess de code)
    """
    def __init__(self, name):
        """The class constructor.
        
        Args:
            self (Player): an instance of Player.
        """
        self._name = name
        self._code = None
        
    def get_code(self):
        """Returns the player's last selection (an instance of Selection). If the player 
        hasn't guessed yet this method returns None.

        Args:
            self (Player): an instance of Player.
        """
        

    def get_name(self):
        """Returns the player's name.

        Args:
            self (Player): an instance of Player.
        """
        

    def set_code(self, code):
        """Sets the player's last guessed to the given instance of Selection.

        Args:
            self (Player): an instance of Player.
            code (Selection): an instance of Selection
        """
        