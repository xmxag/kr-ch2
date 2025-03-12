import psycopg2
import PySide6 
from PySide6 import QtWidgets
from PySide6.QtWidgets import QMainWindow,QTableWidgetItem,QApplication,QVBoxLayout,QHBoxLayout,QPushButton,QTableWidget,QWidget,QDialog



def connect ():
    return psycopg2.connect (
     dbname = "postgres",
        user = "postgres",
        password = "1234",
        host = "localhost", 
        port = "5432"     
        )
    
    
class MainWindow (QMainWindow):
    def __init__ (self):
        super().__init__()    

        self.resize(750,500)
        self.setWindowTitle ("KR")
        self.widget = QWidget()
        
        self.setCentralWidget(self.widget)
        
        
        layout= QVBoxLayout (self.widget)
        
        self.button1 = QPushButton ("добавить")
        self.button2 = QPushButton ("редактировать")
        
        self.table1 = QTableWidget()
        
        self.table1.setColumnCount (7)
        self.table1.setHorizontalHeaderLabels(["id","first_name","last_name","position","salary","hire_date","department_id"])
        
        self.table2 = QTableWidget()
        
        self.table2.setColumnCount (6)
        self.table2.setHorizontalHeaderLabels(["id","name","description","status","project_id","assignee_id"])
        
        
        
        
        layout.addWidget (self.table1)
        layout.addWidget (self.button1)
        layout.addWidget (self.button2)
        
        layout.addWidget (self.table2)    
        layout.addWidget (self.button1)
        layout.addWidget (self.button2)
         
        self.load1() 
        self.load2()          
         
    def load1(self):
        conn = connect()
        cur = conn.cursor()
        cur.execute("select * from employees")
        data = cur.fetchall()     
    
        self.table1.setRowCount(len(data) )
        for row_id,rows in enumerate (data):
            for col_id, value in enumerate (rows):
                self.table1.setItem(row_id,col_id,QTableWidgetItem(str(value)))
        
        cur.close()
        conn.close()
    
    
    
    def load2(self):
        conn = connect()
        cur = conn.cursor()
        cur.execute("select * from tasks")
        data = cur.fetchall()     
    
        self.table2.setRowCount(len(data) )
        for row_id,rows in enumerate (data):
            for col_id, value in enumerate (rows):
                self.table1.setItem(row_id,col_id,QTableWidgetItem(str(value)))
        
        cur.close()
        conn.close()    
    
    
#class add1 (QDialog):
    #def __init__(self):
      #  super().__init__()
        
       # self.setWindowTitle("добавить")
        
        
        
        
        
        
        
        
        
            
    
app = QApplication([])
window = MainWindow()
window.show()
app.exec()    
