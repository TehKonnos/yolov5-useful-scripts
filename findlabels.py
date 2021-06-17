import json
import os
import csv
from tqdm import tqdm #For the progress bar

#Set paths
mypath = "./mtsd_v2_fully_annotated/annotations/"


#Read all json files in a folder
for file in tqdm(os.listdir(mypath)):
    if file.endswith(".json"):
        json_name=file
        txt_name = json_name.rstrip(".json") + ".txt"
        """ Open input text files """
        txt_path = mypath + json_name
        with open(txt_path) as f:
            data = json.load(f)

        the_list = []

        for objects in data['objects']:
            if objects['label'] not in list:
                the_list.append(objects['label'])
        f.close()

        print("Total Labels: ",len(the_list))

        with open("final_labels","w+") as file:
            for i in the_list:
                    print(i,file=file)
print("Done!")