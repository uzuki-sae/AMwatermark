# Import libraries
from matplotlib.image import imread
import matplotlib.pyplot as plt
import numpy as np
import click
from tqdm import tqdm
from DFT import fft2d
window = [12, 12]
overlay = [2, 2]
band = [3, 3]
@click.command()
@click.argument('image')
@click.option('--show',default=True)
def stft(image, show=True):
    
    # Read data & check to display
    fig = imread(image)
    fig = np.mean(fig, -1)
    if show:
        plt.imshow(fig)
        plt.show()
    print(f'Window: {window}')
    fig_h, fig_w = fig.shape
    print(f'image size:{fig.shape}')
    hout=[]
    for h in tqdm(range(0, fig_h-window[0]-1, overlay[0])):
        
        wout=[]
        for w in range(0, fig_w-window[1]-1, overlay[1]):
            
            win=fig[h:h+window[0],w:w+window[1]]
            #print(w,h)
            #print(win)
            f=fft2d(win,show=False)
            f=np.abs(f)
            f=float(f[band[0]][band[1]])
            wout.append(f)
            #print(wout)
        hout.append(wout)
    #print(hout)
    plt.imshow(hout)
    plt.show()

if __name__ == '__main__':
    stft()
    

