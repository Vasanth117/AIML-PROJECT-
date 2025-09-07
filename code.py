import os

extract_dir = "/content/plant_disease_dataset"

# List all files in the folder
for root, dirs, files in os.walk(extract_dir):
    for name in files:
        print(os.path.join(root, name))


import os
import pandas as pd

# Path to the extracted folder
extract_dir = "/content/plant_disease_dataset"

# List all files
file_list = []
for root, dirs, files in os.walk(extract_dir):
    for name in files:
        full_path = os.path.join(root, name)
        file_list.append(full_path)

# Create a DataFrame
df = pd.DataFrame(file_list, columns=["File Path"])

# Save to Excel
excel_output = "/content/plant_disease_dataset/file_list.xlsx"
df.to_excel(excel_output, index=False)

print(f"File list saved to {excel_output}")


from google.colab import files

files.download("/content/plant_disease_dataset/file_list.xlsx")
