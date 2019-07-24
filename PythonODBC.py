import pyodbc


class Northwind:
    def __init__(self):
        self.server = 'localhost,1433'
        self.database = 'Northwind'
        self.username = 'sa'
        self.password = 'Passw0rd2018'
        self.docker_northwind = pyodbc.connect('DRIVER={SQL Server} ;SERVER=' + self.server
                                               + ' ;DATABASE=' + self.database + ' ;UID=' + self.username + ' ;PWD='
                                               + self.password)
        self.cursor = self.docker_northwind.cursor()

    def read_from_db(self, table, condition=''):
        table_data = self.cursor.execute(f"SELECT * FROM {table} {condition}")
        return table_data.fetchall()

    def create_db(self, tablename):
        try:
            self.cursor.execute("CREATE TABLE " + tablename + "( ID int NOT NULL IDENTITY PRIMARY KEY,"
                                                              "Name VARCHAR (32));")
            my_db.docker_northwind.commit()
        except:
            print("Something has gone wrong")
        finally:
            my_db.docker_northwind.close()

    def write_to_db(self, table, *field):
        fields = '()'
        for each in field:
            fields = fields + each
            if each != field[-1]:
                fields = fields + ', '
        try:
            self.cursor.execute(f"INSERT INTO {table} VALUES {fields};")
            self.docker_northwind.commit()
        except:
            print('Something went wrong')
        finally:
            self.docker_northwind.close()

