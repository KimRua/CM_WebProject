import pymysql
import hashlib

def check(userID, password):
    con = pymysql.connect(host='db.gyounggicm.co.kr', user='gyeonggicm', password='rhksflwk010203',
                        db='dbgyeonggicm', charset='utf8')
    cur = con.cursor(pymysql.cursors.DictCursor)
    sql = "SELECT USERID, USERPW FROM PERSON WhERE USERID=%s"
    cur.execute(sql,(userID))
    rows = cur.fetchall()
    result = hashlib.sha256(password.encode()) 
    if rows == ():
        return(None, None)
    for row in rows:
        if row['USERPW'] == result.hexdigest() :
            con.close()
            return("확인", userID)
        else:
            return (None, None)

def logup(userID, password, code):
    f = open('authentication.txt','r')
    auth = f.read()
    f.close
    if hashlib.sha256(code.encode()).hexdigest() != auth:
        return False
    con = pymysql.connect(host='db.gyounggicm.co.kr', user='gyeonggicm', password='rhksflwk010203',
                        db='dbgyeonggicm', charset='utf8')
    cur = con.cursor(pymysql.cursors.DictCursor)
    password = hashlib.sha256(password.encode())
    try:
        sql = "INSERT INTO PERSON(USERID, USERPW) VALUES (%s, %s)"
        cur.execute(sql,(userID, password.hexdigest()))
        con.commit()
    except:
        return False
    return True