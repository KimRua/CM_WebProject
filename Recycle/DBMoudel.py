import pymysql

class Database():
    def __init__(self):
        self.db = pymysql.connect(
            host='211.47.75.102',
            user='gyeonggicm',
            db='dbgyeonggicm',
            password = 'rhksflwk010203',
            port=3306
        )
        # self.db = pymysql.connect(
        #     host='localhost',
        #     user='root',
        #     db='recycle',
        #     password = '1234',
        #     port=3306
        # )
        self.cursor = self.db.cursor(pymysql.cursors.DictCursor)
    
    def execute(self, query, args={}):
        self.cursor.execute(query, args)
        self.db.commit()
    
    def executeOne(self, query, args={}):
        self.cursor.execute(query, args)
        return self.cursor.fetchone()
    
    def executeAll(self, query, args={}):
        self.cursor.execute(query, args)
        return self.cursor.fetchall()
    
    def close(self):
        self.db.close()