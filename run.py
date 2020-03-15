# global imports
from PIL import Image
from matplotlib import image
from matplotlib import pyplot
import numpy as np
from numpy import asarray

def plot_image(imagedata):
    pyplot.imshow(imagedata)
    pyplot.show()
    
    
def invert(image, plot=True):
    inputdata = asarray(image)
    outputdata = np.zeros_like(inputdata)
    plot_image(inputdata)
    
    origin = int(inputdata.shape[0] / 2) , int(inputdata.shape[1] / 2) 
    radius = int(min(origin[0], origin[1]) / 2)
    
    standard_array = outputdata[0,0]
   
    m = inputdata.shape[0]
    n = inputdata.shape[1]
    
    
    for i in range(m):
        for j in range(n):
            xp = i-origin[0]
            yp = j-origin[1]
            b = ((xp)**2 + (yp)**2)**0.5
            if b != 0:
                #outside
                x = (radius**2 / b**2) * xp + origin[0]
                y = (radius**2 / b**2) * yp + origin[1]
                
                x = min(x, n-1)
                x = max(x, 0)
                y = min(y, m-1)
                y = max(y, 0)
                
                outputdata[i,j] = inputdata[int(y), int(x)]
    if plot:
        plot_image(outputdata)
    return outputdata


basic_images   = ['plain_line.png', 'colorful.png']
picture_images = ['pencils.png', 'present.png', 'plant.png']
checkerboard   = ['checkerboard{}.png'.format(i+1) for i in range(3)]
images_files =  checkerboard

for file in images_files:
    image = Image.open('images/' + file)
    outputdata = invert(image)
    invert(outputdata)
    
# invert process: