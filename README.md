## KANISHKA GUPTA CLASS 12TH C Roll No: 22 ##

### PROJECT FOR ANIMAL SPECIES DETECTION CHATBOT ###
- This chatbot for now detects only Butterfly, Cat, Cow, Dog, Elephat, Horse, Sheep, Spider, Squirrel
- This chatbot uses **tensorflow's VGG16** model which already have trained neural networks for images
- I build this project on top of VGG16 to **categorize and remember different animals based on the VGG16 learned knowledge.**
- Please note that Model's accuracy depends upon the amount of dataset used, for this project we are only using 100 images per animal
- Chatbot is added as a hardcoded additional feature above prediction model which generate texts for provided input based on the predicted species.
- For user interface we are using html, css and javascript and a custom server made in flask.

## HOW TO RUN THE PROJECT ##
- Create virtual python environment
 ```bash
python -m venv .venv

.venv\Scripts\activate
```

- Install dependencies:
```bash
pip install -r requirements.txt
```

- [Optional] Train the model using command
```bash
python train.py
```

- Run the app:
```bash
python app.py
```

- Open browser:
```
http://127.0.0.1:5000
```


### SPECIES DETECTION DATASET USED FROM KAGGLE ###
Dataset used: https://www.kaggle.com/datasets/alessiocorrado99/animals10?resource=download

