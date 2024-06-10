from src.gates.LogicGate import LogicGate


class UnaryGate(LogicGate):
    """
    UnaryGate is a type of logic gate that takes a single input

    Attributes:
        pin (int): The input pin for the gate

    Methods:
        __init__(n): Initializes the UnaryGate with a label
        getPin(): Prompts the user to enter the pin input for the gate and
        returns it as an integer
        setNextPin(): Sets a pin to a connector
    """

    def __init__(self, label: str):
        """
        Initializes a UnaryGate instance

        Args:
            label (str): The label for the gate
        """
        super().__init__(label)
        self.pin = None

    def getPin(self) -> int:
        """
        Prompts the user to enter the pin input for the gate and returns it

        Returns:
            int: The input pin value entered by the user
        """
        if self.pin is None:
            return int(input("Enter Pin input for gate " + self.getLabel() +
                             "-->"))
        return self.pin.getFrom().getOutput()

    def setNextPin(self, source: LogicGate):
        """
        Sets the next available input pin

        If the pin is not set, it sets the pin to the source. If the pin is
        already set, it raises a RuntimeError indicating that there are no
        empty pins

        Args:
            source: The source to be connected to the next available input pin
        """
        if self.pin is None:
            self.pin = source
        else:
            raise RuntimeError("Error: No empty pins")
