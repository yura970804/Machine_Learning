import numpy as np

class PCA():

    def __init__(self, num):
      
        self.num = num
        
        self.eig_mat = None
        
        self.eig_value = None
        
    def fit(self, x):
        
        n, d = x.shape

        cov = np.matmul(x.T,x)/n
        
        eig_values, eig_vectos = np.linalg.eig(cov)
        
        eig_pairs = [(eig_values[i], eig_vectos[:, i]) for i in range(d)]
        
        sort_eig = sorted(eig_pairs, key=lambda tup: tup[0], reverse=True)
        
        self.eig_mat = np.stack(list(map(lambda tup: tup[1], sort_eig)), axis=1)
        
        self.eig_value = np.array(list(map(lambda tup: tup[0], sort_eig)))
        
    def transform(self, x):
        
        if self.eig_mat is None:
            print("model is not fitted")
            return
        
        reduced_eig_mat = self.eig_mat[:, :self.num]
        
        y = np.matmul(x, reduced_eig_mat)
        
        return y
    
    
class LDA():
    def __init__(self, num):
      
        self.num = num
        
        self.eig_mat = None
        
        self.eig_value = None
        
    def fit(self, x):
        
        n, d = x.shape
        
        num_c = int(n/10)
        
        # 데이터 나누기
        trunc_x = np.array(np.split(x, 10, axis=0))
        trunc_x_r=trunc_x.reshape(num_c,10,10304)
        n, d = x.shape
        
        m_c =[] #class mean
        for i in range(num_c):
            m_c.append(np.mean(trunc_x_r[i],axis=0,keepdims=True))
        m_c = np.array(m_c)
        m_c = m_c.reshape(num_c,10304)
        
        # sb 구하기
        diff = m_c-np.mean(m_c,axis=0,keepdims=True)
        sb = np.matmul(diff.T,diff)
        
        # sw 구하기
        sw = 0
        si = trunc_x - m_c
        for i in range(len(si)):
            sw += np.matmul(si[i].T,si[i])/10
            
        # sw의 역행렬 구하기
        s_w_i=np.linalg.pinv(sw)

        # eigen value, vector 구하기
        mat = np.matmul(s_w_i,sb)
        mat = (mat.T+mat)/2

        eig_values, eig_vectos = np.linalg.eig(mat)
        
        # eigen value, vector sort하기
        eig_pairs = [(eig_values[i], eig_vectos[:, i]) for i in range(10304)]

        sort_eig = sorted(eig_pairs, key=lambda tup: tup[0], reverse=True)

        self.eig_mat = np.stack(list(map(lambda tup: tup[1], sort_eig)), axis=1)

        self.eig_value = np.array(list(map(lambda tup: tup[0], sort_eig)))
        
    def transform(self, x):
        
        if self.eig_mat is None:
            print("model is not fitted")
            return
        
        reduced_eig_mat = self.eig_mat[:, :self.num]
        
        y = np.matmul(x, reduced_eig_mat)
        
        return y