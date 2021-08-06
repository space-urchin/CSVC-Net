import os
from scipy.io import wavfile
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import keras
from tqdm import tqdm
from python_speech_features import mfcc
from keras.models import model_from_json
from sklearn.metrics import confusion_matrix

# load model
json_file = open("results/cnnlstm.json", "r")
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)

# load model weights
loaded_model.load_weights("results/cnnlstm.h5")
print("Loaded model from disk")

audio_dir = "path/to/testset/folder/"  # directory where the test set is stored
file_names = [f for f in os.listdir(audio_dir) if ".wav" in f]
length = []

_x = []
_y = []


for f in tqdm(file_names):
    classlabel = int(f[1:4]) - 1
    rate, signal = wavfile.read(audio_dir+ f)
    mel = mfcc(signal, rate, nfilt=26, numcep=26, nfft=512)
    imarray = np.resize(mel, (250, 26))
    _x.append(imarray)
    _y.append(classlabel)

x_test = np.array(_x, dtype="object")
y_test = np.array(_y, dtype="object")

print(x_test.shape)
print(y_test.shape)


num_classes = 11
Y_predicted = []

Y = keras.utils.to_categorical(y_test, num_classes)
X = x_test.reshape(x_test.shape[0], x_test.shape[1], x_test.shape[2], 1)

Y = np.asarray(Y).astype(np.int)
X = np.asarray(X).astype(np.int)

loaded_model.summary()
loaded_model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["acc"])
score = loaded_model.evaluate(X, Y, verbose=0)
y = loaded_model.predict(X, verbose=0)
print("Accuracy - %s: %.2f%%" % (loaded_model.metrics_names[1], score[1] * 100))

