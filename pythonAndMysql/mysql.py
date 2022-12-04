import pymysql

connect = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='root', db='student', charset='utf8')
cursor=connect.cursor()
cursor.execute("select * from major where majorid=1;")
data=cursor.fetchone()
print(data)
connect.close()
