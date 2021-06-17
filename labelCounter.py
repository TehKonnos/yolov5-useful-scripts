import os
from os import listdir,replace
from os.path import isfile,join
from tqdm import tqdm #For the flex
from pathlib import Path
import shutil


file="/train/"
output="./trash/"

pathToCheck="labels/"+file #Tou Train
totalLabels= [f for f in listdir(pathToCheck) if isfile(join(pathToCheck,f))]

toDelete = list()
counter=0
counter2=0
print("Scanning: ")
for label in tqdm(totalLabels):
    my_file=open(pathToCheck+label,"r")
    content=my_file.read()
    txt_classes=content.split("\n")
    my_file.close()
    flag=True
    #print("----------")
    for my_class in txt_classes:
        #print(my_class)
        c = my_class.split(" ")[0]
        if c!='': c = int(c)
        if c!=521 and c!='': flag = False
    if flag: toDelete.append(label)
#print(toDelete)
print("Other-Sign only images:",len(toDelete))
print("Images with at least 1 label different:",len(totalLabels) - len(toDelete))

print("Deleting...")
os.makedirs(output+"labels/", exist_ok=True)
os.makedirs(output+"images/", exist_ok=True)

for label in tqdm(toDelete):
    name = label.rsplit(".",1)[0]
    shutil.move(pathToCheck+label, output+"labels/")
    shutil.move("images"+file+name+".jpg", output+"images/")
    