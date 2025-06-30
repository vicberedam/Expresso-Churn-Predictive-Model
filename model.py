import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

model = pickle.load(open("model.pkl", "rb"))
encode = pickle.load(open("encoder.pkl", "rb"))

def prediction(data : list) -> str:
   df = pd.DataFrame(data)
   le = LabelEncoder()

   # encoding on our string
   for i in data:
      if type(i) == str:
         df.iloc[data.index(i)] = le.fit_transform(df.iloc[data.index(i)])
   df = df.dropna()
   pred = model.predict(df.values.reshape(1, -1))
   
   if pred[0] == 1:
        return "The customer will stop using the telecomunication services"
   else:
        return "The customer is stil an active user of the telecommunication services"
            
         
         #print(predicton(['00001dd6fa45f7ba044bd5d84937be464ce78ac2', 'DAKAR', 'K > 24 month', 13500.0, 15.0, 13502.0, 4501.0, 18.0, 43804.0, 41.0, 102.0, 2.0, 1.0, 1.0, 'NO', 62, 'Data:1000F=5GB,7d', 11.0]))
# print(prediction(['00001dd6fa45f7ba044bd5d84937be464ce78ac2', 'DAKAR', 'K > 24 month', 13500.0, 15.0, 13502.0, 4501.0, 18.0, 43804.0, 41.0, 102.0, 2.0, 1.0, 1.0, 'NO', 62, 'Data:1000F=5GB,7d', 11.0]))