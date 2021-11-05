import keras
from keras.layers import Dense, Conv2D, Flatten, MaxPooling2D
import numpy as np
import matplotlib.pyplot as plt

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

pic_size = 28
col_deep = 1
out_num = 10
x_train = x_train.reshape(60000,pic_size,pic_size,col_deep)
x_test = x_test.reshape(10000,pic_size,pic_size,col_deep)

y_train = keras.utils.to_categorical(y_train)
y_test = keras.utils.to_categorical(y_test)

model = keras.models.Sequential()
model.add(Conv2D(64, kernel_size=3, activation='relu', input_shape=(pic_size,pic_size,col_deep)))

model.add(MaxPooling2D())

model.add(Conv2D(32, kernel_size=3, activation='relu'))
model.add(Flatten())


model.add(Dense(out_num, activation='softmax'))

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
print('**********************************************')
hist = model.fit(x_train, y_train, validation_data=(x_test, y_test), epochs=10)
#print(hist.history)


# Plot training & validation accuracy values
#plt.plot(history.history['acc'])
#plt.plot(history.history['val_acc'])
#plt.title('Model accuracy')
#plt.ylabel('Accuracy')
#plt.xlabel('Epoch')
#plt.legend(['Train', 'Test'], loc='upper left')
#plt.show()
#
#plt.plot(history.history['loss'])
#plt.plot(history.history['val_loss'])
#plt.title('Model loss')
#plt.ylabel('Loss')
#plt.xlabel('Epoch')
#plt.legend(['Train', 'Test'], loc='upper left')
#plt.show()