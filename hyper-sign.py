import numpy as np
import matplotlib.pyplot as plt

def generate_signature(width, height, max_iter):
    """
    Generate a self-rewriting combinatorial graph's discrete 2D signature using spherical harmonics.
    """
    # Grid
    x, y = np.linspace(-1,1,width), np.linspace(-1,1,width)
    X, Y = np.meshgrid(x,y)
    Z = X + 1j * Y
    output = np.zeros(Z.shape, dtype=float)

    for i in range(max_iter):
        mask = np.abs(Z) <= 1
        if mask.any():
            Z+=np.sin(np.linspace(-np.pi,np.pi,height))[:,None]*-np.cos(np.linspace(-np.pi,np.pi,width))
        output+=mask/max_iter


    return np.clip(output,0,1)

width,height=256,256
signature=generate_signature(width,height,69)
plt.figure(figsize=(width/100,height/100),dpi=100)
plt.axis('off')
plt.imshow(signature,extent=(-1,1,-1,1))
output_path = "sign.png"
plt.savefig(output_path,bbox_inches='tight',pad_inches=0)
plt.close()

