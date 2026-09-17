import pandas as pd


class JobAnalyzer:
    def __init__(self, df):
        self.df = df

    def salary_by_experience(self):
        return (
            self.df
            .groupby('formatted_experience_level')['normalized_salary']
            .median()
            .sort_values(ascending=False)
        )

    def salary_by_location(self, min_postings=20, top_n=15):
        counts = self.df['location'].value_counts()
        valid = counts[counts >= min_postings].index
        filtered = self.df[self.df['location'].isin(valid)]
        return (
            filtered
            .groupby('location')['normalized_salary']
            .median()
            .sort_values(ascending=False)
            .head(top_n)
        )

    def top_skills(self, job_skills_named, min_count=1, top_n=15):
        counts = job_skills_named['skill_name'].value_counts()
        return counts[counts >= min_count].head(top_n)

    def salary_by_skill(self, job_skills_named, min_count=500, top_n=15):
        merged = job_skills_named.merge(
            self.df[['job_id', 'normalized_salary']], on='job_id', how='left'
        )
        counts = merged.groupby('skill_name')['normalized_salary'].count()
        valid_skills = counts[counts >= min_count].index
        merged = merged[merged['skill_name'].isin(valid_skills)]
        return (
            merged
            .groupby('skill_name')['normalized_salary']
            .median()
            .sort_values(ascending=False)
            .head(top_n)
        )

    def skills_by_experience(self, job_skills_named, top_n=5):
        merged = job_skills_named.merge(
            self.df[['job_id', 'formatted_experience_level']], on='job_id', how='inner'
        )
        cross = (
            merged
            .groupby(['formatted_experience_level', 'skill_name'])
            .size()
            .reset_index(name='count')
        )
        result = {}
        for level in cross['formatted_experience_level'].unique():
            result[level] = (
                cross[cross['formatted_experience_level'] == level]
                .sort_values('count', ascending=False)
                .head(top_n)
            )
        return result