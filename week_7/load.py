import pandas as pd

path ="/dtu/projects/02613_2025/data/dmi/2023_01.csv.zip"

# Load the data into a pandas dataframe
df = pd.read_csv(path)

# Function to calculate memory size of dataframe
def df_memsize(df):
    return df.memory_usage(deep=True).sum()

# Print the memory size of the dataframe
print(f"Memory size of the dataframe: {df_memsize(df)} bytes")

# Function to calculate total precipitation how muche
def total_precip(df):
    total = 0.0
    for i in range(len(df)):
        row = df.iloc[i]
        if row['parameterId'] == 'precip_past10min':
            total += row['value']
    return total

print(f"Total precipitation: {total_precip(df)} mm")