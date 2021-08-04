import cv2 as cv
import numpy as np
import os
from pathlib import Path

def drawContours(image):
    ret, thresh = cv.threshold(image, 127, 255, 0)
    contours, hierarchy = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    cv.drawContours(image, [contours], 0, (0,255,0), 3)
    imgray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    return imgray

def prepareToSaveRaw(image, width=256, height=256):
    dim = (width, height)
    image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    return cv.resize(image, dim, interpolation=cv.INTER_AREA)

def prepareToSaveContour(image, width=256, height=256):
    dim = (width, height)
    image = drawContours(image)
    image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    return cv.resize(image, dim, interpolation=cv.INTER_AREA)

def prepareToSaveGaussian(image, width=256, height=256):
    dim = (width, height)
    image = cv.GaussianBlur(image, (7,7), cv.BORDER_DEFAULT)
    image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    return cv.resize(image, dim, interpolation=cv.INTER_AREA)

def prepareToSaveCanny(image, width=256, height=256):
    dim = (width, height)
    image = cv.Canny(image, 125, 175)
    return cv.resize(image, dim, interpolation=cv.INTER_AREA)

def prepareToSaveGCanny(image, width=256, height=256):
    dim = (width, height)
    image = cv.GaussianBlur(image, (7,7), cv.BORDER_DEFAULT)
    image = cv.Canny(image, 125, 175)
    return cv.resize(image, dim, interpolation=cv.INTER_AREA)

def createDataSet(directory, datasetFolder="dataset"):
    Path(datasetFolder).mkdir(parents=True, exist_ok=True)
    for folder in os.walk(directory):
        if(folder[0] != directory):
            folderName = folder[0].split("\\")[1]
            classPath = datasetFolder+"/"+folderName
            Path(classPath).mkdir(parents=True, exist_ok=True)
            for source in folder[2]:
                img = prepareToSaveCanny(cv.imread(directory+"/"+folderName+"/"+source))
                cv.imwrite(classPath+"/canny"+source, img)  
                img = prepareToSaveGaussian(cv.imread(directory+"/"+folderName+"/"+source))
                cv.imwrite(classPath+"/gaussian"+source, img) 
                img = prepareToSaveCanny(cv.imread(directory+"/"+folderName+"/"+source))
                cv.imwrite(classPath+"/gcanny"+source, img)  
                img = prepareToSaveRaw(cv.imread(directory+"/"+folderName+"/"+source))
                cv.imwrite(classPath+"/raw"+source, img)         

datasetRoot = "dataset"
if not os.path.exists(datasetRoot):
    os.makedirs(datasetRoot)

createDataSet("raw_set", datasetRoot+"/train")

