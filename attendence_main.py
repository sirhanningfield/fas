import sys, os
import time
import hashlib
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import mysql.connector
import ntpath
import shutil
import datetime

from attendance import Ui_attendance

try:
    _fromUtf8 = QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s


mydb = mysql.connector.connect(
	  host="localhost",
	  user="root",
	  passwd="",
	  database="fas"
	)
cursor = mydb.cursor(named_tuple=True)

class Main(QMainWindow, Ui_attendance):
	"""docstring for Main"""
	def __init__(self):
		super(Main, self).__init__()
		# self.arg = arg
		self.cursor = cursor
		self.attendance_ui = Ui_attendance()
		self.attendance_ui.setupUi(self)
		self.classes = self.getAllClasses()
		self.attendance_ui.scan_class_no.addItems(self.classes)

	def getAllClasses(self):
		print "Get all classes ..."
		query = "SELECT * FROM classes"
		cursor.execute(query)
		result = cursor.fetchall()
		classes = []

		for row in result:
			classes.append(row.class_code)
		
		return classes


def main():
	
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()