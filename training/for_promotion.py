from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

df_train = pd.read_csv("training/train.csv")
df_test = pd.read_csv("training/test.csv")

