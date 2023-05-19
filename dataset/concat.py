import pandas as pd 

df1 = pd.read_csv('D:/Major project/dataset/draw.csv')
df2 = pd.read_csv('D:/Major project/dataset/erase.csv')
df3 = pd.read_csv('D:/Major project/dataset/none.csv')

df4 = pd.concat([df1, df2])
df5 = pd.concat([df4, df3])
df5.to_csv("D:/Major project/dataset/dataset.csv")