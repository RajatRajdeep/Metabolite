import pandas as pd

# 1 Task
def task1(file_path):
    df = pd.read_excel(file_path)
    pc = df[df['Accepted Compound ID'].str.endswith(' PC', na=False)]
    lpc = df[df['Accepted Compound ID'].str.endswith('LPC', na=False)]
    plasmalogen = df[df['Accepted Compound ID'].str.endswith('plasmalogen', na=False)]
    return pc, lpc, plasmalogen

# 2 Task
def task2(file_path):
    df = pd.read_excel(file_path)
    df['Retention Time Roundoff (in mins)'] = df['Retention time (min)']
    df = df.round({'Retention Time Roundoff (in mins)': 0})
    return df

# 3 Task
def task3(file_path):
    df = pd.read_excel(file_path)
    df['Retention Time Roundoff (in mins)'] = df['Retention time (min)']
    df = df.round({'Retention Time Roundoff (in mins)': 0})
    df2 = df.groupby('Retention Time Roundoff (in mins)').mean()
    df2 = df2.drop(['m/z', 'Retention time (min)'], axis=1)
    return df2