## PCA
원래의 데이터를 가장 잘 표현해줄 수 있는 차원 축소된 y를 찾는 방법  
(목표: y의 분산이 최대가 되는 것)  
![image](https://user-images.githubusercontent.com/62591011/204686270-47e6945e-3228-438e-99b1-b7b9d16a2a3d.png)

## LDA
클래스의 평균 간의 거리는 멀게 하면서, 클래스 내의 분산은 작게하여 클래스를 분리하는 방법  
PCA보다 원신호를 보존하지는 못 하지만 분류가 중요할 때 사용하는 방법
C-class problems -> (C-1)개의 projection을 찾는다  
![image](https://user-images.githubusercontent.com/62591011/204686465-ebcd9110-3603-4fc9-8cf0-14042ac1b021.png)
![image](https://user-images.githubusercontent.com/62591011/204686481-b3c96d00-6c18-4013-87f4-6fca067cbbec.png)
