#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Returns a new matrix with each value squared"""
    # Yeni matris yaratmaq üçün list comprehension istifadə edirik
    new_matrix = [[x ** 2 for x in row] for row in matrix]
    return new_matrix
