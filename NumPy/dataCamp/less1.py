# Import NumPy
import numpy as np
import plt

# # Convert sudoku_list into an array
# sudoku_array = np.array([[0, 0, 4, 3, 0, 0, 2, 0, 9],
#  [0, 0, 5, 0, 0, 9, 0, 0, 1],
#  [0, 7, 0, 0, 6, 0, 0, 4, 3],
#  [0, 0, 6, 0, 0, 2, 0, 8, 7],
#  [1, 9, 0, 0, 0, 7, 4, 0, 0],
#  [0, 5, 0, 0, 8, 3, 0, 0, 0],
#  [6, 0, 0, 0, 0, 0, 1, 0, 5],
#  [0, 0, 3, 5, 0, 8, 6, 9, 0],
#  [0, 4, 2, 9, 1, 0, 3, 0, 0]])
#
# # Print the type of sudoku_array
# print(type(sudoku_array))
# print(sudoku_array.dtype)
#
# """Create an array of zeros which has four columns and two rows"""
#
# z = np.zeros((2,4))
# print(z)
#
#
# random_arr = np.random.rand(3,6)
# print(random_arr)
#
# """Create an array of integers from one to ten
# """
# one_ten_arr = np.arange(1,11)
#
# # Create your scatterplot
# doubling_array = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
# plt.scatter(one_ten_arr, doubling_array)
# plt.show()

sudoku_game = np.array([1, 2, 4, 8, 16])

sudoku_solution = np.array([1,2,3,4,5])

game_and_solution = np.array([sudoku_game, sudoku_solution])

# Print game_and_solution
print(game_and_solution)

print("____________________")
