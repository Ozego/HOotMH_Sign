import numpy as np
import matplotlib.pyplot as plt

def hypershpere_signature(width,height,max_iter):
    # Grid
    x, y = np.linspace(-8, 8, width), np.linspace(-8, 8, height)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y
    output = np.zeros(Z.shape, dtype = float)
    Phi,phi=( _ := 5 ** .5 * .5) + .5, _ - .5
    for i in range(max_iter):
        mask = np.abs(Z) <= 1
        output += mask
        Z += Z * (0 + 1j * phi) + np.sqrt(5)
    return np.clip(output, 0, 1)

width, height = 512, 512
signature=hypershpere_signature(width, height, 69)
plt.figure(figsize = (width / 100, height / 100), dpi = 100)
plt.axis('off')
plt.imshow(signature, extent=(-1, 1, -1, 1))
output_path = "sign.png"
plt.savefig(output_path,bbox_inches = 'tight', pad_inches=0)
plt.close()

