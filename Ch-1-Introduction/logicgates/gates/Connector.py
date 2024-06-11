from logicgates.gates import LogicGate


class Connector:
    """
    Represents a connector between two logic gates in a circuit

    Attributes:
        fromGate: The gate from which the connector originates
        toGate: The gate to which the connector leads
    """

    def __init__(self, fromGate: LogicGate, toGate: LogicGate):
        """
        Initializes a Connector instance between two gates

        Args:
            fromGate: The gate from which the connector originates
            toGate: The gate to which the connector leads
        """
        self.fromGate = fromGate
        self.toGate = toGate

        # Sets this connector as the next input pin for the target gate
        toGate.setNextPin(self)

    def getFrom(self):
        """
        Returns the gate from which the connector originates

        Returns:
            The gate from which the connector originates
        """
        return self.fromGate

    def getTo(self):
        """
        Returns the gate to which the connector leads

        Returns:
            The gate to which the connector leads
        """
        return self.toGate
