import pandas 

df = pandas.read_csv("ejemplo pandas.csv")

#print(df)


#print("columnas ", df.columns)


#print(df.head())

#print(df.tail())

#print(df.info())


#df2 = df.dropna()


#df.dropna(inplace=True)



#df.fillna(130, inplace=True)


x = df["Resultado"].mean()
x = df["Resultado"].median()
x = df["Resultado"].mode()
x = df["Resultado"].std()
x = df["Resultado"].var()
x = df["Resultado"].min()
x = df["Resultado"].max()
x = df["Resultado"].sum()
x = df["Resultado"].count()
x = df["Resultado"].describe()


print(x)