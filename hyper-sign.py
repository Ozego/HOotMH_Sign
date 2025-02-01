import numpy as np
import matplotlib.pyplot as plt

def generate_signature(width, height, max_iter):
    """
    Generate a self-rewriting combinatorial graph's discrete 2D signature using spherical harmonics.
    """
    # Grid
    x, y = np.linspace(-3,3,width), np.linspace(-3,3,width)
    X, Y = np.meshgrid(x,y)
    Z = X + 1j * Y
    output = np.zeros(Z.shape, dtype=float)

    for i in range(max_iter):
        mask = np.abs(Z) <= 1
        Z[mask]=Z[mask]**2 +complex(.69,-.69)
        if mask.any():
            factor = np.exp(-i/max_iter)
            pattern = np.cos(np.linspace(0,np.pi,height))[:,None]*np.sin(np.linspace(0,np.pi,width))
            pattern = (pattern-0.5)*factor
            Z+=pattern
        output+=mask


    return np.clip(output,0,1)

width,height=256,256
signature=generate_signature(width,height,69)
plt.figure(figsize=(width/100,height/100),dpi=100)
plt.axis('off')
plt.imshow(signature,extent=(-1,1,-1,1))
output_path = "sign.png"
plt.savefig(output_path,bbox_inches='tight',pad_inches=0)
plt.close()

