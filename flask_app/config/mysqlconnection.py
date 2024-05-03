import pymysql.cursors

class mySQLConnection:
    def __init__(self, DB):
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="root_root",
            db=DB,
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=False
        )
        self.connection = connection
        
    def query_db(self, query:str, data:dict=None):
        with self.connection.cursor() as cursor:
            try:
                query = cursor.mogrify(query, data)
                print("*****")
                print("Running Query:", query)
                
                cursor.execute(query)
                # INSERT
                if query.lower().find("insert") >= 0:
                    self.connection.commit()
                    return cursor.lastrowid
                # SELECT
                elif query.lower().find("select") >= 0:
                    result = cursor.fetchall()
                    return result
                # UPDATE, DELETE
                else:
                    self.connection.commit()
            
            except Exception as error:
                print("---------------")
                print("Something went wrong:", error)
                print("---------------")
                return False
                
            finally:
                self.connection.close()
                

def connectToMySQL(DB):
    return mySQLConnection(DB)