import numpy as np
import os 
from PIL import Image


def make_trainset(origin_path='./att_faces/s'):
    train=[]
    for i in range(1,37):
        path = origin_path+str(i)
        file_list = os.listdir(path)

        for j in range(10):
            with Image.open(path+"/"+file_list[j]) as im:
                a = np.asarray(im)
                a = a.reshape(112*92,)
                train.append(a)
    train=np.asarray(train)
    return train

def make_testset(path='./att_faces/s'):
    test=[]
    for i in range(37,41):
        path = './att_faces/s'+str(i)
        file_list = os.listdir(path)

        for j in range(10):
            with Image.open(path+"/"+file_list[j]) as im:
                a = np.asarray(im)
                a = a.reshape(112*92,)
                test.append(a)
    test=np.asarray(test)
    return test

# testset의 gallery, query 나누기
def divide(test):
    gallery = []
    query = []
    for i in range(40):
        if i % 10 < 7:
              gallery.append(test[i, :])
        else:
              query.append(test[i, :])
    gallery = np.array(gallery)
    query = np.array(query)
    
    return gallery, query