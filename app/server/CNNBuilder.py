import base64
from flask import Flask, request
from tensorflow import keras
import numpy as np
import cv2 as cv
import numpy as np
import os
from sklearn.model_selection import KFold
from pathlib import Path

from tensorflow.python.ops.gen_batch_ops import batch

train_path = "dataset/train"
num_classes = 5
height = 256
width = 256
epochs = 22
inputDim = height*width

def loadImages(datasetFolder, num_categories):
    images = []
    estimed = []
    categories = []
    for folder in os.walk(datasetFolder):
        if(folder[0] != datasetFolder):
            folderName = folder[0].split("\\")[1]
            categories.append(folderName)
            classPath = datasetFolder+"/"+folderName
            Path(classPath).mkdir(parents=True, exist_ok=True)
            for source in folder[2]:
                img = cv.imread(datasetFolder+"/"+folderName+"/"+source)
                img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
                img = img.flatten()
                img = img/255
                images.append(img)
                prob = np.zeros(num_categories)
                prob[int(folderName)]=1
                estimed.append(prob)
    resultImg = np.array(images)
    estimedValues = np.array(estimed)
    return resultImg, estimedValues

model1 = keras.Sequential([
    keras.layers.InputLayer(input_shape=(inputDim, )),
    keras.layers.Reshape((width,height,1)),
    keras.layers.Conv2D(64, kernel_size=(4, 4), strides=2, activation='relu'),
    keras.layers.MaxPooling2D(2, 2),
    keras.layers.Conv2D(64, kernel_size=(3, 3), activation='relu'),
    keras.layers.MaxPooling2D(2, 2),
    keras.layers.Dropout(0.20),
    keras.layers.Flatten(),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(num_classes, activation='softmax')
])
model1.compile(
    loss='categorical_crossentropy',
    optimizer='adam',
    metrics=['accuracy', keras.metrics.Recall()]
)
model1.summary()

model2 = keras.Sequential([
    keras.layers.InputLayer(input_shape=(inputDim, )),
    keras.layers.Reshape((width,height,1)),
    keras.layers.Conv2D(32, kernel_size=(6, 6), activation='relu'),
    keras.layers.MaxPooling2D(2, 2),
    keras.layers.Conv2D(32, kernel_size=(4, 4), activation='relu'),
    keras.layers.MaxPooling2D(2, 2),
    keras.layers.Conv2D(32, kernel_size=(2, 2), activation='relu'),
    keras.layers.MaxPooling2D(2, 2),
    keras.layers.Dropout(0.10),
    keras.layers.Flatten(),
    keras.layers.Dense(128, activation='linear'),
    keras.layers.Dense(num_classes, activation='softmax')
])
model2.compile(
    loss='categorical_crossentropy',
    optimizer='adam',
    metrics=['accuracy', keras.metrics.Recall()]
)

model3 = keras.Sequential([
    keras.layers.InputLayer(input_shape=(inputDim, )),
    keras.layers.Reshape((width,height,1)),
    keras.layers.Conv2D(64, kernel_size=6,
                           activation='relu'),
    keras.layers.MaxPooling2D(4, 2),
    keras.layers.Dropout(0.25),
    keras.layers.Flatten(),
    keras.layers.Dense(64, activation='relu'),
    keras.layers.Dense(64),
    keras.layers.Dense(64, activation='relu'),
    keras.layers.Dense(num_classes, activation='softmax')
])
model3.compile(
    loss='categorical_crossentropy',
    optimizer='adam',
    metrics=['accuracy', keras.metrics.Recall()],
)


def kfoldValidator(model, X, y):
    kfd = KFold(n_splits=10, shuffle=True)
    print(X)
    for t, test in kfd.split(X, y):
        trainX, testX = X[t], X[test]
        trainY, testY = y[t], y[test]
        model.fit( trainX, trainY, validation_data=(testX, testY), epochs=epochs)

train_data, labels = loadImages("dataset/train", num_classes)         
print("model1")
kfoldValidator(model1, train_data, labels)
model1.save("model1.h5")
print("model2")
kfoldValidator(model2, train_data, labels)
model2.save("model2.h5")
print("model3")
kfoldValidator(model3, train_data, labels)
model1.save("model3.h5")