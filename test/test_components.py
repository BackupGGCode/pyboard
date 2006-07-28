""" This module tests the component objects in components.py"""
import unittest
from components import Transistor, AndGate, OrGate

class TransistorTest(unittest.TestCase):
    
    trans = Transistor()

    def testOff(self):
        self.trans.input = False
        self.trans.control = False
        self.assert_(not self.trans.output)

        # input is false

        # switch control on and off
        self.trans.control = True
        self.assert_(not self.trans.output)

        self.trans.control = False
        self.assert_(not self.trans.output)
    
        # input is true

        # switch control on and off

        self.trans.input = True
        self.assert_(not self.trans.output)
        
        self.trans.control = True
        self.assert_(self.trans.output)
        
        self.trans.control = False        
        self.assert_(not self.trans.output)

class AndGateTest(unittest.TestCase):
    gate = AndGate()
    gate.input = [True, True]
    assert_(gate.output)
    gate.input = [False, True]
    assert_(not gate.output)
    gate.input = [True, False]
    assert_(not gate.output)
        
        

if __name__ == "__main__":
    unittest.main()
