import pandas as pd

path ="/dtu/projects/02613_2025/data/dmi/2023_01.csv.zip"

# Load the data into a pandas dataframe
df = pd.read_csv(path)

# Function to calculate memory size of dataframe
def df_memsize(df):
    return df.memory_usage(deep=True).sum()

# Print the memory size of the dataframe
print(f"Memory size of the dataframe: {df_memsize(df)} bytes")

def summarize_columns(df):
    print(pd.DataFrame([
        (
            c,
            df[c].dtype,
            len(df[c].unique()),
            df[c].memory_usage(deep=True) // (1024**2)
        ) for c in df.columns
    ], columns=['name', 'dtype', 'unique', 'size (MB)']))
    print('Total size:', df.memory_usage(deep=True).sum() / 1024**2, 'MB')
    
summarize_columns(df)