import random


class Interface:

    def _init_(self):
        self._code1 = ''
        self._code2 = ''
        self._name1 = ''
        self._name2 = ''
        self._prepare()
        self._choice1 = "----"
        self._choice2 = "----"
        self._hint1 = "**"
        self._hint2 = "**"
    
    def get_name(self, name):
       #get the name of the players and store it in name1  and name2

    def apply(self, code, player):
        #get the instance of selection and player so we can compare the inputed code (choice1 or choice 2 depending the player)
        #to the ramdom generated code stored in (code1 or code 2)
        # the player is to get the name of the player and compare with name1 and name2
        # and know who is the player that is playing 


    def is_equal(self):
       #check if a player guessed the secret code(code1 or code2)

        

    def display(self):        
       #displays the content ot the game like in the example of the assignment
       #with the names of the players, the last guess input for each player
       #and the hint: the string formated by symbols *, X, O, 
       #to create the hint format we use the make_hint method

    def make_hint(self, code, self_code):
       #this method receives the instance of code received, and seld_code (it could be code1 or code2 depending in wich player is playing)
       # it have to compare the two codes and make the format
       # it returns a string with symbols (*, X , O)
       # store or updates the hint1 or hint2       


    

    def _prepare(self):
        #this method will ramdom and store the secretc codes in code1 and code2