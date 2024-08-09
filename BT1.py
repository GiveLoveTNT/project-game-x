import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox, QVBoxLayout, QWidget

class YesNoApp(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Pushbutton widgets (Yes or No)?")
        self.setGeometry(100, 100, 400, 200)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.yes_button = QPushButton("Bắt đầu game")
        self.no_button = QPushButton("Thoát game")

        self.yes_button.clicked.connect(self.show_yes_message)
        self.no_button.clicked.connect(self.show_no_message)

        # Set up layout
        layout = QVBoxLayout()
        layout.addWidget(self.yes_button)
        layout.addWidget(self.no_button)

        central_widget.setLayout(layout)

    def show_yes_message(self):
        QMessageBox.information(self, "Choice", "Chương trình đã bắt đầu.")

    def show_no_message(self):
        QMessageBox.information(self, "Choice", "Bạn đã thoát game.")

def main():
    app = QApplication(sys.argv)
    window = YesNoApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
