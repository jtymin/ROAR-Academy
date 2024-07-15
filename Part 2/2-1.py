#2
from matplotlib import image
from matplotlib import pyplot
import os

path = os.path.dirname(os.path.abspath(__file__))
filename = path + '/' + 'lenna.bmp'
data = image.imread(filename)

path2 = os.path.dirname(os.path.abspath(__file__))
filename2 = path2 + '/' + 'south-korea-flag-xs.jpg'
data2 = image.imread(filename2)

plot_data = data.copy()
plot_data2 = data2.copy()
for width in range(250):
    for height in range(167):
        plot_data[height][width+262] = plot_data2[height][width]

pyplot.imshow(plot_data)
pyplot.show()