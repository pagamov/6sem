import cv2
import numpy as np

# select file to deal with
file_to_read = 'lesha_data.jpg'
# path to save cutted files
path_to_save = './lesha3/'

# Управление!
# WASD = изменение начала по картинке
# z - уменьшение по х
# x - увеличение по х
# c - уменьшение по y
# v - увеличение по y
# enter - обрезка и сохранение в формате 32 на 32
image = cv2.imread(file_to_read)
x,y = 0,0
xl,yl = 100,100

step_coord = 5
step_len = 5
while(1):
    # cv2.imshow('img',image)
    cropped = image[x:x+xl, y:y+yl]
    to_show = cv2.resize(cropped, (300, 300), interpolation = cv2.INTER_AREA)
    cv2.imshow("show image", to_show)
    k = cv2.waitKey(33)
    if k == 27:    # Esc key to stop
        break
    elif k == -1:  # normally -1 returned,so don't print it
        continue
    elif k == 119:
        # pressed w
        x = max(0,x-step_coord)
    elif k == 115:
        # pressed s
        x = min(image.shape[0]-xl,x+step_coord)
    elif k == 97:
        # pressed a
        y = max(0,y-step_coord)
    elif k == 100:
        # pressed d
        y = min(image.shape[1]-yl,y+step_coord)
    elif k == 122:
        # pressed z
        xl = max(32, xl - step_len)
        yl = max(32, yl - step_len)
    elif k == 120:
        # pressed x
        xl = min(400, xl + step_len)
        yl = min(400, yl + step_len)
    elif k == 13:
        # pressed enter
        print('saved ' + str(x)+'_'+str(y)+'.jpg')
        dim = (32, 32)
        resized = cv2.resize(cropped, dim, interpolation = cv2.INTER_AREA)
        cv2.imwrite(path_to_save+str(x)+'_'+str(y)+'.jpg', resized)
    else:
        print(k) # else print its value

# print(image.shape)
#
# # Нам надо сохранить соотношение сторон
# # чтобы изображение не исказилось при уменьшении
# # для этого считаем коэф. уменьшения стороны
# final_wide = 200
# r = float(final_wide) / image.shape[1]
# dim = (final_wide, int(image.shape[0] * r))
#
# # уменьшаем изображение до подготовленных размеров
# resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
# cv2.imshow("Resize image", resized)
# cv2.waitKey(0)
#
# вырежем участок изображения используя срезы
# мы же используем NumPy

# s_x, s_y = 0,0
# s = 100
# cropped = image[s_x:s_x+s, s_y:s_y+s]
# cv2.imshow("Cropped image", cropped)
# cv2.waitKey(0)
#
# # запишем изображение на диск в формате png
# cv2.imwrite("flip.png", flip_image)
