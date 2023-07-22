import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, InputLayer
from keras.optimizers import RMSprop
import matplotlib.pyplot as plt
import numpy as np

# MNISTデータの読込、前処理
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train = x_train.reshape(60000, 784)
x_test = x_test.reshape(10000, 784)
x_train = x_train.astype('float32')
x_test =x_test.astype('float32')
x_train /= 255
x_test /=255
y_train = keras.utils.to_categorical(y_train, 10)
y_test = keras.utils.to_categorical(y_test, 10)

# 人工知能(AI)の構築
model = Sequential()
model.add(InputLayer(input_shape=(784,)))
model.add(Dense(10, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

# 人工知能(AI)の学習
epochs = 10
batch_size = 128
history = model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, verbose=1, validation_data = (x_test, y_test))

# 人工知能(AI)の制度検証
score = model.evaluate(x_test, y_test, verbose=1)
print()
print('Test loss:', score[0])
print('Test accuracy:', score[1])

# 認識結果の表示
pred = model.predict(x_test)
ans = np.argmax(pred[0])
sco = np.max(pred[0]) * 100
plt.title('Predict:{} Score:{:.2f}'.format(ans, sco))
plt.imshow(x_test[0].reshape(28, 28), cmap='Greys')
plt.show()


