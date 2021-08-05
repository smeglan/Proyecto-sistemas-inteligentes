import numpy as np
import cv2 as cv
import os
import base64
import requests
import json

def shapeDetector(image):
    imgray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, thresh = cv.threshold(imgray, 127, 255, 0)
    contours, hierarchy = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    #tem = cv.drawContours(imgray, contours, -1 , (0,255,0), 20)
    #cv.imshow("Test", tem)
    max = 0
    maxCt = None
    for c in contours:
        peri = cv.arcLength(c, True)
        approx = cv.approxPolyDP(c, 0.04 * peri, True)
        if len(approx) == 4:
            x,y,w,h = cv.boundingRect(c)
            if(w*h>max):
                max = w*h
                maxCt = c
    return maxCt

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
            base64_bytes = base64.b64encode(buffer)
            jpg_as_text = base64_bytes.decode('utf-8')
            results.append({"id":img,"value":jpg_as_text})
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
        name = "images/"+str(count)+".jpg"
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
        print(len(images))
        req = {
            "id_client": 1, 
            "images": images,
            "models": [1, 2, 3]
        }
        req_json = json.dumps(req, indent=2)
        response = requests.post("http://127.0.0.1:5000/predict", json=req_json)
        print("response " + response.text)
    if k == 97:
        if(name != ""):
            lastImage = cv.imread(name)
            cv.imshow(name, lastImage)
    if k == 116:
        approx = shapeDetector(frame)
        if approx is not None:
            print("Creando recorte...")
            image = createCrop(frame, approx)
            retval, buffer = cv.imencode('.jpg', image)
            jpg_as_text = base64.b64encode(buffer)
            req = {
                "class_name": "Martillo", 
                "image": jpg_as_text
            }
            response = requests.post("http://127.0.0.1:5000/train", req)
            print(response.text) 
        else:
            print("No se creo recorte correctamente")
               
cv.destroyAllWindows()
