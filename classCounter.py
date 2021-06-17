from os import listdir

from os.path import isfile,join

from shutil import copyfile,copy

from tqdm import tqdm #For the flex

from pathlib import Path

pathToCheck="../'Διπλωματική'/'Data & Dataset'/output/" #Tou Train
totalLabels= [f for f in listdir(pathToCheck) if isfile(join(pathToCheck,f))]

dict={}
counter=0
a_file=open("Mapilary.txt")
for line in a_file:
    dict[str(counter)]=0
    counter = counter + 1
a_file.close()



for label in tqdm(totalLabels):
    my_file=open(pathToCheck+label,"r")
    content=my_file.read()
    txt_classes=content.split("\n")
    my_file.close()
    for my_class in txt_classes:
        c = my_class.split(" ")[0]
        if str(c) in dict:
           # if dict[str(c)] < 1500:
            dict[str(c)] = dict[str(c)] +1
           # else:
            #    if str(c)!='521':
             #       print("class is full:",str(c))
print(dict)
print("-----")
for i in dict:
    if dict[i] > 1500:
        print("Einai megalirero tou 1500:",i,"-",dict[i])



