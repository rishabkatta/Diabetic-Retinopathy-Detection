from PIL import Image
import os, sys

def resize_images(path, image_height, image_width):
  dirs = os.listdir( path )
  for item in dirs:
      if os.path.isfile(path+item) and item.endswith('.jpeg'):
          im = Image.open(path+item)
          f, e = os.path.splitext(path+item)
          imResize = im.resize((image_height,image_width), Image.ANTIALIAS)
          imResize.save(f + '.jpeg', 'JPEG', quality=100)

resize_images(path='../validation_processed_299_299/', image_height=299, image_width=299)