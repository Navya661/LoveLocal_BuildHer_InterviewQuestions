def countDigitOne(n):
    """
    Counts the total number of digit 1 appearing in all non-negative integers up to n.

    Args:
    - n: The input integer.

    Returns:
    - int: The total number of digit 1.
    """
    count = 0
    factor = 1

    while factor <= n:
        # Split the number into two parts: higher and lower
        higher_part = n // (factor * 10) * factor
        lower_part = n % factor

        # Calculate the total count for the current factor
        current_part = (n // factor) % 10
        if current_part == 1:
            count += higher_part + lower_part + 1
        elif current_part > 1:
            count += (higher_part + factor)
        
        # Move to the next factor (multiply by 10)
        factor *= 10

    return count

# Example usage:
n1 = 13
print(countDigitOne(n1))  # Output: 6

n2 = 0
print(countDigitOne(n2))  # Output: 0
