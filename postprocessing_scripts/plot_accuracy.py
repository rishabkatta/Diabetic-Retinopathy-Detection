import pickle
import matplotlib.pyplot as plt

def plot_accuracy(history_file_path):
  pickle_in=open(history_file_path,'rb')
  history=pickle.load(pickle_in)
  plt.plot(history['accuracy'], label=' Accuracy(testing data)')
  plt.plot(history['val_accuracy'], label=' Accuracy (validation data)')
  plt.title('Accuracy for Diabetic Retinopathy Detection')
  plt.ylabel('Accuracy')
  plt.xlabel('No. epoch')
  plt.legend(loc="upper left")
  plt.show()

plot_accuracy(history_file_path='../trained_hist/clahe_iv3.history')