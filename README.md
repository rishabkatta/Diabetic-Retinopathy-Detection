**INSTRUCTIONS ON HOW TO EXECUTE** <br/>

* Download train.zip.001 dataset and trainLabels.csv from Kaggle.(Due to hardware restrictions training/testing is done only one dataset.) 
* Link to download: https://www.kaggle.com/c/diabetic-retinopathy-detection/data
(May require to sign in)
* remove blurry images by running preprocessing_scripts/remove_blurry_images
* Remove background noise from images by running preprocessing_scripts/remove_background.py
* Then resize the image to (299 x 299) by giving appropriate folder path and image_height and image_width to preprocessing_scripts/resize_images.py
* Apply clahe to resized images by running preprocessing_scripts/apply_clahe.py
* Now run training on clahe applied images by running training_scripts/train_inceptionv3.py by giving appropriate arguments
* After training is completed trained_models/*.pkl and trained_hist/*.history will be generated.
* Now run post processing_scripts/plot_accuracy.py to generate accuracy plots and postprocessing_scripts/predict.py to run the model on unseen data.

**INSTRUCTIONS ON HOW TO QUICKLY TEST THE TRAINED MODEL** <br/>

*I'm uploading the trained model and trained history objects directly to my GitLab account, in order for the grader to quickly test the model.
* cd into postprocessing_scripts/ in a terminal
* Directly run <br/>"python3 plot_accuracy.py", <br/>"python3 plot_cce.py", <br/>"python3 predict.py"
* requires matplolib, numpy, scipy, keras. If not available install using "pip3 install < package_name >"
* It assumes some files are present in certain folders. If not please try to get those files into appropriate folders or change the parameter names and run again.

