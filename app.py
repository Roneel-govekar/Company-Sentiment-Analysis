from flask import Flask,request, render_template
import numpy as np
import keras

app=Flask(__name__)

model = keras.models.load_model("company_model.h5")