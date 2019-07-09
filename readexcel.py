import pandas as pd
import numpy as np
df = pd.read_excel(r"K:\Public-KL\人事課\出勤表\108年當月\出勤表-0606~0609s.xls")
df.head(15)
df_fillna=df.fillna(0)
department = df.部門.values
Numbering = df.員編.values
Name = df.姓名.values
time=df_fillna.上班.values
Off_work=df_fillna.下班.values
count=0
for i in range(len(time)):
    if time[i]!=0 or Off_work[i]!=0:
        if int(time[i].split(':')[0]) > 7 and (int(time[i].split(':')[0]) > 7 and int(time[i].split(':')[1]) > 0):
            print("部門:"+str(department[i])+'\n員編:'+str(Numbering[i])+"姓名:"+str(Name[i])+"\n上班時間"+str(time[i]))