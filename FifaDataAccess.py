import sqlite3

class accessdata:
    def __init__(self):
        self.connectionString= "FIFA24.db"

    #Insert data
    def insertQuery(self, query, records):
        try:
            with sqlite3.connect(self.connectionString) as connection:
                connection.executemany(query, records)
                connection.commit()
        except Exception as err:
            print(err)

    #Delete data
    def deleteQuery(self, query):
        try:
            with sqlite3.connect(self.connectionString) as connection:
                connection.execute(query)
                connection.commit()
        except Exception as err:
            print(err)
    #Update data
    def updateQuery(self, query):
        try:
            with sqlite3.connect(self.connectionString) as connection:
                connection.execute(query)
                connection.commit()
        except Exception as err:
            print(err)
            
    #Search within data
    def searchData(self,query):
        try:
            with sqlite3.connect(self.connectionString) as connection:
                results=connection.execute(query)
                rows=results.fetchall()
                return rows
        except Exception as err:
            print(err)