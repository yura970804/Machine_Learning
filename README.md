# Machine_Learning
## first project
### 내용
Curse of Dimensionality 문제를 해결하기 위해, 차원 축소 방법인 PCA와 LDA를 사용하여 차원을 축소하고, 축소한 차원으로 생성된 벡터가 원래의 데이터를 잘 표현하고 있는지 확인한다.  

### 실험 방법
40명의 얼굴 사진(각 사람마다 10장씩)을 사용하여 같은 사람의 사진이 가까운 공간에 위치하는 지 확인한다.  
PCA, LDA를 구현하고, 36명의 사진으로 fit한 후 4명의 사진으로 test한다.  
4명의 사진을 각 사람마다, 7개의 사진을 gallery, 3개의 사진을 query로 한 후 query가 얼마나 gallery 근처로 왔는지를 확인하여 두 방법의 성능을 측정한다.  
위와 같은 방법으로 test에 사용되는 사람(4명)을 바꿔가면서 10-fold cross validation을 하여 성능을 확인한다.   
