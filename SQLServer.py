import pyodbc 
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
class SqlSvr:
    server = '127.0.0.1' 
    database = 'msdb' 
    username = 'sa' 
    password = '' 
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = cnxn.cursor()
    
    def select(self):
        self.cursor.execute("SELECT @@version;") 
        row = self.cursor.fetchone() 
        while row: 
            print(row[0])
            row = self.cursor.fetchone()
            
