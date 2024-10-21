#Import Libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report, precision_score, recall_score, f1_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
#Constant Variables
TEST_SIZE = 0.2
RANDOM_STATE = 42
#Load Dataset
def load_data (file path):
data = pd.read_csv ('clin_fert_data.csv')
#Preprocess Data
X = data.drop (['clin_fert_outcome'], axis = 1)
y = data ['clin_fert_outcome']
#Handle Categorical Variables
categorical_cols = ['Sex', 'Sperm_Quality', 'Stress_Levels', 'Diet']
X = pd.get_dummies (X, columns = categorical_cols)
 return X, y
except Exception as e:
print (f"Error loading data: {e}")
#Split Data into Training and Testing sets
def split_data (X, y): 
  return train_test_split (X, y, test_size = TEST_SIZE, random_state = RANDOM_STATE)
#Scale Data using StandardScaler
def scale_data (X_train, X_test):
  scaler = StandardScaler()
  X_train_scaled = scaler.fit transform (X_train)
  X_test_scaled = scaler.transform (X_test)
   return X_train_scaled, X_test_scaled
#Define Machine Learning Models
def define_models():
  models = {'Logistic Regression': LogisticRegression(max_iter = 1000),
            'Decision Tree': DecesionTreeClassifier(),
            'Random Forest': RandomForestClassifier(),
            'SVM': SVC(),
            'Neural Network': MLPClassifier(max_iter = 1000)}
   return models
#Train and Evaluate Models
def train_and_evaluate models, (X_train_scaled, X_test_scaled, y_train, y_test):
  for name, model in models.items():
    model.fit (X_train_scaled, y_train)
    y_pred = 
    model.predict (X_test_scaled)
#Evaluate Model Performance
    accuracy = accuracy_score (y_test, y_pred)
    precision = precision_score (y_test, y_pred)
    recall = recall_score (y_test, y_pred)
    f1 = f1_score (y_test, y_pred)
 print (f"Model: {name}")
 print (f"Accuracy : {accuracy:.3f}")
 print (f"Precision : {precision:.3f}")
 print (f"Recall: {recall:.3f}")
 print (f"F1-score : {f1:.3f}")
 print ("Classification_Report:")
 print (classification_report(y_test, y_pred))
#Main Function
def main():
  file_path = 'clin_fert_data.csv'
  X, y = load_data (file_path)
 X_train, X_test, y_train, y_test = split_data (X, y) 
X_train_scaled, X_test_scaled = scale_data (X_train, X_test)
models = define_models()
train_and_evaluation (models, X_train_scaled, X_test_scaled, y_train, y_test)
if _name_ == "_main_":
  main()
