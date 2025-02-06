from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
import pandas as pd
import numpy as np

# Load the data
df = pd.read_csv('vgsales.csv')

# Define the processing pipeline
processing = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), ['Year', 'NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']),
        ('cat', OneHotEncoder(sparse=False), ['Platform', 'Genre', 'Publisher'])
    ]
)

# Fit and transform the data
transformed_data = processing.fit_transform(df)

# Get feature names
num_features = ['Year', 'NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']
cat_features = processing.named_transformers_['cat'].get_feature_names_out(['Platform', 'Genre', 'Publisher'])
all_features = list(num_features) + list(cat_features)

# Create a DataFrame from the transformed data
normal_df = pd.DataFrame(transformed_data, columns=all_features)

# Print summary statistics
sos = np.round(normal_df.describe(), 1)
print(sos)
