import numpy as np

X = np.array([[1],[2],[3],[4],[5]], dtype = float)
y = np.array([[2],[4],[6],[8],[10]], dtype = float)

b= 0.0
w = np.array([[0]], dtype= float)
hours= np.array([[6]], dtype= float)

m = X.shape[0]
learning_rate = 0.01
prediction = (X @ w)+b
error = prediction-y
J= (1/(2*m)*np.sum(error**2))
print("Initial cost is:", J)

for epoch in range(1000):
       prediction = (X @ w)+b
       error = prediction-y
       J= (1/(2*m)*np.sum(error**2))
       dw= ((1/m)*(X.T@error))
       db= ((1/m)*np.sum(error))
       w= w-(learning_rate*dw)
       b= b-(learning_rate*db)
prediction = (hours@w)+b
print("New value of w is :", w)
print("New value of b is :", b)
print("The final prediction is :", prediction)
print("The final cost is :", J)
