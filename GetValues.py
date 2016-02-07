import pymysql
con=pymysql.connect(host='localhost',port=3306,user='root',passwd='root',db='test') 
cursor=con.cursor()
sql="SELECT * FROM `student`"
cursor.execute(sql)
results=cursor.fetchall()
for i in results:
    print(i)
