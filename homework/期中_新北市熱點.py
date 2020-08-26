import sqlite3,os
conn=sqlite3.connect("NewTaipei_wifilocate.db")
cursor=conn.cursor()


#只查詢部分區域，另外存成CSV檔
x=input("熱點查詢，請輸入新北市地區:")
sqlstr="select * from wifilocation01 where district like '%"+x+"%'"
cursor.execute(sqlstr)

if os.path.exists(r"C:\Users\user\Desktop\大數據班資料 eclipse\python報告\\"+x+"地區.csv"):
    os.remove(r"C:\Users\user\Desktop\大數據班資料 eclipse\python報告\\"+x+"地區.csv")

newfile=""
print("institution,spot_name,address")
for row in cursor:
#     print=("{},{},{}".format(row[3],row[0],row[2]))
    newfile+=row[3]+","+row[0]+","+row[2]+"\n"
print(newfile)
fw=open(r"C:\Users\user\Desktop\大數據班資料 eclipse\python報告\\"+x+"地區.csv","w")
fw.write("institution,spot_name,address\n"+newfile)
print("存檔成功")
conn.close()



