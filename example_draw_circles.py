# Example code for the my_image module
# Description: Draw circles on all images in a directory

import my_image

# create ImageCollection from directory
images = my_image.ImageCollection.from_directory('images')

for i, image in enumerate(images):

    print(image)

    x_mid = image.x_mid()
    y_mid = image.y_mid()

    images[i] = image.draw_circle(
        x=x_mid, y=y_mid, # center cirlce in middle of image
        radius=min(x_mid, y_mid) // 2, # radius = min(width, height) / 2
        color=(0, 255, 255) # cyan
    )

# save edited images to directory
images.save_to_directory(directory='output', output_name='circles')