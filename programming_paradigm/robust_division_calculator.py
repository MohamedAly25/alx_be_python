# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Perform division of numerator by denominator with error handling.
    Args:
        numerator (str): The numerator input as string.
        denominator (str): The denominator input as string.
    Returns:
        str: Result message or error message.
    """
    try:
        num = float(numerator)
        den = float(denominator)
        result = num / den
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
