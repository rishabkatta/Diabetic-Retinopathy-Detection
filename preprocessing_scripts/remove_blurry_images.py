import cv2
import os


def remove_blurry_images(src_folder):
  img_names_list = os.listdir(src_folder)

  for img in img_names_list:
      if img.endswith('.jpeg'):
          img2 = cv2.imread(src_folder+img, cv2.IMREAD_GRAYSCALE)
          laplacian_var = cv2.Laplacian(img2, cv2.CV_64F).var()
          if laplacian_var < 10:
              print(img + " :Image blurry")
              os.remove(src_folder+img)

remove_blurry_images(src_folder = '../processed_299_299/')