import kaggle

# Authenticate using your API token
kaggle.api.authenticate()

# Specify the dataset you want to download
dataset_name = 'kannanaikkal/food-demand-forecasting '

# Set the path where you want to download and unzip the dataset
download_path = './data/'

# Download and unzip the dataset
kaggle.api.dataset_download_files(dataset_name, path=download_path, unzip=True)
