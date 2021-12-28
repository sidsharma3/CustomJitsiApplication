from flask import Flask
from flask_restful import Api, Resource
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np

X = [[2500000,2500000,2500000,2500000,2500000], [2500000,2500000,2500000,2500000,2500000], [2500000,2500000,2500000,2500000,2500000]]
y = [2500000,2500000,2500000]
X = np.array(X)
y = np.array(y)


n_features = 1
X = X.reshape((X.shape[0], X.shape[1], n_features))
n_steps = 5
model = tf.keras.Sequential()
model.add(layers.LSTM(50, activation='relu', input_shape=(n_steps, n_features)))
model.add(layers.Dense(1))

app = Flask(__name__)
api = Api(app)

class Model(Resource):
    def get(self):
        # get request runs the model
        theTestData = np.array([2500000, 2500000, 2500000, 2500000, 2500000])
        theTestData = theTestData.reshape((1, n_steps, n_features))
        return {"data" : str(model.predict(theTestData))}
        
    def post(self):
        # post request trains the model
        model.compile(optimizer=tf.keras.optimizers.Adam(0.01), loss=tf.keras.losses.MeanSquaredError())
        model.fit(X, y, epochs=200, verbose=1)
        return {"data" : "trained the model"}

api.add_resource(Model, "/predict")

if __name__ == "__main__":
    app.run(debug=True)


