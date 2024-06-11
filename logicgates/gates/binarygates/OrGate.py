from logicgates.gates.binarygates.BinaryGate import BinaryGate


class OrGate(BinaryGate):
    """
    Represents a logic gate that performs the logical OR operation on two input
    pins

    Methods:
        __init__(label): Initializes an OrGate instance with a label
        performGateLogic(): Performs the logical OR operation on the input pins
        and returns the result
    """

    def __init__(self, label: str):
        """
        Initializes an OrGate instance with a label

        Args:
            label (str): The label for the OR gate
        """
        super().__init__(label)

    def performGateLogic(self) -> int:
        """
        Performs the logical OR operation on the gate's input pins

        Returns:
            int: The result of the OR operation (1 if at least one input is 1,
            otherwise 0)
        """
        return int(self.getPinA() or self.getPinB())
