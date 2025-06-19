import numpy as np
import statistics as s
baked_food=[200,300,150,130,200,300,170,180]
a=np.array(baked_food)

#Mean
print(np.mean(baked_food))

#Median
print(np.median(baked_food)) #The values will sort and then the average is taken of middle values

#Mode
print(s.mode(baked_food))

#Standard Deviation
print(np.std(baked_food))

#Variance
print(np.var(baked_food)) #Square of Standard Deviation