from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [0, 255, 0]

# Testing
m1 = new_matrix()
m2 = new_matrix(rows = 0)


add_edge(m2, 1, 2, 3, 4, 5, 6)
print("Testing add_edge. Adding (1, 2, 3), (4, 5, 6) m2 =")
print_matrix(m2)

print("Testing ident. m1 =")
ident(m1)
print_matrix(m1)

print("Testing Matrix mult. m1 * m2 =")
matrix_mult(m1, m2)
print_matrix(m2)

print("Testing Matrix mult. m1 =")
matrix = new_matrix(rows = 0)
add_edge(matrix, 1, 2, 3, 4, 5, 6)
add_edge(matrix, 7, 8, 9, 10, 11, 12)
print_matrix(matrix)

print("Testing Matrix mult. m1 * m2 =")
matrix_mult(matrix, m2)
print_matrix(m2)

# Drawing
image = new_matrix(rows = 0)
for x in range(0, 500, 50):
    add_edge(image, x, 0, 0, x, 500, 0)
    add_edge(image, 0, x, 0, 500, x, 0)

draw_lines(image, screen, color)

save_extension(screen, 'image.png')
display(screen)
