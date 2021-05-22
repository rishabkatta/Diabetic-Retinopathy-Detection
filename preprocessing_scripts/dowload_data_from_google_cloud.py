from google.cloud import storage
from google.colab import auth
import os

def download_from_google_cloud(bucket_directory, local_directory):
    storage_client = storage.Client(project='cloud_tpu_tutorial')
    bucket = storage_client.get_bucket("diabetic-retinopathy-dataset")
    prefix = bucket_directory
    dl_dir = local_directory

    blobs = bucket.list_blobs(prefix=prefix)  # Get list of files
    for blob in blobs:
        print(os.path.basename(blob.name))
        filename = os.path.basename(blob.name)
        blob.download_to_filename("/" + dl_dir + filename)  # Download

    if not os.path.exists('./trained_models'):  # to store trained models in.
        os.makedirs('./trained_models')

    if not os.path.exists('./trained_hist'):  # to store trained history objects in.
        os.makedirs('./trained_hist')

auth.authenticate_user()
download_from_google_cloud(bucket_directory='data/', local_directory='../')
