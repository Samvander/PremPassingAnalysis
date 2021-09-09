import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
import seaborn as sns

#Always like to set pandas to max columns
pd.set_option('display.max_columns', None)

#Merging dataframes, dropping unnecessary columns
epl_passing_df = pd.read_csv('data/epl_passing.csv')
wins_df = pd.read_csv('data/epl wins.csv')
wins_df = wins_df.drop(columns='A')
epl_passing_df = pd.merge(epl_passing_df,wins_df, on='Team')
epl_passing_df = epl_passing_df.drop(columns=["# Pl","90s","Att","ShortCmp","ShortAtt","MedCmp","MedAtt","LngCmp","LngAtt","A-xA"])

#Scatter plot for single variable. Replace 'Cmp%' with other column headers for different stats
# epl_passing_df.plot(kind='scatter', x='Wins',y='Cmp%', xlabel='Wins',ylabel='Pass Completion Rate')

#Prints scatter matrix of all dataframe columns 
# scatter_matrix(epl_passing_df, alpha=0.2, figsize=(6, 6), diagonal="kde")
# plt.show()

#Creates correlation matrix 
corr = epl_passing_df.corr()

#Creating heatmap
ax = sns.heatmap(
    corr,
    vmin=-1, vmax=1, center=0,
    cmap=sns.diverging_palette(20, 220, n=200),
    square=True
)
ax.set_xticklabels(
    ax.get_xticklabels(),
    rotation=45,
    horizontalalignment='right'
);

plt.show()
