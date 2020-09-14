import pandas as pd

# Operation 1
def task1(file):
    df = pd.read_excel(file)
    pc = df[df['Accepted Compound ID'].str.endswith(' PC', na=False)]
    lpc = df[df['Accepted Compound ID'].str.endswith('LPC', na=False)]
    plasmalogen = df[df['Accepted Compound ID'].str.endswith('plasmalogen', na=False)]
    return pc, lpc, plasmalogen

# Operation 2
def task2(file):
    df = pd.read_excel(file)
    df['Retention Time Roundoff (in mins)'] = df['Retention time (min)']
    df = df.round({'Retention Time Roundoff (in mins)': 0})
    return df

# Operation 3
def task3(file):
    df = pd.read_excel(file)
    df['Retention Time Roundoff (in mins)'] = df['Retention time (min)']
    df = df.round({'Retention Time Roundoff (in mins)': 0})
    df2 = df.groupby('Retention Time Roundoff (in mins)').mean()
    df2 = df2.drop(['m/z', 'Retention time (min)'], axis=1)
    return df2