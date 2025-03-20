def df_cleaned(df):
    df['NCAA'] = df['School'].str.contains('NCAA').astype(int)
    df['School'] = df['School'].str.replace('NCAA', '', regex=False)
    df = df.drop(columns = [i for i in df.columns if 'Unnamed' in i])
    df = df.rename(columns={'W.1': 'Conf. W', 'W.2': 'Home W', 'W.3': 'Away W'})
    df = df.rename(columns={'L.1': 'Conf. L', 'L.2': 'Home L', 'L.3': 'Away L'})
    return df