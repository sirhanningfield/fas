import sys
import time
import hashlib
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import mysql.connector


from login import Ui_login
from admin import Ui_FAS

mydb = mysql.connector.connect(
	  host="localhost",
	  user="root",
	  passwd="",
	  database="fas_test"
	)
cursor = mydb.cursor(named_tuple=True)



class Main(QWidget, Ui_login, Ui_FAS):

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
    	self.admin_ui = Ui_FAS()
    	self.admin_ui.setupUi(self.window)
    	self.window.show()
    	self.admin_ui.add_class_btn.clicked.connect(lambda: self.addClass())
    	self.admin_ui.reg_std_btn.clicked.connect(lambda: self.addStudent())
    	pass

    def addStudent(self):
    	print "Adding student"
    	pass

    def addClass(self):
    	print "Add class method"

    	# check if both fields are filled 

    	# check if any previous results are available 

    	# if not add the class 

    	# change status label to class added !

    	# clear both text fields
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
    
    def validateCredentials(self,username,password):
   		if len(username) == 0 or len(password) == 0 :   			
   			self.message = "Please fill in username and password!"
   			self.showErrorMessage(self.message)
   			return False
   		else:
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

    	# check if username and password are not null
    	if self.validateCredentials(username,password) == False :
    		return 
    		pass
 
    	# hex the password
    	password = self.hexPassword(password)

    	# query database for result of this username and password
    	result = self.findAdmin(username,password)
    	
    	# if no result throw error
    	self.checkAdmin(result)

    	return True

# class Admin(Main):
# 	"""docstring for Admin"""
# 	def __init__(self, parent = None):
# 		super(Admin, self).__init__(parent)
# 		print "admin class"
# 		self.parent = parent
# 		# self.window = QTabWidget()
#   #   	self.admin_ui = Ui_FAS()
#   #   	self.admin_ui.setupUi(self.window)
#   #   	self.window.show()
						 	
   	
def main():
	
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()