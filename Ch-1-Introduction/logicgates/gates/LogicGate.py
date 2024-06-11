class LogicGate:
    """
    A base class representing a logic gate

    Attributes:
        label (str): The label of the logic gate
        output (int or None): The output of the logic gate, initially set to
        None
    """

    def __init__(self, label: str):
        """
        Initializes a LogicGate instance with a label

        Args:
            label (str): The label of the logic gate
        """
        self.label = label
        self.output = None

    def getLabel(self) -> str:
        """
        Returns the label of the logic gate

        Returns:
             str: the label of the logic gate
        """
        return self.label

    def getOutput(self) -> int:
        """
        Returns the output of the logic gate after performing the gate logic

        Returns:
             int: The output of the logic gate
        """
        self.output = self.performGateLogic()
        print(str(self.getLabel()) + " Output: " + str(self.output))
        return self.output

    # abstract method
    def performGateLogic(self) -> int:
        """
        Performs the logic operation specific to the type of gate

        This method should be overridden by subclasses

        Returns:
            int: The result of the logic operation
        """
        pass
