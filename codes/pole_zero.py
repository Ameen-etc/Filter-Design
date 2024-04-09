from sympy import symbols, solve, simplify
import numpy as np
import matplotlib.pyplot as plt

# Define symbolic variable
s = symbols('s')

# Define the expression for H_{a,LP}(j\Omega_L)^2
expression = (1 + 0.16 * (8 * s**4 - 8 * s**2 + 1)**2)
expression = simplify(expression)

roots =  solve(expression, s)

# Extract the real and imaginary parts of the roots
real_parts = [root.evalf().as_real_imag()[0] for root in roots]
imag_parts = [root.evalf().as_real_imag()[1] for root in roots]

# Plot the pole-zero plot
plt.scatter(real_parts, imag_parts, marker='x', color='r', label='Roots')
plt.axhline(0, color='k', linestyle='--', linewidth=0.5)  # Horizontal line at y=0
plt.axvline(0, color='k', linestyle='--', linewidth=0.5)  # Vertical line at x=0
plt.xlabel('Real')
plt.xlim(-2, 2)
plt.ylabel('Imaginary')
plt.ylim(-1, 1)
plt.title('Pole-Zero Plot')
plt.legend()
plt.grid(True)
plt.show()

# Write the roots to a file
with open('roots.txt', 'w') as file:
    file.write("Real\tImaginary\n")
    for real, imag in zip(real_parts, imag_parts):
        file.write(f"{real}\t{imag}\n")

print("Roots are stored in 'roots.txt' file.")
