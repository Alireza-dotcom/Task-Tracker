import sys
import os
from utils import load_stylesheet
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QFrame,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QStackedWidget,
)

from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QPixmap, QCursor


class ClickableLabel(QLabel):
    clicked = Signal()

    def __init__(self, text="", parent=None):
        super().__init__(text, parent)
        self.setCursor(Qt.PointingHandCursor)


    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._mouse_pressed = True
        super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        if self._mouse_pressed and event.button() == Qt.LeftButton:
            if self.rect().contains(event.position().toPoint()): # Released inside label
                self.clicked.emit()
        self._mouse_pressed = False
        super().mouseReleaseEvent(event)


class LoginPanel(QFrame):
    forgot_clicked = Signal()
    signup_clicked = Signal()

    def __init__(self):
        super().__init__()
        self.setObjectName("LoginPanel")

        layout = QVBoxLayout(self)
        layout.setContentsMargins(50, 40, 50, 40)
        layout.setSpacing(10)
        layout.setAlignment(Qt.AlignTop)
        layout.addStretch(0.5)

        # Logo placeholder
        logo = QLabel()
        logo_file = QPixmap(os.path.abspath('../res/logo.svg'))
        logo.setPixmap(QPixmap(logo_file))
        logo.setAlignment(Qt.AlignCenter)
        layout.addWidget(logo, alignment=Qt.AlignCenter)
        layout.addStretch(0.5)

        # Title
        title = QLabel("Login")
        title.setObjectName("TitleLabel")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        # Email field
        email_label = QLabel("Email")
        email_label.setObjectName("EmailLabel")
        layout.addWidget(email_label)

        email_input = QLineEdit()
        email_input.setObjectName("EmailInput")
        layout.addWidget(email_input)

        # Password field
        password_label = QLabel("Password")
        password_label.setObjectName("PasswordLabel")
        layout.addWidget(password_label)

        password_input = QLineEdit()
        password_input.setEchoMode(QLineEdit.Password)
        password_input.setObjectName("PasswordInput")
        layout.addWidget(password_input)

        # Forgot password link
        forgot_label = ClickableLabel('Forgot your password?')
        forgot_label.clicked.connect(self.onForgotClicked)
        forgot_label.setObjectName("ForgotLabel")
        forgot_label.setAlignment(Qt.AlignRight)
        layout.addWidget(forgot_label)

        # Login button
        login_btn = QPushButton("Login")
        # login_btn.setCursor(Qt.PointingHandCursor)
        login_btn.setObjectName("LoginButton")
        layout.addWidget(login_btn)

        # Divider
        divider = QLabel("──────────  or continue offline  ──────────")
        divider.setAlignment(Qt.AlignCenter)
        divider.setObjectName("DividerLabel")
        layout.addWidget(divider)

        # Continue button
        cont_btn = QPushButton("Continue without Account")
        cont_btn.setObjectName("ContinueButton")
        layout.addWidget(cont_btn)

        # Signup text
        signup_label = ClickableLabel("Don't have an account? Sign up")
        signup_label.clicked.connect(self.onSignupClicked)
        signup_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(signup_label)
        layout.addStretch(0.1)

    def onForgotClicked(self):
        self.forgot_clicked.emit()
    
    def onSignupClicked(self):
        self.signup_clicked.emit()


class ForgotPasswordPanel(QFrame):
    back_to_login_clicked = Signal()

    def __init__(self):
        super().__init__()
        self.setObjectName("ForgotPanel")

        layout = QVBoxLayout(self)
        layout.setContentsMargins(50, 40, 50, 40)
        layout.setSpacing(13)
        layout.setAlignment(Qt.AlignTop)
        layout.addStretch(0.5)

        # Logo placeholder
        logo = QLabel()
        logo_file = QPixmap(os.path.abspath('../res/logo.svg'))
        logo.setPixmap(QPixmap(logo_file))
        logo.setAlignment(Qt.AlignCenter)
        layout.addWidget(logo, alignment=Qt.AlignCenter)
        layout.addStretch(0.5)

        # Title
        title = QLabel("Trouble logging in?")
        title.setObjectName("TitleLabel")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        # Email field
        email_label = QLabel("Email")
        email_label.setObjectName("EmailLabel")
        layout.addWidget(email_label)

        email_input = QLineEdit()
        email_input.setObjectName("EmailInput")
        layout.addWidget(email_input)

        # Send login link button
        send_btn = QPushButton("Send login link")
        send_btn.setObjectName("SndLoginLink")
        layout.addWidget(send_btn)

        # Divider
        divider = QLabel("──────────  or  ──────────")
        divider.setAlignment(Qt.AlignCenter)
        divider.setObjectName("DividerLabel")
        layout.addWidget(divider)

        # Create new account button
        create_new_acc_label = ClickableLabel("Create new account")
        create_new_acc_label.clicked.connect(self.onBackToLoginClicked)
        create_new_acc_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(create_new_acc_label)

        layout.addStretch(0.5)

        # Continue button
        bck_to_login_btn = QPushButton("Back to login")
        bck_to_login_btn.setObjectName("BackToLogin")
        bck_to_login_btn.clicked.connect(self.onBackToLoginClicked)
        layout.addWidget(bck_to_login_btn)
        layout.addStretch(0.1)

    def onBackToLoginClicked(self):
        self.back_to_login_clicked.emit()


