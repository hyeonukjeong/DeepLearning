from os.path import *

import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread('./kr/hs/dgsw/nyup/hello_python/matplotlib/gd.png')

plt.imshow(img)
plt.show()
