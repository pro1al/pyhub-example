# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import subprocess, requests, time, os, sys, random
import datetime as dt

class WindowResized(object):
    
    def frontEnd(self, MainWindow):
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        MainWindow.setMinimumSize(QtCore.QSize(600, 400))
        MainWindow.setMaximumSize(QtCore.QSize(600, 400))
        MainWindow.setWindowTitle('Exemplo Login using GitHub')
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 600, 400))
        self.stackedWidget.setObjectName("stackedWidget")
        
        self.loginPage = QtWidgets.QWidget()
        self.loginPage.setObjectName("loginPage")
        
        self.usernameEntry = QtWidgets.QLineEdit(self.loginPage)
        self.usernameEntry.setGeometry(QtCore.QRect(200, 110, 200, 20))
        self.usernameEntry.setAlignment(QtCore.Qt.AlignCenter)
        self.usernameEntry.setObjectName("usernameEntry")
        
        self.passwordEntry = QtWidgets.QLineEdit(self.loginPage)
        self.passwordEntry.setGeometry(QtCore.QRect(200, 190, 200, 20))
        self.passwordEntry.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordEntry.setAlignment(QtCore.Qt.AlignCenter)
        self.passwordEntry.setObjectName("passwordEntry")
        
        self.usernameLabel = QtWidgets.QLabel(self.loginPage)
        self.usernameLabel.setGeometry(QtCore.QRect(203, 91, 61, 16))
        self.usernameLabel.setObjectName("usernameLabel")
        self.passwordLabel = QtWidgets.QLabel(self.loginPage)
        self.passwordLabel.setGeometry(QtCore.QRect(203, 171, 61, 16))
        self.passwordLabel.setObjectName("passwordLabel")
        
        self.loginButton = QtWidgets.QPushButton(self.loginPage)
        self.loginButton.setGeometry(QtCore.QRect(238, 270, 125, 25))
        self.loginButton.setObjectName("loginButton")
        
        self.stackedWidget.addWidget(self.loginPage)
        self.loggedPage = QtWidgets.QWidget()
        self.loggedPage.setObjectName("loggedPage")
        
        self.loginStatus = QtWidgets.QLabel(self.loggedPage)
        self.loginStatus.setGeometry(QtCore.QRect(0, 385, 600, 15))
        self.loginStatus.setStyleSheet("background-color: rgb(170, 255, 0);")
        self.loginStatus.setObjectName("loginStatus")
        
        self.hardwarePanel = QtWidgets.QLineEdit(self.loggedPage)
        self.hardwarePanel.setGeometry(QtCore.QRect(125, 259, 350, 30))
        self.hardwarePanel.setText("")
        self.hardwarePanel.setAlignment(QtCore.Qt.AlignCenter)
        self.hardwarePanel.setReadOnly(True)
        self.hardwarePanel.setObjectName("hardwarePanel")
        
        self.datePanel = QtWidgets.QLineEdit(self.loggedPage)
        self.datePanel.setGeometry(QtCore.QRect(125, 180, 350, 30))
        self.datePanel.setText("")
        self.datePanel.setAlignment(QtCore.Qt.AlignCenter)
        self.datePanel.setReadOnly(True)
        self.datePanel.setObjectName("datePanel")
        
        self.randomPanel = QtWidgets.QLineEdit(self.loggedPage)
        self.randomPanel.setGeometry(QtCore.QRect(126, 100, 350, 30))
        self.randomPanel.setText("")
        self.randomPanel.setAlignment(QtCore.Qt.AlignCenter)
        self.randomPanel.setReadOnly(True)
        self.randomPanel.setObjectName("randomPanel")
        
        self.randomLabel = QtWidgets.QLabel(self.loggedPage)
        self.randomLabel.setGeometry(QtCore.QRect(129, 81, 111, 16))
        self.randomLabel.setObjectName("randomLabel")
        
        self.dateLabel = QtWidgets.QLabel(self.loggedPage)
        self.dateLabel.setGeometry(QtCore.QRect(128, 161, 80, 16))
        self.dateLabel.setObjectName("dateLabel")
        
        self.hardwareLabel = QtWidgets.QLabel(self.loggedPage)
        self.hardwareLabel.setGeometry(QtCore.QRect(128, 240, 151, 16))
        self.hardwareLabel.setObjectName("hardwareLabel")
        
        self.backButton = QtWidgets.QPushButton(self.loggedPage)
        self.backButton.setGeometry(QtCore.QRect(15, 15, 25, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.backButton.setFont(font)
        self.backButton.setObjectName("backButton")
        self.stackedWidget.addWidget(self.loggedPage)
        
        MainWindow.setCentralWidget(self.centralwidget)
        _translate = QtCore.QCoreApplication.translate
        
        self.usernameLabel.setText(_translate("MainWindow", "USERNAME"))
        self.passwordLabel.setText(_translate("MainWindow", "PASSWORD"))
        self.loginButton.setText(_translate("MainWindow", "Login"))
        self.loginStatus.setText(_translate("MainWindow", " Logged as: "))
        self.randomLabel.setText(_translate("MainWindow", "STORE LOCALIZATION"))
        self.dateLabel.setText(_translate("MainWindow", "DATE AND TIME"))
        self.hardwareLabel.setText(_translate("MainWindow", "HARDWARE IDENTIFICATION"))
        self.backButton.setText(_translate("MainWindow", "<"))

        # Chamada da Função "BACKEND".
        self.backEnd(MainWindow)

        # Define a Pagina Inicial.
        self.stackedWidget.setCurrentIndex(0)
        

    def backEnd(self, MainWindow):

        def debbugActions():
            clearDecals()

            # Quando Pressionado -> Conecta a Função "GOTO"
            self.loginButton.clicked.connect(goTo) 
            self.backButton.clicked.connect(goTo)

            # Quando "ENTER" é Pressionado no Objeto -> Executa o Click do Botão.
            self.usernameEntry.returnPressed.connect(self.loginButton.animateClick) 
            self.passwordEntry.returnPressed.connect(self.loginButton.animateClick)

            

        def popthat(title, text):

            # Cria uma PopUP com "TITLE" e "TEXT".
            msg = QMessageBox()
            msg.setWindowTitle(title)
            msg.setText(text)   
            x = msg.exec_()

            

        def clearDecals():

            # Reestabelece Todos os Campos ao Original.
            self.usernameEntry.setText("")
            self.passwordEntry.setText("")


            
        def getUsername():

            # Coleta o Conteúdo de LineEdit "USERNAMEENTRY"
            username = self.usernameEntry.text()
            return username



        def getPassword():

            # Coleta o Conteúdo de LineEdit "PASSWORDENTRY"
            password = self.passwordEntry.text()
            return password



        def getHardware():

            # Busca o Identificador HWID.
            hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
            return hwid



        def getDateTime():

            # Calcula a Data e Horário Atual.
            thisTime = dt.datetime.now()
            date = thisTime.strftime("[%Y \\ %m \\ %d] -> %H:%M:%S")
            return date



        def getRandomNumber():

            # Calcula um Numero Aleatório.
            number = str(random.randint(900000000000000000000000000000000,900000000000000000000000000000000000))
            return number

        

        def requestServer(url):

            # Busca e Armazena Todo o Conteúdo de uma Página.
            myRequest = requests.get(url)
            return myRequest.text.split('\n') # "SPLIT" Corta e Separa a String em Listas.



        def goTo():

            # Verifica Qual a Página Atual.
            if self.stackedWidget.currentIndex() == 0:

                # Reliza Requests na Função "REQUESTSERVER"
                serverUsers = requestServer('https://raw.githubusercontent.com/pro1al/pyhub-db/master/usernames.txt')
                serverPassr = requestServer('https://raw.githubusercontent.com/pro1al/pyhub-db/master/passwords.txt')
                serverHardw = requestServer('https://raw.githubusercontent.com/pro1al/pyhub-db/master/hwidchanges.txt')

                # Realiza Requests nos Campos do Programa.
                localUser = getUsername()
                localPass = getPassword()

                # Realiza o Cálculo do HWID.
                localHard = getHardware()


                for i in range(len(serverUsers)):
                
                    # Verifica Usuário Digitado -> Usuário no GitHub.
                    if serverUsers[i] == localUser and serverUsers[i] != "":

                        # Verifica Senha Recorrente ao Usuário.
                        if localPass == serverPassr[i]:

                            # Verifica se o HWID é Registrado. 
                            if localHard in serverHardw: 
                                self.loginStatus.setText(" Logged as: %s"%(localUser))
                                self.randomPanel.setText(getRandomNumber())
                                self.datePanel.setText(getDateTime())
                                self.hardwarePanel.setText(localHard)
                                
                                self.stackedWidget.setCurrentIndex(1)
                            else:
                                popthat('!!!', 'HARDWARE NÃO AUTORIZADO')
                                clearDecals()
                
                clearDecals()

                # Consede Foco à "USERNAMEENTRY".
                self.usernameEntry.setFocus()
                
            elif self.stackedWidget.currentIndex() == 1:
                clearDecals()
                self.stackedWidget.setCurrentIndex(0)

        debbugActions()
        


# Executa Toda a Aplicação.
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    unity = WindowResized()
    unity.frontEnd(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
