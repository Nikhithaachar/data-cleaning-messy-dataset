import pandas as pd

#Load data
df=pd.read_csv("messy_data.csv")

#Remove duplicates
df=df.drop_duplicates()

#Fix age column(Convert text to number)
df['Age']=pd.to_numeric(df['Age'],errors='coerce')

#Fill missing age eith average
df['Age']=df['Age'].fillna(df['Age'].mean())

#Fill missing salary with median
df['Salary']=df['Salary'].fillna(df['Age'].median())

#fix email(replace invalid or missing)
df['Email']=df['Email'].fillna("unknown@gmail.com")
df['Email']=df['Email'].apply(lambda x:x if "@" in x else "invalid@gmail.com")

#standardize Date format
df[ 'JoinDate']=pd.to_datetime(df['JoinDate'],errors='coerce')
df['JoinDate']=df['JoinDate'].dt.strftime('%Y-%m-%d')

#save cleaned file
df.to_csv("cleaned_data.csv",index=False)
print(df)