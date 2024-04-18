#PROBLEM 1#
import pandas as pd
import numpy as np 

tweets_df = pd.read_json('AOC_recent_tweets.txt')

def time_in_hours(created_at):
    return created_at.hour + created_at.minute / 60 + created_at.second / 3600

tweets_df['created_at'] = pd.to_datetime(tweets_df['created_at'])
tweets_df['hours'] = tweets_df['created_at'].apply(time_in_hours)

selected_columns = ['created_at', 'hours', 'full_text']
tweets_df[selected_columns].to_csv('AOC_recent_tweets_processed.txt')

print(tweets_df[selected_columns])



#PROBLEM 2#
import seaborn as sns
import matplotlib.pyplot as plt

planets_data = sns.load_dataset('planets')

planets_data.dropna(inplace=True)

plt.figure(figsize=(10, 6))
sns.scatterplot(x='orbital_period', y='mass', hue='method', data=planets_data, palette='viridis')
plt.xscale('log')
plt.yscale('log')
plt.title('Exoplanets: Orbital Period vs Mass')
plt.xlabel('Orbital Period (days)')
plt.ylabel('Mass (Jupiter Mass)')
plt.legend(title='Discovery Method')
plt.grid(True)
plt.show()

plt.figure(figsize=(12, 6))
sns.countplot(x='year', hue='method', data=planets_data, palette='Set1')
plt.title('Exoplanet Discoveries by Year and Method')
plt.xlabel('Year')
plt.ylabel('Number of Exoplanets Discovered')
plt.legend(title='Discovery Method', loc='upper left')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.show()
