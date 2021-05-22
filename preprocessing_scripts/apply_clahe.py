import cv2
import os, sys

def apply_clahe(src_folder, dst_folder):
    img_names_list = os.listdir(src_folder)
    if not os.path.exists(dst_folder):
        os.makedirs(dst_folder)

    for img in img_names_list:
        if img.endswith('.jpeg'):
            img2 = cv2.imread(src_folder + img, cv2.IMREAD_UNCHANGED)
            clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
            b, g, r = cv2.split(img2)
            cl_b = clahe.apply(b)
            cl_g = clahe.apply(g)
            cl_r = clahe.apply(r)
            cl_rgb = cv2.merge([cl_b, cl_g, cl_r])
            cv2.imwrite(dst_folder + img, cl_rgb)

    print("Histogram Equalization successfully applied on training dataset.")


apply_clahe(src_folder='../processed_299_299/', dst_folder='../clahe_processed_299_299/')