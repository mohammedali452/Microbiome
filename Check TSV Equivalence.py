##Script that checks if sample ids that identify indivual sampples are equivalent in both the tsv that provide subject information and the download tsv with the download links
import pandas as pd
import os

base_path = r"BASE_PATH"

sample_path = os.path.join(base_path, "Sample Info.tsv")
download_path = sample_path = os.path.join(base_path, "Download Links.tsv")

sample_sheet = pd.read_csv(sample_path, delimiter="\t", usecols=["sample_id"])
download_sheet = pd.read_csv(download_path, delimiter="\t", usecols=["sample_id"])

for i in sample_sheet.index:

    if sample_sheet["sample_id"][i] != download_sheet["sample_id"][i]:
        print(i + 1)
print(download_sheet)
