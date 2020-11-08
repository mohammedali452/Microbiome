from urllib import request
import os
import pandas as pd

base_path = r"C:\Users\imohammed\Desktop\Microbiome"

sample_path = os.path.join(base_path, "Sample Info.tsv")
download_path  = os.path.join(base_path, "Download Links.tsv")

database_path = os.path.join(base_path, "Database")

sample_sheet = pd.read_csv(sample_path, delimiter="\t", usecols=["sample_id", "subject_id"])
download_sheet = pd.read_csv(download_path, delimiter="\t", usecols=["sample_id", "urls"])


print("Downloading Poop Files")
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


            # if not os.path.exists(final_path):
            #     os.makedirs(final_path)

            request.urlretrieve(url_download, final_path + "\\" + temp_sample_id + "fastq.gz")
            #wget.download(url_download, os.path.join(final_path, temp_subject_id + ".fastq.gz"))
            print("Poop Sample " + str(cnt) + " downloaded")
            cnt += 1

        except:
            print(temp_sample_id)

print("Poop downloaded")