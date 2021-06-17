import os
from shutil import copyfile
from tqdm import tqdm
from pathlib import Path
import sys, getopt

#Get N files from given folder
def getFiles(path,stop,start):
    files=list()
    for filename in os.listdir(path)[start:(start+stop)]:
        files.append(filename)
    return files

def getCopy(images_path,labels_path,num):
    files=getFiles(images_path,num,start)
    os.makedirs(output+images_path, exist_ok=True)
    os.makedirs(output+labels_path, exist_ok=True)
    for file in tqdm(files):
        name = file.rsplit(".",1)[0]
        copyfile(images_path+file,output+images_path+file)
        copyfile(labels_path+name+".txt",output+labels_path+name+".txt")

def args(argv):
    global start,train_num,val_prc,yaml
    try:
        opts, args = getopt.getopt(argv,"hys:n:v:",["--start","--number","--validation","--yaml"])
    except getopt.GetoptError:
        print("Running with default settings.")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('MakeDataset.py -n <No. Files>')
            print("-s for the first file to start")
            print("-n for number of files")
            print("-v for validation %")
            print("-y to copy the data.yaml file")
            sys.exit()
        elif opt in ('-s', "--start"):
            start=int(arg)
        elif opt in ('-n', "--number"):
            train_num = int(arg)
        elif opt in ('-y',"--yaml"):
            yaml=True
        elif opt in ('-v',"--validation"):
            if arg>1:
                val_prc = float(arg/100)
            else:
                val_prc=float(arg)
        else:
            print("Running with default settings.")
            
#------------------------------
train_num=1000
val_prc = 0.2 #20% Default value
start=0
yaml = False
args(sys.argv[1:])
val_num = int(val_prc*train_num)
#------------------------------

#Make output file
output="./Dataset-"+str(train_num)+"/"
os.makedirs(output, exist_ok=True)

#Check to copy or not yaml file
if yaml:
    copyfile("data.yaml",output+"data.yaml")

#Prepare the paths for the next steps
ITPATH='images/train/'
IVPATH='images/validation/'
LTPATH='labels/train/'
LVPATH='labels/validation/'

print("Train set:")
getCopy(ITPATH,LTPATH,train_num)

print("Validation set:")
getCopy(IVPATH,LVPATH,val_num)

""" #Old way:
print("Train set:")
train_files=getFiles(ITPATH,train_num)
os.makedirs(output+ITPATH, exist_ok=True)
os.makedirs(output+LTPATH, exist_ok=True)
for file in tqdm(train_files):
    name = file.rsplit(".",1)[0]
    copyfile(ITPATH+file,output+ITPATH+file)
    copyfile(LTPATH+name+".txt",output+LTPATH+name+".txt")
    
print("Validation set:")
val_files=getFiles(IVPATH,val_num)
os.makedirs(output+IVPATH, exist_ok=True)
os.makedirs(output+LVPATH, exist_ok=True)
for file in tqdm(val_files):
    name = file.rsplit(".",1)[0]
    copyfile(IVPATH+file,output+IVPATH+file)
    copyfile(LVPATH+name+".txt",output+LVPATH+name+".txt")
"""
