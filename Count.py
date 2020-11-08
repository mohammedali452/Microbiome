import pandas as pd
import os
import csv
from matplotlib import pyplot as plt

base_path = r"C:\Users\imohammed\Desktop\Microbiome\Database"
# sample_path = os.path.join(base_path, "Sample Info.tsv")
#
# sample_sheet = pd.read_csv(sample_path, delimiter="\t", usecols=["subject_id"])
# sample_count = {}
#
#
# for i in sample_sheet.index:
#     id = sample_sheet["subject_id"][i]
#
#     if id not in sample_count:
#         sample_count[id] = 1
#
#     else:
#         sample_count[id] += 1
#
# print(sample_count)

database_files = os.listdir(base_path)
sample_count = {}

for file in database_files:
    subject_path = os.path.join(base_path, file)
    subject_dir = os.listdir(subject_path)

    cnt = 0

    for seq in subject_dir:
        cnt += 1



    sample_count[file] = cnt

print(sample_count)

