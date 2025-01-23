class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Static method to add two numbers.
        :param a: First number (int or float).
        :param b: Second number (int or float).
        :return: Sum of a and b.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Class method to multiply two numbers.
        :param a: First number (int or float).
        :param b: Second number (int or float).
        :return: Product of a and b.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
