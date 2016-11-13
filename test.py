import pandas as pd

x = pd.DataFrame([])
h = pd.Series(['g',4,2,1,1])
print h
x.append(h,ignore_index=True)

print x
