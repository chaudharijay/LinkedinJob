import pandas as pd

class BaseCleaner():
    def __init__(self, df):
        self.original = df.copy()
        self.df = df

    def handle_miss_vals(self):
        pass

    def handle_dups(self):
        dup_count = self.df.duplicated().sum()
        print(f"Found {dup_count} duplicate rows")
        self.df = self.df.drop_duplicates()
        print(f"New Shape: {self.df.shape}")

    def report(self):
        print(self.df.shape)
        print(self.df.isnull().sum())

class JobCleaner(BaseCleaner):
    def handle_miss_vals(self):
        before = self.df.isnull().sum()
        print(f"Before:\n{before}")

        self.df = self.df.dropna(subset = ['company_name', 'company_id', 'views'])

        mode_val = self.df['formatted_experience_level'].mode().iloc[0]
        self.df['formatted_experience_level'] = self.df['formatted_experience_level'].fillna(mode_val)

        print(f"New Shape: {self.df.shape}")