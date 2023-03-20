# Example code for the my_image module
# Description: Segment image of retina into multiple regions with multi otsu thresholding

import my_image
import os

image_name = 'retina.jpg'
image_path = os.path.join('images', image_name)
my_image = my_image.RGB_Image.from_file(image_path)

my_image = my_image.threshold_multiotsu()
my_image.show()