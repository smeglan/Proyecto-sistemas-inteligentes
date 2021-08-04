import numpy as np
import cv2 as cv
import os
import base64
import requests

def shapeDetector(image):
    imgray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, thresh = cv.threshold(imgray, 127, 255, 0)
    contours, hierarchy = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    for c in contours:
        peri = cv.arcLength(c, True)
        approx = cv.approxPolyDP(c, 0.04 * peri, True)
        if len(approx) == 4:
            return c
    return None

def createCrop(image, approx):
    points = np.squeeze(approx)
    x = points[:, 0]
    y = points[:, 1]
    (topy, topx) = (np.min(y), np.min(x))
    (bottomy, bottomx) = (np.max(y), np.max(x))
    out = image[topy:bottomy+1, topx:bottomx+1]
    return out

def loadImages(directory = "images"):
    results = []
    for folder in os.walk(directory):
        for img in folder[2]:
            loadedImage =cv.imread(directory+"/"+img)
            retval, buffer = cv.imencode('.jpg', loadedImage)
            jpg_as_text = base64.b64encode(buffer)
            results.append({"id": img, "image":jpg_as_text})
    return results

video = cv.VideoCapture(0)
count = 0
name = ""
width = 256
height = 256
dimensions =(width, height)
while True:
    _, frame = video.read() 
    cv.imshow("Imagen ROI", frame)
    k = cv.waitKey(5)
    if k != -1:
        print(k)
    if k == 27:
        break
    if k == 99:
        name = "images/img"+str(count)+".jpg"
        approx = shapeDetector(frame)
        if approx is not None:
            print("Creando recorte...")
            image = createCrop(frame, approx)
            imgray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
            resized = cv.resize(imgray, dimensions, interpolation=cv.INTER_AREA)
            #cv.imshow(name, resized)
            cv.imwrite(name, resized)
        else:
            print("No se creo recorte correctamente")
        count+=1
    if k == 101:
        images = loadImages()
        req = {
            "id_client": 1, 
            "images": images,
            "models": [1, 2, 3]
        }
        response = requests.post("http://127.0.0.1:5000/predict", req)
        print(response.text)
    if k == 97:
        if(name != ""):
            lastImage = cv.imread(name)
            cv.imshow(name, lastImage)
cv.destroyAllWindows()