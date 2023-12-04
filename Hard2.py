def shortestPalindrome(s):
    """
    Finds the shortest palindrome by adding characters in front of the given string.

    Args:
    - s: The input string.

    Returns:
    - str: The shortest palindrome.
    """
    def is_palindrome(prefix):
        # Helper function to check if a string is a palindrome
        return prefix == prefix[::-1]

    if not s:
        return ""

    for i in range(len(s), 0, -1):
        # Iterate from the end of the string and find the longest palindrome prefix
        if is_palindrome(s[:i]):
            # Reverse the remaining characters and add to the front
            return s[i:][::-1] + s

    # If the input string is already a palindrome, return it as is
    return s

# Example usage:
s1 = "aacecaaa"
print(shortestPalindrome(s1))  # Output: "aaacecaaa"

s2 = "abcd"
print(shortestPalindrome(s2))  # Output: "dcbabcd"
