import numpy as np
import matplotlib.pyplot as plt
import math
import pandas

def arctan(x):
    return np.arctan(x)

x = math.sqrt(2)

def derivative2c(h):
    return (arctan(x+(h))-arctan(x))/(h)

def derivative3c(h):
    return (arctan(x+(h))-arctan(x-(h)))/(2*h)

def error(computed, exact):
    return abs((computed-exact)/exact)

hraw = np.linspace(1,1000,1000)
h = hraw/1000

computed2c = []
computed3c = []

for i in h:
    computed2c.append(derivative2c(i))
    computed3c.append(derivative3c(i))

errorvalues2c = []
errorvalues3c = []

for val in computed2c:
    errorvalues2c.append(error(val,1/3)*100)
for val in computed3c:
    errorvalues3c.append(error(val,1/3)*100)

lst1 = h
lst2 = computed2c
lst3 = computed3c
lst4 = errorvalues2c
lst5 = errorvalues3c

table = pandas.DataFrame({'h': lst1, 'Computed-2c': lst2, 'Computed-3c': lst3,'Error Values-2c': lst4,'Error Values-3c': lst5})
print(table)

log102c =[]
log103c = []

for value in errorvalues2c:
    log102c.append(math.log10(value))
for value in errorvalues3c:
    log103c.append(math.log10(value))

plt.plot(h, log102c)
plt.title("Log10 of Error 2c")
plt.ylabel("Log10")
plt.xlabel("Error Calculated")
plt.show()

plt.plot(h, log103c)
plt.title("Log10 of Error 3c")
plt.ylabel("Log10")
plt.xlabel("Error Calculated")
plt.show()
