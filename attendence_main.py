import sys, os
import time
import hashlib
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import mysql.connector
import ntpath
import shutil
import datetime
import serial

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

Comport = 'COM3'
Baudrate = 115200

class Main(QMainWindow, Ui_attendance):
	"""docstring for Main"""
	def __init__(self):
		super(Main, self).__init__()
		# self.arg = arg
		self.cursor = cursor
		self.attendance_ui = Ui_attendance()
		self.attendance_ui.setupUi(self)
		self.classes = self.getAllClasses()
		# self.attendance_ui.scan_class_no.addItems(self.classes)
		self.fid = ""
		self.attendance_ui.std_attn_status.setDisabled(True)
		self.Connect_Arduino()
		self.attendance_ui.scan_finger_btn.clicked.connect(lambda: self.readFingerprint())
		self.attendance_ui.dateEdit.setDateTime(QDateTime.currentDateTime())
		self.attendance_ui.scan_done_btn.clicked.connect(lambda: self.addAttendance())

	def showErrorMessage(self,message):
		msg = QMessageBox()
		msg.setWindowTitle("oops!")
		msg.setIcon(QMessageBox.Information)
		msg.setText(message)
		retval = msg.exec_()

	def addAttendance(self):
		student_id = str(self.attendance_ui.scan_std_id.text())
		class_code = str(self.attendance_ui.scan_class_no.currentText())
		date = str(self.formatDate(str(self.attendance_ui.dateEdit.text())))

		credentials = [class_code,student_id,date]

		if self.validateCredentials(credentials,"Please enter all fields") == False :
			return 
			pass

		result = self.checkAttendanceExists(class_code,student_id,date)

		if result:
			self.showErrorMessage("Attendance already exists for this date")
		 	pass
		else:
		 	print "here"
		 	if self.addAttendanceRow(class_code,student_id,date):
				self.showErrorMessage("Attendance Added!")
				self.attendance_ui.scan_std_id.setText("")
				self.attendance_ui.scan_std_name.setText("") 
				self.attendance_ui.scan_std_dob.setText("")
				self.attendance_ui.scan_std_guardian.setText("")
				self.attendance_ui.scan_std_pic.setPixmap(QPixmap(_fromUtf8(":/holder/img/holder_1.PNG")))
				self.attendance_ui.scan_finger_btn.setEnabled(True)
				pass
		pass

	def addAttendanceRow(self,class_code,student_id,date):
		sql = "INSERT INTO attendance (student_id, class_code, date) VALUES (%s, %s, %s)"
		val = (student_id, class_code, date)
		cursor.execute(sql, val)
		mydb.commit()
		return True
		pass

	def checkAttendanceExists(self, class_code, student_id, date):

		query = "SELECT * FROM attendance WHERE class_code = '"+class_code+"' AND student_id = '"+student_id+"' AND date = '"+date+"'"
		cursor.execute(query)
		result = cursor.fetchone()
		return result
		pass

	def validateCredentials(self,credentials,message):
    	
		for i in range(len(credentials)) :
			if (not credentials[i]):
				self.showErrorMessage(message)
				return False
		return True

	def formatDate(self, date):
		return datetime.datetime.strptime(date, "%d/%m/%Y").date()

	def getAllClasses(self):
		print "Get all classes ..."
		query = "SELECT * FROM classes"
		cursor.execute(query)
		result = cursor.fetchall()
		classes = []

		for row in result:
			classes.append(row.class_code)

		return classes

	def Connect_Arduino(self):

	    try:
	        self.ser = serial.Serial(Comport,Baudrate, timeout=0)
	        print "Connecting to arduino"
	        self.workThread = WorkThread(self)
	        self.connect( self.workThread,SIGNAL("update(QString)"), self.dummy )
	        self.workThread.start()

	    except:
	        print ('No Arduino found')
	        sys.exit()

	def Buffer(self):
	    buffer = ''
	    while True:
	        buffer = buffer + str(self.ser.read(self.ser.inWaiting()).strip().decode())
	        return buffer

	def dummy(self,text):

		text = str(text)
		if len(text) > 0:
			text = text + "\n"
			if text.startswith("#"):
				self.parseText(text)
			else:
				# print text
				self.attendance_ui.std_attn_status.insertPlainText(text)
	    	
	def readFingerprint(self):
		self.ser.write("B")
		pass

	def parseText(self, text):
		print "Parsing and understanding text..."

		# If string starts with F its finding an ID , if it starts with E its enrolling an ID

		fid = text.split(" ")[1] 
		if text.startswith("#F"):
			self.findStudentById(fid)
			pass
		if text.startswith("#E"):
			self.fid = fid
			pass

		pass

	def findStudentById(self, fid):
		student = self.checkIfExists("students","fingerprint_id", fid)
		# print student
		self.attendance_ui.scan_finger_btn.setEnabled(False)
		if student:
			self.attendance_ui.std_attn_status.insertPlainText("Found match at ID: "+fid)
			self.attendance_ui.scan_std_id.setText(student.student_id)
			self.attendance_ui.scan_std_name.setText(student.name) 
			self.attendance_ui.scan_std_dob.setText(student.dob.strftime('%m/%d/%Y'))
			self.attendance_ui.scan_std_guardian.setText(student.guardian)

			if student.image_path:
				pixmap = QPixmap(student.image_path)
		    	pixmap = pixmap.scaled(300,300)
		    	if pixmap:
		    		self.attendance_ui.scan_std_pic.setPixmap(pixmap)
		    		pass
				pass
			
			if student.student_id:
				classes = self.getStudentClasses(student.student_id)
				self.attendance_ui.scan_class_no.addItems(classes)
				pass
			pass
		pass

	def getStudentClasses(self, studentId):
		table = "student_classes"
		column = "student_id"
		value = studentId
		classesTable = "classes"
		query = "SELECT * FROM "+table+" WHERE "+column+" = '"+value+"'"
		cursor.execute(query)
		result = cursor.fetchall()

		classes = []

		for row in result:
			classes.append(row.class_code)
		
		return classes
		pass

	def checkIfExists(self, table,column, value):
		query = "SELECT * FROM "+table+" WHERE "+column+" = '"+value+"'"
		cursor.execute(query)
		result = cursor.fetchone()
		return result

class WorkThread(QThread):

    def __init__(self,parent= None):
        QThread.__init__(self,parent)
        self.parent = parent
        self.wert = ""

    def run(self):

        while True:
            time.sleep(0.2)
            self.wert = str(self.parent.Buffer())
            self.emit(SIGNAL('update(QString)'),self.wert)
        return

def main():
	
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()