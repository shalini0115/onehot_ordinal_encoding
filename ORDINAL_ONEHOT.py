import pandas as pd

data = {
    'Category': ['Electronics', 'Clothing', 'Groceries', 'Electronics', 'Clothing'],
    'Priority': ['High', 'Medium', 'Low', 'Medium', 'High'],
    'Size': ['Large', 'Small', 'Medium', 'Large', 'Medium'],
    'Color': ['Red', 'Blue', 'Green', 'Yellow', 'Red']
}

df = pd.DataFrame(data)

def onehot_encode(df, columns):
    encoded_df = df.copy()  
    for column in columns:
        unique_vals = df[column].unique() 
        for val in unique_vals:
            encoded_df[f"{column}_{val}"] = (df[column] == val).astype(int)  
    return encoded_df.drop(columns, axis=1) 


def ordinal_encode(df, column, order=None):
    if order is None:
        order = {value: idx for idx, value in enumerate(df[column].unique())}
    return df[column].map(order)  


df_one_hot_encoded = onehot_encode(df, columns=['Category', 'Color'])


df_one_hot_encoded['Priority_ordinal'] = ordinal_encode(df, 'Priority', order={'Low': 0, 'Medium': 1, 'High': 2})
df_one_hot_encoded['Size_ordinal'] = ordinal_encode(df, 'Size', order={'Small': 0, 'Medium': 1, 'Large': 2})

print(df_one_hot_encoded)
