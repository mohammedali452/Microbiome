import pandas as pd
import os

base_path = r"C:\Users\imohammed\Desktop\Microbiome"

sample_path = os.path.join(base_path, "Sample Info.tsv")
download_path = sample_path = os.path.join(base_path, "Download Links.tsv")

sample_sheet = pd.read_csv(sample_path, delimiter="\t", usecols=["sample_id"])
download_sheet = pd.read_csv(download_path, delimiter="\t", usecols=["sample_id"])

for i in sample_sheet.index:

    if sample_sheet["sample_id"][i] != download_sheet["sample_id"][i]:
        print(i + 1)
print(download_sheet)