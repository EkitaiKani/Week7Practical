import math
def add(a, b):
    """
    Performs addition of two numbers.
    
    Args:
        a (int/float): First number
        b (int/float): Second number
    
    Returns:
        int/float: Sum of a and b
    """
    return a + b

def subtract(a, b):
    """
    Performs subtraction of two numbers.
    
    Args:
        a (int/float): Number to be subtracted from
        b (int/float): Number to subtract
    
    Returns:
        int/float: Difference between a and b
    """
    return a - b

def multiply(a, b):
    """
    Performs multiplication of two numbers.
    
    Args:
        a (int/float): First number
        b (int/float): Second number
    
    Returns:
        int/float: Product of a and b
    """
    return a * b

def divide(a, b):
    """
    Performs division of two numbers.
    
    Args:
        a (int/float): Dividend
        b (int/float): Divisor
    
    Returns:
        float: Result of division
    
    Raises:
        ZeroDivisionError: If b is zero
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def natural_log(x):
    """
    Calculates the natural logarithm (base e) of a number.
    
    Args:
        x (float): Positive number to calculate logarithm for
    
    Returns:
        float: Natural logarithm of x
    
    Raises:
        ValueError: If x is less than or equal to zero
    """
    if x <= 0:
        raise ValueError("Input must be a positive number")
    return math.log(x)

def log_base_10(x):
    """
    Calculates the base-10 logarithm of a number.
    
    Args:
        x (float): Positive number to calculate logarithm for
    
    Returns:
        float: Base-10 logarithm of x
    
    Raises:
        ValueError: If x is less than or equal to zero
    """
    if x <= 0:
        raise ValueError("Input must be a positive number")
    return math.log10(x)

def custom_log(x, base):
    """
    Calculates the logarithm of a number with a specified base.
    
    Args:
        x (float): Positive number to calculate logarithm for
        base (float): Base of the logarithm (must be positive and not 1)
    
    Returns:
        float: Logarithm of x with specified base
    
    Raises:
        ValueError: If x is less than or equal to zero or base is invalid
    """
    if x <= 0:
        raise ValueError("Input must be a positive number")
    if base <= 0 or base == 1:
        raise ValueError("Base must be positive and not equal to 1")
    return math.log(x, base)

def exponential(x):
    """
    Calculates the exponential function (e^x).
    
    Args:
        x (float): Exponent
    
    Returns:
        float: e raised to the power of x
    """
    return math.exp(x)

def power(base, exponent):
    """
    Calculates base raised to the power of exponent.
    
    Args:
        base (float): Base number
        exponent (float): Exponent
    
    Returns:
        float: base raised to the power of exponent
    """
    return math.pow(base, exponent)

# def main():
   

# Only run the main function if the script is run directly
# if __name__ == "__main__":
#    main()