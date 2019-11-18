#access args[0] directory from launch.json
#var annotatedFiles = get all .txt files != classes.txt
#var classfile = get classes.txt from dir
#var dictionary = or whatever matrix of class - count (int classId, int numAnnotated)
#open each annotatedfile and incremement each new line first char corresponding with classId
#print out final tally list of the dictionary with classId converted to className

import os
import json
import glob

##Open the files/directories
launchOptionsFile = open(".vscode\\launch.json","r")
launchOptionsJson = json.loads(launchOptionsFile.read())
fileDirectory = launchOptionsJson["configurations"][0]["args"][0]
classFile = open(launchOptionsJson["configurations"][0]["args"][1])

classes = classFile.read().split('\n')
dictionaryOfClasses = {}
dictionaryOfClassCount = {}

##Initialize Class Dictionaries
count = 0
for annotationClass in classes:
    if(len(annotationClass) > 0):
        dictionaryOfClasses[count] = annotationClass
        dictionaryOfClassCount[count] = 0
        count += 1

##Tally the classes
for fileName in glob.glob(os.path.join(fileDirectory, '*.txt')):
    annotatedFile = open(fileName)
    annotations = annotatedFile.read()
    annotationSplit = annotations.split('\n')
    for split in annotationSplit:
        if(len(split) > 0):
            try:
                classNum = int(split[0])
                dictionaryOfClassCount[classNum] += 1
            except ValueError:
                pass 
                
prettyDictionary = {}

for key in dictionaryOfClasses:
    prettyDictionary[dictionaryOfClasses[key]] = dictionaryOfClassCount[key]
    
print(dictionaryOfClasses)
print(dictionaryOfClassCount)
print('\n')   
print(prettyDictionary)