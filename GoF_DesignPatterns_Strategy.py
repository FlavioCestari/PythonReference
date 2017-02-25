
# python3
# coding = utf-8

"""
Implementation Example of Strategy's Design Pattern (also known as the Policy)
http://en.wikipedia.org/wiki/Strategy_pattern

In most of other languages Strategy pattern is implemented via creating some
base strategy interface/abstract class and subclassing it with a number of
concrete strategies, however Python supports higher-order functions and allows
us to have only one class and inject functions into it's instances, as shown
in this example.
"""


class PLRStrategies:
    """Inteface / Abstract Class concept for readability."""

    def __init__(self, strategy):
        """"Class constructor."""
        self.interface = strategy

    def calculate(self, performance_grade):
        """Interface method"concept."""
        return self.interface.calculate(performance_grade)


class CSharpProgramming():
    """"Concrete Class - CSharpProgramming Strategy."""

    def calculate(self, performance_grade):
        """Method replaced by this strategy."""
        return 0 * performance_grade


class PythonProgramming():
    """"Concrete Class - PythonProgramming Strategy."""

    def calculate(self, performance_grade):
        """Method replaced by this strategy."""
        return 50000 * performance_grade


class EmployeeCalculator:
    """Just a abstract client concept for readability."""


class EmployeePLRCalculator(EmployeeCalculator, PLRStrategies):
    """Client who needs a calculate behavior with strategies."""


if __name__ == '__main__':
    # Calculate Miano's PLR - CSharpProgramming Strategy
    NAME = "Miano"
    GRADE = 10  # excellent grade
    PLR = EmployeePLRCalculator(strategy=CSharpProgramming())
    print("PLR " + NAME + " = R$ " + str(format(PLR.calculate(GRADE), ",d")))

    # Calculate Cestari's PLR - PythonProgramming Strategy
    NAME = "Cestari"
    GRADE = 9  # good grade
    PLR = EmployeePLRCalculator(strategy=PythonProgramming())
    print("PLR " + NAME + " = R$ " + str(format(PLR.calculate(GRADE), ",d")))