class SignupPanel(QFrame):
    already_have_account_clicked = Signal()

    def __init__(self):
        super().__init__()
        self.setObjectName("SingupPanel")

        layout = QVBoxLayout(self)
        layout.setContentsMargins(50, 40, 50, 40)
        layout.setSpacing(13)
        layout.setAlignment(Qt.AlignTop)
        layout.addStretch(0.5)

        # Logo placeholder
        logo = QLabel()
        logo_file = QPixmap(os.path.abspath('../res/logo.svg'))
        logo.setPixmap(QPixmap(logo_file))
        logo.setAlignment(Qt.AlignCenter)
        layout.addWidget(logo, alignment=Qt.AlignCenter)
        layout.addStretch(0.5)

        # Title
        title = QLabel("Create a new account")
        title.setObjectName("TitleLabel")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        # first name
        first_name_label = QLabel("First Name")
        first_name_input = QLineEdit()
        first_name_layout = QVBoxLayout()
        first_name_layout.addWidget(first_name_label)
        first_name_layout.addWidget(first_name_input)

        # last name
        last_name_label = QLabel("Last Name")
        last_name_input = QLineEdit()
        last_name_layout = QVBoxLayout()
        last_name_layout.addWidget(last_name_label)
        last_name_layout.addWidget(last_name_input)

        #name layout
        name_layout = QHBoxLayout()
        name_layout.addLayout(first_name_layout)
        name_layout.addLayout(last_name_layout)
        layout.addLayout(name_layout)

        # display name field
        display_name_label = QLabel("Display name")
        display_name_label.setObjectName("EmailLabel")
        layout.addWidget(display_name_label)

        display_name_input = QLineEdit()
        display_name_input.setObjectName("EmailInput")
        layout.addWidget(display_name_input)

        # Email field
        email_label = QLabel("Email")
        email_label.setObjectName("EmailLabel")
        layout.addWidget(email_label)

        email_input = QLineEdit()
        email_input.setObjectName("EmailInput")
        layout.addWidget(email_input)

        # Password field
        password_label = QLabel("Password")
        password_label.setObjectName("PasswordLabel")
        layout.addWidget(password_label)

        password_input = QLineEdit()
        password_input.setEchoMode(QLineEdit.Password)
        password_input.setObjectName("PasswordInput")
        layout.addWidget(password_input)

        # signup button
        signup_btn = QPushButton("Sign up")
        signup_btn.setObjectName("Signup")
        # bck_to_login_btn.clicked.connect(self.onBackToLoginClicked)
        layout.addWidget(signup_btn)
        layout.addStretch(0.1)

        # already have account link
        already_have_acc_label = ClickableLabel("Already have an account?")
        already_have_acc_label.clicked.connect(self.onBackToLoginClicked)
        already_have_acc_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(already_have_acc_label)

    def onBackToLoginClicked(self):
        self.already_have_account_clicked.emit()



class MainWindow(QMainWindow):
    LOGIN_PAGE = 0
    FORGOT_PASS_PAGE = 1
    SIGNUP_PAGE = 2

    def __init__(self):
        super().__init__()
        self.setObjectName("MainWindow")

        load_stylesheet(self, os.path.abspath('../res/qss/login.qss'))

        self.setMinimumSize(1024, 768)
        self.resize(1280, 720)

        self.centeral_widget = QWidget()
        self.setCentralWidget(self.centeral_widget)

        self.stack = QStackedWidget()
        self.login_panel = LoginPanel()
        self.forgot_pass_panel = ForgotPasswordPanel()
        self.signup_panel = SignupPanel()


        self.stack.addWidget(self.login_panel)
        self.stack.addWidget(self.forgot_pass_panel)
        self.stack.addWidget(self.signup_panel)

        # Connect signals
        self.login_panel.forgot_clicked.connect(self.showForgotPasswordPage)
        self.forgot_pass_panel.back_to_login_clicked.connect(self.showLoginPage)
        self.signup_panel.already_have_account_clicked.connect(self.showLoginPage)
        self.login_panel.signup_clicked.connect(self.showSignupPage)

        self.layout = QHBoxLayout(self.centeral_widget)
        # self.layout.setContentsMargins(0,0,0,0)
        # self.layout.addStretch(1)
        self.layout.addWidget(self.stack)
        # self.layout.addStretch(1)

    def showLoginPage(self):
        self.stack.setCurrentIndex(self.LOGIN_PAGE)

    def showForgotPasswordPage(self):
        self.stack.setCurrentIndex(self.FORGOT_PASS_PAGE)

    def showSignupPage(self):
        self.stack.setCurrentIndex(self.SIGNUP_PAGE)

    def resizeEvent(self, event):
        window_width = self.width()
        target_width = max(430, int(window_width * 0.32)) # 35% of width, min 430px
        self.stack.setFixedWidth(target_width)

        super().resizeEvent(event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
