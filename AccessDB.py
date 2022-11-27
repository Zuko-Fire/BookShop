import pyodbc
import os

#Создание шаблона объекта базы данных
class AccessDB():
    def __init__(self):
        self.connStr = (
        r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};" 
        fr"DBQ={os.getcwd ()}\Shop.accdb"
        )

#Функция подключения к базе данных
    def connect(self):
        self.connection = pyodbc.connect(self.connStr)
        self.cursor = self.connection.cursor() # создается курсор



#Функция получения данных из базы(селекция)
    def getData(self):

        self.cursor.execute('SELECT * FROM Product;')
        result = []
        result = self.cursor.fetchall()
        print(result)
        return result

#Функция получения данных по предикату(поиск данных по запросу)
    def findData(self, predicate):
        self.cursor.execute(f"SELECT * FROM Product WHERE Product.Название LIKE'%{predicate}%';")
        result = self.cursor.fetchall()
        print(result)
        return result

#Функция закрытия соединения с базой данных
    def close(self):
        self.cursor.close()
        self.connection.close()


