##This script downloads the different FASTQ/FASTA files from the NIH Human Microbiome Project page. We were able to download tsv files that held the download links which we accessed via this script. We were also able to add the downloaded files to specific folders that were organized by subjects in order to keep track each subjects' individual sample
from urllib import request
import os
import pandas as pd

base_path = r"BASE_DIRECTORY"

sample_path = os.path.join(base_path, "Sample Info.tsv")
download_path  = os.path.join(base_path, "Download Links.tsv")

database_path = os.path.join(base_path, "Database")

sample_sheet = pd.read_csv(sample_path, delimiter="\t", usecols=["sample_id", "subject_id"])
download_sheet = pd.read_csv(download_path, delimiter="\t", usecols=["sample_id", "urls"])


print("Downloading Files")
cnt = 1
for i in sample_sheet.index:

    if download_sheet["urls"][i] == "Private: Data not accessible via the HMP DACC.":
        pass

    else:

        try:
            temp_subject_id = sample_sheet["subject_id"][i]
            temp_sample_id = sample_sheet["sample_id"][i]
            final_path = os.path.join(database_path, temp_subject_id)

            if not os.path.exists(final_path):
                os.makedirs(final_path)

            url_download = download_sheet["urls"][i]

            request.urlretrieve(url_download, final_path + "\\" + temp_sample_id + "fastq.gz") ##Change to .fna as some diseases (i.e. Type 2 Diabeties are in fasta format)
            print("Sample " + str(cnt) + " downloaded")
            cnt += 1

        except:
            print(temp_sample_id)

print("Files downloaded")
