# yolov5-useful-scripts
Some usefull scripts, &lt;made with python>, to help me, my m8 and all of the yolov5 users play with their datasets and more.


### MakeDataset.py

MakeDataset.py helps you extract some images from your original dataset easy, with their labels, so you can have a "test" training dataset.

You can use it for example like this:
` python MakeDataset.py -n 1000 -y ` 

Note that the py file has to be inside the original's dataset directory, next to images and labels folders.
-n is for the number of files you want to extract and -y is to copy your yaml file (must be included in the same directory.)
