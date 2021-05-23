import os
from scipy.io import wavfile
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import keras
from keras.layers import Conv2D, MaxPool2D, Flatten, LSTM, BatchNormalization
from keras.layers import Dropout, Dense, TimeDistributed
from keras.models import Sequential
from keras.utils import to_categorical
from tqdm import tqdm
from python_speech_features import mfcc
import statistics as stat
from sklearn.model_selection import train_test_split
from keras.models import model_from_json
from audiomentations import SpecCompose, SpecFrequencyMask



audio_dir = "./trainlean/"
file_names = [f for f in os.listdir(audio_dir) if '.wav' in f]

_x = []
_y  = []

augment = SpecCompose([
SpecFrequencyMask(min_mask_fraction = 0.10,
        max_mask_fraction = 0.20)
])

for f in tqdm(file_names):
    rate, signal = wavfile.read('clean/'+f)
    mel = mfcc(signal,rate,nfilt = 26, numcep = 26, nfft = 512)
    imarray = np.resize(mel,(250,26))
    _x.append(imarray)   
    _y.append(int(f[1:4])-1)

    aug = augment(magnitude_spectrogram = mel)
    aug_ = np.resize(aug,(250,26))
    _x.append(aug_)   
    _y.append(int(f[1:4])-1)

x = np.array(_x,dtype="object")
y = np.array(_y,dtype="object")

x_train, x_test, y_train, y_test = train_test_split(x, y)

print("Size of Training Data:", np.shape(x_train))
print("Size of Training Labels:", np.shape(y_train))
print("Size of Test Data:", np.shape(x_test))
print("Size of Test Labels:", np.shape(y_test))

num_classes = 11

y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)

x_train = x_train.reshape(x_train.shape[0], x_train.shape[1], x_train.shape[2])
x_test = x_test.reshape(x_test.shape[0], x_train.shape[1], x_train.shape[2])
input_shape = (x_train.shape[1], x_train.shape[2])

x_train=np.asarray(x_train).astype(np.int)
y_train=np.asarray(y_train).astype(np.int)
x_test=np.asarray(x_train).astype(np.int)
y_test=np.asarray(y_train).astype(np.int)

def create_model():
    model = Sequential()
    model.add(LSTM(128,return_sequences = True, input_shape = input_shape))
    model.add(BatchNormalization())
    model.add(LSTM(128, return_sequences = True))
    model.add(Dropout(0.2))
    model.add(LSTM(128, return_sequences = True))
    model.add(Dropout(0.3))
    model.add(LSTM(128, return_sequences = True))
    model.add(Dropout(0.3))
    model.add(BatchNormalization())
    model.add(TimeDistributed(Dense(64, activation = "relu")))
    model.add(TimeDistributed(Dense(32, activation = "relu")))
    model.add(BatchNormalization())
    model.add(TimeDistributed(Dense(16, activation = "relu")))
    model.add(TimeDistributed(Dense(8, activation = "relu")))
    model.add(Flatten())
    model.add(Dense(11, activation = "softmax"))
    model.compile(loss = 'categorical_crossentropy', optimizer = 'adam', metrics = ['acc'])

    return model

model = create_model()
model.summary()
model.fit(x_train, y_train, batch_size=20, epochs=100, verbose=1, validation_data=(x_test, y_test))


model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)

model.save_weights("model.h5")
print("Saved model to disk")
 
