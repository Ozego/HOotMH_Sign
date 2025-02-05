"""
Copyright (c) 2025 𝔖

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

import numpy as np
import matplotlib.pyplot as plt

Phi,phi=( _ := 5 ** .5 * .5) + .5, _ - .5

"""
Complex imaginary fractal tentacles of rotational reflected hyperspheres
"""
def hypershpere_sign(width,height,max_iter):
    # Grid
    x, y = np.linspace(-4, 4, width), np.linspace(-4, 4, height)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y
    output = np.zeros(Z.shape, dtype = float)
    for i in range (2):
        Z = X + 1j * Y
        r = 6
        offset = -np.pi/r*2
        zeta = (np.pi/( .5 * r)) * np.floor( .5 * r * np.angle(Z)/np.pi + .5 * r +.5)
        spin = (np.sin(zeta)+np.cos(zeta)*1j)
        Z *= spin
        if (i==1):
            Z *= np.cos(offset)+np.sin(offset)*1j 
        theta = np.pi * .25
        for j in range(max_iter):
            output += 1 - np.abs(Z) > 0
            scalar = Phi
            Z *= scalar
            Z += (scalar + 1) * 1j 
            Z *= np.cos(theta) + np.sin(theta) * 1j

    return np.clip(output, 0, 1)

width, height = 1024, 1024
signature=hypershpere_sign(width, height, 13)
plt.figure(figsize = (width / 100, height / 100), dpi = 100)
plt.axis('off')
plt.imshow(signature, extent=(-1, 1, -1, 1))
output_path = "sign.png"
plt.savefig(output_path,bbox_inches = 'tight', pad_inches=0)
plt.close()

