import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

x = np.array([1, 10, 20, 40, 60, 71, 80, 95, 120, 125])
y = np.array([3, 20, 90, 110, 130, 170, 150, 220, 260, 300])
x = x.reshape(-1, 1)

lin_reg = LinearRegression()
lin_reg.fit(x, y)

y_pred = lin_reg.predict(x)
print(lin_reg.coef_) # slope (m/B0)
print(lin_reg.intercept_) # intercept (c/B0)

plt.scatter(x, y)
plt.plot(x, y_pred, color='red')
plt.show()