import kagglehub
import os
import shutil

path = kagglehub.dataset_download("maitam/vietnamese-traffic-signs")

destination_path = '/kaggle'
os.makedirs(destination_path, exist_ok=True)
shutil.move(path, destination_path)
print("Path to dataset files:", destination_path)

