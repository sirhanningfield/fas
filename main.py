import sys
import time
import hashlib
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import mysql.connector


from login import Ui_login
from admin import Ui_admin

mydb = mysql.connector.connect(
	  host="localhost",
	  user="root",
	  passwd="",
	  database="fas_test"
	)
cursor = mydb.cursor(named_tuple=True)



class Main(QWidget, Ui_login, Ui_admin):

    def __init__(self, parent = None):
        super(Main,self).__init__(parent)
        self.parent = parent
        self.cursor = cursor
        self.login_ui = Ui_login()
        self.login_ui.setupUi(self)
        self.message = ""
        self.login_ui.login_btn.clicked.connect(lambda: self.login())

    def openAminWindow(self):
    	# self.admin_window = Admin(self)
    	self.window = QTabWidget()
    	self.admin_ui = Ui_admin()
    	self.admin_ui.setupUi(self.window)
    	self.window.show()
    	self.admin_ui.add_class_btn.clicked.connect(lambda: self.addClass())
    	self.admin_ui.reg_std_btn.clicked.connect(lambda: self.addStudent())
    	pass

    def addStudent(self,):
    	print "Adding student"
    	pass

    def findClass(self,class_id, class_code):
    	query = "SELECT * FROM classes WHERE class_id = '"+class_id+"' OR class_code = '"+class_code+"'"
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
    	result = self.findClass(class_id, class_code)

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
    		self.openAminWindow()
    		return True
    	pass
    	

    def findAdmin(self,username,password):
    	
    	self.cursor.execute("SELECT username FROM admin WHERE username = '"+ username+"' AND password = '"+password+"'")
    	result = self.cursor.fetchone()
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