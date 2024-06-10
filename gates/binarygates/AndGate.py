from src.gates.binarygates.BinaryGate import BinaryGate


class AndGate(BinaryGate):
    """
    Represents a logic gate that performs the logical AND operation on two
    input pins

    Attributes:
        label (str): The label of the AND gate
        output (int or None): The output of the AND gate, initially set to None

    Methods:
        __init__(n): Initializes an AndGate instance with a label n
        performGateLogic(): Performs the logical AND operation on the input pins
        and returns the result
    """

    def __init__(self, label: str):
        """
        Initializes an AndGate instance with a label

        Args:
            label (str): The label for the AND gate
        """
        super().__init__(label)

    def performGateLogic(self) -> int:
        """
        Performs the logical AND operation on the gate's input pins

        Returns: int: The result of the AND operation (1 if both inputs are
        1, otherwise 0)
        """
        return int(self.getPinA() and self.getPinB())
