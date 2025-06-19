a=("bmw","Audii","Porsche")
print("Before Conversion : ",type(a))

a=list(a)
print("After Conversion : ",type(a))

# Now we can manipulate the elements

a.append("Supra")
print(a)

#Index
print(a.index("bmw"))
