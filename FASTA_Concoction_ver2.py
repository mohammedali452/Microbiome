##This script combines all the fasta files into one file so we can feed it into QIIME and retrieve OTU Tables 

import os

data_folder = r"DATA_PATH"
content = []

for subject_folder in os.listdir(data_folder):
    decomp_folder_path = os.path.join(data_folder, subject_folder, "Decompressed")

    for file in os.listdir(decomp_folder_path):
        if file.endswith("tsv"):
            pass
        else:
            fasta_file_path = os.path.join(decomp_folder_path, file)
            fasta_file = open(fasta_file_path, "r")
            read = fasta_file.read()
            content.append(read)
            fasta_file.close()
    
master_fasta_path = os.path.join(data_folder, "Master_FASTA.fna")
master_fasta_file = open(master_fasta_path, "w+")
for i in range(len(content)):
    if i == 0:
        master_fasta_file.write(content[i])
    else:
        master_fasta_file.write("\n" + content[i])
master_fasta_file.close()
