import matplotlib.pyplot as plt
import pandas as pd
plt.rc('font',family='SimHei')
plt.rcParams['axes.unicode_minus'] = False
file_path = r"C:\Users\DELL\Desktop\SHL(5).xlsx"
df=pd.read_excel(file_path,sheet_name='供应预测')
df=df.iloc[:,2:]
for i in range(50):
    h=0;t=68000
    for j in range(24):
        if t>=34000*(j+1):
            t=t+sum(df.iloc[0:i+1,j])
            h=h+1
    if h==24:
        print(f'至少需要{i+1}家供应商')
        break