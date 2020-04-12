# 1 Import the required modules

from sklearn.datasets import make_classification
from matplotlib import pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import pandas as pd

# 2 Generate the dataset

x, y = make_classification(
	n_samples=100,
	n_features=1,
	n_classes=2,
	n_clusters_per_class=1,
	flip_y=0.03,
	n_informative=1,
	n_redundant=0,
	n_repeated=0
	)
print(x)
print(y)

# 3 Visualize the data

plt.scatter(x, y, c=y, cmap="rainbow")
plt.title('Scatter Plot of Logistic Regression')
plt.show()

# 4 Split the dataset

x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=1)
print(x_train.shape)
print(x_test.shape)

# 5 Perform the logistic regression

log_reg = LogisticRegression()
log_reg.fit(x_train, y_train)

# 6 Make a prediction using the model

y_pred = log_reg.predict(x_test)
print(log_reg.coef_) # slope (m/B1)
print(log_reg.intercept_) # intercept (c/B0)

# 7 Display the confusion matrix

print(confusion_matrix(y_test, y_pred))
