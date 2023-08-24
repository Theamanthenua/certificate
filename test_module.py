import pandas as pd

data = {
    'age': [39, 50, 38, 53, 28],
    'workclass': ['State-gov', 'Self-emp-not-inc', 'Private', 'Private', 'Private'],
    'fnlwgt': [77516, 83311, 215646, 234721, 338409],
    'education': ['Bachelors', 'Bachelors', 'HS-grad', '11th', 'Bachelors'],
    'education-num': [13, 13, 9, 7, 13],
    'marital-status': ['Never-married', 'Married-civ-spouse', 'Divorced', 'Married-civ-spouse', 'Married-civ-spouse'],
    'occupation': ['Adm-clerical', 'Exec-managerial', 'Handlers-cleaners', 'Handlers-cleaners', 'Prof-specialty'],
    'relationship': ['Not-in-family', 'Husband', 'Not-in-family', 'Husband', 'Wife'],
    'race': ['White', 'White', 'White', 'Black', 'Black'],
    'sex': ['Male', 'Male', 'Male', 'Male', 'Female'],
    'capital-gain': [2174, 0, 0, 0, 0],
    'capital-loss': [0, 0, 0, 0, 0],
    'hours-per-week': [40, 13, 40, 40, 40],
    'native-country': ['United-States', 'United-States', 'United-States', 'United-States', 'Cuba'],
    'salary': ['<=50K', '<=50K', '<=50K', '<=50K', '<=50K']
}
df = pd.DataFrame(data)
# Print DataFrame
df
 #Save DataFrame to a CSV file
df.to_csv('demographic_data.csv', index=False)
race_acount = df['race'].value_counts()
average_age_men = df.loc[df['sex'] == 'Male', 'age'].mean()
percentage_bachelors = (df['education'] == 'Bachelors').sum() / len(df) * 100
higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
higher_education_rich = (df['salary'] == '>50K') & higher_education
percenatage_higher_education_rich = (higher_education_rich.mean()) * 100
lower_education = ~higher_education
lower_education_rich = (df['salary'] == '>50K') & lower_education
percentage_lower_education_rich = (lower_education_rich.mean()) * 100
min_work_hours = df['hours-per-week'].min()
num_min_workers = df[df['hours-per-week'] == min_work_hours]
rich_percentage = (num_min_workers['salary'] == '>50K').mean() * 100
country_stats = df.groupby('native-country')['salary'].apply(lambda x: (x == '>50K').mean() * 100)
highest_earning_country = country_stats.idxmax()
highest_earning_country_percentage = country_stats.max()
# Find the most common occupation among individuals earning >50K in India
high_earning_india = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]

if not high_earning_india.empty:
    top_IN_occupation = high_earning_india['occupation'].mode()
    if not top_IN_occupation.empty:
        top_IN_occupation = top_IN_occupation[0]
        print(f"The most common occupation for >50K earners in India is: {top_IN_occupation}")
    else:
        print("No occupation data available for >50K earners in India")
else:
    print("No data available for >50K earners in India")



