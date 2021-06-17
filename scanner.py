from os import listdir

from os.path import isfile,join

from shutil import copyfile,copy

from tqdm import tqdm #For the flex

from pathlib import Path



my_file=open("val.txt","r")
content=my_file.read()
content_list=content.split("\n")
my_file.close()
print ("Total Output:",len(content_list))


outPath="./output/"
Path(outPath).mkdir(parents=True,exist_ok=True)

pathToCheck="./validation2/"
onlyLabels= [f for f in listdir(pathToCheck) if isfile(join(pathToCheck,f))]
print ("Total Input",len(onlyLabels))

for label in tqdm(onlyLabels):
    if(label.split(".")[0] in content_list):
        copy(pathToCheck+label,outPath)