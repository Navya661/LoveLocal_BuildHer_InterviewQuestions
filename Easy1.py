def length_of_last_word(s):
    # Split the string into words using spaces as separators
    words = s.split()

    # Check if there are any words in the string
    if not words:
        return 0

    # Return the length of the last word in the string
    return len(words[-1])

# Example usage:
s1 = "Hello World"
print(length_of_last_word(s1))  # Output: 5

s2 = "   fly me   to   the moon  "
print(length_of_last_word(s2))  # Output: 4

s3 = "luffy is still joyboy"
print(length_of_last_word(s3))  # Output: 6
