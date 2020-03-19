import os
#batches of 100
nextBatch = 100

batchCounter = 0
fileCounter = 1
batchName = ""
thisFile = os.path.realpath(__file__)

for filename in os.listdir("."):
    if(fileCounter % nextBatch == 1):
        batchCounter += 1
        batchName = "bn" + str(batchCounter)
        os.mkdir(batchName)
        fileCounter = 1
    path = os.getcwd() + "/"
    currentFile = path + filename
    extension = os.path.splitext(currentFile)[1]
    
    if(currentFile == thisFile):#do not batch this file (batchPartitioner.py) with other files
        continue
    renamed = path + "/" + batchName + "/bn" + str(batchCounter) + "n" + str(fileCounter) + extension
    os.rename(currentFile, renamed)
    fileCounter += 1
