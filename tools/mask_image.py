# import packages
from PIL import Image, ImageOps, ImageDraw
import os
import glob
import cv2
import numpy as np





# add masks to faces
def mask():

# image path and the path you want to save them
    content_list = ['/Users/a3055/Desktop/stim/ori/male/M', '/Users/a3055/Desktop/stim/ori/female/F']
    save_dir = ['/Users/a3055/Desktop/stim/colored/male/M', '/Users/a3055/Desktop/stim/colored/female/F']

    image_list = []
    for v in range(10):

        # the file name in my folder goes like /morphed/test_m/m1.jpg, /morphed/test_m/m2.jpg
        # change based on your needs
        # find each face in the loop
        for content in content_list:

            image_id = content + str(v+1)

            for i in range(11):

                if i < 10:

                    images = image_id + '_0' + str(i) + '.jpg'
                else:
                    images = image_id + '_10.jpg'


                image_list.append(images)

                filename = images


# add ellipse mask to each face change the shape parameter based on your need. You might need to try multiple times to find the best fit
                mask = Image.new("L", Image.open(filename).size, 0)
                draw = ImageDraw.Draw(mask)
                shape = [(479, 399), (867, 970)]
                draw.ellipse(shape, fill=255)

                # if you need grayscale mask. uncommet the lines below
                # stole from stackoverflow, but I cannot find the link
                # im2 = Image.new("L", Image.open(filename).size, 125)
                # im = Image.composite(Image.open(filename), im2, mask)
                
                #colored mask
                # stole from stackoverflow, but I cannot find the link
                im2 = Image.new("L", Image.open(filename).size, 125).convert('RGB')  # create a image SIZE x SIZE
                im = Image.composite(Image.open(filename).convert('RGB'), im2, mask).convert('RGB')



# save masked images to the directory
                im.save(content + '%s_%s_masked.jpg'% (int(v), int(i)))
                print(im)
# you have to imclud the line below, otherwise all the faces will automatically pop out and kill your laptop
                cv2.destroyAllWindows()




if __name__ == '__main__':
    # file_path = '/Users/a3055/Desktop/morphed_faces/'
    mask()



