#Plot History: Categorical Cross-Entropy
import pickle
import matplotlib.pyplot as plt


def plot_cce(history_file_path):
  pickle_in=open(history_file_path,'rb')
  history=pickle.load(pickle_in)
  plt.plot(history['loss'], label=' Categorical Cross-Entropy (testing data)')
  plt.plot(history['val_loss'], label=' Categorical Cross-Entropy (validation data)')
  plt.title('Categorical Cross-Entropy  for Diabetic Retinopathy Detection')
  plt.ylabel('CCE value')
  plt.xlabel('No. epoch')
  plt.legend(loc="upper left")
  plt.show()

plot_cce(history_file_path='../trained_hist/clahe_iv3.history')