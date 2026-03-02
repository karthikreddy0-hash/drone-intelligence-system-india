import os

print("Running Data Pipeline...")

# Step 1: Generate Synthetic Data
os.system("python generate_synthetic_data.py")

# Step 2: Preprocess Data
os.system("python preprocess_data.py")

print("Data Pipeline Completed Successfully!")