
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QTableWidget, QTableWidgetItem, \
    QHBoxLayout, QVBoxLayout, QPushButton, QTextEdit, QPlainTextEdit,QLineEdit,QHeaderView
from PyQt5.QtCore import Qt
from  AccessDB import AccessDB


#Cоздание шаблона класса программы

class Program():
    def __init__(self):
        self.acess = None
        self.app = QApplication([])
        self.mainWidget = QWidget()
        self.table = QTableWidget()
        self.mainLayout = QVBoxLayout()
        self.girdlayout = QGridLayout()
        self.textEdit = QLineEdit('поиск')
        self.updateButton = QPushButton('Обновить')
        self.findButton = QPushButton('Найти')
        self.layoutTools = QHBoxLayout()
        self.widgets()



#Настройка элементов взаимодействия пользователя с графическим интерфейсом

    def widgets(self):

        self.table = self.table
        self.mainWidget.setWindowTitle('Магазин книг')

        self.table.resizeColumnToContents(2)
        self.table.resizeColumnToContents(1)
        self.table.resizeColumnToContents(0)
        self.girdlayout.addWidget(self.table)
        self.layoutTools.addWidget(self.updateButton, alignment=Qt.AlignLeft,stretch=4)
        self.layoutTools.addWidget(self.textEdit, alignment=Qt.AlignRight,stretch=1000)
        self.layoutTools.addWidget(self.findButton, alignment=Qt.AlignRight,stretch=4)
        self.layoutTools.setSpacing(10)
        self.mainLayout.addLayout(self.layoutTools)
        self.mainLayout.addLayout(self.girdlayout)
        self.mainWidget.setStyleSheet('background-color: #fcfcfc')
        self.mainWidget.resize(800, 600)
        self.updateButton.clicked.connect(self.update)
        self.findButton.clicked.connect(self.find)


#Функция инициализирующая подключение к базе данных
    def connect(self):
        try:
            acess = AccessDB()
            acess.connect()
            self.acess = acess
        except:
            print('Error')

#Функция для обновления данных по нажатию на кнопку
    def update(self):
        data = self.acess.getData()
        size = len(data)
        columns = ['Код', 'Цена','Автор','Издатель','Колличество','Название']
        sizeColumn = len(columns)
        self.table.setColumnCount(sizeColumn)
        self.table.setHorizontalHeaderLabels(columns)
        print(size)
        # print(self.acess.getColumn())
        self.table.setRowCount(size)
        self.table.setHorizontalHeaderLabels(columns)
        self.table.resizeColumnsToContents()
        for i in range(size):
            for j in range(len(data[i])):
                print(data[i][j])
                self.table.setItem(i, j, QTableWidgetItem(str(data[i][j])))
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


#Функция для реализации поиска по названию
    def find(self):

        findPredicate = self.textEdit.text()
        result = self.acess.findData(findPredicate)
        size = len(result)
        print(size)
        self.table.setRowCount(size)
        for i in range(size):
             for j in range(len(result[i])):
                self.table.setItem(i, j, QTableWidgetItem(str(result[i][j])))
#Функция отключения от базы данных
    def disconnect(self):
        self.acess.close()





#Создание объекта программы и запуск
program = Program()
program.mainWidget.setLayout(program.mainLayout)
program.connect()
program.update()
print(program.acess.getData())
program.mainWidget.show()
program.app.exec_()
program.disconnect()

