import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 평균 구하기
def mean(data):
    return np.mean(data, axis=0, keepdims=True)

# 정확도 구하기
def compute_result_and_accuracy(similarity):
    KNN = np.argsort(similarity, axis=1)
    KNN = KNN//7
    labeledKNN =KNN[:,0:7]
    
    c = []
    for row in labeledKNN:
        temp = [0 for i in range(4)]
        for i in range(7):
            temp[row[i]]+=1
        c.append(temp)
    
    result = np.split(np.array(c), 4, axis=0)
    
    acc = []
    for row in result:
        acc.append(np.sum(row,axis=0))
    acc = np.array(acc)/21.*100
    return result, acc    

# 3d plot 찍기
def make_3d_plot(gallery_transformed, query_transformed):
    plt.figure(figsize=(8, 8), dpi=120)

    fig = plt.figure()

    ax = fig.gca(projection='3d')

    ax.scatter(gallery_transformed[:, 0].astype(np.float32), gallery_transformed[:,1].astype(np.float32), gallery_transformed[:, 2].astype(np.float32), c='red')

    ax.scatter(query_transformed[:, 0].astype(np.float32), query_transformed[:,1].astype(np.float32), query_transformed[:, 2].astype(np.float32), c='blue')

    plt.show()
    
# plot_pca
def plot_pca(test, row, col):
    fig, axes=plt.subplots(row,col,figsize=(12,12))
    for i in range(row*col):
        for image, ax in zip(test.astype(np.float32), axes.ravel()):
            ax.imshow(image)
    plt.show()

# plot_lda
def plot_lda(test, people, m):
    fig, axes=plt.subplots(people,m,figsize=(12,12))
    for i in range(people*m):
        for image, ax in zip(test.astype(np.float32), axes.ravel()):
            ax.imshow(image)
    plt.show()