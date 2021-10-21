from game.interface import Interface
from game.console import Console
from game.selection import Selection
from game.player import Player
from game.roster import Roster

class Director:
    

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self._interface = Interface()
        self._console = Console()
        self._keep_playing = True
        self._selection = None
        self._roster = Roster()
        
        
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        

    def _prepare_game(self):
        """Prepares the game before it begins. In this case, that means getting the player names and adding them to the roster.
        
        Args:
            self (Director): An instance of Director.
        """
       
    
    def _get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means getting the guess from the current player.

        Args:
            self (Director): An instance of Director.
        """
       

    def _do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means updating the previous guesses with the current guess.

        Args:
            self (Director): An instance of Director.
        """
        
        
 
    def _do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means checking if a player guessed the code

        Args:
            self (Director): An instance of Director.
        """
        
     
       