def draw_a_cross(n):

    if n < 3:
        return "Not possible to draw cross for grids less than 3x3!"
   # Check if n is even
    if n % 2 == 0:
        return "Centered cross not possible!"

    # Create an empty grid
    grid = []

    # Loop through each row
    for i in range(n):
        row = [' '] * n  # Create a row filled with spaces
        row[i] = 'x'  # Place 'x' on the first diagonal
        row[n - 1 - i] = 'x'  # Place 'x' on the second diagonal
        grid.append(''.join(row))  # Join the row into a string and add to the grid
    print(grid)
    # Join the rows into a string, each row on a new line
    return '\n'.join(grid)


# Example usage:
print(draw_a_cross(2))