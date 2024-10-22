# onehot_ordinal_encoding
This script demonstrates the use of Ordinal Encoding and One-Hot Encoding to convert categorical variables into numerical formats for machine learning algorithms. 
One-Hot and Ordinal Encoding Script
This Python script demonstrates how to perform One-Hot Encoding and Ordinal Encoding on a sample dataset using Pandas. The script provides two functions, onehot_encode() and ordinal_encode(), that encode categorical data for machine learning models without using external libraries like sklearn.

Features
One-Hot Encoding: Transforms categorical features into binary columns for each unique value. Example: "Category" -> Category_Electronics, Category_Clothing, etc.
Ordinal Encoding: Maps categorical values to numeric values based on a predefined or automatic ordering. Example: "Priority" -> Low = 0, Medium = 1, High = 2.

Dataset
The example dataset consists of the following columns:

Category: ['Electronics', 'Clothing', 'Groceries']
Priority: ['High', 'Medium', 'Low']
Size: ['Large', 'Small', 'Medium']
Color: ['Red', 'Blue', 'Green', 'Yellow']

Sample Data
| Category    | Priority | Size   | Color  |
|-------------|----------|--------|--------|
| Electronics | High     | Large  | Red    |
| Clothing    | Medium   | Small  | Blue   |
| Groceries   | Low      | Medium | Green  |
| Electronics | Medium   | Large  | Yellow |
| Clothing    | High     | Medium | Red    |


Functions
1. onehot_encode(df, columns)
Performs One-Hot Encoding on the specified columns.

Parameters:
df: Input DataFrame
columns: List of column names to one-hot encode
Returns: DataFrame with one-hot encoded columns.
2. ordinal_encode(df, column, order=None)
Performs Ordinal Encoding on a single column.

Parameters:
df: Input DataFrame
column: Column name to ordinal encode
order: Dictionary specifying the order of values (e.g., {'Low': 0, 'Medium': 1, 'High': 2}). If None, the order is automatically derived from unique values.
Returns: Series with ordinal encoded values.
Usage
Clone or download this repository.
Install required dependencies (only pandas is used).
Run the script in a Python environment to view the encoded DataFrame.


Example Output

   Priority    Size  Category_Electronics  Category_Clothing  Category_Groceries  Color_Red  Color_Blue  Color_Green  Color_Yellow  Priority_ordinal  Size_ordinal
0      High   Large                    1                  0                   0          1           0            0             0                 2             2
1    Medium   Small                    0                  1                   0          0           1            0             0                 1             0
2       Low  Medium                    0                  0                   1          0           0            1             0                 0             1
3    Medium   Large                    1                  0                   0          0           0            0             1                 1             2
4      High  Medium                    0                  1                   0          1           0            0             0                 2             1


Requirements
Python 3.x
Pandas


How to Run
Ensure you have Python 3.x installed.
Install Pandas if you don't have it:
pip install pandas

Run the script:
python encoding_script.py
