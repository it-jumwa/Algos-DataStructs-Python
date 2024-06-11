from gates.Connector import Connector
from gates.binarygates.AndGate import AndGate
from gates.unarygates.NotGate import NotGate
from gates.binarygates.OrGate import OrGate

"""
# Setting up gates
g1 = AndGate("G1")
g2 = AndGate("G2")
g3 = OrGate("G3")
g4 = NotGate("G4")

# Setting up connectors
c1 = Connector(g1, g3)
c2 = Connector(g2, g3)
c3 = Connector(g3, g4)

# Instantiating the circuit
g4.getOutput()
"""

# Setting up gates
g1 = AndGate("G1")
g2 = NotGate("G2")
g3 = AndGate("G3")
g4 = OrGate("G4")

# Setting up connectors
c1 = Connector(g1, g4)
c2 = Connector(g2, g3)
c3 = Connector(g3, g4)

# Instantiating the circuit
g4.getOutput()
