import glob
import os
import re

#Pre-procesamiento de imagenes
from tensorflow.python.keras.preprocessing.image import ImageDataGenerator
from tensorflow.python.keras import optimizers
from tensorflow.python.keras.models import Sequential
from 


data_train= "Train"
data_test ="Test"
gendata_train = ImageDataGenerator(
    rescale = 1./255,
    shear_range = 0.3,
    zoom_range = 0.3,
    horizontal_flip = True,
)

gendata_test = ImageDataGenerator(rescale = 1./255)

height = 100
length = 100
image_train = gendata_train.flow_from_directory(
    data_train,
    target_size = (height,length),
    batch_size = 32,
    class_mode = 'categorical',
)

image_test =gendata_test.flow_from_directory(
    data_test,
    target_size = (height,length)
    batch_size = 32,
    class_mode = 'categorical'
)

#Crear CNN

cnn = Sequential()
cnn.add(C)