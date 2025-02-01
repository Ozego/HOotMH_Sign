import numpy as np
import matplotlib.pyplot as plt

def generate_signature(width, height, time, max_iter, entropy_scale):
    """
    Generate a self-rewriting combinatorial graph's discrete 2D signature using spherical harmonics.
    """
    # Grid
    x, y = np.linspace(-1,1,width), np.linspace(-1,1,width)
    X, Y = np.meshgrid(x,y)
    Z = X + 1j * Y
    output = np.zeros(Z.shape, dtype=float)

    return np.clip(output,0,1)

width,height=256,256
signature=generate_signature(width,height,1,69,0)
plt.figure(figsize=(width/100,height/100),dpi=100)
plt.axis('off')
plt.imshow(signature,extent=(-1,1,-1,1))
output_path = "sign.png"
plt.savefig(output_path,bbox_inches='tight',pad_inches=0)
plt.close()

