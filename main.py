import pandas as pd

df1 = pd.read_json('file1.json')

# view data
print(df1)

# load json file using pandas
df2 = pd.read_json('file2.json')

# view data
print(df2)

# use pandas.concat method 
df = pd.concat([df1,df2])

# view the concatenated dataframe
print(df)

# convert dataframe to csv file
df.to_csv("CSV.csv",index=False)

# load the resultant csv file
result = pd.read_csv("CSV.csv")

# and view the data
print(result)
