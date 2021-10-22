from abc import ABC, abstractmethod

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
    
   class StrValidator(Validator):
    """
    String validation
    """
    
   """
   Gets user input for names.
   """
    def get_name(self) -> str:
        prompt = "Codebreaker, what is your name? "
        return self.capitalize(self.get_input(prompt))

   
    """
    Capitalize all words of a string.
    """
    def capitalize(self, string: str) -> str:
    return " ".join([word.capitalize() for word in string.split()])

    
    """
    Validates user input to contain only alphabet characters or spaces
    or will re-prompt user to re-enter.
    """
    def get_input(self, prompt: str) -> str:
        while True:
            string = input(prompt).strip()
            if self.is_alpha_or_space(string):
                return string
            else:
                print("Invalid input. Only alphabet characters and spaces only.")

    
    """
    Determines if given string has only alphabet characters or spaces.
    Returns true if it has at least one letter.
    """ 
    def is_alpha_or_space(self, string: str) -> bool:
            one_letter = False
        for c in list(string):
            if c == " ":
                continue
            if not c.isalpha():
                return False
            one_letter = True
        return one_letter   
    
    
    """
    Number validation
    """

    def get_guess(self, guess_count: int, min_value: int, max_value: int) -> int:
        """
        Gets user input for guesses.
        """
        prompt = f"Enter in your guess for position {str(guess_count)}: "
        return self.get_input(prompt, min_value, max_value, True)

   
     """
     Gets user input for endgame options.
     """
    def get_endgame(self, min_value: int, max_value: int) -> int:
        prompt = "Select an option: "
        return self.get_input(prompt, min_value, max_value)

    
    
      """
      Validates user input is in accepted number range or will re-prompt user
      to re-enter. Returns -1 if hints are allowed and user enters in 'h'.
      """
      def get_input(self, prompt: str, min_value: int, max_value,
                  allow_hints: bool = False) -> int:
        while True:
            num = input(prompt).strip()
            try:
                if allow_hints and num == "h":
                    return -1
                num = int(num)
                if num < min_value or num > max_value:
                    raise Exception
                return num
            except Exception:
                print(
                    f"Invalid input. Please enter in a number from {min_value}"
                    f" to {max_value}.")
    
    """
    Validator abstraction
    """

    @abstractmethod
    def get_input(self):
        """
        Method to get user input.
        """
        pass   
       
    
    
    
    
        """Returns the player's last selection (an instance of Selection). If the player 
        hasn't guessed yet this method returns None.
        Args:
            self (Player): an instance of Player.
        """
        def get_code(self):
        
        
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
        
