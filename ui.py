from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import pymongo
import pandas as pd
import random

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["address"]
users = db["users"]
epin = db["epin"]

from interface import Ui_lo as Ui_MainWindow
# import ui
from address import Ui_Dialog as Ui_Address_Dialog




class Address_dialog(QDialog):
    def __init__(self, parent=None):
        super(Address_dialog, self).__init__(parent)
        self.ui = Ui_Address_Dialog()
        self.ui.setupUi(self)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
       
        self.setupUi(self)
        
        
        self.pushButton_9.pressed.connect(self.save_address)
        self.pushButton_9.pressed.connect(self.show_address)
        


    def save_address(self):
        self.address = {
            'name':	self.name_input.text(),
            'house': self.house_input.text(),
            'area':	self.area_input.text(),
            'city': self.city_input.text(),
            'state': self.state_input.text(),
            'pin-code': self.pin_input.text(),
        }
        users.insert_one(self.address)
        
        
        
    def show_address(self):
        self.state_name=" "
        input_dlg = Address_dialog()
        state = self.address["state"]
        file = open("test.txt","r")
        for x in file.readlines():
            if x == state.upper():
                second = x.partition(':')
                self.state_name = second[1]
        x = random.randint(200,300)
        final = "121001-"+str(x)+"-23-1"
        input_dlg.ui.address.setText(final)
        input_dlg.exec()
                

app = QApplication([])
window = MainWindow()
window.show()
app.exec()
