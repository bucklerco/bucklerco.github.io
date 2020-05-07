import pandas as pd

df = pd.read_excel("directories.xlsx")
df.to_csv("directories.csv")
