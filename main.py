import joe_def_v2 as sw
import pymysql
from colorama import init
init()

# Version 1 initalized。

# DB Args
db_settings = {"host": "192.168.68.252", "user": "python", "password": "Kx12930780@@", "db": "kx_db", "charset": "utf8"}

# Connect DB
try:
    conn = pymysql.connect(**db_settings); cursor = conn.cursor()
except pymysql.err.OperationalError as err:
    code, msg = err.args
    if code == 2003:
        print("Can't Connect to KB Database, Check Your Connection.")
        input("Press Enter to Exit ... ")
    raise

# Main
try:
    Success = 0; Error = 0
    command = "SELECT * FROM TAB_ITM WHERE ITM_HAD_MOD LIKE " + "'" + "%XI%" + "'"
    cursor.execute(command); data = cursor.fetchall()
    for row in data:
        print (row[1] + \
               sw.col_green() + "," + row[6] + \
               sw.col_green() + "," + row[4] + \
               sw.col_green() + "," + row[8] + \
               sw.col_yellow() + "," + row[9] + sw.col_def())
        Success += 1
    cursor.close(); conn.close()
    print("")
    print("Success Quary Data : " + sw.col_green() + str(Success) + sw.col_def())
    print("Error Quary Data : " + sw.col_red() + str(Error) + sw.col_def())
    print("")
    input("Press Enter to Exit ...")

except Exception:
    input("Something Error, Check with Coder ...")
    raise
