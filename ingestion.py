import kagglehub
 
# Download latest version
path = kagglehub.dataset_download("muhammadshahidazeem/customer-churn-dataset")
 
print("Path to dataset files:", path)