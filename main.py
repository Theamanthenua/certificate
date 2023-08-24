import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv("C:\\Users\\drago\\Downloads\\medical_examination.csv")

# Set up the figure with subplots
fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(20, 10))

# Define the categorical variables
categorical_vars = ['cholesterol', 'gluc', 'alco', 'active', 'smoke']

# Create the subplots
for i, var in enumerate(categorical_vars):
    row = i // 3
    col = i % 3
    sns.countplot(data=df, x=var, hue='cardio', ax=axes[row, col])
    axes[row, col].set_title(var.capitalize())
    axes[row, col].set_xlabel('')
    axes[row, col].set_ylabel('Count')

plt.tight_layout()
plt.show()

# Calculate BMI
df['BMI'] = df['weight'] / (df['height'] / 100) ** 2

# Add overweight column
df['overweight'] = (df['BMI'] > 25).astype(int)
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)
g = sns.catplot(data=df.melt(id_vars=['cardio'], value_vars=categorical_vars), kind='count', hue='value', col='variable', col_wrap=3)
g.set_axis_labels('', 'Count')
g.set_titles('{col_name}')
g.legend.set_title('Value')
plt.show()
df = df[(df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))]
corr_matrix = df.corr()

mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
plt.figure(figsize=(12, 8))
sns.heatmap(corr_matrix, mask=mask, annot=True, fmt=".1f", cmap='coolwarm')
plt.title('Correlation Matrix Heatmap')
plt.show()

