import pandas as pd


df = pd.read_csv('pooja.csv',index_col=False)

df_norm = (df.ix[:, 1:-1] - df.ix[:, 1:-1].mean()) / (df.ix[:, 1:-1].max() - df.ix[:, 1:-1].min())
print df_norm 
rslt =  pd.concat([df_norm, df.ix[:,-1]], axis=1)
rslt.to_csv('example.csv',index=False,header=False)
