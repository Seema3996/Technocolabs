import pandas as pd
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

#Path of the file to read
iowa_file_path='../input/home-data-for-ml-course/train.csv'
home_data=pd.read_csv(iowa_file_path)

#Create target object  and call it y
y=home_data.SalePrice
#Create X
features=['LotArea','YearBuilt','1stFlrSF','2ndFlrSF','FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']
X=home_data[features]

#Split into validation and training data
train_X,val_X,train_y,val_y=train_test_split(X,y,random_state=1)

#Specify Model
iowa_model=DecisionTreeRegressor(random_state=1)
#Fit model
iowa_model.fit(train_X,train_y)

#Make validation predictions and calculate mean absolute error
val_predictions=iowa_model.predict(val_X)
val_mae=mean_absolute_error(val_predictions, val_y)
print("Validation MAE: {:, .0f}".format(val_mae))

#Setup code checking
from learntools.core import binder
binder.bind(globals())
from learntools.machine_learning.ex5 import *
print("\nSetup complete")

def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
  model=DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
  model.fit(train_X, train_y)
  preds_val=model.predict(val_X)
  mae=mean_absolute_error(val_y,pred_val)
  return mae

candidate_max_leaf_nodes=[5,10,25,50,100,250,500]
# Write loop to find the ideal tree size from candidate_max_leaf_nodes
scores = {leaf_size: get_mae(leaf_size, train_X, val_X, train_y, val_y) for leaf_size in candidate_max_leaf_nodes}
best_tree_size = min(scores, key=scores.get)

# Fill in argument to make optimal size and uncomment
final_model = DecisionTreeRegressor(max_leaf_nodes=best_tree_size,random_state=1)

# fit the final model and uncomment the next two lines
final_model.fit(X,y)

#RandomForestRegressor
from sklearn.ensemble import RandomForestRegressor

# Define the model. Set random_state to 1
rf_model = RandomForestRegressor()

# fit your model
rf_model.fit(train_X, train_y)

# Calculate the mean absolute error of your Random Forest model on the validation data
rf_val_predictions = rf_model.predict(val_X)
rf_val_mae = mean_absolute_error(rf_val_predictions, val_y)

print("Validation MAE for Random Forest Model: {}".format(rf_val_mae))



























