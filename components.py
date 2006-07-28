"""This module defines a number of electrical components."""

class Transistor(object):
    input = False
    
    control = False

    def __get_output(self):
        try:
            input = self.input.output
        except AttributeError:
            input = self.input
            
        return self.control and self.input


        

    output = property(self.__get_output)

    def __init__(self, input=False, control=False):
        self.input = input
        self.control = control

