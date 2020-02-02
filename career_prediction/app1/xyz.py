import os
import pandas as pd
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
filepath = os.path.join(BASE_DIR, "app1")
file2 = os.path.join(filepath, "roo_data.csv")
dataset = pd.read_csv(file2)
data = dataset.iloc[:, :-1].values
label = dataset.iloc[:, -1].values
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
le = LabelEncoder()
data[:,14]=le.fit(data[:,14])
canwork="yes"
canwork=le.transform(canwork)
print(canwork)





