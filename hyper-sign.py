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
        r = 7
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

width, height = 512, 512
signature=hypershpere_sign(width, height, 13)
plt.figure(figsize = (width / 100, height / 100), dpi = 100)
plt.axis('off')
plt.imshow(signature, extent=(-1, 1, -1, 1))
output_path = "sign.png"
plt.savefig(output_path,bbox_inches = 'tight', pad_inches=0)
plt.close()

