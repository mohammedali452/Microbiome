##Script that counts the number of FASTQ/FASTA files each patient has. Each patient had multiple samples so we wanted to see the range of samples each patient had.

import pandas as pd
import os

##Folder that holds all the FASTQ/FASTA Samples. 
base_path = r"DATA_FOLDER"

database_files = os.listdir(base_path)
sample_count = {}

##Each subdirectory within base_path represents a patient
for file in database_files:
    subject_path = os.path.join(base_path, file)
    subject_dir = os.listdir(subject_path)

    cnt = 0
    
    ## Counts the number of samples within a particular patient directory
    for seq in subject_dir:
        cnt += 1

    sample_count[file] = cnt

##Prints the the number of sample each patient has
print(sample_count)

