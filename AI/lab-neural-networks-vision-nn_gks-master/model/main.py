import logging  # в представлении не нуждается
import argparse # ... аналогично

from keras.datasets import mnist      # subroutines for fetching the MNIST dataset
from keras.models import Model        # basic class for specifying and training a neural network
from keras.layers import Input, Dense # the two types of neural network layer we will be using
from keras.utils import np_utils      # utilities for one-hot encoding of ground truth values

if __name__ == "__main__":
    # создаем логгер (в stderr, куда же еще)
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler() # stderr by default
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # считываем входные параметры
    parser = argparse.ArgumentParser(description='Идентифицируем буковки')
    # добавляем в параметры гиперпараметры
    parser.add_argument('--batch-size', default=128, dest='batch_size',
                        type=int, help='как много тренировочных данных на каждой итерации')
    parser.add_argument('--num-epochs', default=20, dest='num_epochs',
                        type=int, help='сколько раз проходимся по всему тренировочному сету')
    parser.add_argument('--hidden-size', default=512, dest='hidden_size',
                        type=int, help='кол-во нейронов в скрытых слоях')
    parser.add_argument('--image-size', default=32, dest='image_size',
                        type=int, help='ширина(высота) картинки')
    parser.add_argument('--color-freedom', default=1, dest='color_freedom',
                        type=int, help='1 для серых; 3 для ргб; 4 для ргб с альфой')
    args = parser.parse_args()

    # выведем гиперпараметры
    logger.info(f"batch_size:    {args.batch_size}")
    logger.info(f"num_epochs:    {args.num_epochs}")
    logger.info(f"hidden_size:   {args.hidden_size}")
    logger.info(f"image_size:    {args.image_size}")
    logger.info(f"color_freedom: {args.color_freedom}")

    # задаем свои константы
    num_classes = 10    # в русском алфавите 33 буквы
    num_train   = 60000 # there are 60000 training examples in MNIST
    num_test    = 10000 # there are 10000 test examples in MNIST

    height, width, depth = 28, 28, 1 # MNIST images are 28x28 and greyscale
    num_classes = 10 # there are 10 classes (1 per digit)

    (X_train, y_train), (X_test, y_test) = mnist.load_data() # fetch MNIST data

    X_train = X_train.reshape(num_train, height * width) # Flatten data to 1D
    X_test = X_test.reshape(num_test, height * width) # Flatten data to 1D
    X_train = X_train.astype('float32') 
    X_test = X_test.astype('float32')
    X_train /= 255 # Normalise data to [0, 1] range
    X_test /= 255 # Normalise data to [0, 1] range

    Y_train = np_utils.to_categorical(y_train, num_classes) # One-hot encode the labels
    Y_test = np_utils.to_categorical(y_test, num_classes) # One-hot encode the labels

    inp = Input(shape=(height * width,)) # Our input is a 1D vector of size 784
    hidden_1 = Dense(args.hidden_size, activation='relu')(inp) # First hidden ReLU layer
    hidden_2 = Dense(args.hidden_size, activation='relu')(hidden_1) # Second hidden ReLU layer
    out = Dense(num_classes, activation='softmax')(hidden_2) # Output softmax layer
    model = Model(inputs=inp, outputs=out) # To define a model, just specify its input and output layers

    model.compile(loss='categorical_crossentropy', # using the cross-entropy loss function
                  optimizer='adam', # using the Adam optimiser
                  metrics=['accuracy']) # reporting the accuracy
    model.fit(X_train, Y_train, # Train the model using the training set...
              batch_size=args.batch_size, epochs=args.num_epochs,
              verbose=1, validation_split=0.1) # ...holding out 10% of the data for validation
    model.evaluate(X_test, Y_test, verbose=1) # Evaluate the trained model on the test set!
