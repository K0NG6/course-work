import numpy as np
from sympy import diff, symbols, cos, sin
x=symbols('x')
print(diff(diff(np.power(x, 4) + 2 * np.power(x, 3) - x - 1)))