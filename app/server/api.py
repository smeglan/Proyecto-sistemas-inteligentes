import base64
import json
from flask import Flask, request
from tensorflow import keras
import numpy as np
import cv2 as cv

app = Flask(__name__)
models = []
models.append(keras.models.load_model('model1.h5', compile=True))
models.append(keras.models.load_model('model2.h5', compile=True))
models.append(keras.models.load_model('model3.h5', compile=True))


def runCNN(list, images):
    global models
    results = []
    for i in list:
        count = 0
        for image in images:
            im_bytes = base64.b64decode(image["value"])
            # im_arr is one-dim Numpy array
            im_arr = np.frombuffer(im_bytes, dtype=np.uint8)
            img = cv.imdecode(im_arr, flags=cv.IMREAD_GRAYSCALE)
            img = img.flatten()
            img = img/255
            predict = models[i].predict(img)
            results.append({
                "model_id": i,
                "results": {
                    "id": images["id"],
                    "class": np.argmax(predict, axis=1),
                }
            })
            count += 1
    return results


@app.route("/")
def test():
    return "<p>Hello, World!</p>"


@app.route("/predict", methods=["POST"])
def predict():
    content = request.get_json()
    data = json.loads(content)
    id_client = data["id_client"]
    images = data["images"]
    models = data["models"]
    res_predict = runCNN(models, images)
    if(res_predict is not None):
        result = {
            "state": "success",
            "message": "Predicciones realizadas correctamente.",
            "results": res_predict
        }
        return result
    else:
        errorMessage = {
            "state": "sucess",
            "message": "Problemas en el sistema de predicción"
        }
        return errorMessage


count = 0


@app.route("/train", methods=["POST"])
def train():
    global count
    class_name = request.form["class_name"]
    image = request.form["image"]
    name = "raw/"+class_name+"/"+str(count)+".jpg"
    with open(name, "wb") as fh:
        fh.write(base64.b64decode(image))
    result = {
        "state": "success",
        "message": "Imagen agregada." + name,
    }
    count += 1
    return result
