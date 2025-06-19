import pandas as pd

#PIVOTING

dic = {
    "keys": ["k1", "k2", "k1", "k2"],
    "Names": ["John", "Ben", "David", "Peter"],
    "Houses": ["red", "blue", "green", "red"],
    "Grades":["3rd","8th","9th","8th"]
}

# df = pd.DataFrame(dic)
# print(df)
#
# print(df.pivot(index="keys", columns="Names", values=["Houses","Grades"]))

#MELTING

dict = {

    "Names": ["John", "Ben", "David", "Peter"],
    "Houses": ["red", "blue", "green", "red"],
    "Grades":["3rd","8th","9th","8th"]
}
df1 = pd.DataFrame(dict)
print(df1)
print()

print(pd.melt(df1,id_vars=["Names"],value_vars=["Houses","Grades"],var_name="Houses&Grades",value_name="values"))