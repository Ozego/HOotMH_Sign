import numpy as np
import matplotlib.pyplot as plt

def generate_signature(width, height, max_iter):
    """
    Generate a self-rewriting combinatorial graph's discrete 2D signature using spherical harmonics.
    """
    # Grid
    x, y = np.linspace(-8,8,width), np.linspace(-8,8,width)
    X, Y = np.meshgrid(x,y)
    Z = X + 1j * Y
    output = np.zeros(Z.shape, dtype=float)
    Phi,phi=(_:=5**.5*.5)+.5,_-.5
    for i in range(max_iter):
        mask = np.abs(Z) <=2
        if mask.any():
            Z+=Z*(phi+1j*phi)+np.pi
        output+=mask/max_iter
    return np.clip(output,0,1)

width,height=256,256
signature=generate_signature(width,height,9)
plt.figure(figsize=(width/100,height/100),dpi=100)
plt.axis('off')
plt.imshow(signature,extent=(-1,1,-1,1))
output_path = "sign.png"
plt.savefig(output_path,bbox_inches='tight',pad_inches=0)
plt.close()

