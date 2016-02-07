import pymysql
try:
    con=pymysql.connect(host='localhost',port=3306,user='root',passwd='root',db='sample')
    print("Connection Successful :-)")
except:
    print("Connection Unsuccessful :-(")
