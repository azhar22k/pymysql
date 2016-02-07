import pymysql
con=pymysql.connect(host='localhost',port=3306,user='root',passwd='root',db='test') 
cursor=con.cursor()
sql='INSERT INTO `student`(`name`) VALUES(%s)'
cursor.execute(sql,('Azhar Khan'))
con.commit()
con.close()
