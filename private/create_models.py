from partials.db.BaseModel import BaseModel


class CreateTables(BaseModel):

    def __init__(self,file:str):
        super().__init__(**self.keys_db)
        self.file = file

    def execute(self):
        file_sql = self.read_sql_file(self.file)

        self.read_sql_file(file_sql)

    def create_tables(self,query:str):
        con,cur = self.connect()
        try:
            cur.execute(query)
            con.commit()
        except:
            print('no se pudo crear las tablas')
        finally:
            cur.close()
            con.close()


    def read_sql_file(self,file):
        with open(file,'r') as f:
            for line in f.readlines():
                print(line)




