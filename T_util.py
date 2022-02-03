import numpy as np
from PIL import Image
from IPython.display import Image as Image_dsp
import matplotlib.pyplot as plt

def plotImgPair(img1, img2, cm = 'gray', title=['','']):
    fig, ax = plt.subplots(1, 2, figsize=(15, 20))
    for i,a in enumerate(ax):
        a.set_axis_off()
        if title[i] != '':
            a.set_title(title[i])
    ax[0].imshow(img1, cmap=cm)    
    ax[1].imshow(img2, cmap=cm)

def imAdjust(I, thres=[1,99]):
    # compute percentile: remove too big or too small values
    I_low, I_high = np.percentile(I.reshape(-1), thres)
    # thresholding
    I[I > I_high] = I_high
    I[I < I_low] = I_low
    # scale to 0-1
    I = (I.astype(float)- I_low)/ (I_high-I_low)
    # convert it to uint8
    I = (I * 255).astype(np.uint8)
    return I

def dispGif(img1, img2, filename='tmp.gif'):
    im1 =  Image.fromarray(img1)
    im2 =  Image.fromarray(img2)
    im1.save(filename, format='GIF',
                   append_images=[im2],
                   save_all=True,
                   duration=300, loop=0)
    return Image_dsp(open(filename,'rb').read())    
