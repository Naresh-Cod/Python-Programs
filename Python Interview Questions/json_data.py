import pandas as pd

try:
    df = pd.read_json('recipe.json')
    print(df)
except ValueError as e:
    print(f"Error: {e}")
