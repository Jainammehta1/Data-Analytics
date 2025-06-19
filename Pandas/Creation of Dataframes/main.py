import pandas as p

data={"Name":["John","Jai","Hari"],
      "Age":[25,30,35],
      "Salary":[3000,4000,6000]}

df=p.DataFrame(data)
print(df)

data=p.read_csv("Sample.csv")
print(data)

dat=p.read_excel("C:/Users/Lenovo/OneDrive/Desktop/Excel/hotel_bookings.csv.xlsx")
print(dat)