##This script extracts the zipped fastq/fasta files downloaded from the NIH HMP Page and places them in folders based on the subject they belong to. It also creates manifest files (Files that list the sample id and file path) for each patient so we can feed that file to qiime and create OTU Table

import os
import gzip
import shutil
import tarfile

Data_folder = r"DATA_PATH"
cnt = 1

#Extracting the .fastq.gz files to .fastq files in the same folder
for subject in os.listdir(Data_folder):
    subject_path = os.path.join(Data_folder, subject)
    decompressed_folder_path = os.path.join(subject_path, "Decompressed")

    try:
        os.mkdir(decompressed_folder_path)

    except FileExistsError:
        shutil.rmtree(decompressed_folder_path)
        os.mkdir(decompressed_folder_path)

    for compressed_file in os.listdir(subject_path):
        new_file_name = compressed_file.replace("fastq.gz", ".fastq")
        compressed_path = os.path.join(subject_path, compressed_file)
        new_file_path = os.path.join(decompressed_folder_path, new_file_name)

        try:

            try:
                input_file = tarfile.open(compressed_path, "r:bz2")
                input_file.extractall(path=decompressed_folder_path)

                temp_file_path = os.path.join(decompressed_folder_path, input_file.getnames()[0])
                os.rename(temp_file_path, new_file_path)

            except tarfile.ReadError:
                input_file = gzip.open(compressed_path, "rb")
                output_file = open(new_file_path, "wb")
                shutil.(copyfileobjinput_file, output_file)

                input_file.close()
                output_file.close()

        except PermissionError:
            pass

    print("File {}/{} subjects extracted".format(cnt, len(os.listdir(Data_folder))))
    cnt += 1

#Making manifest for each subject in a new folder (manifests are seperated by subject)
for folder in os.listdir(Data_folder):
    path2 = os.path.join(Data_folder, folder)
    for decomp_folder in os.listdir(path2):
        if decomp_folder.endswith(".gz"):
            pass
        else:
            header = "sample-id\tabsolute-filepath"
            file_list = [header]
            path = "{0}\\{1}"
            fastqCounter = 0
            for file in os.listdir(path2 + r"\\" + decomp_folder):
                if file.endswith(".fastq"):
                    fastqCounter += 1
                    samples = "sample-{0}\t{1}\\{2}\\{3}"
                    file_list.append(samples.format(fastqCounter, path2, decomp_folder, file))
                man_path = "{0}\\{1}\\subject_manifest.tsv"
                manifest_file = open(man_path.format(path2, decomp_folder), "w+")
                for i in range(len(file_list)):
                    if i == 0:
                        manifest_file.write(file_list[i])
                    else:
                        manifest_file.write("\n" + file_list[i])
                manifest_file.close()
