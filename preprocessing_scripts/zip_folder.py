import shutil

def zip_folder(folder_to_be_zipped, zip_file_name):
  shutil.make_archive(zip_file_name, 'zip', folder_to_be_zipped)

zip_folder(folder_to_be_zipped='../trained_hist/', zip_file_name='trained_hist')