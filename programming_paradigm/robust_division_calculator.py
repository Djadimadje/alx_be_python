def safe_divide(numerator, denominator):
    """
    Safely divides two numbers and handles errors.
    
    Args:
        numerator (str): The numerator as a string.
        denominator (str): The denominator as a string.
    
    Returns:
        str: The result of the division or an error message.
    """
    try:
        # Convert inputs to floats
        numerator = float(numerator)
        denominator = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."
    
    try:
        # Perform division
        result = numerator / denominator
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
