
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, BatchNormalization
from keras.layers import Conv2D, MaxPool2D

class CNN:

  @staticmethod
  def model_build(width, height, ch , Num_classes):
    model = Sequential()

    model.add(Conv2D(filters = 64, kernel_size = (5,5), activation ='relu',input_shape=(width, height, ch)))
    model.add(BatchNormalization(axis=3))
    model.add(Conv2D(filters = 64, kernel_size = (5,5), activation ='relu'))
    model.add(MaxPool2D(pool_size=(2,2)))
    model.add(BatchNormalization(axis=3))
    model.add(Dropout(0.25))

    model.add(Conv2D(filters = 128, kernel_size = (5,5), activation ='relu'))
    model.add(BatchNormalization(axis=3))
    model.add(Conv2D(filters = 128, kernel_size = (5,5), activation ='relu'))
    model.add(MaxPool2D(pool_size=(2,2)))
    model.add(BatchNormalization(axis=3))
    model.add(Dropout(0.25))

    model.add(Conv2D(filters = 256, kernel_size = (5,5), activation ='relu'))
    model.add(BatchNormalization(axis=3))
    model.add(Conv2D(filters = 256, kernel_size = (5,5), activation ='relu'))
    model.add(MaxPool2D(pool_size=(2,2)))
    model.add(BatchNormalization(axis=3))
    model.add(Dropout(0.25))

    model.add(Flatten())

    model.add(Dense(256, activation = "relu")) #Fully connected layer
    model.add(BatchNormalization())
    model.add(Dropout(0.5))

    model.add(Dense(60, activation = "relu")) #Fully connected layer
    model.add(BatchNormalization())
    model.add(Dropout(0.5))

    model.add(Dense(Num_classes, activation = "softmax")) #Classification layer or output layer

    model.summary()

    return model
