from src.gates.LogicGate import LogicGate


class BinaryGate(LogicGate):
    """
    A class representing a binary logic gate, which has two input pins (A and B)

    Inherits from:
        LogicGate: The base class for logic gates.

    Attributes:
        pinA (int or None): The first input pin of the gate, initially set
         to None
        pinB (int or None): The second input pin of the gate, initially set
        to None
    """

    def __init__(self, label: str):
        """
        Initializes a BinaryGate instance with a label

        Args:
            label (str): The label of the binary gate
        """
        super().__init__(label)
        self.pinA = None
        self.pinB = None

    def getPinA(self) -> int:
        """
        Prompts the user to enter the value for Pin A and returns it as an
        integer

        Returns:
            int: The value of Pin A input by the user
        """
        if self.pinA is None:
            return int(
                input("Enter Pin A input for gate " + self.getLabel() + "-->"))
        return self.pinA.getFrom().getOutput()

    def getPinB(self) -> int:
        """
        Prompts the user to enter the value for Pin B and returns it as an
        integer

        Returns:
            int: The value of Pin B input by the user
        """
        if self.pinB is None:
            return int(
                input("Enter Pin B input for gate " + self.getLabel() + "-->"))
        return self.pinB.getFrom().getOutput()

    def setNextPin(self, source: LogicGate):
        """
        Sets the next available input pin

        If pinA is not set, it sets pinA to the source. If pinA is already set
        but pinB is not set, it sets pinB to the source. Otherwise, it raises
        a RuntimeError indicating that there are no empty pins

        Args:
            source: The source to be connected to the next available input pin
        """
        if self.pinA is None:
            self.pinA = source
        elif self.pinB is None:
            self.pinB = source
        else:
            raise RuntimeError("Error: No empty pins")
