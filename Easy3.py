def generate_pascals_triangle(numRows):
    """
    Generates the first numRows of Pascal's triangle.

    Args:
    - numRows: An integer representing the number of rows to generate.

    Returns:
    - List[List[int]]: A list of lists representing Pascal's triangle.
    """
    # Initialize Pascal's triangle with the first row
    triangle = [[1]]

    # Generate subsequent rows based on the previous row
    for i in range(1, numRows):
        # Initialize the new row with the first element
        row = [1]

        # Calculate the middle elements based on the previous row
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])

        # Add the last element to the row
        row.append(1)

        # Add the generated row to the triangle
        triangle.append(row)

    return triangle

# Example usage:
numRows1 = 5
result1 = generate_pascals_triangle(numRows1)
print(result1)
# Output: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

numRows2 = 1
result2 = generate_pascals_triangle(numRows2)
print(result2)
# Output: [[1]]
