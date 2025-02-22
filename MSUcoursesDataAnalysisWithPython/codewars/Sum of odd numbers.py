"""
Given the triangle of consecutive odd numbers:

             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
Calculate the sum of the numbers in the nth row of
this triangle (starting at index 1) e.g.: (Input --> Output)

1 -->  1
2 --> 3 + 5 = 8
"""

#решение
"""В этом треугольнике каждая строка содержит последовательные нечетные числа,"
  а число элементов в n-й строке равно n.
   Примечательно, что сумма чисел в n-й строке равна n³. 
   Это означает, что для любого положительного целого числа n сумма чисел в n-й строке
    равна n * n * n)
"""

def row_sum_odd_numbers(n):
    return n**3


print(row_sum_odd_numbers(13))  #-> 2197