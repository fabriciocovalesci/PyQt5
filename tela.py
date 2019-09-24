from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLineEdit,  QLabel, QMessageBox, QFrame, QAction, QInputDialog, QLineEdit, QFileDialog, QMainWindow
import sys
from PyQt5 import QtCore, QtWidgets

from PyQt5.QtGui import QIcon
from PyQt5 import QtGui, QtCore

class Login( QMainWindow):
    switch_window = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(Login, self).__init__(parent)

        self.setWindowTitle('Login')
        self.resize(300, 350)
        self.setWindowIcon(QIcon("archlinux.png"))
        # Idêntificação dos campos
        self.login = QLabel("SISTEMA DE AUTENTICAÇÃO ", self)
        self.login.move(100, 30)
        self.login.setStyleSheet('QLabel { color: black; font:bold}')
        self.nameUser = QLabel("Usuario", self)
        self.nameUser.move(125, 55)
        self.nameSenha = QLabel("Senha", self)
        self.nameSenha.move(125, 125)

        # Label  Usuario
        self.usuario = QLineEdit("", self)
        self.usuario.setGeometry(50, 80, 200, 30)

        # Label Senha Usuario
        self.senha = QLineEdit("", self)
        self.senha.setGeometry(50, 150, 200, 30)
        self.senha.setEchoMode(QLineEdit.Password)

        # Botao Entrar
        self.botaoEntrar = QPushButton("Entrar",self)
        self.botaoEntrar.setToolTip('Entrar')
        self.botaoEntrar.setGeometry(50, 220, 100, 30)
        self.botaoEntrar.clicked.connect(self.botao_entrar)

        # Botao Registrar
        self.botaoRegistrar = QPushButton("Registrar", self)
        self.botaoRegistrar.setToolTip('Entrar')
        self.botaoRegistrar.setGeometry(150, 220, 100, 30)
        self.botaoRegistrar.clicked.connect(self.registra_login)

        self.botaoAbrir = QPushButton("Abrir Arquivo", self)
        self.botaoAbrir.setToolTip("Abrir arquivo")
        self.botaoAbrir.setGeometry(150, 300, 100, 30)
        self.botaoAbrir.clicked.connect(self.abrir_arquivo)

    def registra_login(self):
        self.switch_window.emit()


        # Metodo para botao entrar
    def botao_entrar(self):
        textoUsuario = self.usuario.text()
        textoSenha = self.senha.text()
        if textoUsuario == 'fabricio' and textoSenha == '123':
            QMessageBox.question(self, 'Message', "Ola" , QMessageBox.Ok,
                                 QMessageBox.Ok)
        else:
            QMessageBox.question(self, "Message", " Usuário ou Senha incorreto  " , QMessageBox.Ok)

        self.usuario.setText("")

    # Abre arquivos
    def abrir_arquivo(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(self, "QFileDialog.getOpenFileNames()", "",
                                                "All Files (*);;Python Files (*.py)", options=options)
        if files:
            print(files)

# Classe para registrar novos usuarios
class Registrar(QtWidgets.QWidget):
    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Registrar')
        self.setGeometry(300, 350, 100, 100)

        self.setWindowTitle('Login')
        self.resize(300, 350)
        self.setWindowIcon(QIcon("archlinux.png"))
        # Idêntificação dos campos
        self.Novologin = QLabel("SISTEMA DE AUTENTICAÇÃO", self)
        self.Novologin.move(80, 30)
        self.Novologin.setStyleSheet('QLabel { color: black; font:bold}')
        self.NovonameUser = QLabel("Usuario", self)
        self.NovonameUser.move(125, 55)
        self.NovonameSenha = QLabel("Senha", self)
        self.NovonameSenha.move(125, 130)

        # Label  Usuario
        self.Novouser = QLineEdit("", self)
        self.Novouser.setGeometry(50, 80, 200, 30)

        # Label Senha Usuario
        self.Novosenha = QLineEdit("", self)
        self.Novosenha.setGeometry(50, 150, 200, 30)
        self.Novosenha.setEchoMode(QLineEdit.Password)

        # Botao Registrar
        self.btnregistrar = QPushButton("Registrar", self)
        self.btnregistrar.setToolTip('Registrar')
        self.btnregistrar.setGeometry(50, 220, 100, 30)
        self.btnregistrar.clicked.connect(self.cadastro)

    def cadastro(self):
        self.switch_window.emit()

# controle dos metodos entre as classes
class Controller:

    def __init__(self):
        pass

    def show_login(self):
        self.login = Login()
        self.login.switch_window.connect(self.main_login)
        self.login.show()

    def main_login(self):
        self.window = Registrar()
        self.window.switch_window.connect(self.main_registrar)
        self.login.close()
        self.window.show()

    def mainregistrar(self):
        self.window_two = Registrar()
        self.window.close()
        self.window_two.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_login()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()



