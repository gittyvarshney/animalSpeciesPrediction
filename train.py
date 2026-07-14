# train.py

import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import VGG16
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.models import Model
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = os.path.join(BASE_DIR, "model", "animal_model.keras")
DATASET_PATH = os.path.join(BASE_DIR, "dataset")

IMG_SIZE = (224,224)

train = ImageDataGenerator(rescale=1./255,
                           validation_split=0.2)

train_data = train.flow_from_directory(
    DATASET_PATH,
    target_size=IMG_SIZE,
    batch_size=16,
    subset='training'
)

val_data = train.flow_from_directory(
    DATASET_PATH,
    target_size=IMG_SIZE,
    batch_size=16,
    subset='validation'
)

base = VGG16(weights='imagenet',
             include_top=False,
             input_shape=(224,224,3))

for layer in base.layers:
    layer.trainable=False

x = Flatten()(base.output)
x = Dense(128, activation='relu')(x)
output = Dense(train_data.num_classes,
               activation='softmax')(x)

model = Model(base.input, output)

model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

model.fit(train_data,
          validation_data=val_data,
          epochs=5)

model.save(MODEL_PATH)