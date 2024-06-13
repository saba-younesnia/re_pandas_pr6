import pandas as pd

data=pd.read_csv('C:\\Users\\YOONES-NIA\\Desktop\\csv_files\\nba.csv',index_col='Team')

data1=data.loc[['Toronto Raptors']]
index_labels1=data1.index

data2=data.loc[['Phoenix Suns']]
index_labels2=data2.index

data3=data.loc[['Chicago Bulls']]
index_labels3=data3.index

new_data1=data.drop(index_labels1,axis=0,inplace=False)
new_data2=new_data1.drop(index_labels2,axis=0,inplace=False)
new_data3=new_data2.drop(index_labels3,axis=0,inplace=False)

s_salary=new_data3['Salary']
l_salary=s_salary.tolist()

new_lsalary=[]
for element in l_salary:
    new_salary=element/1000
    new_lsalary.append(new_salary)

new_data3.insert(8,'Salary/1000',new_lsalary,True)
print(new_data3.to_string())







