import sys
import time
import hashlib
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import mysql.connector


from login import Ui_login

mydb = mysql.connector.connect(
	  host="localhost",
	  user="root",
	  passwd="",
	  database="fas_test"
	)
cursor = mydb.cursor(named_tuple=True)


class Main(QWidget, Ui_login):

    def __init__(self, parent = None):
        super(Main,self).__init__(parent)
        self.parent = parent
        self.cursor = cursor
        self.login_ui = Ui_login()
        self.login_ui.setupUi(self)
        self.message = ""
        self.login_ui.login_btn.clicked.connect(lambda: self.login())

    def checkAdmin(self,result):
    	if result == None:
    		self.showErrorMessage("Invalid Username or Password")
    		return
    		pass
    	else:
    		print "login success!"
    		self.showErrorMessage("Logged in successfully as : '"+result.username+"'")
    		exit() # remove this line 
    	pass
    	

    def findAdmin(self,username,password):
    	
    	self.cursor.execute("SELECT username FROM admin WHERE username = '"+ username+"' AND password = '"+password+"'")
    	 # +"' AND password = '"+password+"'")
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

    	# if result, then display message
   	
def main():
	
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()