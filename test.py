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


json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)

loaded_model.load_weights("model.h5")
print("Loaded model from disk")

audio_dir = "./testclean/"
file_names = [f for f in os.listdir(audio_dir) if '.wav' in f]

_x = []
_y  = []


for f in tqdm(file_names):
    classlabel = int(f[1:4])-1
    rate, signal = wavfile.read('./testclean/'+f)
    mel = mfcc(signal,rate,nfilt = 26, numcep = 26, nfft = 512)
    imarray = np.resize(mel,(250,26))
    _x.append(imarray)   
    _y.append(classlabel)

x_test = np.array(_x,dtype="object")
y_test = np.array(_y,dtype="object")
Y_predicted = []

print(x_test.shape)
print(y_test.shape)

num_classes = 11

Y = keras.utils.to_categorical(y_test, num_classes)
X = x_test.reshape(x_test.shape[0], x_test.shape[1], x_test.shape[2])

Y = np.asarray(Y).astype(np.int)
X = np.asarray(X).astype(np.int)
loaded_model.summary()

loaded_model.compile(loss = 'categorical_crossentropy', optimizer = 'adam', metrics = ['acc'])
score = loaded_model.evaluate(X, Y, verbose=0)
y = loaded_model.predict(X, verbose = 0)
print("%s: %.2f%%" % (loaded_model.metrics_names[1], score[1]*100))

#Confusion Matrix
for i in range(len(file_names)):
	Y_predicted.append(np.argmax(y[i]))
	
cm = confusion_matrix(_y, Y_predicted)
class_labels = list(range(1,12))
# Normalise
cmn = cm.astype('float')/cm.sum(axis=1)[:, np.newaxis]
fig, ax = plt.subplots(figsize=(7,5))
sns.color_palette("light:b", as_cmap=True)
sns.heatmap(cmn, annot=True, fmt='.2f', xticklabels=class_labels, yticklabels=class_labels, cmap="rocket_r")
plt.ylabel('Actual')
plt.xlabel('Predicted')
plt.show()

