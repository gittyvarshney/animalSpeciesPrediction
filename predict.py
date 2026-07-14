import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

model = load_model("model/animal_model.keras")

classes = [
    "Butterfly",
    "Cat",
    "Cow",
    "Dog",
    "Elephant",
    "Horse",
    "Sheep",
    "Spider",
    "Squirrel"
]

def predict_species(img_path):

    img = image.load_img(img_path,
                         target_size=(224,224))

    img = image.img_to_array(img)

    img = np.expand_dims(img, axis=0)

    img = img / 255.0

    prediction = model.predict(img)

    index = np.argmax(prediction)

    return classes[index]