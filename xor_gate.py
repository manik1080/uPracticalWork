import pandas as pd
xor2 = pd.DataFrame({'X':[0]*4, 'Y':[0]*4, 'Output':[0]*4})
xor3 = pd.DataFrame({'X':[0]*8, 'Y':[0]*8, 'Z':[0]*8, 'Output':[0]*8})

def xor(x, y):
    out = (~x & y) + (x & ~y)
    return [ x, y, out ]

def xor_3(x, y, z):
    out = (x & ~y & ~z) + (~x & y & ~z) \
           + (~x & ~y & z) + (x & y & z)
    return [ x, y, z, out ]

print("Truth table for 2 value XOR: ")
for i in range(4):
    xor2.loc[i] = xor(i//2, i%2)
print(xor2)


print("\nTruth table for 3 value XOR: ")
for i in range(8):
    xor3.loc[i] = xor_3(i//4, (i//2)%2, i%2)
print(xor3)
