from flask import Flask, request
from PIL import Image
from base64 import decodestring

app = Flask(__name__)
model = ""
def predict(models, data):
    results = []
    for m in models:
        if(model == m):
            results.append(m)
    return results

@app.route("/")
def test():
    return "<p>Hello, World!</p>"

@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "GET":
        t = {
            "id_client": "number", 
            "images": "[<base64>]",
            "models": "[<numbers>]"
        }
        return t
    elif request.method == "POST":
        id_client = request.form["id_client"]
        images = request.form["images"]
        models = request.form["models"]
        res_predict = predict(models, images)
        if(res_predict is not None):
            result = {
                "state":"success",
                "message":"Predicciones realizadas correctamente.",
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
        class_name = request.form["class_name"]
        image = request.form["image"]
        image = Image.fromstring('RGB',(256,256),decodestring(image))
        image.save("raw"/class_name/str(count)+".jpg")
        result = {
            "state":"success",
            "message":"Imagen añadida.",
        }
        return result

        

