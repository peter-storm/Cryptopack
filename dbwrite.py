import MySQLdb as mdb

##icocount_list = 

conn =mdb.connect(host="localhost",user="dbadmin", ##host, if left off, defaults to localhost
                  passwd="Sparhawk9",db="ico") ##pword is required, db is required

cur = conn.cursor()

sqltest = "INSERT INTO `ico count` ( `Transaction ID`) VALUES ( %s )"

## Following Line willl be the final code
## sql = "INSERT INTO `ico count` ( `Transaction ID`, `Date`, `ICO Count` ) VALUES ( %(id)s, %(thing)s, %(value)s )"



cur.execute( sqltest , [1])
con.close()



##Old SQL DB code, stashing this for now, didnt work
"""conn = pyodbc.connect( #Initiate connection, send credentials, get verification
    r'DRIVER={ODBC Driver 13 for SQL Server};' ##Drivers needed for specific DB install
    r'SERVER=test;' ##Name of the SQL Server
    r'DATABASE=test;' ##Name of the SQL DB
    r'UID=user;' ##DB Admin Username
    r'PWD=password' ##DB Admin Password
    )

cursorprod.execute("SELECT Servername = @@servername    ,Date = getdate()   ,wait_type  ,waiting_tasks_count    ,wait_time_ms   ,max_wait_time_ms   ,signal_wait_time_ms FROM sys.dm_os_wait_stats GO") ##Picking columns in question
rows = conn.fetchall() ##Fetching the columns I want to insert values into

for row in rows
cursor.execute('insert into ___ values (')
cnxn.commit()	