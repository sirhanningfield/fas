import sys, os
import time
import hashlib
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import mysql.connector
import ntpath
import shutil
import datetime


from login import Ui_login
from admin import Ui_admin

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



class Main(QWidget, Ui_login, Ui_admin):

    def __init__(self, parent = None):
        super(Main,self).__init__(parent)
        self.parent = parent
        self.cursor = cursor
        self.login_ui = Ui_login()
        self.login_ui.setupUi(self)
        self.stdRegImg = ""
        self.login_ui.login_btn.clicked.connect(lambda: self.login())
        self.login_ui.password.returnPressed.connect(lambda: self.login())
        self.classes = self.getAllClasses()

    def getAllClasses(self):
    	print "Get all classes ..."
    	query = "SELECT * FROM classes"
    	cursor.execute(query)
    	result = cursor.fetchall()
    	classes = []

    	for row in result:
    		classes.append(row.class_code)

    	return classes

    def openAdminWindow(self):
    	# self.admin_window = Admin(self)
    	self.window = QTabWidget()
    	self.admin_ui = Ui_admin()
    	self.admin_ui.setupUi(self.window)
    	self.window.show()
    	self.admin_ui.add_class_btn.clicked.connect(lambda: self.addClass())
    	self.admin_ui.reg_std_btn.clicked.connect(lambda: self.addStudent())
    	self.admin_ui.reg_std_upload_btn.clicked.connect(lambda: self.chooseFile())
    	self.admin_ui.reg_std_class_list.addItems(self.classes)
    	self.admin_ui.add_class_list.addItems(self.classes)
    	self.admin_ui.res_class.addItems(self.classes)
    	self.getClassStudents()
    	self.admin_ui.res_class.currentIndexChanged.connect(lambda: self.getClassStudents())
    	self.admin_ui.res_display_btn.clicked.connect(lambda: self.getAttendence())
    	self.resetTableView()
    	self.admin_ui.res_reset_btn.clicked.connect(lambda: self.resetTableView())
    	pass

    def resetTableView(self):

    	self.admin_ui.res_table_view.setRowCount(1)
    	self.admin_ui.res_table_view.setColumnCount(4)
    	self.admin_ui.res_table_view.setItem(0,0, QTableWidgetItem("Student ID"))
    	self.admin_ui.res_table_view.setItem(0,1, QTableWidgetItem("Student Name"))
    	self.admin_ui.res_table_view.setItem(0,2, QTableWidgetItem("Class Code"))
    	self.admin_ui.res_table_view.setItem(0,3, QTableWidgetItem("Date"))
    	self.admin_ui.res_display_btn.setEnabled(True);
    	self.admin_ui.result_count.setText("0");

    	pass

    def getAttendence(self):

    	self.admin_ui.res_display_btn.setEnabled(False);
    	# check all fields are filled, get attendence
    	class_code = str(self.admin_ui.res_class.currentText())
    	student_id = str(self.admin_ui.res_std_id.currentText().split(" ")[0])
    	date_from = str(self.formatDate(str(self.admin_ui.res_date_from.text())))
    	date_to = str(self.formatDate(str(self.admin_ui.res_date_to.text())))
    	credentials = [class_code,student_id,date_from,date_to]
    	if self.validateCredentials(credentials,"Please enter all fields") == False :
    		return 
    		pass

    	#  Query and find all records of the attendence of the student from and to date
    	query = "SELECT a.student_id, s.name,a.class_code, a.date FROM attendance a LEFT JOIN students s ON s.student_id = a.student_id WHERE a.class_code = '"+class_code+"' AND a.student_id='"+student_id+"' AND a.date >='"+date_from+"' AND date <='"+date_to+"'"

    	cursor.execute(query)
    	result = cursor.fetchall()
    	print result
    	# fill in the table
    	for row_number, row_data in enumerate(result):
    		row_number += 1
    		self.admin_ui.res_table_view.insertRow(row_number)
    		for column_number, data in enumerate(row_data):
    			self.admin_ui.res_table_view.setItem(row_number,column_number,QTableWidgetItem(str(data)))
    			pass
    		pass
    	
    	self.admin_ui.result_count.setText(str(len(result)));
    	pass

    def getClassStudents(self):
    	self.admin_ui.res_std_id.clear() 
    	class_code = str(self.admin_ui.res_class.currentText())
    	# get all the students that are registered in this class
    	query = "SELECT sc.student_id, s.name FROM student_classes sc LEFT JOIN students s on s.student_id = sc.student_id WHERE sc.class_code='"+class_code+"'"

    	
    	cursor.execute(query)
    	result = cursor.fetchall()
    	students = []

    	for row in result:
    		students.append(row.student_id+" - "+row.name)

    	self.admin_ui.res_std_id.addItems(students)
    	pass
    def copyToProject(self,fileName):
    	path, fileExtension = os.path.splitext(str(fileName))
    	timestamp = str(time.time())
    	currentDirectory = os.getcwd()
    	targetPath = currentDirectory+"/assets/project_img/"
    	targetFileName = targetPath+timestamp+fileExtension
    	if not os.path.exists(targetPath):
    		os.mkdir(targetPath) 
    		pass
    	shutil.copy(fileName,targetFileName)
    	return targetFileName

    def chooseFile(self):
    	print "Select picture .."
    	
    	# show file selector
    	fileName = QFileDialog.getOpenFileName(self, "Select File","C://","Images (*.png *.xpm *.jpg)")

    	# save file in assets folder
    	fileName = self.copyToProject(fileName)

    	pixmap = QPixmap(fileName)
    	pixmap = pixmap.scaled(300,300)
    	if pixmap:
    		self.admin_ui.register_student_pic.setPixmap(pixmap)
    		self.stdRegImg = fileName
    		# self.admin_ui.reg_std_upload_btn.setEnabled(False)
    		pass

    def formatDate(self, date):
    	return datetime.datetime.strptime(date, "%d/%m/%Y").date()
    	
    def selectedClasses(self,selectedClasses):
    	classes = []
        for i in range(len(selectedClasses)):
            classes.append(str(selectedClasses[i].text()))
    	return classes

    def addNewStudent(self,studentId, name, dob, guardian,address, imagePath):

    	# add student to database
    	sql = "INSERT INTO students (student_id, name, dob, guardian, address, image_path, fingerprint_id) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    	val = (studentId, name, dob,guardian,address,imagePath,'') # change '' to a value later
    	cursor.execute(sql, val)
    	mydb.commit()
    	return True
    
    def addNewStudentClass(self,studentId, classes):
    	for i in range(len(classes)):
    		print classes[i]
    		sql = "INSERT INTO student_classes (student_id, class_code) VALUES (%s, %s)"
    		val = (studentId, classes[i]) # change false to a value later
	    	cursor.execute(sql, val)
	    	mydb.commit()
    		pass
    	return True
    	pass

    def clearList(self):
    	for i in range(self.admin_ui.reg_std_class_list.count()):
	        item = self.admin_ui.reg_std_class_list.item(i)
	        self.admin_ui.reg_std_class_list.setItemSelected(item, False)
    	pass

    def addStudent(self,):
    	print "Adding student ..."
    	studentId = str(self.admin_ui.reg_std_id.text())
    	name = str(self.admin_ui.reg_std_name.text())
    	dob = self.formatDate(str(self.admin_ui.reg_std_dob.text()))
    	guardian = str(self.admin_ui.reg_std_guardian.text())
    	address = str(self.admin_ui.reg_std_address.toPlainText())
    	classes = self.admin_ui.reg_std_class_list.selectedItems()
    	classes = self.selectedClasses(classes)
    	imagePath = self.stdRegImg
    	credentials = [studentId, name, dob, guardian, address, imagePath, classes]


    	if self.validateCredentials(credentials,"Please enter all fields") == False :
    		return 
    		pass

    	# check if student with the same ID exists.
    	result = self.checkIfExists("students","student_id", studentId)

    	if result:
    		self.showErrorMessage("Student already exists")
    		return
    	 	pass

    	# If student doesnt already exist, then create a new one and link to classes
    	addStudent = self.addNewStudent(studentId, name, dob, guardian,address, imagePath)
    	addStudentClass = self.addNewStudentClass(studentId, classes)
    	
    	if addStudent and addStudentClass:
    		# change status label to class added !
    		self.showErrorMessage("Student added !")
    		# self.admin_ui.reg_std_upload_btn.setEnabled(True)
    		self.admin_ui.reg_std_id.setText("")
    		self.admin_ui.reg_std_name.setText("")
    		
    		self.admin_ui.reg_std_guardian.setText("")
    		self.admin_ui.reg_std_address.setText("")
    		self.stdRegImg = ""
    		self.admin_ui.register_student_pic.setPixmap(QPixmap(_fromUtf8(":/holder/img/holder_1.PNG")))
    		self.clearList()
    		# self.admin_ui.reg_std_dob.clear()

    	pass

    def checkIfExists(self, table,column, value):
    	query = "SELECT * FROM "+table+" WHERE "+column+" = '"+value+"'"
    	cursor.execute(query)
    	result = cursor.fetchone()
    	return result

    def addNewClass(self, class_id, class_code, teacher_name):
    	sql = "INSERT INTO classes (class_id, class_code, teacher_name) VALUES (%s, %s, %s)"
    	val = (class_id, class_code, teacher_name)
    	cursor.execute(sql, val)
    	mydb.commit()
    	return True



    def addClass(self):
    	print "Add class method"
    	class_code = str(self.admin_ui.add_class_code.text())
    	teacher_name = str(self.admin_ui.add_class_teacher.text())
    	class_id = str(self.admin_ui.add_class_id.text())
    	credentials = [class_id, class_code, teacher_name]	

    	# check if both fields are filled
    	if self.validateCredentials(credentials,"Please enter all fields") == False :
    		return 
    		pass

    	# check if any previous results are available
    	result = self.checkIfExists("classes","class_code", class_code)

    	# if not add the class
    	if result:
    		self.showErrorMessage("Class already exists")
    	 	pass
    	else:
    		if self.addNewClass(class_id, class_code, teacher_name):
    			# change status label to class added !
    			self.showErrorMessage("Class added !")
    			# clear both text fields
    			self.admin_ui.add_class_code.setText("")
    			self.admin_ui.add_class_id.setText("")
    			self.admin_ui.add_class_teacher.setText("")
    			self.admin_ui.reg_std_class_list.addItem(class_code)
    			self.admin_ui.add_class_list.addItem(class_code)
    			pass
    		else:
    			self.showErrorMessage("Class could not be added")
    			return

    	
    	pass


    def checkAdmin(self,result):
    	if result == None:
    		self.showErrorMessage("Invalid Username or Password")
    		return False
    		pass
    	else:
    		print "login success!"
    		self.close()
    		self.openAdminWindow()
    		return True
    	pass
    	

    def findAdmin(self,username,password):
    	
    	query = "SELECT username FROM admin WHERE username = '"+ username+"' AND password = '"+password+"'"
    	cursor.execute(query)
    	result = cursor.fetchone()
    	return result
    	

    def hexPassword(self,password):
    	h = hashlib.new('ripemd160')
    	h.update(password)
    	return h.hexdigest()
    
    def validateCredentials(self,credentials,message):
    	
    	for i in range(len(credentials)) :
    		if (not credentials[i]):
    			self.showErrorMessage(message)
    			return False
    	return True
	   		

    def showErrorMessage(self,message):
   		msg = QMessageBox()
		msg.setWindowTitle("oops!")
		msg.setIcon(QMessageBox.Information)
		msg.setText(message)
		retval = msg.exec_()

    def login(self):

    	print "login attempt ..."
    	username = str(self.login_ui.username.text())
    	password = str(self.login_ui.password.text())
    	credentials = [username,password]


    	# check if username and password are not null
    	if self.validateCredentials(credentials,"Please enter username and password") == False :
    		return 
    		pass
 
    	# hex the password
    	password = self.hexPassword(password)

    	# query database for result of this username and password
    	result = self.findAdmin(username,password)
    	
    	# if no result throw error
    	self.checkAdmin(result)

    	return True

						 	
   	
def main():
	
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()