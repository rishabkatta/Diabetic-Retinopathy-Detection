# Predict on validation data
import os
import pickle
import numpy as np
import math

from keras.preprocessing import image
from keras.applications.inception_v3 import preprocess_input
from scipy.special import softmax
import csv


def classify_data(pickle_model_file_path, validation_data_folder_path, validation_labels_file_path):
    pickle_in = open(pickle_model_file_path, 'rb')
    model = pickle.load(pickle_in)
    data_path = validation_data_folder_path
    img_names_list = os.listdir(data_path)
    predictions_dict = dict()
    for img_name in img_names_list:
        if img_name.endswith('.jpeg'):
            img_path = data_path + img_name
            img = image.load_img(img_path, target_size=(299, 299))
            x = image.img_to_array(img)
            x = np.expand_dims(x, axis=0)
            x = preprocess_input(x)
            features = model.predict(x)
            index = np.argmax(softmax(features)[0])
            predictions_dict[img_name] = index

    with open(validation_labels_file_path) as csv_file:
        reader = csv.reader(csv_file)
        temp_dict = dict(reader)
    gt_dict = {}
    for k, v in temp_dict.items():
        k = (k.encode('ascii', 'ignore')).decode("utf-8")
        v = int(v)
        gt_dict[k] = v
    count = 0
    for img_name, y_true in gt_dict.items():
        y_pred = predictions_dict[img_name + ".jpeg"]
        if y_true == y_pred:
            count += 1

    print("Accuracy: ", round((count / len(predictions_dict)),3))


classify_data(pickle_model_file_path='../trained_models/trained_inceptionv3.pkl',
              validation_data_folder_path='../validation_processed_299_299/',
              validation_labels_file_path='../validationLabels.csv')