import pandas as pd
import matplotlib.pyplot as plt

# loading the dataset
df = pd.read_csv('diabetes.csv')
# print(df.head())

# Getting some stats
print(df.describe())

'''
You can tell rightaway that the data's means is far from each other,
which will negatively affects our model performance.
Hence, we need to scale our data using some standard scalar 
to have the same range and mean
'''

print(df.Outcome.value_counts())

'''
The samples for non-diabetic patients is way more the one who 
have diabetes, which can show some bias in our results because 
the model will always think that 75% are non-diabetes, which is deluding. 
'''

df.boxplot(column=[s for s in df.columns if s != 'Outcome'])
plt.show()

'''
We can see the insulin column has the greatest numner of outliers
'''

df.Insulin.hist()
plt.show()
