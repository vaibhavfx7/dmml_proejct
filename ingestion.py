import pandas as pd
import logging
import os

# Ensure logs directory exists
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)
# Download latest version
log_file = os.path.join(log_dir, "app.log")
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
try:
    path= "data\customer_churn_dataset-training-master.csv"
    data = pd.read_csv(path)
    logging.info("Data ingested")
except:
    # Configure logging

# Example log messages
    logging.error("Data ingestion failed")

print(data.head(5))

