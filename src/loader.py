import pandas as pd

class DataLoader:
    def __init__(self, filepath):
        self.filepath = filepath

    def load(self):
        return pd.read_csv(self.filepath)
    
    def drop_sparse_columns(self, df, threshold):
        null_pct = df.isnull().sum() / len(df) * 100
        cols_to_drop = null_pct[null_pct > threshold].index.tolist()
        print(f"Dropping : {cols_to_drop}")
        return df.drop(columns=cols_to_drop)
