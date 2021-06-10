def get_data(path):
    import cv2 as cv
    import numpy as np
    import os
    import random
    import time

    percent_data = 0.2
    learn_data, check_data = [], []
    t = time.time()
    for dir in [path+'1',path+'2',path+'3']:
        for file in os.listdir(dir):
           # print('\r read file', dir + '/' + file, end='')
            if random.random() > percent_data:
                # add to learn_data
                learn_data.append([cv.imread(dir + '/' + file), int(dir[-1])-1])
            else:
                # add to check_data
                check_data.append([cv.imread(dir + '/' + file), int(dir[-1])-1])
    print('\n recieved', len(learn_data), 'of learn_data and', len(check_data), 'in', time.time() - t, 'sec')
    random.shuffle(learn_data)
    random.shuffle(check_data)
    return learn_data, check_data


# get_data('./')
