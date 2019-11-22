import sqlite3


class Waterholes_DB: 
    def __init__(self,path):
        self.connection = sqlite3.connect(path)

    def add_int_row(self,name, default_value):
            addColumn = "ALTER TABLE waterholes ADD COLUMN" + name + "INTEGER DEFAULT("+ default_value +")"
            cur   = self.connection.cursor()
            cur.execute(addColumn)
    
    def get_all_waterholes(self):
        """
        Query all rows in the tasks table
        :param conn: the Connection object
        :return:
        """
        cur = self.connection.cursor()
        cur.execute("SELECT * FROM waterholes")
        rows = cur.fetchall()
        return rows

    @staticmethod
    def response_to_json(response):
        """
        response is array [[id,x,y,s]]
        """
        result = []
        for row in response:
            result.append({'index': row[0],'x':row[1],'y':row[2],'state':row[3]})
        return result


db = Waterholes_DB('waterholes.db')
print(db.response_to_json(db.get_all_waterholes()))