
import sqlite3
conn=sqlite3.connect("NewTaipei_wifilocate.db")
cursor=conn.cursor()
sqlstr="drop table if exists wifilocation01"
cursor.execute(sqlstr)
sqlstr='create table if not exists wifilocation01 \
 ("spot_name" TEXT, "district" TEXT, "address" TEXT, "institution" TEXT, "company" TEXT)'
cursor.execute(sqlstr)

 
f=open(r"C:\Users\user\Desktop\大數據班資料 eclipse\python報告\新北市NewTaipei熱點.csv","r",encoding="UTF-8")
s=f.readlines()
# print(s)
for i in range(1,len(s)):
    list1=s[i].split(",")
#     print(list1)
    sqlstr="insert into wifilocation01 values \
     ('{}','{}','{}','{}','{}')".format(list1[1],list1[4],list1[5],list1[6],list1[3].strip("\n"))
    cursor.execute(sqlstr)
 
 
conn.commit()
conn.close()
print("寫入完成!!")
