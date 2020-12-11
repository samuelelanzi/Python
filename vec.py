from array import array

x = array('d')

x.append(1.1)
x.append(2.8)
x.append(3.0)

for i in range(len(x)):
    print(x[i])
