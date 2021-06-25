from keras.layers import Flatten, LSTM, BatchNormalization
from keras.layers import Dropout, Dense, TimeDistributed
from keras.models import Sequential


def create_model():
    model = Sequential()
    model.add(LSTM(128, return_sequences=True, input_shape=input_shape))
    model.add(BatchNormalization())
    model.add(LSTM(128, return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(128, return_sequences=True))
    model.add(Dropout(0.3))
    model.add(LSTM(128, return_sequences=True))
    model.add(Dropout(0.3))
    model.add(BatchNormalization())
    model.add(TimeDistributed(Dense(64, activation="relu")))
    model.add(TimeDistributed(Dense(32, activation="relu")))
    model.add(BatchNormalization())
    model.add(TimeDistributed(Dense(16, activation="relu")))
    model.add(TimeDistributed(Dense(8, activation="relu")))
    model.add(Flatten())
    model.add(Dense(11, activation="softmax"))
    model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["acc"])

    return model
