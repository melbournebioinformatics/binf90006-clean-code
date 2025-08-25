# TO-DO: don't use global variables for functions

# relies on a global df (defined in notebooks)
def clean_data():
    df['island'] = df['island'].fillna('Biscoe')
    if 'body_mass' in df.columns:
        df['body_mass_g'] = df['body_mass']
    return df

def summarize():
    return df.groupby('species')['flipper_length_mm'].mean()
