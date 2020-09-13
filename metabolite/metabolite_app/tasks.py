import pandas as pd

df = pd.read_excel ('mass_spec_data_assgnmnt.xlsx')

# 1 Task
pc = df[df['Accepted Compound ID'].str.endswith(' PC', na=False)]
lpc = df[df['Accepted Compound ID'].str.endswith('LPC', na=False)]
plasmalogen = df[df['Accepted Compound ID'].str.endswith('plasmalogen', na=False)]

# 2 Task
df2 = df.copy()
df2['Retention Time Roundoff (in mins)'] = df2['Retention time (min)']
df2 = df2.round({'Retention Time Roundoff (in mins)': 0})
print(df2['Retention Time Roundoff (in mins)'])

# 3 Task
print(df2.columns)
df3 = df2.groupby('Retention Time Roundoff (in mins)').mean()
df3 = df3.drop(['m/z', 'Retention time (min)'], axis=1)
print(df3)