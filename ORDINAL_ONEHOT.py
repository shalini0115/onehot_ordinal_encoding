
import pandas as pd
from sklearn.preprocessing import OrdinalEncoder, OneHotEncoder


data = {'Education': ['Bachelor', 'Master', 'PhD', 'Bachelor', 'Master'],
        'Department': ['CSE', 'IT', 'SOFTWARE', 'MECHANICAL', 'IT']}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)


education_categories = ['Bachelor', 'Master', 'PhD']

ordinal_encoder = OrdinalEncoder(categories=[education_categories])

df['Education_Ordinal'] = ordinal_encoder.fit_transform(df[['Education']])

print("\nDataFrame with Ordinal Encoding:")
print(df)


onehot_encoder = OneHotEncoder(sparse_output=False)

department_encoded = onehot_encoder.fit_transform(df[['Department']])

department_encoded_df = pd.DataFrame(department_encoded, columns=onehot_encoder.get_feature_names_out(['Department']))

df = pd.concat([df, department_encoded_df], axis=1)

print("\nDataFrame with One-Hot Encoding:")
print(df)
