from src.gates.unarygates.UnaryGate import UnaryGate


class NotGate(UnaryGate):
    """
    Represents a logic gate that performs the logical NOT operation on a
    single input pin

    Attributes:
        label (str): The label of the NOT gate
        output (int or None): The output of the NOT gate, initially set to None

    Methods:
        __init__(label): Initializes a NotGate instance with a label
        performGateLogic(): Performs the logical NOT operation on the input pin
        and returns the result
    """

    def __init__(self, label: str):
        """
        Initializes a NotGate instance with a label

        Args:
            label (str): The label for the NOT gate
        """
        super().__init__(label)

    def performGateLogic(self) -> int:
        """
        Performs the logical NOT operation on the gate's input pin

        Returns:
            int: The result of the NOT operation (1 if input is 0, otherwise 0)
        """
        return 0 if (self.getPin() == 1) else 1
